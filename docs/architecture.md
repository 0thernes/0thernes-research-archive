# Archive Architecture (`docs/architecture.md`)

`0thernes-research-archive` organizes all public scientific outputs authored by Alexander Stephen Donahue (`ORCID 0009-0006-8168-9648`) into **three strictly separated epistemic tiers**, backed by **20 pinned public Git submodules** under `repos/` and a unified SHA-256 integrity manifest (`CHECKSUMS.sha256` & `data/MANIFEST.sha256`).

```mermaid
flowchart LR
    R1["registry/PAPERS.json<br/>Tier I: 12 Standalone Preprints"] --> V["scripts/verify_archive.py"]
    R2["registry/BUILD_PAPERS.json<br/>Tier II: 9 Public Build Papers & Lean Suites"] --> V
    R3["registry/LAWS_AND_DISCOVERIES.json<br/>Tier III: 10 Public Laws, Claims & Atlases"] --> V
    S["repos/* (20 Pinned Public Submodules)"] --> V
    V --> C["CHECKSUMS.sha256 & data/MANIFEST.sha256"]
    V --> D["Per-Entry METADATA.json + EVIDENCE.md"]
    V --> P["scripts/build_site.py -> GitHub Pages Portal"]
```

## Verification Invariants

1. **Single-script deterministic derivation (`scripts/verify_archive.py --sync`):** Regenerates all `METADATA.json`, `EVIDENCE.md`, `registry/*.md`, and `CHECKSUMS.sha256` directly from the three canonical JSON registries.
2. **Exact submodule commit pinning:** Every `pinned_commit` in `PAPERS.json` and `BUILD_PAPERS.json` is cross-checked against `git ls-files --stage repos`.
3. **Strict axiom & ORCID enforcement:** Every entry must carry ORCID `0009-0006-8168-9648`, an explicit `verification_boundary`, and Lean axiom allowlists strictly within `[propext, Classical.choice, Quot.sound]`.
4. **Public-only privacy firewall:** Zero private repositories or third-party forks may appear in `registry/` or `.gitmodules`.
