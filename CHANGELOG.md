# Changelog

All notable archive registrations, cryptographic pin updates, and hardening releases are logged here.

## [2026.11.26] - 2026-11-26

### Added
- **Single Canonical Hub & Real-Time Live Ecosystem Sync ([ADR 0002](docs/adr/0002-canonical-hub-and-live-sync.md)):** Added [`scripts/live_sync.py`](scripts/live_sync.py), [`.github/workflows/live-sync.yml`](.github/workflows/live-sync.yml) (`repository_dispatch` + 2-hour `cron` + `workflow_dispatch`), [`registry/LIVE_ECOSYSTEM_MIRROR.json`](registry/LIVE_ECOSYSTEM_MIRROR.json), [`registry/LIVE_ECOSYSTEM_MIRROR.md`](registry/LIVE_ECOSYSTEM_MIRROR.md), [`docs/upstream-notify-workflow.yml`](docs/upstream-notify-workflow.yml), and deterministic [`scripts/generate_llms_full.py`](scripts/generate_llms_full.py).
- **Solved Sub-Conjectures & Mega-Atlas V2 Bridge:** Added [`registry/SOLVED_AND_ATLAS_BRIDGE.json`](registry/SOLVED_AND_ATLAS_BRIDGE.json) & [`registry/SOLVED_AND_ATLAS_BRIDGE.md`](registry/SOLVED_AND_ATLAS_BRIDGE.md) and restored [`builds/0TH-BUILD-007_unsolved-problems-mega-atlas/0THERNES_SOLVED_AUDIT_2026-11-25.md`](builds/0TH-BUILD-007_unsolved-problems-mega-atlas/0THERNES_SOLVED_AUDIT_2026-11-25.md) recording the complete 1,900-problem × 72-public-repo × local `Z:` audit (`0 / 1,900` grand problems retired; 4 peer-literature open sub-conjectures/questions formally proved in Lean 4.35.0).
- **Registered `0TH-2026-013` (`p-vs-np-frontier-lab` `v1.1.0`):** Published newly hardened P vs NP barrier anatomy repository (`14` zero-Mathlib Lean 4.35.0 barrier theorems / `15` Palomar targets, exact CaDiCaL SAT MC audit, 4 heuristic falsifiers, 15-page 0-overfull PDF, 100% Build Standard v1.2.0) and pinned `repos/p-vs-np-frontier-lab`.
- **Registered 4 Missing Public A-Life Omega Repositories:** Added `0TH-BUILD-010` (`noetic-organism-omega`, 48 Lean 4 theorems, CI `#45076052369`), `0TH-BUILD-011` (`asmodensius-native`, 20 Lean 4 decls with explicit disclosure of arithmetic `rfl` witnesses `A15/A16/A20`), `0TH-DISC-011` (`alife-singularity-omega-package`, 1.13 MB Master Dossier PDF), and `0TH-DISC-012` (`omega-triscale-observatory`).
- **3-Cycle Hardening Index & Dossier:** Added [`HARDENING_INDEX.md`](HARDENING_INDEX.md), [`docs/reviews/2026-11-25-3cycle-hardening-log.md`](docs/reviews/2026-11-25-3cycle-hardening-log.md), and [`pytest.ini`](pytest.ini).

### Updated & Fixed
- **Upgraded `0TH-2026-006` (`multinomial-tv-conjecture` → `v2.2.0`):** Advanced `repos/multinomial-tv-conjecture` to `5ceae10ee73d` (Palomar Lean 4.35.0 `module` headers across all 10 files, 5,626 lines, exhaustive 723-theorem named+private axiom audit, 6 independent kernels via CI `#45747471704` Rekor `4117130014` & Release `#45747471531` Rekor `4116986681`, REUSE SPDX headers, dual DigiCert RFC 3161 `.tsr` + 3-calendar Bitcoin OpenTimestamps `.ots`, clickable `plainurl` 16/16 live citations, 0.00pt 20-page PDF, 31/31 3-OS pytest, 66/66 Build Standard v1.2.0).
- **Upgraded `0TH-BUILD-004` (`unsolved-mathematics` → `v0.5.0`):** Advanced `repos/unsolved-mathematics` to `0604df5c70c8` (8-domain zero-Mathlib Lean 4.35.0 core with 69 audited declarations across 6 independent kernels, CI `#45742870717`, frozen 10-page monograph PDF & arXiv bundle) while preserving the historical July 2026 Collatz case-study artifacts.
- **Linked Spoke Catalogue `0TH-DISC-006` (`unsolved-black-hole-problems`):** Added canonical hub banner and `notify-archive.yml` upstream (`0686cf9729fa`) and refreshed archived snapshot.
- **Upgraded Static Portal (`scripts/build_site.py`):** Expanded from 2 tiers to all 3 tiers + Solved/Mega-Atlas Bridge + Live Upstream Mirror with client-side search/tier filters, WCAG 2.2 AA skip link & landmarks, and all 5 JSON endpoints.
- **Hardened `scripts/verify_archive.py` & `tests/test_archive_integrity.py`:** Added automated broken-markdown-link auditing, active zero-LLC enforcement, 5 MB A24 artifact size guard, bridge/mirror policy validation, failure-injection tests, and metamorphic `--sync` idempotence testing.
- **Identity & R4 Compliance Fixes:** Removed residual unformed `"0thernes LLC"` from `LICENSE`, `scripts/register_paper.py`, and all 3 JSON registries; disabled GitHub `automated-security-fixes` (R4); set repository `homepageUrl` to `https://0thernes.github.io/0thernes-research-archive/`.

## [2026.11.25] - 2026-11-25

### Updated & Added
- **Updated `0TH-2026-006` (`multinomial-tv-conjecture` `v2.1.0`), `0TH-2026-011` (`secmesh-pqsi` `v2.4.0`), `0TH-2026-012` (`coded-pir-mlwe-complexity-lab` `v3.0.0`), `0TH-BUILD-002` (`planaria` `v2.3.0`), `0TH-BUILD-003` (`ultrametrica` `v1.4.1`), and `0TH-BUILD-007` (`unsolved-problems-mega-atlas` `v2.4.0`).**
- **Build Standard v1.2.0 Hardening (`18.0% → 100.0%`):** Full governance, docs, cross-platform CI, static Pages portal, and `SHA256SUMS` + Sigstore SLSA release workflow.

## [2026.11.21] - 2026-11-21

### Added
- Initial three-tier public master vault covering Tier I standalone preprints (`registry/PAPERS.json`), Tier II public build white papers & embedded Pure Lean 4 suites (`registry/BUILD_PAPERS.json`), Tier III laws/discoveries/atlases (`registry/LAWS_AND_DISCOVERIES.json`), 20 pinned public submodules, and `scripts/verify_archive.py`.
