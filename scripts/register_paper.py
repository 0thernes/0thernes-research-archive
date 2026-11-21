#!/usr/bin/env python3
"""
Register a new Lean 4-verified white paper into the 0thernes Research Archive.

Example:
    python scripts/register_paper.py \
      --id 0TH-2026-007 \
      --slug my-new-theorem \
      --title "Exact Solution of ..." \
      --domain "Mathematical Statistics" \
      --version v1.0.0 \
      --date 2026-11-25 \
      --repo https://github.com/0thernes/my-new-theorem \
      --pdf /path/to/paper.pdf \
      --ci-url https://github.com/0thernes/my-new-theorem/actions/runs/... \
      --core-result "Concise statement of proved theorem." \
      --boundary "Exact kernel-checked vs paper-proof boundary." \
      --falsify "cd repos/my-new-theorem/lean && lake build && lake env lean VerifyAxioms.lean"
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description="Register a new paper in 0thernes-research-archive.")
    parser.add_argument("--id", required=True, help="Paper ID, e.g. 0TH-2026-007")
    parser.add_argument("--slug", required=True, help="Short repository slug")
    parser.add_argument("--title", required=True)
    parser.add_argument("--domain", required=True)
    parser.add_argument("--version", required=True, help="Release tag, e.g. v1.0.0")
    parser.add_argument("--date", required=True, help="YYYY-MM-DD")
    parser.add_argument("--repo", required=True, help="GitHub repository URL")
    parser.add_argument("--pdf", required=True, help="Path to frozen release PDF")
    parser.add_argument("--lean-framework", default="Lean 4.35.0 / Mathlib")
    parser.add_argument("--lean-entry", default="lean/Main.lean")
    parser.add_argument("--lean-audit", default="lean/VerifyAxioms.lean")
    parser.add_argument("--ci-url", default=None)
    parser.add_argument("--arxiv-bundle-url", default=None)
    parser.add_argument("--arxiv-bundle-sha256", default="pending")
    parser.add_argument("--core-result", required=True)
    parser.add_argument("--boundary", required=True)
    parser.add_argument("--falsify", required=True)
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    sub_rel = f"repos/{args.slug}"
    sub_abs = root / sub_rel

    if not sub_abs.exists():
        subprocess.run(
            ["git", "submodule", "add", f"{args.repo.rstrip('/')}.git", sub_rel],
            cwd=root,
            check=True,
        )

    sha = subprocess.check_output(
        ["git", "-C", str(sub_abs), "rev-parse", "HEAD"], text=True
    ).strip()

    pdf_src = Path(args.pdf).resolve()
    pdir = root / "papers" / f"{args.id}_{args.slug}"
    pdir.mkdir(parents=True, exist_ok=True)
    pdf_dst = pdir / pdf_src.name
    shutil.copy2(pdf_src, pdf_dst)
    pdf_hash = sha256_file(pdf_dst)

    reg_path = root / "registry" / "PAPERS.json"
    data = json.loads(reg_path.read_text(encoding="utf-8"))
    data["archive"]["updated_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    entry = {
        "id": args.id,
        "slug": args.slug,
        "title": args.title,
        "domain": args.domain,
        "date_released": args.date,
        "version": args.version,
        "peer_review_status": "Research preprint (not peer reviewed; AI-assisted under human direction)",
        "author": "Alexander Stephen Donahue",
        "orcid": "0009-0006-8168-9648",
        "affiliation": "0thernes LLC",
        "repository": args.repo.rstrip("/"),
        "submodule_path": sub_rel,
        "pinned_commit": sha,
        "release_url": f"{args.repo.rstrip('/')}/releases/tag/{args.version}",
        "pages_url": None,
        "pdf_archive_path": pdf_dst.relative_to(root).as_posix(),
        "pdf_sha256": pdf_hash,
        "arxiv_bundle_url": args.arxiv_bundle_url,
        "arxiv_bundle_sha256": args.arxiv_bundle_sha256,
        "lean_verification": {
            "framework": args.lean_framework,
            "axiom_allowlist": ["propext", "Classical.choice", "Quot.sound"],
            "entry_point": args.lean_entry,
            "axiom_audit_file": args.lean_audit,
        },
        "ci_run_url": args.ci_url,
        "preservation": {
            "software_heritage": None,
            "wayback_machine": None,
            "doi": None,
        },
        "core_result": args.core_result,
        "verification_boundary": args.boundary,
        "falsification_command": args.falsify,
    }

    data["papers"] = [p for p in data["papers"] if p["id"] != args.id] + [entry]
    reg_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    subprocess.run(["python", "scripts/verify_archive.py", "--sync"], cwd=root, check=True)
    print(f"Registered {args.id} ({args.slug}) @ {sha[:10]} with PDF SHA-256 {pdf_hash}.")


if __name__ == "__main__":
    main()
