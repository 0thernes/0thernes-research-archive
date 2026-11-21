#!/usr/bin/env python3
"""
Cryptographic & structural integrity auditor for the 0thernes Research Archive.

Checks:
  1. Schema validity and canonical ORCID (0009-0006-8168-9648) on every entry.
  2. Byte-for-byte SHA-256 verification of every archived frozen PDF against
     registry/PAPERS.json and CHECKSUMS.sha256.
  3. Presence of per-paper METADATA.json and EVIDENCE.md dossiers.
  4. Exact Git submodule commit pin matching registry/PAPERS.json (when git tree is present).

Optional flags:
  --sync   Regenerate per-paper METADATA.json, EVIDENCE.md, registry/PAPERS.md,
           and CHECKSUMS.sha256 directly from registry/PAPERS.json before verifying.
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
        f"- **Axiom Audit Script:** `{lv['axiom_audit_file']}`",
        f"- **Permitted Axioms:** `{', '.join(lv['axiom_allowlist'])}`",
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
    return "\n".join(lines)


def render_papers_md(data: dict) -> str:
    arch = data["archive"]
    author = arch["author"]
    lines = [
        "# Master Paper Registry — 0thernes Research Archive",
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


def sync_derived_files(root: Path, data: dict) -> None:
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

    papers_md = root / "registry" / "PAPERS.md"
    papers_md.write_text(render_papers_md(data), encoding="utf-8", newline="\n")

    reg_json = root / "registry" / "PAPERS.json"
    reg_json.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8", newline="\n")
    checksum_entries.append((sha256_file(reg_json), "registry/PAPERS.json"))

    checksums_path = root / "CHECKSUMS.sha256"
    checksums_path.write_text(
        "\n".join(f"{digest}  {rel}" for digest, rel in sorted(checksum_entries, key=lambda x: x[1])) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"Synced {len(data['papers'])} paper dossiers, registry/PAPERS.md, and CHECKSUMS.sha256.")


def get_git_submodule_commits(root: Path) -> dict[str, str]:
    """Read pinned gitlink (mode 160000) commits from the Git index/tree."""
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


def verify_archive(root: Path, data: dict) -> None:
    errors: list[str] = []

    if data["archive"]["author"]["orcid"] != EXPECTED_ORCID:
        errors.append(f"Archive ORCID mismatch: expected {EXPECTED_ORCID}")

    seen_ids: set[str] = set()
    git_pins = get_git_submodule_commits(root)

    for p in data["papers"]:
        pid = p["id"]
        if pid in seen_ids:
            errors.append(f"Duplicate paper ID: {pid}")
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
        else:
            actual = sha256_file(pdf_path)
            if actual != p["pdf_sha256"]:
                errors.append(f"{pid}: PDF SHA-256 mismatch! expected={p['pdf_sha256']} actual={actual}")

        pdir = pdf_path.parent
        for req in ("METADATA.json", "EVIDENCE.md"):
            if not (pdir / req).exists():
                errors.append(f"{pid}: Missing {pdir.relative_to(root).as_posix()}/{req}")

        sub = p["submodule_path"]
        if git_pins and sub in git_pins:
            if git_pins[sub] != p["pinned_commit"]:
                errors.append(
                    f"{pid}: Submodule {sub} pinned at {git_pins[sub]}, expected {p['pinned_commit']}"
                )
        elif git_pins:
            errors.append(f"{pid}: Submodule {sub} not found in git index")

    # Verify CHECKSUMS.sha256
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
            else:
                actual_hash = sha256_file(target)
                if actual_hash != expected_hash:
                    errors.append(f"CHECKSUMS.sha256 mismatch for {rel_path}")

    if errors:
        print("ARCHIVE AUDIT FAILED:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    print(
        f"PASS: Verified {len(data['papers'])} papers, all frozen PDF SHA-256 digests, "
        f"CHECKSUMS.sha256, ORCID {EXPECTED_ORCID}, axiom allowlists, and {len(git_pins)} submodule pins."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Verify (and optionally sync) 0thernes Research Archive.")
    parser.add_argument("--sync", action="store_true", help="Regenerate dossiers, PAPERS.md, and CHECKSUMS.sha256")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    reg_path = root / "registry" / "PAPERS.json"
    data = json.loads(reg_path.read_text(encoding="utf-8"))

    if args.sync:
        sync_derived_files(root, data)
    verify_archive(root, data)


if __name__ == "__main__":
    main()
