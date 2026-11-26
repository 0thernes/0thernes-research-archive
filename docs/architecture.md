# Archive Architecture (`docs/architecture.md`)

`0thernes-research-archive` is the **single canonical public master hub** organizing all public scientific outputs authored by Alexander Stephen Donahue (`ORCID 0009-0006-8168-9648`) into **three strictly separated epistemic tiers** (**36 entries**: 13 Tier I + 11 Tier II + 12 Tier III), backed by **23 pinned public Git submodules** under `repos/`, a **Solved Sub-Conjectures & Mega-Atlas V2 Bridge**, a **Real-Time Live Upstream Ecosystem Mirror**, and a unified SHA-256 integrity manifest (`CHECKSUMS.sha256` & `data/MANIFEST.sha256`).

```mermaid
flowchart LR
    UP["Upstream Public 0thernes/* Repos"] -->|repository_dispatch / 2h cron| LS["scripts/live_sync.py"]
    R1["registry/PAPERS.json<br/>Tier I: 13 Standalone Preprints"] --> V["scripts/verify_archive.py"]
    R2["registry/BUILD_PAPERS.json<br/>Tier II: 11 Build Papers & Lean Suites"] --> V
    R3["registry/LAWS_AND_DISCOVERIES.json<br/>Tier III: 12 Laws, Claims & Atlases"] --> V
    BR["registry/SOLVED_AND_ATLAS_BRIDGE.json<br/>0/1900 Grand · 4 Peer Sub-Conjectures"] --> V
    LS --> LM["registry/LIVE_ECOSYSTEM_MIRROR.json/.md"]
    LM --> V
    S["repos/* (23 Pinned Public Submodules)"] --> V
    V --> C["CHECKSUMS.sha256 & data/MANIFEST.sha256"]
    V --> D["Per-Entry METADATA.json + EVIDENCE.md"]
    V --> P["scripts/build_site.py -> WCAG 2.2 AA Pages Portal"]
```

## Verification Invariants

1. **Single-script deterministic derivation (`scripts/verify_archive.py --sync`):** Regenerates all `METADATA.json`, `EVIDENCE.md`, `registry/*.md`, `CHECKSUMS.sha256`, and `data/MANIFEST.sha256` directly from the canonical JSON registries (verified idempotent by B14 tests).
2. **Real-time live upstream mirror (`scripts/live_sync.py` + `.github/workflows/live-sync.yml`):** Tracks live `main` HEADs, latest releases, and CI status across all public non-fork `0thernes/*` repositories without disturbing immutable release-pinned frozen PDFs.
3. **Exact submodule commit pinning & A24 size caps:** Every `pinned_commit` in `PAPERS.json` and `BUILD_PAPERS.json` matches `git ls-files --stage repos`, and every archived file is strictly `< 5 MB`.
4. **Strict axiom, identity, link & ORCID enforcement:** Every entry carries ORCID `0009-0006-8168-9648`, zero unformed `"0thernes LLC"` assertions, an explicit `verification_boundary`, Lean axiom allowlists strictly within `[propext, Classical.choice, Quot.sound]`, and zero broken relative markdown links.
5. **Public-only privacy firewall:** Zero private repositories or third-party forks may appear anywhere in `registry/`, `repos/`, `llms.txt`, or `.gitmodules`.
