# Roadmap

## Completed (`2026.11.26`)
- **Single Canonical Hub & Scheduled Live Mirror ([ADR 0002](docs/adr/0002-canonical-hub-and-live-sync.md)):** Consolidated all public research registries and specialist open-problem catalogues under `0thernes-research-archive`, backed by `scripts/live_sync.py`, `.github/workflows/live-sync.yml` (hourly schedule, manual dispatch and optional `repository_dispatch`, committing only on change), `registry/LIVE_ECOSYSTEM_MIRROR.json/.md`, and `docs/upstream-notify-workflow.yml`.
- **Mega-Atlas V2 Bridge (`0 / 1,900` grand problems retired · 3 answered preprint questions, RESULTS.md section A):** Expanded `registry/SOLVED_AND_ATLAS_BRIDGE.json/.md` to **28 version-checked entries**: 2 entries that answer questions posed in unreviewed preprints (`0TH-2026-006`, `0TH-2026-009`), the other 12 Tier I entries (new theorems, bounded cases, barrier lemmas, known results; `0TH-2026-016` resolves no published question and gives kernel-checked lower bounds for C25, C27, C29 and C31, of which only C25 and C29 exceed published values), and 14 Tier II builds with Lean at the pinned commit (0TH-BUILD-006 has no Lean at its pin and no row), first synced with `builds/0TH-BUILD-007_unsolved-problems-mega-atlas/0THERNES_SOLVED_AUDIT_2026-11-25.md`.
- **48 Public Research Entries (`19 Tier I + 17 Tier II + 12 Tier III`), 35 Pinned Public Submodules & 1,050 Tier-II Lean 4.35.0 Declarations at the pinned commits:** Registered `0TH-2026-013` (`p-vs-np-frontier-lab` `v1.2.0`, 25 audited decls + negative elaboration CI test + 27 bibliography entries with 25 Crossref DOIs—3 mismatched at pinned `v1.2.0`, fixed with title+author verification on `main`—+ DigiCert RFC 3161 TSA), `0TH-2026-014` (`monodromia` `v1.0.0`, 98 decls), `0TH-2026-015` (`promislow-fracton-amoeba` `v1.0.0`, 20 decls), `0TH-2026-016` (`zero-error-torus-frontier` `v1.0.0`, 32 decls), `0TH-2026-017`..`019`, and Tier II builds `0TH-BUILD-010`..`017`.
- **Multi-Round 3-Cycle Hardening, Automated Regression Guards & DigiCert RFC 3161 TSA Seal:** Eliminated all residual `"0thernes LLC"` strings, disabled Dependabot auto-PRs (R4), fixed split Tier II `README.md` table rows, added automated `README.md` table-continuity, count-parity, bridge-version-parity, mirror-parity, and live DigiCert RFC 3161 TSA (`data/RELEASE_FREEZE.sha256.tsr`) verification gates in `scripts/verify_archive.py` and `tests/test_archive_integrity.py`.

## Completed (`2026.11.25`)
- Build Standard v1.2.0 baseline upgrade (`18.0% -> 100.0%`), `0TH-2026-006 v2.1.0`, `0TH-2026-011 v2.4.0`, `0TH-2026-012 v3.0.0`, `0TH-BUILD-002 v2.3.0`, `0TH-BUILD-003 v1.4.1`, `0TH-BUILD-007 v2.4.0`.

## Planned
- Optional owner action for push-triggered refreshes: add an `ARCHIVE_SYNC_TOKEN` secret (a fine-grained token allowed to dispatch to this repository) to each upstream repository that carries the notify workflow. On 2026-11-26, 2 of 41 tracked repositories carried the workflow and none had the secret, so the hourly pull was the only automatic path.
- Register future Zenodo DOIs and Software Heritage `swh:1:rev:` identifiers as manual archival snapshots complete.

## Not Planned
- Adding private repositories, proprietary credentials, or unverified third-party forks to this public vault.
- Conflating Tier III empirical discoveries or atlases with Tier I formally proved theorems.
