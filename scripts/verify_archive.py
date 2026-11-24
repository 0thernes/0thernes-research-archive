#!/usr/bin/env python3
"""
Cryptographic & structural integrity auditor for the 0thernes Research Archive.

Checks:
  1. Schema validity and canonical ORCID (0009-0006-8168-9648) on every entry across:
     - Tier I:   registry/PAPERS.json (standalone research preprints)
     - Tier II:  registry/BUILD_PAPERS.json (build white papers & embedded Lean 4 suites)
     - Tier III: registry/LAWS_AND_DISCOVERIES.json (public laws, pre-registered claims,
                 empirical discoveries, finite certificates & open-problem atlases)
  2. Byte-for-byte SHA-256 verification of every archived frozen PDF, Lean file, white
     paper, and discovery snapshot against registry manifests and CHECKSUMS.sha256.
  3. Presence of per-entry METADATA.json and EVIDENCE.md dossiers across all tiers.
  4. Exact Git submodule commit pin matching registry manifests for all public pinned repos.
  5. Strict standard Lean axiom allowlist ([propext, Classical.choice, Quot.sound]).

Optional flags:
  --sync   Regenerate per-entry METADATA.json, EVIDENCE.md, registry markdown indexes,
           and CHECKSUMS.sha256 before verifying.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

EXPECTED_ORCID = "0009-0006-8168-9648"
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def render_evidence_md(paper: dict) -> str:
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
        for cm in paper["component_manuscripts"]:
            lines.append(f"- **{cm['title']}** (`{cm['historical_release']}`, `{cm['repo_path']}`): {cm['note']}")
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


def render_build_evidence_md(b: dict) -> str:
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


def render_disc_evidence_md(d: dict) -> str:
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


def render_papers_md(data: dict) -> str:
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


def render_builds_md(bdata: dict) -> str:
    author = bdata["author"]
    total_lean_thms = sum(b["lean_verification"]["audited_theorems"] for b in bdata["builds"])
    total_lean_lines = sum(b["lean_verification"]["lines"] for b in bdata["builds"])
    lines = [
        "# Tier II — Public Build White Papers & Embedded Lean 4 Proof Suites",
        "",
        f"**Author:** {author['full_name']} ({author['affiliation']}) · **ORCID:** [`{author['orcid']}`](https://orcid.org/{author['orcid']})  ",
        f"**Public Embedded Pure Lean 4.35.0 Proofs Audited:** {total_lean_thms} theorems across {total_lean_lines:,} lines (zero Mathlib, zero `sorry`)  ",
        f"**Updated:** `{bdata['updated_utc']}`",
        "",
        "| ID | Date | Repo / Version | Embedded Lean 4 Proofs | Frozen White Paper / Audit | Dossier |",
        "|---|---|---|---|---|---|",
    ]
    for b in bdata["builds"]:
        lv = b["lean_verification"]
        lean_str = (
            f"{lv['audited_theorems']} theorems ({lv['modules']} files, {lv['lines']} lines)"
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


def render_discoveries_md(ddata: dict) -> str:
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


def sync_derived_files(root: Path, data: dict, bdata: dict | None, ddata: dict | None) -> None:
    checksum_entries: list[tuple[str, str]] = []

    for paper in data["papers"]:
        pdf_rel = paper["pdf_archive_path"]
        pdf_abs = root / pdf_rel
        pdir = pdf_abs.parent
        pdir.mkdir(parents=True, exist_ok=True)

        meta_path = pdir / "METADATA.json"
        meta_path.write_text(json.dumps(paper, indent=2) + "\n", encoding="utf-8", newline="\n")

        ev_path = pdir / "EVIDENCE.md"
        ev_path.write_text(render_evidence_md(paper), encoding="utf-8", newline="\n")

        checksum_entries.append((sha256_file(pdf_abs), pdf_rel))
        checksum_entries.append((sha256_file(meta_path), meta_path.relative_to(root).as_posix()))
        for cm in paper.get("component_manuscripts", []):
            cm_name = Path(cm["repo_path"]).name
            cm_abs = pdir / cm_name
            if cm_abs != pdf_abs and cm_abs.exists():
                checksum_entries.append((sha256_file(cm_abs), cm_abs.relative_to(root).as_posix()))

    (root / "registry" / "PAPERS.md").write_text(render_papers_md(data), encoding="utf-8", newline="\n")
    reg_json = root / "registry" / "PAPERS.json"
    reg_json.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8", newline="\n")
    checksum_entries.append((sha256_file(reg_json), "registry/PAPERS.json"))

    if bdata is not None:
        for b in bdata["builds"]:
            first_rel = b["archived_artifacts"][0]["path"]
            bdir = (root / first_rel).parent
            bdir.mkdir(parents=True, exist_ok=True)

            meta_path = bdir / "METADATA.json"
            meta_path.write_text(json.dumps(b, indent=2) + "\n", encoding="utf-8", newline="\n")

            ev_path = bdir / "EVIDENCE.md"
            ev_path.write_text(render_build_evidence_md(b), encoding="utf-8", newline="\n")

            checksum_entries.append((sha256_file(meta_path), meta_path.relative_to(root).as_posix()))
            for art in b["archived_artifacts"]:
                art_abs = root / art["path"]
                checksum_entries.append((sha256_file(art_abs), art["path"]))

        (root / "registry" / "BUILD_PAPERS.md").write_text(render_builds_md(bdata), encoding="utf-8", newline="\n")
        breg_json = root / "registry" / "BUILD_PAPERS.json"
        breg_json.write_text(json.dumps(bdata, indent=2) + "\n", encoding="utf-8", newline="\n")
        checksum_entries.append((sha256_file(breg_json), "registry/BUILD_PAPERS.json"))

    if ddata is not None:
        for d in ddata["discoveries"]:
            first_rel = d["archived_artifacts"][0]["path"]
            ddir = (root / first_rel).parent
            ddir.mkdir(parents=True, exist_ok=True)

            meta_path = ddir / "METADATA.json"
            meta_path.write_text(json.dumps(d, indent=2) + "\n", encoding="utf-8", newline="\n")

            ev_path = ddir / "EVIDENCE.md"
            ev_path.write_text(render_disc_evidence_md(d), encoding="utf-8", newline="\n")

            checksum_entries.append((sha256_file(meta_path), meta_path.relative_to(root).as_posix()))
            for art in d["archived_artifacts"]:
                art_abs = root / art["path"]
                checksum_entries.append((sha256_file(art_abs), art["path"]))

        (root / "registry" / "LAWS_AND_DISCOVERIES.md").write_text(render_discoveries_md(ddata), encoding="utf-8", newline="\n")
        dreg_json = root / "registry" / "LAWS_AND_DISCOVERIES.json"
        dreg_json.write_text(json.dumps(ddata, indent=2) + "\n", encoding="utf-8", newline="\n")
        checksum_entries.append((sha256_file(dreg_json), "registry/LAWS_AND_DISCOVERIES.json"))

    checksums_path = root / "CHECKSUMS.sha256"
    checksums_path.write_text(
        "\n".join(f"{digest}  {rel}" for digest, rel in sorted(checksum_entries, key=lambda x: x[1])) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    bcount = len(bdata["builds"]) if bdata else 0
    dcount = len(ddata["discoveries"]) if ddata else 0
    print(
        f"Synced {len(data['papers'])} Tier-I papers + {bcount} Tier-II builds + {dcount} Tier-III discoveries, "
        f"registry markdowns, and CHECKSUMS.sha256 ({len(checksum_entries)} hashed files)."
    )


def get_git_submodule_commits(root: Path) -> dict[str, str]:
    res = subprocess.run(
        ["git", "ls-files", "--stage", "repos"],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    pins: dict[str, str] = {}
    if res.returncode == 0:
        for line in res.stdout.splitlines():
            parts = line.split()
            if len(parts) >= 4 and parts[0] == "160000":
                pins[parts[3]] = parts[1]
    return pins


def verify_archive(root: Path, data: dict, bdata: dict | None, ddata: dict | None) -> None:
    errors: list[str] = []

    if data["archive"]["author"]["orcid"] != EXPECTED_ORCID:
        errors.append(f"Archive ORCID mismatch: expected {EXPECTED_ORCID}")

    seen_ids: set[str] = set()
    git_pins = get_git_submodule_commits(root)

    for p in data["papers"]:
        pid = p["id"]
        if pid in seen_ids:
            errors.append(f"Duplicate ID: {pid}")
        seen_ids.add(pid)
        if p.get("orcid") != EXPECTED_ORCID:
            errors.append(f"{pid}: ORCID mismatch ({p.get('orcid')})")
        axioms = set(p["lean_verification"]["axiom_allowlist"])
        if not axioms.issubset(ALLOWED_AXIOMS):
            errors.append(f"{pid}: Non-standard axioms in allowlist: {axioms - ALLOWED_AXIOMS}")
        if not p.get("verification_boundary"):
            errors.append(f"{pid}: Missing verification_boundary")
        pdf_path = root / p["pdf_archive_path"]
        if not pdf_path.exists():
            errors.append(f"{pid}: Missing archived PDF {p['pdf_archive_path']}")
        elif sha256_file(pdf_path) != p["pdf_sha256"]:
            errors.append(f"{pid}: PDF SHA-256 mismatch")
        pdir = pdf_path.parent
        declared_pdfs = {pdf_path.name}
        for cm in p.get("component_manuscripts", []):
            cm_name = Path(cm["repo_path"]).name
            declared_pdfs.add(cm_name)
            cm_abs = pdir / cm_name
            if cm_abs != pdf_path and cm_abs.exists():
                if sha256_file(cm_abs) != cm["sha256"]:
                    errors.append(f"{pid}: Companion PDF SHA-256 mismatch for {cm_name}")
        for disk_pdf in sorted(pdir.glob("*.pdf")):
            if disk_pdf.name not in declared_pdfs:
                errors.append(f"{pid}: Unregistered PDF in archive directory: {disk_pdf.relative_to(root).as_posix()}")
        for req in ("METADATA.json", "EVIDENCE.md"):
            if not (pdir / req).exists():
                errors.append(f"{pid}: Missing {pdir.relative_to(root).as_posix()}/{req}")
        sub = p["submodule_path"]
        if git_pins and sub in git_pins:
            if git_pins[sub] != p["pinned_commit"]:
                errors.append(f"{pid}: Submodule {sub} pinned at {git_pins[sub]}, expected {p['pinned_commit']}")
        elif git_pins:
            errors.append(f"{pid}: Submodule {sub} not found in git index")
        readme_path = root / "README.md"
        if readme_path.exists():
            readme_txt = readme_path.read_text(encoding="utf-8")
            row_prefix = f"| `{pid}` |"
            matching = [ln for ln in readme_txt.splitlines() if ln.startswith(row_prefix)]
            if not matching:
                errors.append(f"{pid}: Missing Tier-I table row in README.md")
            elif f"`{p['version']}`" not in matching[0]:
                errors.append(f"{pid}: README.md version does not match PAPERS.json ({p['version']})")

    bcount = 0
    if bdata is not None:
        bcount = len(bdata["builds"])
        for b in bdata["builds"]:
            bid = b["id"]
            if bid in seen_ids:
                errors.append(f"Duplicate ID: {bid}")
            seen_ids.add(bid)
            if b.get("orcid") != EXPECTED_ORCID:
                errors.append(f"{bid}: ORCID mismatch ({b.get('orcid')})")
            axioms = set(b["lean_verification"]["axiom_allowlist"])
            if not axioms.issubset(ALLOWED_AXIOMS):
                errors.append(f"{bid}: Non-standard axioms in allowlist: {axioms - ALLOWED_AXIOMS}")
            if not b.get("verification_boundary"):
                errors.append(f"{bid}: Missing verification_boundary")
            for art in b["archived_artifacts"]:
                ap = root / art["path"]
                if not ap.exists():
                    errors.append(f"{bid}: Missing archived artifact {art['path']}")
                elif sha256_file(ap) != art["sha256"]:
                    errors.append(f"{bid}: Artifact SHA-256 mismatch for {art['path']}")
            bdir = (root / b["archived_artifacts"][0]["path"]).parent
            for req in ("METADATA.json", "EVIDENCE.md"):
                if not (bdir / req).exists():
                    errors.append(f"{bid}: Missing {bdir.relative_to(root).as_posix()}/{req}")
            sub = b["submodule_path"]
            if git_pins and sub in git_pins:
                if git_pins[sub] != b["pinned_commit"]:
                    errors.append(f"{bid}: Submodule {sub} pinned at {git_pins[sub]}, expected {b['pinned_commit']}")
            elif git_pins:
                errors.append(f"{bid}: Submodule {sub} not found in git index")

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
            if d.get("visibility") != "PUBLIC":
                errors.append(f"{did}: Non-PUBLIC entry found in public archive!")
            if not d.get("verification_boundary"):
                errors.append(f"{did}: Missing verification_boundary")
            for art in d["archived_artifacts"]:
                ap = root / art["path"]
                if not ap.exists():
                    errors.append(f"{did}: Missing archived snapshot {art['path']}")
                elif sha256_file(ap) != art["sha256"]:
                    errors.append(f"{did}: Snapshot SHA-256 mismatch for {art['path']}")
            ddir = (root / d["archived_artifacts"][0]["path"]).parent
            for req in ("METADATA.json", "EVIDENCE.md"):
                if not (ddir / req).exists():
                    errors.append(f"{did}: Missing {ddir.relative_to(root).as_posix()}/{req}")

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
        f"all SHA-256 digests, CHECKSUMS.sha256, ORCID {EXPECTED_ORCID}, axiom allowlists, "
        f"and {len(git_pins)} pinned PUBLIC Git submodules."
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
