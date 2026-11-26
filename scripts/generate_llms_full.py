#!/usr/bin/env python3
"""Deterministically regenerate llms.txt and llms-full.txt for 0thernes-research-archive."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    papers = json.loads((ROOT / "registry" / "PAPERS.json").read_text(encoding="utf-8"))["papers"]
    builds = json.loads((ROOT / "registry" / "BUILD_PAPERS.json").read_text(encoding="utf-8"))["builds"]
    discs = json.loads((ROOT / "registry" / "LAWS_AND_DISCOVERIES.json").read_text(encoding="utf-8"))["discoveries"]
    bridge = json.loads((ROOT / "registry" / "SOLVED_AND_ATLAS_BRIDGE.json").read_text(encoding="utf-8"))
    mirror_path = ROOT / "registry" / "LIVE_ECOSYSTEM_MIRROR.json"
    mirror = json.loads(mirror_path.read_text(encoding="utf-8")) if mirror_path.exists() else {}
    total = len(papers) + len(builds) + len(discs)

    llms_txt = f"""# 0thernes Research Archive ({version})

> Canonical public master vault, live ecosystem mirror, and Mega-Atlas V2 cross-reference bridge for Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA; ORCID 0009-0006-8168-9648). Tracks {total} public research entries ({len(papers)} Tier I preprints, {len(builds)} Tier II build papers & Lean 4 suites, {len(discs)} Tier III laws/discoveries/atlases) with byte-exact SHA-256 provenance and zero private repository leakage.

## Key Registries & Machine-Readable Endpoints
- [Tier I Preprints (JSON)](registry/PAPERS.json) · [Markdown](registry/PAPERS.md)
- [Tier II Builds & Lean 4 Suites (JSON)](registry/BUILD_PAPERS.json) · [Markdown](registry/BUILD_PAPERS.md)
- [Tier III Laws, Claims & Atlases (JSON)](registry/LAWS_AND_DISCOVERIES.json) · [Markdown](registry/LAWS_AND_DISCOVERIES.md)
- [Solved Sub-Conjectures & Mega-Atlas V2 Bridge (JSON)](registry/SOLVED_AND_ATLAS_BRIDGE.json) · [Markdown](registry/SOLVED_AND_ATLAS_BRIDGE.md)
- [Live Upstream Ecosystem Mirror (JSON)](registry/LIVE_ECOSYSTEM_MIRROR.json) · [Markdown](registry/LIVE_ECOSYSTEM_MIRROR.md)
- [SHA-256 Master Checksums](CHECKSUMS.sha256) · [Data Manifest](data/MANIFEST.sha256)

## Epistemic Status & Verification
- Grand Mega-Atlas V2 open problems retired: {bridge['grand_problems_retired']} / {bridge['mega_atlas_total_problems']}
- Peer-literature open sub-conjectures / open questions formally proved in Lean 4.35.0: {bridge['epistemic_summary']['published_open_subconjectures_proved_in_lean']}
- Tracked unique public repositories: {mirror.get('counts', {}).get('unique_public_repositories', 'N/A')}
- Primary verifier: `python3 scripts/verify_archive.py` and `python3 -m pytest -v tests/`

## Governance & Documentation
- [README.md](README.md) · [CLAIMS.md](CLAIMS.md) · [LIMITATIONS.md](LIMITATIONS.md) · [REPLICATION.md](REPLICATION.md)
- [AGENTS.md](AGENTS.md) · [CHANGELOG.md](CHANGELOG.md) · [ROADMAP.md](ROADMAP.md) · [HARDENING_INDEX.md](HARDENING_INDEX.md)
- [Architecture](docs/architecture.md) · [ADR 0001](docs/adr/0001-three-tier-epistemic-archive.md) · [ADR 0002](docs/adr/0002-canonical-hub-and-live-sync.md)
"""
    (ROOT / "llms.txt").write_bytes(llms_txt.encode("utf-8"))

    sections = [
        "README.md",
        "CLAIMS.md",
        "LIMITATIONS.md",
        "REPLICATION.md",
        "AGENTS.md",
        "registry/SOLVED_AND_ATLAS_BRIDGE.md",
        "registry/LIVE_ECOSYSTEM_MIRROR.md",
        "docs/architecture.md",
        "docs/adr/0001-three-tier-epistemic-archive.md",
        "docs/adr/0002-canonical-hub-and-live-sync.md",
        "docs/faq.md",
    ]
    parts = [f"# 0thernes Research Archive — Complete LLM Context ({version})\n"]
    for rel in sections:
        p = ROOT / rel
        if p.exists():
            parts.append(f"\n---\n\n<!-- FILE: {rel} -->\n\n" + p.read_text(encoding="utf-8").strip() + "\n")
    (ROOT / "llms-full.txt").write_bytes("\n".join(parts).encode("utf-8"))
    print(f"PASS: Regenerated llms.txt and llms-full.txt ({len(sections)} embedded docs).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
