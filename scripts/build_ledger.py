#!/usr/bin/env python3
"""
Render and check the numbered Results Ledger (RESULTS.md).

Source of truth:  registry/RESULTS_LEDGER.json   (one record per audited result)
Joined at render: registry/PAPERS.json, registry/BUILD_PAPERS.json,
                  registry/SOLVED_AND_ATLAS_BRIDGE.json
Outputs:          RESULTS.md and the RESULTS_LEDGER block in README.md

Design rules
  * A result records the commit at which its statement was audited. Version,
    repository, pin and PDF path are never typed into the ledger; they are
    joined from the registries, so the ledger follows every registry update.
  * If the archive pin has moved past the audited commit, the result is
    rendered as "re-audit pending" instead of silently inheriting the new pin.
  * Every registered Tier I / Tier II entry appears: either through its
    results, through an explicit reason, or under "not yet in this ledger".
  * Result numbers are permanent. A withdrawn result keeps its number.

Usage
  python scripts/build_ledger.py            # render RESULTS.md + README block
  python scripts/build_ledger.py --check    # verify; exit 1 on any problem
  python scripts/build_ledger.py --check --checkouts DIR
        also confirm each Lean declaration is at the cited file and line in
        DIR/<slug> (a clone checked out at the audited commit)
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

BLOCK_START = "<!-- RESULTS_LEDGER:START -->"
BLOCK_END = "<!-- RESULTS_LEDGER:END -->"
OWNER = "0thernes"

# kind -> (section letter, section title, one-line definition, singular label, plural label), in display order
KINDS: dict[str, tuple[str, str, str, str, str]] = {
    "ANSWERS_PUBLISHED_QUESTION": (
        "A",
        "Open questions from the literature, answered",
        "A question or conjecture that another author stated as open in a cited paper or preprint "
        "(the citation says which), answered here within the scope given.",
        "open question from the literature answered",
        "open questions from the literature answered",
    ),
    "NEW_THEOREM": (
        "B",
        "New theorems",
        "A statement first formulated in this work. No earlier statement of it was found "
        "in the literature search recorded for the result.",
        "new theorem",
        "new theorems",
    ),
    "BOUNDED_CASE": (
        "C",
        "Bounded and partial cases",
        "An exact answer inside a stated finite range or restricted setting. "
        "The unrestricted problem stays open.",
        "bounded or partial case",
        "bounded or partial cases",
    ),
    "REFUTATION": (
        "D",
        "Refutations",
        "A counterexample or impossibility result against a stated claim or heuristic.",
        "refutation",
        "refutations",
    ),
    "KNOWN_RESULT_FORMALIZED": (
        "E",
        "Known results formalized",
        "Mathematics already in the literature, machine-checked here. The contribution is the formal proof.",
        "known result formalized",
        "known results formalized",
    ),
    "ENGINEERING_INVARIANTS": (
        "F",
        "Engineering invariant suites",
        "Machine-checked properties of a software model or simulator. "
        "They say the model is internally consistent, not that it describes nature.",
        "engineering invariant suite",
        "engineering invariant suites",
    ),
}


def count_phrase(kind: str, n: int) -> str:
    """'1 new theorem' / '3 new theorems'."""
    return f"{n} {KINDS[kind][3] if n == 1 else KINDS[kind][4]}"

EVIDENCE: dict[str, str] = {
    "kernel-checked": "Lean kernel",
    "certificate-checked": "Checked certificate",
    "computation": "Exact computation",
    "paper-proof": "Written proof",
    "empirical": "Experiment",
}

FIDELITY: dict[str, str] = {
    "AUDITED_MATCH": "the formal statement matches the stated claim",
    "AUDITED_NARROWER": "the formal statement is narrower than the usual informal claim (see Limits)",
    "NOT_AUDITED": "not yet audited",
}

PRIOR_WORK: dict[str, str] = {
    "NONE_FOUND": "no earlier proof found",
    "KNOWN": "known mathematics",
    "OVERLAP_FOUND": "overlapping earlier or parallel work found (see Limits)",
    "NOT_SEARCHED": "not yet searched",
}

REBUILD: dict[str, str] = {
    "PASS": "Rebuilt from a clean clone at the audited commit: pass",
    "FAIL": "Rebuilt from a clean clone at the audited commit: FAIL",
    "NOT_REBUILT": "Not rebuilt in this audit",
}

STATUS = {"ACTIVE", "WITHDRAWN"}

# Words a careful referee would strike. Checked in titles, statements and limits.
BANNED = [
    r"world[- ]record",
    r"breakthrough",
    r"revolution",
    r"groundbreaking",
    r"completely (?:re)?solv",
    r"first[- ]ever",
    r"unprecedented",
    r"definitive(?:ly)?",
    r"\bproves? p\s*(?:=|!=|≠|vs\.?)\s*np\b",
]
BANNED_RE = re.compile("|".join(BANNED), re.I)
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
MAX_STATEMENT_WORDS = 75
MAX_TITLE_WORDS = 20

# Bridge resolution class allowed for an entry, decided by the strongest kind among its active
# ledger results (order of KINDS). BARRIER_FORMALIZATION is a named kind of known-results row.
BRIDGE_CLASS: dict[str, tuple[str, ...]] = {
    "ANSWERS_PUBLISHED_QUESTION": ("SOLVED_SUB_CONJECTURE",),
    "NEW_THEOREM": ("NEW_THEOREM_SUITE",),
    "BOUNDED_CASE": ("PARTIAL_BOUNDED_CASE",),
    "REFUTATION": ("REFUTATION",),
    "KNOWN_RESULT_FORMALIZED": ("KNOWN_RESULTS_FORMALIZED", "BARRIER_FORMALIZATION"),
    "ENGINEERING_INVARIANTS": ("FORMAL_INVARIANT_SUITE",),
}


def expected_bridge_classes(ledger: dict[str, Any]) -> dict[str, tuple[str, ...]]:
    """Allowed bridge classes per archive id, from the strongest kind of its active results."""
    order = list(KINDS)
    best: dict[str, str] = {}
    for r in ledger.get("results", []):
        if r.get("status", "ACTIVE") != "ACTIVE" or r.get("kind") not in KINDS:
            continue
        aid, kind = r["archive_id"], r["kind"]
        if aid not in best or order.index(kind) < order.index(best[aid]):
            best[aid] = kind
    return {aid: BRIDGE_CLASS[kind] for aid, kind in best.items()}


def write_utf8_lf(path: Path, text: str) -> None:
    path.write_bytes(text.replace("\r\n", "\n").encode("utf-8"))


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def slug_of(repo_url: str) -> str:
    return repo_url.rstrip("/").split("/")[-1]


def registry_index(root: Path) -> dict[str, dict[str, Any]]:
    """id -> joined registry facts for every Tier I and Tier II entry."""
    index: dict[str, dict[str, Any]] = {}
    papers = load_json(root / "registry" / "PAPERS.json")
    for p in papers["papers"]:
        index[p["id"]] = {
            "tier": "I",
            "title": p.get("title", ""),
            "repository": p.get("repository", ""),
            "slug": slug_of(p.get("repository", "")),
            "version": str(p.get("version", "")),
            "pinned_commit": p.get("pinned_commit", ""),
            "pdf": p.get("pdf_archive_path"),
            "ci_run_url": p.get("ci_run_url"),
            "peer_review_status": p.get("peer_review_status", ""),
        }
    bpath = root / "registry" / "BUILD_PAPERS.json"
    if bpath.exists():
        for b in load_json(bpath)["builds"]:
            pdf = None
            for art in b.get("archived_artifacts", []):
                if str(art.get("path", "")).lower().endswith(".pdf"):
                    pdf = art["path"]
                    break
            index[b["id"]] = {
                "tier": "II",
                "title": b.get("title", ""),
                "repository": b.get("repository", ""),
                "slug": slug_of(b.get("repository", "")),
                "version": str(b.get("version", "")),
                "pinned_commit": b.get("pinned_commit", ""),
                "pdf": pdf,
                "ci_run_url": b.get("ci_run_url"),
                "peer_review_status": "",
            }
    return index


def live_index(root: Path) -> dict[str, Any]:
    """slug -> live upstream state from the last live sync (empty when no live mirror exists)."""
    path = root / "registry" / "LIVE_ECOSYSTEM_MIRROR.json"
    if not path.exists():
        return {"synced_utc": None, "repos": {}}
    mirror = load_json(path)
    return {
        "synced_utc": mirror.get("synced_utc"),
        "repos": {r.get("slug"): r for r in mirror.get("repositories", [])},
    }


def words(text: str) -> int:
    return len(text.split())


def validate(ledger: dict[str, Any], index: dict[str, dict[str, Any]]) -> list[str]:
    errs: list[str] = []
    results = ledger.get("results")
    if not isinstance(results, list):
        return ["RESULTS_LEDGER.json: 'results' must be a list"]

    expected_n = 1
    seen_keys: set[tuple[str, str]] = set()
    for r in results:
        n = r.get("n")
        tag = f"R{n}"
        if n != expected_n:
            errs.append(f"{tag}: result numbers must be 1..N in file order (expected {expected_n})")
        expected_n = (n if isinstance(n, int) else expected_n) + 1

        for field in ("archive_id", "key", "title", "statement", "kind", "evidence", "status"):
            if not r.get(field):
                errs.append(f"{tag}: missing '{field}'")
        aid = r.get("archive_id", "")
        if aid and aid not in index:
            errs.append(f"{tag}: archive_id {aid} is not in registry/PAPERS.json or BUILD_PAPERS.json")
        ident = (aid, str(r.get("key")))
        if ident in seen_keys:
            errs.append(f"{tag}: duplicate (archive_id, key) {ident}")
        seen_keys.add(ident)

        kind = r.get("kind")
        if kind not in KINDS:
            errs.append(f"{tag}: unknown kind {kind!r}")
        if r.get("evidence") not in EVIDENCE:
            errs.append(f"{tag}: unknown evidence {r.get('evidence')!r}")
        if r.get("status") not in STATUS:
            errs.append(f"{tag}: unknown status {r.get('status')!r}")
        if r.get("status") == "WITHDRAWN" and not r.get("withdrawn_reason"):
            errs.append(f"{tag}: a withdrawn result needs 'withdrawn_reason'")

        title, statement = str(r.get("title", "")), str(r.get("statement", ""))
        if words(title) > MAX_TITLE_WORDS:
            errs.append(f"{tag}: title has {words(title)} words (limit {MAX_TITLE_WORDS})")
        if words(statement) > MAX_STATEMENT_WORDS:
            errs.append(f"{tag}: statement has {words(statement)} words (limit {MAX_STATEMENT_WORDS})")
        prose = " ".join([title, statement] + [str(c) for c in r.get("limits", [])])
        hit = BANNED_RE.search(prose)
        if hit:
            errs.append(f"{tag}: promotional wording {hit.group(0)!r} is not allowed in the ledger")

        commit = r.get("audited_commit", "")
        if not SHA_RE.match(str(commit)):
            errs.append(f"{tag}: audited_commit must be a 40-character commit SHA")

        lean = r.get("lean", [])
        if r.get("evidence") == "kernel-checked":
            if not lean:
                errs.append(f"{tag}: kernel-checked results must cite at least one Lean declaration")
            if not r.get("axioms"):
                errs.append(f"{tag}: kernel-checked results must state the axioms used")
        for ref in lean:
            if not (ref.get("decl") and ref.get("file") and isinstance(ref.get("line"), int) and ref["line"] > 0):
                errs.append(f"{tag}: each Lean reference needs decl, file and a positive line")

        audit = r.get("audit") or {}
        for field, table in (("fidelity", FIDELITY), ("prior_work", PRIOR_WORK), ("rebuild", REBUILD)):
            if audit.get(field) not in table:
                errs.append(f"{tag}: audit.{field} must be one of {sorted(table)}")
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(audit.get("date", ""))):
            errs.append(f"{tag}: audit.date must be YYYY-MM-DD")

        if kind == "ANSWERS_PUBLISHED_QUESTION" and r.get("status") == "ACTIVE":
            asked = r.get("asked_in") or {}
            for field in ("citation", "url", "locator"):
                if not asked.get(field):
                    errs.append(f"{tag}: kind A needs asked_in.{field}")
            if audit.get("fidelity") not in ("AUDITED_MATCH", "AUDITED_NARROWER"):
                errs.append(f"{tag}: kind A requires an audited statement (fidelity)")
            if audit.get("prior_work") not in ("NONE_FOUND", "OVERLAP_FOUND"):
                errs.append(f"{tag}: kind A requires a recorded prior-work search")
            if audit.get("fidelity") == "AUDITED_NARROWER" and not r.get("limits"):
                errs.append(f"{tag}: a narrower statement must say how, under 'limits'")
        if kind == "NEW_THEOREM" and r.get("status") == "ACTIVE":
            if audit.get("prior_work") == "KNOWN":
                errs.append(f"{tag}: a known result cannot be listed as a new theorem")
        if audit.get("prior_work") == "OVERLAP_FOUND" and not r.get("limits"):
            errs.append(f"{tag}: overlapping prior work must be described under 'limits'")

    reasons = ledger.get("entries_without_results") or {}
    for aid in reasons:
        if aid not in index:
            errs.append(f"entries_without_results: unknown archive_id {aid}")
    return errs


def check_declarations(ledger: dict[str, Any], index: dict[str, dict[str, Any]], checkouts: Path) -> list[str]:
    """Confirm each cited Lean declaration sits at the cited file and line at the audited commit."""
    errs: list[str] = []
    for r in ledger["results"]:
        ent = index.get(r.get("archive_id", ""))
        if not ent or not r.get("lean"):
            continue
        repo = checkouts / ent["slug"]
        if not (repo / ".git").exists():
            errs.append(f"R{r['n']}: no checkout for {ent['slug']} under {checkouts}")
            continue
        for ref in r["lean"]:
            res = subprocess.run(
                ["git", "-C", str(repo), "show", f"{r['audited_commit']}:{ref['file']}"],
                capture_output=True, text=True, encoding="utf-8", errors="replace", check=False,
            )
            if res.returncode != 0:
                errs.append(f"R{r['n']}: {ref['file']} not found at {r['audited_commit'][:7]} in {ent['slug']}")
                continue
            lines = res.stdout.splitlines()
            lo, hi = max(0, ref["line"] - 3), min(len(lines), ref["line"] + 2)
            short = ref["decl"].split(".")[-1]
            if not any(re.search(r"\b" + re.escape(short) + r"\b", ln) for ln in lines[lo:hi]):
                errs.append(
                    f"R{r['n']}: declaration {ref['decl']} is not at {ref['file']}:{ref['line']} "
                    f"(commit {r['audited_commit'][:7]})"
                )
    return errs


def cell(text: str) -> str:
    """Make text safe inside one Markdown table cell (no row break, no stray column)."""
    return str(text).replace("\\", "\\\\").replace("|", "\\|").replace("\r", " ").replace("\n", " ")


def pending_entries(ledger: dict[str, Any], index: dict[str, dict[str, Any]]) -> list[str]:
    covered = {r["archive_id"] for r in ledger["results"]}
    explained = set((ledger.get("entries_without_results") or {}).keys())
    return [aid for aid in sorted(index) if aid not in covered and aid not in explained]


def answered_count(root: Path) -> int | None:
    """Active section-A results (open questions from the literature answered), or None without a ledger.

    Every summary line (README status block, llms.txt, portal) uses this one number, so the hub
    never states two different counts of answered questions.
    """
    path = root / "registry" / "RESULTS_LEDGER.json"
    if not path.exists():
        return None
    ledger = load_json(path)
    return counts_by_kind(ledger)["ANSWERS_PUBLISHED_QUESTION"]


def counts_by_kind(ledger: dict[str, Any]) -> dict[str, int]:
    out = {k: 0 for k in KINDS}
    for r in ledger["results"]:
        if r.get("status") == "ACTIVE" and r.get("kind") in out:
            out[r["kind"]] += 1
    return out


def atlas_line(root: Path) -> str:
    bpath = root / "registry" / "SOLVED_AND_ATLAS_BRIDGE.json"
    if not bpath.exists():
        return ""
    b = load_json(bpath)
    return (
        f"{b.get('grand_problems_retired', 0)} of {b.get('mega_atlas_total_problems', 0):,} "
        "catalogued open problems in the Unsolved Problems Mega-Atlas are solved by this work."
    )


def evidence_line(r: dict[str, Any], ent: dict[str, Any]) -> str:
    parts = [EVIDENCE[r["evidence"]]]
    refs = []
    for ref in r.get("lean", []):
        url = f"https://github.com/{OWNER}/{ent['slug']}/blob/{r['audited_commit']}/{ref['file']}#L{ref['line']}"
        refs.append(f"[`{ref['decl']}`]({url})")
    if refs:
        parts.append("declaration" + ("s " if len(refs) > 1 else " ") + ", ".join(refs))
    if r.get("axioms"):
        parts.append(f"axioms: {r['axioms']}")
    text = "; ".join(parts) + "."
    note = str(r.get("evidence_note") or "").strip()
    if note:
        text += " " + note[0].upper() + note[1:] + ("" if note.endswith((".", "!", "?")) else ".")
    return text


def upstream_note(ent: dict[str, Any], live: dict[str, Any] | None) -> str | None:
    """One sentence when the source repository has moved past the archived pin."""
    state = ((live or {}).get("repos") or {}).get(ent["slug"]) or {}
    if state.get("sync_status") != "AHEAD_OF_PIN":
        return None
    tag = state.get("latest_release_tag")
    newer = f" (latest release `{tag}`)" if tag and tag != ent["version"] else ""
    return (
        f"The source repository has commits newer than the archived pin{newer}. "
        "They are not covered by this audit."
    )


def render_result(r: dict[str, Any], ent: dict[str, Any], live: dict[str, Any] | None = None) -> list[str]:
    n = r["n"]
    out = [f'<a id="r{n}"></a>', f"### R{n}. {r['title']}", ""]
    if r["status"] == "WITHDRAWN":
        out += [f"**Withdrawn.** {r['withdrawn_reason']}", ""]
        return out
    out.append(f"- **Statement.** {r['statement']}")
    asked = r.get("asked_in")
    if asked and asked.get("citation"):
        loc = f", {asked['locator']}" if asked.get("locator") else ""
        # Only section A answers the cited question; elsewhere the citation is context.
        label = "Asked in" if r["kind"] == "ANSWERS_PUBLISHED_QUESTION" else "Related source"
        out.append(f"- **{label}.** [{asked['citation']}]({asked['url']}){loc}.")
    out.append(f"- **Evidence.** {evidence_line(r, ent)}")
    audit = r["audit"]
    out.append(
        f"- **Audit ({audit['date']}).** {REBUILD[audit['rebuild']]}; "
        f"{FIDELITY[audit['fidelity']]}; prior work: {PRIOR_WORK[audit['prior_work']]}."
    )
    if r["audited_commit"] != ent["pinned_commit"]:
        out.append(
            f"- **Re-audit pending.** Audited at commit `{r['audited_commit'][:7]}`; "
            f"the archive pin has since moved to `{ent['pinned_commit'][:7]}`."
        )
    for lim in r.get("limits", []):
        out.append(f"- **Limit.** {lim}")
    note = upstream_note(ent, live)
    if note:
        out.append(f"- **Upstream.** {note}")
    if r.get("check"):
        out.append(f"- **Check it.** `{r['check']}`")
    src = [f"[{ent['slug']}]({ent['repository']}) `{ent['version']}`", f"archive entry `{r['archive_id']}`"]
    if ent.get("pdf"):
        src.append(f"[paper]({ent['pdf']})")
    out.append(f"- **Source.** {' · '.join(src)}")
    out.append("")
    return out


def render_results_md(root: Path, ledger: dict[str, Any], index: dict[str, dict[str, Any]]) -> str:
    counts = counts_by_kind(ledger)
    active = [r for r in ledger["results"] if r["status"] == "ACTIVE"]
    entries = sorted({r["archive_id"] for r in active})
    author = ledger["author"]
    live = live_index(root)
    lines = [
        "# Results Ledger",
        "",
        "One numbered list of what this body of work has established, and what it has not.",
        "Generated by `scripts/build_ledger.py` from `registry/RESULTS_LEDGER.json`; do not edit by hand.",
        "",
        f"**Author:** {author['full_name']} ({author['affiliation']}, "
        f"ORCID [`{author['orcid']}`](https://orcid.org/{author['orcid']}))",
        "",
        "## Read this first",
        "",
    ]
    for item in ledger.get("read_first", []):
        lines.append(f"- {item}")
    atlas = atlas_line(root)
    if atlas:
        lines.append(f"- {atlas}")
    lines += ["", "## At a glance", "", f"{len(active)} results from {len(entries)} archive entries."]
    slugs = sorted({index[aid]["slug"] for aid in entries})
    states = [(live["repos"].get(s) or {}).get("sync_status") for s in slugs]
    if live["synced_utc"] and any(s in ("EXACT_PIN_MATCH", "AHEAD_OF_PIN") for s in states):
        lines += [
            "",
            f"Source repositories at the last live sync (`{live['synced_utc']}`): "
            f"{states.count('EXACT_PIN_MATCH')} of {len(slugs)} match the archived pin exactly, "
            f"{states.count('AHEAD_OF_PIN')} have newer commits that this ledger does not cover.",
        ]
    lines += ["", "| Section | Kind | Results | Meaning |", "|---|---|---:|---|"]
    for kind, (letter, title, meaning, _one, _many) in KINDS.items():
        lines.append(f"| [{letter}](#section-{letter.lower()}) | {title} | {counts[kind]} | {cell(meaning)} |")
    lines += ["", "## All results", "", "| No. | Result | Kind | Evidence | Entry |", "|---:|---|---|---|---|"]
    for r in ledger["results"]:
        ent = index[r["archive_id"]]
        letter = KINDS[r["kind"]][0]
        title = r["title"] if r["status"] == "ACTIVE" else f"~~{r['title']}~~ (withdrawn)"
        lines.append(
            f"| [R{r['n']}](#r{r['n']}) | {cell(title)} | {letter} | {EVIDENCE[r['evidence']]} | "
            f"`{r['archive_id']}` {ent['version']} |"
        )
    lines.append("")
    for kind, (letter, title, meaning, _one, _many) in KINDS.items():
        group = [r for r in ledger["results"] if r["kind"] == kind]
        lines += [f'<a id="section-{letter.lower()}"></a>', f"## {letter}. {title}", "", f"*{meaning}*", ""]
        if not group:
            lines += ["None recorded.", ""]
        for r in group:
            lines += render_result(r, index[r["archive_id"]], live)

    reasons = ledger.get("entries_without_results") or {}
    pending = pending_entries(ledger, index)
    lines += ["## Archive entries without their own results", ""]
    if reasons:
        lines += ["| Entry | Repository | Reason |", "|---|---|---|"]
        for aid in sorted(reasons):
            ent = index[aid]
            lines.append(f"| `{aid}` | [{ent['slug']}]({ent['repository']}) | {cell(reasons[aid])} |")
        lines.append("")
    if pending:
        lines += ["Registered in the archive but not yet audited into this ledger:", ""]
        for aid in pending:
            ent = index[aid]
            lines.append(f"- `{aid}` [{ent['slug']}]({ent['repository']}) `{ent['version']}`")
        lines.append("")
    if not reasons and not pending:
        lines += ["Every registered entry has results above.", ""]

    lines += ["## Not claimed", ""]
    for item in ledger.get("not_claimed", []):
        lines.append(f"- {item}")
    lines += ["", "## How a result gets on this list", ""]
    for i, step in enumerate(ledger.get("admission_rules", []), 1):
        lines.append(f"{i}. {step}")
    lines += ["", "## How to challenge a result", ""]
    for item in ledger.get("challenge", []):
        lines.append(f"- {item}")
    lines.append("")
    return "\n".join(lines)


def render_readme_block(root: Path, ledger: dict[str, Any], index: dict[str, dict[str, Any]]) -> str:
    counts = counts_by_kind(ledger)
    active = [r for r in ledger["results"] if r["status"] == "ACTIVE"]
    summary = " · ".join(
        count_phrase(k, counts[k]) for k in KINDS if counts[k]
    )
    lines = [
        BLOCK_START,
        "## Results at a glance",
        "",
        f"**{len(active)} audited results.** {summary}. "
        "None is peer reviewed. " + atlas_line(root),
        "",
        "Full numbered list with statements, evidence, limits and check commands: **[RESULTS.md](RESULTS.md)**.",
        "",
    ]
    headline_kinds = ("ANSWERS_PUBLISHED_QUESTION", "NEW_THEOREM", "BOUNDED_CASE", "REFUTATION")
    for kind in headline_kinds:
        group = [r for r in active if r["kind"] == kind]
        if not group:
            continue
        lines += [f"**{KINDS[kind][1]}**", ""]
        for r in group:
            lines.append(f"- [R{r['n']}](RESULTS.md#r{r['n']}) {r['title']} (`{r['archive_id']}`)")
        lines.append("")
    rest = [k for k in KINDS if k not in headline_kinds and counts[k]]
    if rest:
        lines.append(
            "Also in the ledger: "
            + "; ".join(f"{count_phrase(k, counts[k])} (section {KINDS[k][0]})" for k in rest)
            + "."
        )
        lines.append("")
    lines.append(BLOCK_END)
    return "\n".join(lines)


def apply_readme_block(readme: str, block: str) -> str | None:
    if BLOCK_START not in readme or BLOCK_END not in readme:
        return None
    pattern = re.compile(re.escape(BLOCK_START) + r".*?" + re.escape(BLOCK_END), re.S)
    return pattern.sub(lambda _m: block, readme, count=1)


def _load(root: Path) -> tuple[dict[str, Any] | None, dict[str, dict[str, Any]], list[str]]:
    ledger_path = root / "registry" / "RESULTS_LEDGER.json"
    if not ledger_path.exists():
        return None, {}, ["registry/RESULTS_LEDGER.json is missing"]
    try:
        ledger = load_json(ledger_path)
    except (OSError, json.JSONDecodeError) as exc:
        return None, {}, [f"registry/RESULTS_LEDGER.json cannot be read ({exc})"]
    index = registry_index(root)
    return ledger, index, validate(ledger, index)


def _rendered(root: Path, ledger: dict[str, Any], index: dict[str, dict[str, Any]]) -> tuple[str, str, str | None]:
    readme_path = root / "README.md"
    readme = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""
    return (
        render_results_md(root, ledger, index),
        readme,
        apply_readme_block(readme, render_readme_block(root, ledger, index)),
    )


def render_to_disk(root: Path) -> list[str]:
    """Validate the ledger and rewrite RESULTS.md and the README block. Returns problems (empty = ok)."""
    ledger, index, errors = _load(root)
    if errors or ledger is None:
        return [f"RESULTS_LEDGER: {e}" for e in errors]
    results_md, readme, new_readme = _rendered(root, ledger, index)
    write_utf8_lf(root / "RESULTS.md", results_md)
    if new_readme is not None and new_readme != readme:
        write_utf8_lf(root / "README.md", new_readme)
    return []


def check_on_disk(root: Path) -> list[str]:
    """Validate the ledger and confirm RESULTS.md and the README block are current."""
    ledger, index, errors = _load(root)
    if errors or ledger is None:
        return [f"RESULTS_LEDGER: {e}" for e in errors]
    results_md, readme, new_readme = _rendered(root, ledger, index)
    stale: list[str] = []
    out = root / "RESULTS.md"
    if not out.exists() or out.read_text(encoding="utf-8") != results_md:
        stale.append("RESULTS.md is out of date (run: python scripts/build_ledger.py)")
    if new_readme is None:
        stale.append("README.md has no RESULTS_LEDGER block")
    elif new_readme != readme:
        stale.append("README.md RESULTS_LEDGER block is out of date (run: python scripts/build_ledger.py)")
    return stale


def main() -> int:
    parser = argparse.ArgumentParser(description="Render or check the Results Ledger.")
    parser.add_argument("--check", action="store_true", help="verify only; exit 1 on any problem")
    parser.add_argument("--checkouts", type=Path, default=None,
                        help="directory of clones (DIR/<slug>) used to confirm Lean declaration locations")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()

    root: Path = args.root
    problems = check_on_disk(root) if args.check else render_to_disk(root)
    ledger, index, _ = _load(root)
    if not problems and ledger is not None and args.checkouts is not None:
        problems = check_declarations(ledger, index, args.checkouts)
    if problems or ledger is None:
        print("RESULTS LEDGER FAILED:")
        for e in problems:
            print(f"  - {e}")
        return 1

    counts = counts_by_kind(ledger)
    pending = pending_entries(ledger, index)
    moved = sum(1 for r in ledger["results"] if r["audited_commit"] != index[r["archive_id"]]["pinned_commit"])
    print(
        f"PASS: Results Ledger {'verified' if args.check else 'rendered'}: {sum(counts.values())} active results ("
        + ", ".join(f"{KINDS[k][0]}={counts[k]}" for k in KINDS)
        + f"), {moved} awaiting re-audit after a pin move, {len(pending)} registered entries not yet in the ledger."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
