# Roadmap

## Completed (`2026.11.26`)
- **Single Canonical Hub & Live Real-Time Sync ([ADR 0002](docs/adr/0002-canonical-hub-and-live-sync.md)):** Consolidated all public research registries and specialist open-problem catalogues under `0thernes-research-archive`, backed by `scripts/live_sync.py`, `.github/workflows/live-sync.yml` (`repository_dispatch` + 2-hour schedule), `registry/LIVE_ECOSYSTEM_MIRROR.json/.md`, and `docs/upstream-notify-workflow.yml`.
- **Exhaustive Mega-Atlas V2 Bridge (`0 / 1,900` grand problems retired):** Added `registry/SOLVED_AND_ATLAS_BRIDGE.json/.md` and restored `builds/0TH-BUILD-007_unsolved-problems-mega-atlas/0THERNES_SOLVED_AUDIT_2026-11-25.md`.
- **36 Public Research Entries & 23 Pinned Submodules:** Registered `0TH-2026-013` (`p-vs-np-frontier-lab` `v1.1.0`), upgraded `0TH-BUILD-004` (`unsolved-mathematics` `v0.5.0`, 69 Lean decls across 6 kernels), registered `0TH-BUILD-010` (`noetic-organism-omega`, 48 thms), `0TH-BUILD-011` (`asmodensius-native`, 20 decls), `0TH-DISC-011` (`alife-singularity-omega-package`), and `0TH-DISC-012` (`omega-triscale-observatory`).
- **3-Cycle Hardening & WCAG 2.2 AA Portal:** Eliminated all residual `"0thernes LLC"` strings (`LICENSE`, `register_paper.py`, registries), disabled Dependabot auto-PRs (R4), added automated zero-broken-link checking, failure-injection & idempotence tests, and upgraded the GitHub Pages portal to all 3 tiers + Bridge + Live Mirror with interactive search/filter.

## Completed (`2026.11.25`)
- Build Standard v1.2.0 baseline upgrade (`18.0% -> 100.0%`), `0TH-2026-006 v2.1.0`, `0TH-2026-011 v2.4.0`, `0TH-2026-012 v3.0.0`, `0TH-BUILD-002 v2.3.0`, `0TH-BUILD-003 v1.4.1`, `0TH-BUILD-007 v2.4.0`.

## Planned
- Configure optional account/repo secret `ARCHIVE_SYNC_TOKEN` for sub-minute push-triggered `repository_dispatch` (in addition to the already-active 2-hour scheduled sync).
- Register future Zenodo DOIs and Software Heritage `swh:1:rev:` identifiers as manual archival snapshots complete.

## Not Planned
- Adding private repositories, proprietary credentials, or unverified third-party forks to this public vault.
- Conflating Tier III empirical discoveries or atlases with Tier I formally proved theorems.
