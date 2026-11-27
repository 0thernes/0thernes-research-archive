# Master Hardening Index & Table of Contents (`HARDENING_INDEX.md`)

Complete structural index and audit checklist for **0thernes Research Archive (`v2026.11.26`)** and its hardened companion releases **`0thernes/p-vs-np-frontier-lab` (`v1.2.0`)**, **`0thernes/promislow-fracton-amoeba` (`v1.0.0`)**, and **`0thernes/unsolved-black-hole-problems`**, following **Build Standard for LLMs v1.2.0** (`R1`–`R8`, 10 finding classes, 90 items `A01`–`A45` & `B01`–`B45`) and **Defensible Independent AI Research Playbook v1.3**.

---

## Table of Contents

1. [Root Governance, Identity & Packaging](#1-root-governance-identity--packaging)
2. [Canonical Registries, Results Ledger, Bridge & Live Mirror (`registry/`)](#2-canonical-registries-results-ledger-bridge--live-mirror-registry)
3. [Automation, Verification, Live Sync & Portal Scripts (`scripts/`)](#3-automation-verification-live-sync--portal-scripts-scripts)
4. [Automated Test Ladder (`tests/`)](#4-automated-test-ladder-tests)
5. [CI/CD, Live Sync, Pages & Provenance Workflows (`.github/workflows/`)](#5-cicd-live-sync-pages--provenance-workflows-githubworkflows)
6. [Frozen Cryptographic Archives (`papers/`, `builds/`, `discoveries/`) & Submodules (`repos/`)](#6-frozen-cryptographic-archives-papers-builds-discoveries--submodules-repos)
7. [Architecture, ADRs, Run Logs & 3-Cycle Hardening Dossiers (`docs/`)](#7-architecture-adrs-run-logs--3-cycle-hardening-dossiers-docs)
8. [Companion Hardened Releases](#8-companion-hardened-releases)

---

## 1. Root Governance, Identity & Packaging

| File | Role | Audit Status |
|---|---|---|
| [`README.md`](README.md) | Canonical hub overview, live mirror status block, 3-tier tables (**52 public research entries** / **39 pinned public submodules**), Quickstart & Usage | Audited Rounds 1–3 (`H-19` split Tier II table fixed, `H-20` counts & live block enforced in CI) |
| [`RESULTS.md`](RESULTS.md) | Single numbered, statement-audited Results Ledger (**94 active results**: A=3, B=11, C=11, D=0, E=55, F=14) generated deterministically from `registry/RESULTS_LEDGER.json` | Verified by `scripts/build_ledger.py --check` & `tests/test_results_ledger.py` ([ADR 0003](docs/adr/0003-numbered-results-ledger.md)) |
| [`VERSION`](VERSION) / [`CITATION.cff`](CITATION.cff) / [`CHANGELOG.md`](CHANGELOG.md) | Single-source release versioning (`2026.11.26`) & academic citation | Audited Rounds 1–3 (enforced by `test_single_version_consistency`) |
| [`LICENSE`](LICENSE) / [`NOTICE`](NOTICE) / [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) | Dual MIT / CC-BY-4.0 notice, clean Independent Researcher identity (zero unformed LLC) | Audited Rounds 1–3 |
| [`CLAIMS.md`](CLAIMS.md) / [`LIMITATIONS.md`](LIMITATIONS.md) / [`REPLICATION.md`](REPLICATION.md) / [`ROADMAP.md`](ROADMAP.md) | Claims C1–C6, Real-vs-Metaphor, reproducible protocol, roadmap | Audited Rounds 1–3 (synced to 52 public research entries / 39 pinned public submodules / 3 answered preprint questions / RFC 3161 TSA) |
| [`SECURITY.md`](SECURITY.md) / [`CONTRIBUTING.md`](CONTRIBUTING.md) / [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) / [`SUPPORT.md`](SUPPORT.md) | Community & vulnerability governance | Audited Rounds 1–3 |
| [`AGENTS.md`](AGENTS.md) / [`CLAUDE.md`](CLAUDE.md) / [`GEMINI.md`](GEMINI.md) / [`llms.txt`](llms.txt) / [`llms-full.txt`](llms-full.txt) | AI coding-agent instruction & context stack (A32) | Regenerated deterministically via `scripts/generate_llms_full.py` |
| [`repo.yaml`](repo.yaml) / [`repo-standard.schema.json`](repo-standard.schema.json) | Build Standard v1.2.0 Draft 2020-12 validated project manifest | Validated in pytest & CI |
| [`justfile`](justfile) / [`pytest.ini`](pytest.ini) / [`requirements.txt`](requirements.txt) / [`.gitmodules`](.gitmodules) / [`.gitattributes`](.gitattributes) / [`.gitignore`](.gitignore) | Task runner, bracket-safe pytest config, pinned deps, **39 pinned public submodules**, LF enforcement | Audited Rounds 1–3 |
| [`CHECKSUMS.sha256`](CHECKSUMS.sha256) / [`data/MANIFEST.sha256`](data/MANIFEST.sha256) / [`data/RELEASE_FREEZE.sha256`](data/RELEASE_FREEZE.sha256) / [`data/RELEASE_FREEZE.sha256.tsr`](data/RELEASE_FREEZE.sha256.tsr) | Byte-identical SHA-256 manifests + live DigiCert RFC 3161 TSA seal over immutable frozen release artifacts | Verified on 3 OSes (`sha256sum -c`, Python oracle & DER digest check) |

## 2. Canonical Registries, Results Ledger, Bridge & Live Mirror (`registry/`)

- [`registry/PAPERS.json`](registry/PAPERS.json) & [`registry/PAPERS.md`](registry/PAPERS.md) — **23 Tier I standalone preprints** (`0TH-2026-001` through `0TH-2026-023`, with `001/002/003/005` clearly marked as archived historical snapshots consolidated into `0TH-2026-009`).
- [`registry/BUILD_PAPERS.json`](registry/BUILD_PAPERS.json) & [`registry/BUILD_PAPERS.md`](registry/BUILD_PAPERS.md) — **17 Tier II public builds & embedded Pure Lean 4.35.0 suites** (`0TH-BUILD-001` through `0TH-BUILD-017`, **1,050 audited Pure Lean 4.35.0 declarations** across 14 builds with Lean at the pinned commit; the 8 `rfl` theorems of `0TH-BUILD-006` are only on its unmerged branch `pr9`).
- [`registry/LAWS_AND_DISCOVERIES.json`](registry/LAWS_AND_DISCOVERIES.json) & [`registry/LAWS_AND_DISCOVERIES.md`](registry/LAWS_AND_DISCOVERIES.md) — **12 Tier III public laws, pre-registered empirical claims, discoveries, synthesis dossiers & open-problem atlases** (`0TH-DISC-001` through `0TH-DISC-012`).
- [`registry/RESULTS_LEDGER.json`](registry/RESULTS_LEDGER.json) — Machine-validated source of truth for [`RESULTS.md`](RESULTS.md) (**94 active audited results** covering every registered Tier I & Tier II entry).
- [`registry/SOLVED_AND_ATLAS_BRIDGE.json`](registry/SOLVED_AND_ATLAS_BRIDGE.json) & [`registry/SOLVED_AND_ATLAS_BRIDGE.md`](registry/SOLVED_AND_ATLAS_BRIDGE.md) — **28 version-checked rows** cross-referencing all 1,900 Mega-Atlas V2 problems (`0 / 1,900` grand problems retired; **3** results answer questions posed as open in unreviewed preprints, `RESULTS.md` section A).
- [`registry/LIVE_ECOSYSTEM_MIRROR.json`](registry/LIVE_ECOSYSTEM_MIRROR.json) & [`registry/LIVE_ECOSYSTEM_MIRROR.md`](registry/LIVE_ECOSYSTEM_MIRROR.md) — Live upstream commit, release, CI, and Pages status across all **41 unique tracked public non-fork `0thernes/*` repositories**.
- [`registry/PUBLIC_REPO_INVENTORY.json`](registry/PUBLIC_REPO_INVENTORY.json), [`registry/PUBLIC_REPO_INVENTORY.md`](registry/PUBLIC_REPO_INVENTORY.md), [`registry/PUBLIC_CANDIDATE_TRIAGE.md`](registry/PUBLIC_CANDIDATE_TRIAGE.md), [`registry/CLAIM_LANGUAGE_SCAN_2026-11-26.md`](registry/CLAIM_LANGUAGE_SCAN_2026-11-26.md), & [`registry/UPSTREAM_RELEASE_SNAPSHOTS.json`](registry/UPSTREAM_RELEASE_SNAPSHOTS.json) — Full public-account non-fork inventory, triage ledger, claim-language audit scan, and upstream release snapshot cache.

## 3. Automation, Verification, Live Sync & Portal Scripts (`scripts/`)

- [`scripts/verify_archive.py`](scripts/verify_archive.py) — Deterministic `--sync` dossier/checksum/release-freeze generator + full verifier (SHA-256, RFC 3161 TSA digest verification, ORCID, Lean axioms, submodule pins, `README.md` table-continuity & live-block parity, prose-count parity across all `COUNT_GUARDED_FILES` including `HARDENING_INDEX.md`, exact bridge-to-registry version parity, mirror count parity, hashed privacy firewall, zero broken markdown links in hub-authored files, zero unformed LLC strings, `< 5 MB` A24 size guard).
- [`scripts/build_ledger.py`](scripts/build_ledger.py) — Deterministic generator and strict validator (`--check` / `--checkouts`) for `RESULTS.md` and `registry/RESULTS_LEDGER.json`.
- [`scripts/live_sync.py`](scripts/live_sync.py) — Stdlib GitHub API live mirror, public repo inventory refresh, privacy firewall, bridge markdown renderer, and `README.md` live block updater (`--offline` supported, zero-noise idempotent).
- [`scripts/privacy.py`](scripts/privacy.py) — Hashed SHA-256 privacy firewall ensuring zero private repository slugs ever appear in plaintext or leak into public registries/docs.
- [`scripts/stamp_freeze.py`](scripts/stamp_freeze.py) — DigiCert RFC 3161 TSA stamper & verifier for `data/RELEASE_FREEZE.sha256.tsr`.
- [`scripts/build_site.py`](scripts/build_site.py) — WCAG 2.2 AA searchable 3-tier + Bridge + Live Mirror static GitHub Pages generator.
- [`scripts/generate_llms_full.py`](scripts/generate_llms_full.py) — Deterministic `llms.txt` & `llms-full.txt` builder.
- [`scripts/register_paper.py`](scripts/register_paper.py) — Clean registration helper.
- [`scripts/audit-repo.sh`](scripts/audit-repo.sh), [`scripts/Audit-Repo.ps1`](scripts/Audit-Repo.ps1), & [`scripts/Audit-Fleet.ps1`](scripts/Audit-Fleet.ps1) — Cross-platform Build Standard v1.2.0 self-auditors and multi-repo fleet checker.

## 4. Automated Test Ladder (`tests/`)

- [`tests/test_archive_integrity.py`](tests/test_archive_integrity.py) — Draft 2020-12 schema, version parity, R4 zero banned files, privacy firewall across all registries, zero unformed LLC, zero broken local markdown links, `README.md` table-continuity & negative split-table mutant rejection, prose-count drift & colon-format/HARDENING_INDEX regression tests, bridge-to-registry exact version parity & mutant rejection, RFC 3161 TSA verification, end-to-end `verify_archive.py` + manifest parity, Mega-Atlas honesty invariants, `live_sync.py` negative & HTTP-500 failure-injection tests, WCAG portal build check, metamorphic `--sync` idempotence (B14), Hypothesis property-based SHA-256 differential check (B10/B11), and surgical mutant-killing tests (B06/B13).
- [`tests/test_results_ledger.py`](tests/test_results_ledger.py) — Schema, prior-work, promotional-language, staleness, pin-move re-audit detection, withdrawal preservation, and rendering checks for `RESULTS.md` and `registry/RESULTS_LEDGER.json` (0 `mypy` errors).

## 5. CI/CD, Live Sync, Pages & Provenance Workflows (`.github/workflows/`)

- [`.github/workflows/archive-audit.yml`](.github/workflows/archive-audit.yml) — 3-OS (`ubuntu`, `windows`, `macos`) cryptographic audit + `pytest` + `build_ledger.py --check` + `build_site.py` + `ruff`/`mypy` + Build Standard v1.2.0 + `gitleaks`.
- [`.github/workflows/live-sync.yml`](.github/workflows/live-sync.yml) — Hourly `cron` (`17 * * * *`), `workflow_dispatch`, and `repository_dispatch` from upstream repositories that carry the notify workflow and its token.
- [`.github/workflows/pages.yml`](.github/workflows/pages.yml) — Static portal build & GitHub Pages deployment (separate `build` and `deploy` jobs).
- [`.github/workflows/release.yml`](.github/workflows/release.yml) — Release tarball, `SHA256SUMS`, and Sigstore SLSA build provenance attestation.

## 6. Frozen Cryptographic Archives (`papers/`, `builds/`, `discoveries/`) & Submodules (`repos/`)

- `papers/` — **21** directories (`0TH-2026-001`..`0TH-2026-021`), each with frozen PDF(s), `METADATA.json`, `EVIDENCE.md`.
- `builds/` — **17** directories (`0TH-BUILD-001`..`0TH-BUILD-017`), including [`builds/0TH-BUILD-007_unsolved-problems-mega-atlas/0THERNES_SOLVED_AUDIT_2026-11-25.md`](builds/0TH-BUILD-007_unsolved-problems-mega-atlas/0THERNES_SOLVED_AUDIT_2026-11-25.md).
- `discoveries/` — **12** directories (`0TH-DISC-001`..`0TH-DISC-012`), all `< 5 MB` per file.
- `repos/` — **39 pinned public submodules** (`160000` gitlinks verified against registry JSONs).

## 7. Architecture, ADRs, Run Logs & 3-Cycle Hardening Dossiers (`docs/`)

- [`docs/index.md`](docs/index.md), [`docs/architecture.md`](docs/architecture.md), [`docs/configuration.md`](docs/configuration.md), [`docs/operations.md`](docs/operations.md), [`docs/threat-model.md`](docs/threat-model.md), [`docs/faq.md`](docs/faq.md), [`docs/glossary.md`](docs/glossary.md), [`docs/run-log.md`](docs/run-log.md).
- [`registry/LEGACY_INDEX_MIGRATION.md`](registry/LEGACY_INDEX_MIGRATION.md) — migration and authority policy for duplicate local archive/list indexes.
- [`docs/adr/0001-three-tier-epistemic-archive.md`](docs/adr/0001-three-tier-epistemic-archive.md), [`docs/adr/0002-canonical-hub-and-live-sync.md`](docs/adr/0002-canonical-hub-and-live-sync.md), & [`docs/adr/0003-numbered-results-ledger.md`](docs/adr/0003-numbered-results-ledger.md).
- [`docs/upstream-notify-workflow.yml`](docs/upstream-notify-workflow.yml).
- [`docs/reviews/2026-11-26-round3-3cycle-hardening-log.md`](docs/reviews/2026-11-26-round3-3cycle-hardening-log.md), [`docs/reviews/2026-11-26-statement-audit.md`](docs/reviews/2026-11-26-statement-audit.md), [`docs/reviews/2026-11-26-overnight-hardening-log.md`](docs/reviews/2026-11-26-overnight-hardening-log.md), [`docs/reviews/2026-11-25-3cycle-hardening-log.md`](docs/reviews/2026-11-25-3cycle-hardening-log.md), and [`docs/reviews/red-team-2026-11-25.md`](docs/reviews/red-team-2026-11-25.md).

## 8. Companion Hardened Releases

- [`0thernes/p-vs-np-frontier-lab`](https://github.com/0thernes/p-vs-np-frontier-lab) (`v1.2.0` pinned at `a70733f`, hardened on `main`, `0TH-2026-013`) — 25 audited Lean 4.35.0 declarations (14 known statements + conjunction + 5 `NonVacuity` + 5 `AdversarialTests`), 15 Palomar targets across 6 kernel checks (5 checker implementations), negative elaboration CI test asserting expected Lean `decide` rejection, 27 bibliography entries (`25` live Crossref title+author verified DOIs on `main` after fixing the 3 mismatched DOIs present at pinned `v1.2.0`, `2` archival print records without DOIs, `0` retractions), DigiCert RFC 3161 `.tsr`, `0 ruff`/`0 mypy`, interactive WCAG Blueprint, 100.0% Build Standard v1.2.0.
- [`0thernes/promislow-fracton-amoeba`](https://github.com/0thernes/promislow-fracton-amoeba) (`v1.0.0`, `0TH-2026-015`) — GitHub Pages workflow split into separate `build` and `deploy` jobs (`pages.yml` green & live), `check_citations.py` upgraded to enforce Crossref/arXiv title-overlap matching across all `18/18` references.
- [`0thernes/unsolved-black-hole-problems`](https://github.com/0thernes/unsolved-black-hole-problems) (`0TH-DISC-006`) — Linked to canonical hub in `README.md` with `.github/workflows/notify-archive.yml` dispatch hook.
