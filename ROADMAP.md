# Roadmap

## Completed (`2026.11.26`)
- **Single Canonical Hub & Live Real-Time Sync ([ADR 0002](docs/adr/0002-canonical-hub-and-live-sync.md)):** Consolidated all public research registries and specialist open-problem catalogues under `0thernes-research-archive`, backed by `scripts/live_sync.py`, `.github/workflows/live-sync.yml` (`repository_dispatch` + 2-hour schedule with zero-noise idempotence), `registry/LIVE_ECOSYSTEM_MIRROR.json/.md`, and `docs/upstream-notify-workflow.yml`.
- **Exhaustive Mega-Atlas V2 Bridge (`0 / 1,900` grand problems retired · 5 peer-literature sub-conjectures proved):** Expanded `registry/SOLVED_AND_ATLAS_BRIDGE.json/.md` to **26 version-checked entries** covering all 5 Lean-proved peer-literature sub-conjectures (including `0TH-2026-016` Tandon `arXiv:2608.30273` Open Problem #2 + 4 odd-cycle Shannon capacity world records), all 6 active partial/barrier Tier I suites, and all 15 Lean-bearing Tier II builds, synced with `builds/0TH-BUILD-007_unsolved-problems-mega-atlas/0THERNES_SOLVED_AUDIT_2026-11-25.md`.
- **45 Public Research Entries (`16 Tier I + 17 Tier II + 12 Tier III`), 32 Pinned Public Submodules & 1,058 Tier-II Lean 4.35.0 Declarations:** Registered `0TH-2026-013` (`p-vs-np-frontier-lab` `v1.2.0`, 25 audited decls + live negative kernel rejection + 27/27 live Crossref DOIs + DigiCert RFC 3161 TSA), `0TH-2026-014` (`monodromia` `v1.0.0`, 98 decls), `0TH-2026-015` (`promislow-fracton-amoeba` `v1.0.0`, 20 decls), `0TH-2026-016` (`zero-error-torus-frontier` `v1.0.0`, 32 decls), and Tier II builds `0TH-BUILD-010`..`017`.
- **Multi-Round 3-Cycle Hardening, Automated Regression Guards & DigiCert RFC 3161 TSA Seal:** Eliminated all residual `"0thernes LLC"` strings, disabled Dependabot auto-PRs (R4), fixed split Tier II `README.md` table rows, added automated `README.md` table-continuity, count-parity, bridge-version-parity, mirror-parity, and live DigiCert RFC 3161 TSA (`data/RELEASE_FREEZE.sha256.tsr`) verification gates in `scripts/verify_archive.py` and `tests/test_archive_integrity.py`.

## Completed (`2026.11.25`)
- Build Standard v1.2.0 baseline upgrade (`18.0% -> 100.0%`), `0TH-2026-006 v2.1.0`, `0TH-2026-011 v2.4.0`, `0TH-2026-012 v3.0.0`, `0TH-BUILD-002 v2.3.0`, `0TH-BUILD-003 v1.4.1`, `0TH-BUILD-007 v2.4.0`.

## Planned
- Configure optional account/repo secret `ARCHIVE_SYNC_TOKEN` for sub-minute push-triggered `repository_dispatch` (in addition to the already-active 2-hour scheduled sync).
- Register future Zenodo DOIs and Software Heritage `swh:1:rev:` identifiers as manual archival snapshots complete.

## Not Planned
- Adding private repositories, proprietary credentials, or unverified third-party forks to this public vault.
- Conflating Tier III empirical discoveries or atlases with Tier I formally proved theorems.
