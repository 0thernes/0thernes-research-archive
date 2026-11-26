#!/usr/bin/env python3
"""
Cryptographic & structural integrity auditor for the 0thernes Research Archive.

Checks:
  1. Schema validity and canonical ORCID (0009-0006-8168-9648) on every entry across:
     - Tier I:   registry/PAPERS.json (standalone research preprints)
     - Tier II:  registry/BUILD_PAPERS.json (build white papers & embedded Lean 4 suites)
     - Tier III: registry/LAWS_AND_DISCOVERIES.json (public laws, pre-registered claims,
                 empirical discoveries, finite certificates & open-problem atlases)
     - Bridge:   registry/SOLVED_AND_ATLAS_BRIDGE.json (Mega-Atlas V2 cross-map)
     - Mirror:   registry/LIVE_ECOSYSTEM_MIRROR.json (live upstream repo sync state)
  2. Byte-for-byte SHA-256 verification of every archived frozen PDF, Lean file, white
     paper, and discovery snapshot against registry manifests and CHECKSUMS.sha256.
  3. Presence of per-entry METADATA.json and EVIDENCE.md dossiers across all tiers.
  4. Exact Git submodule commit pin matching registry manifests for all public pinned repos.
  5. Strict standard Lean axiom allowlist ([propext, Classical.choice, Quot.sound]).
  6. Zero broken relative markdown links across root, docs/, registry/, and dossier files.
  7. Active identity hygiene (zero unformed '0thernes LLC' assertions in active headers/registries)
     and A24 artifact size guard (< 5 MB per archived file).

Optional flags:
  --sync   Regenerate per-entry METADATA.json, EVIDENCE.md, registry markdown indexes,
           CHECKSUMS.sha256, and data/MANIFEST.sha256 before verifying.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any
from urllib.parse import unquote


def write_utf8_lf(path: Path, text: str) -> None:
    """Write deterministic UTF-8/LF bytes on every supported Python/OS pair."""
    path.write_bytes(text.encode("utf-8"))

EXPECTED_ORCID = "0009-0006-8168-9648"
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
MAX_TRACKED_ARTIFACT_BYTES = 5_000_000
PRIVATE_DENYLIST = ("0thernes-private-research-vault", "gigachad-browser", "grade-a-standard")
ACTIVE_IDENTITY_FILES = (
    "README.md",
    "LICENSE",
    "NOTICE",
    "CITATION.cff",
    "AGENTS.md",
    "CLAIMS.md",
    "LIMITATIONS.md",
    "scripts/register_paper.py",
)
MD_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def render_evidence_md(paper: dict[str, Any]) -> str:
    lv = paper["lean_verification"]
    pres = paper["preservation"]
    lines = [
        f"# Evidence & Falsification Dossier — `{paper['id']}`",
        "",
        f"**Title:** {paper['title']}  ",
        f"**Author:** {paper['author']} ({paper['affiliation']}, ORCID [`{paper['orcid']}`](https://orcid.org/{paper['orcid']}))  ",
        f"**Domain:** {paper['domain']}  ",
        f"**Version / Date:** `{paper['version']}` ({paper['date_released']})  ",
        f"**Status:** {paper['peer_review_status']}",
        "",
        "## Cryptographic Identity & Provenance",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Source Repository | {paper['repository']} |",
        f"| Pinned Git Submodule | `{paper['submodule_path']}` @ `{paper['pinned_commit']}` |",
        f"| GitHub Release | {paper['release_url']} |",
        f"| Frozen Archived PDF | `{paper['pdf_archive_path']}` |",
        f"| Frozen PDF SHA-256 | `{paper['pdf_sha256']}` |",
        f"| arXiv / Source Bundle SHA-256 | `{paper['arxiv_bundle_sha256']}` |",
        f"| CI Verification Run | {paper['ci_run_url'] or 'Local verification (see repository)'} |",
        f"| Software Heritage SWHID | `{pres['software_heritage'] or 'Pending manual Save Code Now'}` |",
        f"| Wayback Machine Snapshot | {pres['wayback_machine'] or 'Not yet captured'} |",
        f"| External DOI | {pres['doi'] or 'None claimed'} |",
        "",
        "## Core Result",
        "",
        paper["core_result"],
        "",
        "## Lean 4 Formal Verification & Axiom Allowlist",
        "",
        f"- **Framework:** {lv['framework']}",
        f"- **Library Entry Point:** `{lv['entry_point']}`",
        f"- **Primary Axiom Audit Script:** `{lv['axiom_audit_file']}`",
        f"- **Permitted Axioms:** `{', '.join(lv['axiom_allowlist'])}`",
    ]
    if lv.get("additional_audit_files"):
        lines.append(f"- **Additional Audit Scripts:** `{', '.join(lv['additional_audit_files'])}`")
    if paper.get("component_manuscripts"):
        lines.extend(["", "## Preserved Component Manuscripts (Historical Provenance)", ""])
        lines.extend(
            f"- **{cm['title']}** (`{cm['historical_release']}`, `{cm['repo_path']}`): {cm['note']}"
            for cm in paper["component_manuscripts"]
        )
    lines.extend(
        [
            "",
            "## Verification Boundary (Honest Epistemic Scope)",
            "",
            paper["verification_boundary"],
            "",
            "## Independent Reproduction & Falsification Protocol",
            "",
            "To verify or attempt to falsify this paper from scratch:",
            "",
            "```bash",
            "git clone --recursive https://github.com/0thernes/0thernes-research-archive.git",
            "cd 0thernes-research-archive",
            paper["falsification_command"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def render_build_evidence_md(b: dict[str, Any]) -> str:
    lv = b["lean_verification"]
    lines = [
        f"# Build White Paper & Proof Evidence Dossier — `{b['id']}`",
        "",
        f"**Title:** {b['title']}  ",
        f"**Author:** {b['author']} ({b['affiliation']}, ORCID [`{b['orcid']}`](https://orcid.org/{b['orcid']}))  ",
        f"**Domain:** {b['domain']}  ",
        f"**Version / Date:** `{b['version']}` ({b['date']})",
        "",
        "## Cryptographic Identity & Provenance",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Source Repository | {b['repository']} |",
        f"| Pinned Git Submodule | `{b['submodule_path']}` @ `{b['pinned_commit']}` |",
    ]
    if b.get("secondary_branch_ref"):
        lines.append(f"| Additional Branch Ref | `{b['secondary_branch_ref']}` |")
    for art in b["archived_artifacts"]:
        lines.append(f"| Archived Artifact | `{art['path']}` (from `{art['source_path']}`) |")
        lines.append(f"| Artifact SHA-256 | `{art['sha256']}` |")
    lines.extend(
        [
            "",
            "## Summary",
            "",
            b["summary"],
            "",
            "## Embedded Lean 4 Proof Suite Audit",
            "",
            f"- **Framework:** {lv['framework']}",
            f"- **Lean Modules / Lines:** {lv['modules']} files / {lv['lines']} lines",
            f"- **Audited Theorems (`#print axioms`):** {lv['audited_theorems']}",
            f"- **Entry Point:** `{lv['entry_point'] or 'N/A'}`",
            f"- **Permitted Axioms:** `{', '.join(lv['axiom_allowlist']) if lv['axiom_allowlist'] else ('NONE (zero axioms)' if lv['has_lean'] else 'N/A')}`",
            f"- **Live Audit Status:** {lv['live_audit_status']}",
            *( [f"- **Reflection Axiom Disclosure:** {lv['reflection_axioms_note']}"] if lv.get("reflection_axioms_note") else [] ),
            "",
            "## Verification Boundary",
            "",
            b["verification_boundary"],
            "",
            "## Independent Reproduction & Falsification Protocol",
            "",
            "```bash",
            "git clone --recursive https://github.com/0thernes/0thernes-research-archive.git",
            "cd 0thernes-research-archive",
            b["falsification_command"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def render_disc_evidence_md(d: dict[str, Any]) -> str:
    lines = [
        f"# Discovery / Law / Pre-Registered Evidence Dossier — `{d['id']}`",
        "",
        f"**Title:** {d['title']}  ",
        f"**Author:** {d['author']} ({d['affiliation']}, ORCID [`{d['orcid']}`](https://orcid.org/{d['orcid']}))  ",
        f"**Epistemic Tier:** `{d['epistemic_tier']}`  ",
        f"**Domain:** {d['domain']} · **Date:** {d['date']}",
        "",
        "## Source Provenance & Frozen Snapshots",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Source Repository | {d['repository']} |",
        f"| Branch / Ref | `{d['branch']}` @ `{d['pinned_commit']}` |",
    ]
    for art in d["archived_artifacts"]:
        lines.append(f"| Frozen Snapshot | `{art['path']}` (from `{art['source_path']}`) |")
        lines.append(f"| Snapshot SHA-256 | `{art['sha256']}` |")
    lines.extend(
        [
            "",
            "## Summary",
            "",
            d["summary"],
            "",
            "## Verification Boundary (Honest Epistemic Scope)",
            "",
            d["verification_boundary"],
            "",
        ]
    )
    return "\n".join(lines)


def render_papers_md(data: dict[str, Any]) -> str:
    arch = data["archive"]
    author = arch["author"]
    lines = [
        "# Master Paper Registry — Tier I: Standalone Research Preprints",
        "",
        f"**Author:** {author['full_name']} ({arch['organization']}, {arch['location']})  ",
        f"**ORCID:** [`{author['orcid']}`]({author['orcid_url']}) · **GitHub:** {author['github']} · **Updated:** `{arch['updated_utc']}`",
        "",
        "| ID | Date | Version | Domain | Title | Frozen PDF SHA-256 (prefix) | Repo / Evidence |",
        "|---|---|---|---|---|---|---|",
    ]
    for p in data["papers"]:
        pdir = Path(p["pdf_archive_path"]).parent.as_posix()
        lines.append(
            f"| `{p['id']}` | {p['date_released']} | `{p['version']}` | {p['domain']} | "
            f"[{p['title']}](../{p['pdf_archive_path']}) | `{p['pdf_sha256'][:12]}…` | "
            f"[Repo]({p['repository']}) · [Evidence](../{pdir}/EVIDENCE.md) |"
        )
    lines.append("")
    lines.append("---")
    lines.append("")
    for p in data["papers"]:
        pdir = Path(p["pdf_archive_path"]).parent.as_posix()
        lines.extend(
            [
                f"## {p['id']} — {p['title']}",
                "",
                f"- **Domain:** {p['domain']} · **Release:** [`{p['version']}`]({p['release_url']}) ({p['date_released']})",
                f"- **Pinned Commit:** `{p['pinned_commit']}` (`{p['submodule_path']}`)",
                f"- **Frozen PDF:** [`{p['pdf_archive_path']}`](../{p['pdf_archive_path']}) (SHA-256: `{p['pdf_sha256']}`)",
                f"- **Lean 4 Audit:** {p['lean_verification']['framework']} · Allowlist: `{', '.join(p['lean_verification']['axiom_allowlist'])}`",
                f"- **Summary:** {p['core_result']}",
                f"- **Verification Boundary:** {p['verification_boundary']}",
                f"- **Dossier:** [`EVIDENCE.md`](../{pdir}/EVIDENCE.md) · [`METADATA.json`](../{pdir}/METADATA.json)",
                "",
            ]
        )
    return "\n".join(lines)


def render_builds_md(bdata: dict[str, Any]) -> str:
    author = bdata["author"]
    total_lean_thms = sum(b["lean_verification"]["audited_theorems"] for b in bdata["builds"])
    total_lean_lines = sum(b["lean_verification"]["lines"] for b in bdata["builds"])
    lines = [
        "# Tier II — Public Build White Papers & Embedded Lean 4 Proof Suites",
        "",
        f"**Author:** {author['full_name']} ({author['affiliation']}) · **ORCID:** [`{author['orcid']}`](https://orcid.org/{author['orcid']})  ",
        f"**Public Embedded Pure Lean 4.35.0 Proofs Audited:** {total_lean_thms} declarations across {total_lean_lines:,} lines (zero Mathlib, zero `sorry`)  ",
        f"**Updated:** `{bdata['updated_utc']}`",
        "",
        "| ID | Date | Repo / Version | Embedded Lean 4 Proofs | Frozen White Paper / Audit | Dossier |",
        "|---|---|---|---|---|---|",
    ]
    for b in bdata["builds"]:
        lv = b["lean_verification"]
        lean_str = (
            f"{lv['audited_theorems']} decls ({lv['modules']} files, {lv['lines']} lines)"
            if lv["has_lean"]
            else "Audit / Methodology (non-Lean)"
        )
        primary_art = b["archived_artifacts"][0]["path"]
        bdir = Path(primary_art).parent.as_posix()
        lines.append(
            f"| `{b['id']}` | {b['date']} | [`{b['slug']}`]({b['repository']}) `{b['version']}` | "
            f"{lean_str} | [{Path(primary_art).name}](../{primary_art}) | "
            f"[Evidence](../{bdir}/EVIDENCE.md) |"
        )
    lines.append("")
    lines.append("---")
    lines.append("")
    for b in bdata["builds"]:
        primary_art = b["archived_artifacts"][0]["path"]
        bdir = Path(primary_art).parent.as_posix()
        lv = b["lean_verification"]
        lines.extend(
            [
                f"## {b['id']} — {b['title']}",
                "",
                f"- **Repository:** {b['repository']} (`{b['version']}`, pinned `{b['pinned_commit'][:12]}` at `{b['submodule_path']}`)",
                f"- **Lean 4 Audit:** {lv['live_audit_status']}",
                f"- **Summary:** {b['summary']}",
                f"- **Verification Boundary:** {b['verification_boundary']}",
                f"- **Dossier:** [`EVIDENCE.md`](../{bdir}/EVIDENCE.md) · [`METADATA.json`](../{bdir}/METADATA.json)",
                "",
            ]
        )
    return "\n".join(lines)


def render_discoveries_md(ddata: dict[str, Any]) -> str:
    author = ddata["author"]
    total_snaps = sum(len(d["archived_artifacts"]) for d in ddata["discoveries"])
    lines = [
        "# Tier III — Public Laws, Pre-Registered Empirical Claims, Discoveries & Open-Problem Atlases",
        "",
        f"**Author:** {author['full_name']} ({author['affiliation']}) · **ORCID:** [`{author['orcid']}`](https://orcid.org/{author['orcid']})  ",
        f"**Totals:** {len(ddata['discoveries'])} public registries · {total_snaps} SHA-256 frozen snapshots  ",
        f"**Updated:** `{ddata['updated_utc']}`",
        "",
        "> **Epistemic Discipline:** Tier III entries preserve binding architectural laws, SHA-256-locked pre-registrations, controlled empirical discoveries (including null/falsified results), finite computational certificates, and structured open-problem atlases. None of these are represented as Lean-proved general mathematical theorems.",
        "",
        "| ID | Date | Epistemic Tier | Source Repo | Title | Snapshots | Dossier |",
        "|---|---|---|---|---|---:|---|",
    ]
    for d in ddata["discoveries"]:
        first_art = d["archived_artifacts"][0]["path"]
        ddir = Path(first_art).parent.as_posix()
        lines.append(
            f"| `{d['id']}` | {d['date']} | `{d['epistemic_tier']}` | "
            f"[`{d['repository'].split('/')[-1]}`]({d['repository']}) | {d['title']} | "
            f"{len(d['archived_artifacts'])} | [Evidence](../{ddir}/EVIDENCE.md) |"
        )
    lines.append("")
    lines.append("---")
    lines.append("")
    for d in ddata["discoveries"]:
        first_art = d["archived_artifacts"][0]["path"]
        ddir = Path(first_art).parent.as_posix()
        lines.extend(
            [
                f"## {d['id']} — {d['title']}",
                "",
                f"- **Epistemic Tier:** `{d['epistemic_tier']}` · **Repository:** {d['repository']} (`{d['branch']}` @ `{d['pinned_commit'][:12]}`)",
                f"- **Summary:** {d['summary']}",
                f"- **Verification Boundary:** {d['verification_boundary']}",
                f"- **Dossier:** [`EVIDENCE.md`](../{ddir}/EVIDENCE.md) · [`METADATA.json`](../{ddir}/METADATA.json)",
                "",
            ]
        )
    return "\n".join(lines)


def sync_derived_files(
    root: Path,
    data: dict[str, Any],
    bdata: dict[str, Any] | None,
    ddata: dict[str, Any] | None,
) -> None:
    checksum_entries: list[tuple[str, str]] = []

    for paper in data["papers"]:
        pdf_rel = paper["pdf_archive_path"]
        pdf_abs = root / pdf_rel
        pdir = pdf_abs.parent
        pdir.mkdir(parents=True, exist_ok=True)

        meta_path = pdir / "METADATA.json"
        write_utf8_lf(meta_path, json.dumps(paper, indent=2) + "\n")

        ev_path = pdir / "EVIDENCE.md"
        write_utf8_lf(ev_path, render_evidence_md(paper))

        checksum_entries.append((sha256_file(pdf_abs), pdf_rel))
        checksum_entries.append((sha256_file(meta_path), meta_path.relative_to(root).as_posix()))
        for cm in paper.get("component_manuscripts", []):
            cm_name = Path(cm["repo_path"]).name
            cm_abs = pdir / cm_name
            if cm_abs != pdf_abs and cm_abs.exists():
                checksum_entries.append((sha256_file(cm_abs), cm_abs.relative_to(root).as_posix()))

    write_utf8_lf(root / "registry" / "PAPERS.md", render_papers_md(data))
    reg_json = root / "registry" / "PAPERS.json"
    write_utf8_lf(reg_json, json.dumps(data, indent=2) + "\n")
    checksum_entries.append((sha256_file(reg_json), "registry/PAPERS.json"))

    if bdata is not None:
        for b in bdata["builds"]:
            first_rel = b["archived_artifacts"][0]["path"]
            bdir = (root / first_rel).parent
            bdir.mkdir(parents=True, exist_ok=True)

            meta_path = bdir / "METADATA.json"
            write_utf8_lf(meta_path, json.dumps(b, indent=2) + "\n")

            ev_path = bdir / "EVIDENCE.md"
            write_utf8_lf(ev_path, render_build_evidence_md(b))

            checksum_entries.append((sha256_file(meta_path), meta_path.relative_to(root).as_posix()))
            for art in b["archived_artifacts"]:
                art_abs = root / art["path"]
                checksum_entries.append((sha256_file(art_abs), art["path"]))

        write_utf8_lf(root / "registry" / "BUILD_PAPERS.md", render_builds_md(bdata))
        breg_json = root / "registry" / "BUILD_PAPERS.json"
        write_utf8_lf(breg_json, json.dumps(bdata, indent=2) + "\n")
        checksum_entries.append((sha256_file(breg_json), "registry/BUILD_PAPERS.json"))

    if ddata is not None:
        for d in ddata["discoveries"]:
            first_rel = d["archived_artifacts"][0]["path"]
            ddir = (root / first_rel).parent
            ddir.mkdir(parents=True, exist_ok=True)

            meta_path = ddir / "METADATA.json"
            write_utf8_lf(meta_path, json.dumps(d, indent=2) + "\n")

            ev_path = ddir / "EVIDENCE.md"
            write_utf8_lf(ev_path, render_disc_evidence_md(d))

            checksum_entries.append((sha256_file(meta_path), meta_path.relative_to(root).as_posix()))
            for art in d["archived_artifacts"]:
                art_abs = root / art["path"]
                checksum_entries.append((sha256_file(art_abs), art["path"]))

        write_utf8_lf(root / "registry" / "LAWS_AND_DISCOVERIES.md", render_discoveries_md(ddata))
        dreg_json = root / "registry" / "LAWS_AND_DISCOVERIES.json"
        write_utf8_lf(dreg_json, json.dumps(ddata, indent=2) + "\n")
        checksum_entries.append((sha256_file(dreg_json), "registry/LAWS_AND_DISCOVERIES.json"))

    for extra_rel in (
        "registry/SOLVED_AND_ATLAS_BRIDGE.json",
        "registry/LIVE_ECOSYSTEM_MIRROR.json",
        "registry/UPSTREAM_RELEASE_SNAPSHOTS.json",
    ):
        extra_abs = root / extra_rel
        if extra_abs.exists():
            checksum_entries.append((sha256_file(extra_abs), extra_rel))

    snapshot_path = root / "registry" / "UPSTREAM_RELEASE_SNAPSHOTS.json"
    if snapshot_path.exists():
        snapshots = json.loads(snapshot_path.read_text(encoding="utf-8"))
        for snapshot in snapshots.get("snapshots", []):
            for artifact in snapshot.get("artifacts", []):
                artifact_path = root / artifact["path"]
                if artifact_path.exists():
                    checksum_entries.append((sha256_file(artifact_path), artifact["path"]))

    checksums_text = (
        "\n".join(f"{digest}  {rel}" for digest, rel in sorted(checksum_entries, key=lambda x: x[1])) + "\n"
    )
    checksums_path = root / "CHECKSUMS.sha256"
    write_utf8_lf(checksums_path, checksums_text)
    data_manifest = root / "data" / "MANIFEST.sha256"
    data_manifest.parent.mkdir(parents=True, exist_ok=True)
    write_utf8_lf(data_manifest, checksums_text)
    freeze_entries = [
        (digest, rel)
        for digest, rel in sorted(checksum_entries, key=lambda x: x[1])
        if rel not in {
            "registry/LIVE_ECOSYSTEM_MIRROR.json",
            "registry/UPSTREAM_RELEASE_SNAPSHOTS.json",
        }
        and not rel.startswith("builds/0TH-BUILD-004_unsolved-mathematics/releases/")
    ]
    freeze_text = "\n".join(f"{digest}  {rel}" for digest, rel in freeze_entries) + "\n"
    write_utf8_lf(root / "data" / "RELEASE_FREEZE.sha256", freeze_text)
    bcount = len(bdata["builds"]) if bdata else 0
    dcount = len(ddata["discoveries"]) if ddata else 0
    print(
        f"Synced {len(data['papers'])} Tier-I papers + {bcount} Tier-II builds + {dcount} Tier-III discoveries, "
        f"registry markdowns, CHECKSUMS.sha256, data/MANIFEST.sha256 ({len(checksum_entries)} hashed files), "
        f"and data/RELEASE_FREEZE.sha256 ({len(freeze_entries)} frozen release files)."
    )


def get_git_submodule_commits(root: Path) -> dict[str, str]:
    res = subprocess.run(
        ["git", "ls-files", "--stage", "repos"],
        cwd=root,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    pins: dict[str, str] = {}
    if res.returncode == 0:
        for line in res.stdout.splitlines():
            parts = line.split()
            if len(parts) >= 4 and parts[0] == "160000":
                pins[parts[3]] = parts[1]
    return pins


def check_markdown_links(root: Path) -> list[str]:
    """Verify every relative markdown link in archive-authored docs resolves to an existing path."""
    broken: list[str] = []
    md_files: list[Path] = []
    md_files.extend(sorted(root.glob("*.md")))
    for sub in ("docs", "registry"):
        d = root / sub
        if d.is_dir():
            md_files.extend(sorted(d.rglob("*.md")))
    for sub in ("papers", "builds", "discoveries"):
        d = root / sub
        if d.is_dir():
            md_files.extend(sorted(d.glob("*/EVIDENCE.md")))

    for md in md_files:
        raw = md.read_text(encoding="utf-8")
        # Strip fenced code blocks and inline code spans so syntax examples do not trigger false positives
        cleaned = re.sub(r"```.*?```", "", raw, flags=re.S)
        cleaned = re.sub(r"`[^`\n]+`", "", cleaned)
        for m in MD_LINK_RE.finditer(cleaned):
            href = m.group(1).strip()
            if not href or href.startswith(("#", "http://", "https://", "mailto:", "file://", "data:")):
                continue
            target_part = unquote(href.split("#", 1)[0].split("?", 1)[0])
            if not target_part:
                continue
            resolved = (md.parent / target_part).resolve()
            if not resolved.exists():
                broken.append(f"Broken markdown link in {md.relative_to(root).as_posix()}: {href}")
    return broken


def check_readme_table_integrity(readme_text: str) -> list[str]:
    """Ensure no blank line splits consecutive 0TH-* registry table rows in README.md."""
    issues: list[str] = []
    lines = readme_text.splitlines()
    prev_was_row = False
    saw_blank = False
    blank_line_no = 0
    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        is_row = stripped.startswith("| `0TH-")
        if is_row:
            if prev_was_row and saw_blank:
                issues.append(
                    f"README.md: blank line at L{blank_line_no} splits consecutive registry table rows before L{idx}"
                )
            prev_was_row = True
            saw_blank = False
        elif stripped == "":
            if prev_was_row and not saw_blank:
                saw_blank = True
                blank_line_no = idx
        else:
            prev_was_row = False
            saw_blank = False
    return issues


def check_readme_counts(
    readme_text: str,
    pcount: int,
    bcount: int,
    dcount: int,
    subcount: int,
    total_build_lean: int,
) -> list[str]:
    """Verify README.md Scope line and Tier II Lean totals match canonical JSON registries."""
    issues: list[str] = []
    total = pcount + bcount + dcount
    expected_scope = (
        f"**{total} public research entries** (`{pcount} Tier I + {bcount} Tier II + {dcount} Tier III`) "
        f"+ **{subcount} pinned public Git submodules**"
    )
    if subcount > 0 and expected_scope not in readme_text:
        issues.append(f"README.md: Scope line does not match exact counts ({expected_scope})")
    if total_build_lean > 0 and f"{total_build_lean:,}" not in readme_text and str(total_build_lean) not in readme_text:
        issues.append(f"README.md: Tier II Lean declaration total ({total_build_lean:,}) missing or stale")
    return issues


def check_rfc3161_tsa(freeze_path: Path, tsr_path: Path) -> list[str]:
    """Verify RFC 3161 DER timestamp response embeds the exact SHA-256 digest of freeze_path."""
    issues: list[str] = []
    if not tsr_path.exists():
        return issues
    if not freeze_path.exists():
        return [f"Missing {freeze_path.name} required by {tsr_path.name}"]
    tsr_bytes = tsr_path.read_bytes()
    if len(tsr_bytes) < 128 or tsr_bytes[0] != 0x30:
        issues.append(f"{tsr_path.name}: invalid RFC 3161 DER structure")
        return issues
    raw_digest = hashlib.sha256(freeze_path.read_bytes()).digest()
    if raw_digest not in tsr_bytes:
        issues.append(f"{tsr_path.name}: embedded SHA-256 digest does not match {freeze_path.name}")
    return issues


def check_upstream_release_snapshots(root: Path) -> list[str]:
    """Verify separately retained upstream release candidates and their digests."""
    issues: list[str] = []
    registry_path = root / "registry" / "UPSTREAM_RELEASE_SNAPSHOTS.json"
    if not registry_path.exists():
        return issues
    try:
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"UPSTREAM_RELEASE_SNAPSHOTS.json: cannot read registry ({exc})"]
    for snapshot in registry.get("snapshots", []):
        label = f"{snapshot.get('repository', 'unknown')} {snapshot.get('release', 'unknown')}"
        if snapshot.get("promotion_status") != "CANDIDATE_SEPARATE_FROM_FROZEN_V0.5.0":
            issues.append(f"{label}: missing explicit separate-candidate status")
        for artifact in snapshot.get("artifacts", []):
            rel = artifact.get("path")
            target = root / rel if rel else None
            if target is None or not target.exists():
                issues.append(f"{label}: missing candidate artifact {rel}")
            elif sha256_file(target) != artifact.get("sha256"):
                issues.append(f"{label}: candidate SHA-256 mismatch for {rel}")
    return issues


def verify_archive(
    root: Path,
    data: dict[str, Any],
    bdata: dict[str, Any] | None,
    ddata: dict[str, Any] | None,
) -> None:
    errors: list[str] = []

    if data["archive"]["author"]["orcid"] != EXPECTED_ORCID:
        errors.append(f"Archive ORCID mismatch: expected {EXPECTED_ORCID}")

    seen_ids: set[str] = set()
    id_to_version: dict[str, str] = {}
    git_pins = get_git_submodule_commits(root)
    readme_txt = (root / "README.md").read_text(encoding="utf-8") if (root / "README.md").exists() else ""

    for p in data["papers"]:
        pid = p["id"]
        if pid in seen_ids:
            errors.append(f"Duplicate ID: {pid}")
        seen_ids.add(pid)
        id_to_version[pid] = str(p["version"])
        if p.get("orcid") != EXPECTED_ORCID:
            errors.append(f"{pid}: ORCID mismatch ({p.get('orcid')})")
        if "0thernes LLC" in str(p.get("affiliation", "")):
            errors.append(f"{pid}: Unformed entity '0thernes LLC' in affiliation")
        axioms = set(p["lean_verification"]["axiom_allowlist"])
        if not axioms.issubset(ALLOWED_AXIOMS):
            errors.append(f"{pid}: Non-standard axioms in allowlist: {axioms - ALLOWED_AXIOMS}")
        if not p.get("verification_boundary"):
            errors.append(f"{pid}: Missing verification_boundary")
        pdf_path = root / p["pdf_archive_path"]
        if not pdf_path.exists():
            errors.append(f"{pid}: Missing archived PDF {p['pdf_archive_path']}")
        else:
            if pdf_path.stat().st_size > MAX_TRACKED_ARTIFACT_BYTES:
                errors.append(f"{pid}: Archived PDF exceeds 5 MB A24 cap ({pdf_path.stat().st_size} bytes)")
            if sha256_file(pdf_path) != p["pdf_sha256"]:
                errors.append(f"{pid}: PDF SHA-256 mismatch")
        pdir = pdf_path.parent
        declared_pdfs = {pdf_path.name}
        for cm in p.get("component_manuscripts", []):
            cm_name = Path(cm["repo_path"]).name
            declared_pdfs.add(cm_name)
            cm_abs = pdir / cm_name
            if cm_abs != pdf_path and cm_abs.exists() and sha256_file(cm_abs) != cm["sha256"]:
                errors.append(f"{pid}: Companion PDF SHA-256 mismatch for {cm_name}")
        errors.extend(
            f"{pid}: Unregistered PDF in archive directory: {disk_pdf.relative_to(root).as_posix()}"
            for disk_pdf in sorted(pdir.glob("*.pdf"))
            if disk_pdf.name not in declared_pdfs
        )
        errors.extend(
            f"{pid}: Missing {pdir.relative_to(root).as_posix()}/{req}"
            for req in ("METADATA.json", "EVIDENCE.md")
            if not (pdir / req).exists()
        )
        sub = p["submodule_path"]
        if git_pins and sub in git_pins:
            if git_pins[sub] != p["pinned_commit"]:
                errors.append(f"{pid}: Submodule {sub} pinned at {git_pins[sub]}, expected {p['pinned_commit']}")
        elif git_pins:
            errors.append(f"{pid}: Submodule {sub} not found in git index")
        if readme_txt:
            row_prefix = f"| `{pid}` |"
            matching = [ln for ln in readme_txt.splitlines() if ln.startswith(row_prefix)]
            if not matching:
                errors.append(f"{pid}: Missing Tier-I table row in README.md")
            elif f"`{p['version']}`" not in matching[0]:
                errors.append(f"{pid}: README.md version does not match PAPERS.json ({p['version']})")

    bcount = 0
    total_build_lean = 0
    if bdata is not None:
        bcount = len(bdata["builds"])
        for b in bdata["builds"]:
            bid = b["id"]
            if bid in seen_ids:
                errors.append(f"Duplicate ID: {bid}")
            seen_ids.add(bid)
            id_to_version[bid] = str(b["version"])
            total_build_lean += int(b["lean_verification"]["audited_theorems"])
            if b.get("orcid") != EXPECTED_ORCID:
                errors.append(f"{bid}: ORCID mismatch ({b.get('orcid')})")
            if "0thernes LLC" in str(b.get("affiliation", "")):
                errors.append(f"{bid}: Unformed entity '0thernes LLC' in affiliation")
            axioms = set(b["lean_verification"]["axiom_allowlist"])
            if not axioms.issubset(ALLOWED_AXIOMS):
                errors.append(f"{bid}: Non-standard axioms in allowlist: {axioms - ALLOWED_AXIOMS}")
            if not b.get("verification_boundary"):
                errors.append(f"{bid}: Missing verification_boundary")
            for art in b["archived_artifacts"]:
                ap = root / art["path"]
                if not ap.exists():
                    errors.append(f"{bid}: Missing archived artifact {art['path']}")
                else:
                    if ap.stat().st_size > MAX_TRACKED_ARTIFACT_BYTES:
                        errors.append(f"{bid}: Artifact exceeds 5 MB A24 cap ({art['path']})")
                    if sha256_file(ap) != art["sha256"]:
                        errors.append(f"{bid}: Artifact SHA-256 mismatch for {art['path']}")
            bdir = (root / b["archived_artifacts"][0]["path"]).parent
            errors.extend(
                f"{bid}: Missing {bdir.relative_to(root).as_posix()}/{req}"
                for req in ("METADATA.json", "EVIDENCE.md")
                if not (bdir / req).exists()
            )
            sub = b["submodule_path"]
            if git_pins and sub in git_pins:
                if git_pins[sub] != b["pinned_commit"]:
                    errors.append(f"{bid}: Submodule {sub} pinned at {git_pins[sub]}, expected {b['pinned_commit']}")
            elif git_pins:
                errors.append(f"{bid}: Submodule {sub} not found in git index")
            if readme_txt:
                row_prefix = f"| `{bid}` |"
                matching = [ln for ln in readme_txt.splitlines() if ln.startswith(row_prefix)]
                if not matching:
                    errors.append(f"{bid}: Missing Tier-II table row in README.md")
                elif b["version"].startswith("v") and f"`{b['version']}`" not in matching[0]:
                    errors.append(f"{bid}: README.md version does not match BUILD_PAPERS.json ({b['version']})")

    dcount = 0
    if ddata is not None:
        dcount = len(ddata["discoveries"])
        for d in ddata["discoveries"]:
            did = d["id"]
            if did in seen_ids:
                errors.append(f"Duplicate ID: {did}")
            seen_ids.add(did)
            if d.get("orcid") != EXPECTED_ORCID:
                errors.append(f"{did}: ORCID mismatch ({d.get('orcid')})")
            if "0thernes LLC" in str(d.get("affiliation", "")):
                errors.append(f"{did}: Unformed entity '0thernes LLC' in affiliation")
            if d.get("visibility") != "PUBLIC":
                errors.append(f"{did}: Non-PUBLIC entry found in public archive!")
            if not d.get("verification_boundary"):
                errors.append(f"{did}: Missing verification_boundary")
            for art in d["archived_artifacts"]:
                ap = root / art["path"]
                if not ap.exists():
                    errors.append(f"{did}: Missing archived snapshot {art['path']}")
                else:
                    if ap.stat().st_size > MAX_TRACKED_ARTIFACT_BYTES:
                        errors.append(f"{did}: Snapshot exceeds 5 MB A24 cap ({art['path']})")
                    if sha256_file(ap) != art["sha256"]:
                        errors.append(f"{did}: Snapshot SHA-256 mismatch for {art['path']}")
            ddir = (root / d["archived_artifacts"][0]["path"]).parent
            errors.extend(
                f"{did}: Missing {ddir.relative_to(root).as_posix()}/{req}"
                for req in ("METADATA.json", "EVIDENCE.md")
                if not (ddir / req).exists()
            )

    bridge_path = root / "registry" / "SOLVED_AND_ATLAS_BRIDGE.json"
    if bridge_path.exists():
        bridge = json.loads(bridge_path.read_text(encoding="utf-8"))
        if bridge.get("author", {}).get("orcid") != EXPECTED_ORCID:
            errors.append("SOLVED_AND_ATLAS_BRIDGE.json: ORCID mismatch")
        if bridge.get("grand_problems_retired") != 0:
            errors.append("SOLVED_AND_ATLAS_BRIDGE.json: grand_problems_retired must be 0")
        solved_count = 0
        for ent in bridge.get("entries", []):
            aid = ent.get("archive_id")
            if aid not in seen_ids:
                errors.append(f"SOLVED_AND_ATLAS_BRIDGE.json: unknown archive_id {aid}")
            elif aid in id_to_version and str(ent.get("version")) != id_to_version[aid]:
                errors.append(
                    f"SOLVED_AND_ATLAS_BRIDGE.json: version mismatch for {aid} "
                    f"(bridge={ent.get('version')}, registry={id_to_version[aid]})"
                )
            if ent.get("grand_atlas_problem_retired") is not False:
                errors.append(f"SOLVED_AND_ATLAS_BRIDGE.json: entry {aid} must not claim grand retirement")
            if ent.get("resolution_class") == "SOLVED_SUB_CONJECTURE":
                solved_count += 1
        declared_solved = bridge.get("epistemic_summary", {}).get("published_open_subconjectures_proved_in_lean")
        if declared_solved != solved_count:
            errors.append(
                f"SOLVED_AND_ATLAS_BRIDGE.json: published_open_subconjectures_proved_in_lean={declared_solved} "
                f"does not match SOLVED_SUB_CONJECTURE entries ({solved_count})"
            )

    mirror_path = root / "registry" / "LIVE_ECOSYSTEM_MIRROR.json"
    if mirror_path.exists():
        mirror_raw = mirror_path.read_text(encoding="utf-8")
        for slug in PRIVATE_DENYLIST:
            if slug in mirror_raw:
                errors.append(f"LIVE_ECOSYSTEM_MIRROR.json: privacy firewall violation ({slug})")
        mirror = json.loads(mirror_raw)
        if mirror.get("privacy_firewall") != "PUBLIC_NON_FORK_0THERNES_ONLY":
            errors.append("LIVE_ECOSYSTEM_MIRROR.json: missing PUBLIC_NON_FORK_0THERNES_ONLY firewall declaration")
        mcounts = mirror.get("counts") or {}
        expected_total = len(data["papers"]) + bcount + dcount
        if mcounts.get("total_entries") != expected_total:
            errors.append(
                f"LIVE_ECOSYSTEM_MIRROR.json: total_entries={mcounts.get('total_entries')} != {expected_total}"
            )
        if git_pins and mcounts.get("pinned_submodules") != len(git_pins):
            errors.append(
                f"LIVE_ECOSYSTEM_MIRROR.json: pinned_submodules={mcounts.get('pinned_submodules')} != {len(git_pins)}"
            )

    if readme_txt:
        errors.extend(check_readme_table_integrity(readme_txt))
        errors.extend(
            check_readme_counts(readme_txt, len(data["papers"]), bcount, dcount, len(git_pins), total_build_lean)
        )

    errors.extend(
        check_rfc3161_tsa(root / "data" / "RELEASE_FREEZE.sha256", root / "data" / "RELEASE_FREEZE.sha256.tsr")
    )
    errors.extend(check_upstream_release_snapshots(root))

    for rel in ACTIVE_IDENTITY_FILES:
        fp = root / rel
        if fp.exists() and "0thernes LLC" in fp.read_text(encoding="utf-8"):
            errors.append(f"Unformed entity '0thernes LLC' found in {rel}")

    errors.extend(check_markdown_links(root))

    checksums_path = root / "CHECKSUMS.sha256"
    if not checksums_path.exists():
        errors.append("Missing CHECKSUMS.sha256")
    else:
        for line in checksums_path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            expected_hash, rel_path = line.split("  ", 1)
            target = root / rel_path
            if not target.exists():
                errors.append(f"CHECKSUMS.sha256 references missing file: {rel_path}")
            elif sha256_file(target) != expected_hash:
                errors.append(f"CHECKSUMS.sha256 mismatch for {rel_path}")

    if errors:
        print("ARCHIVE AUDIT FAILED:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    print(
        f"PASS: Verified {len(data['papers'])} Tier-I papers + {bcount} Tier-II builds + {dcount} Tier-III discoveries, "
        f"bridge & live mirror policies, zero broken markdown links, all SHA-256 digests, CHECKSUMS.sha256, "
        f"ORCID {EXPECTED_ORCID}, axiom allowlists, and {len(git_pins)} pinned PUBLIC Git submodules."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Verify (and optionally sync) 0thernes Research Archive.")
    parser.add_argument("--sync", action="store_true", help="Regenerate dossiers, markdown registries, and CHECKSUMS.sha256")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    data = json.loads((root / "registry" / "PAPERS.json").read_text(encoding="utf-8"))
    bpath = root / "registry" / "BUILD_PAPERS.json"
    bdata = json.loads(bpath.read_text(encoding="utf-8")) if bpath.exists() else None
    dpath = root / "registry" / "LAWS_AND_DISCOVERIES.json"
    ddata = json.loads(dpath.read_text(encoding="utf-8")) if dpath.exists() else None

    if args.sync:
        sync_derived_files(root, data, bdata, ddata)
    verify_archive(root, data, bdata, ddata)


if __name__ == "__main__":
    main()
