# Master Hardening Index & Table of Contents (`HARDENING_INDEX.md`)

Complete structural index and audit checklist for **0thernes Research Archive (`v2026.11.26`)** and its hardened companion releases **`0thernes/p-vs-np-frontier-lab` (`v1.2.0`)** and **`0thernes/unsolved-black-hole-problems`**, following **Build Standard for LLMs v1.2.0** (`R1`–`R8`, 10 finding classes, 90 items `A01`–`A45` & `B01`–`B45`) and **Defensible Independent AI Research Playbook v1.3**.

---

## Table of Contents

1. [Root Governance, Identity & Packaging](#1-root-governance-identity--packaging)
2. [Canonical Registries, Bridge & Live Mirror (`registry/`)](#2-canonical-registries-bridge--live-mirror-registry)
3. [Automation, Verification, Live Sync & Portal Scripts (`scripts/`)](#3-automation-verification-live-sync--portal-scripts-scripts)
4. [Automated Test Ladder (`tests/`)](#4-automated-test-ladder-tests)
5. [CI/CD, Live Sync, Pages & Provenance Workflows (`.github/workflows/`)](#5-cicd-live-sync-pages--provenance-workflows-githubworkflows)
6. [Frozen Cryptographic Archives (`papers/`, `builds/`, `discoveries/`) & Submodules (`repos/`)](#6-frozen-cryptographic-archives-papers-builds-discoveries--submodules-repos)
7. [Architecture, ADRs, Run Logs & 3-Cycle Hardening Dossiers (`docs/`)](#7-architecture-adrs-run-logs--3-cycle-hardening-dossiers-docs)
8. [Companion Hardened Releases (`p-vs-np-frontier-lab` & `unsolved-black-hole-problems`)](#8-companion-hardened-releases)

---

## 1. Root Governance, Identity & Packaging

| File | Role | Audit Status |
|---|---|---|
| [`README.md`](README.md) | Canonical hub overview, live mirror status block, 3-tier tables (**45 entries** / **32 submodules**), Quickstart & Usage | Audited Round 1 & Round 2 (`H-19` split Tier II table fixed, `H-20` counts enforced in CI) |
| [`VERSION`](VERSION) / [`CITATION.cff`](CITATION.cff) / [`CHANGELOG.md`](CHANGELOG.md) | Single-source release versioning (`2026.11.26`) & academic citation | Audited Rounds 1–2 (enforced by `test_single_version_consistency`) |
| [`LICENSE`](LICENSE) / [`NOTICE`](NOTICE) / [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) | Dual MIT / CC-BY-4.0 notice, clean Independent Researcher identity (zero unformed LLC) | Audited Rounds 1–2 |
| [`CLAIMS.md`](CLAIMS.md) / [`LIMITATIONS.md`](LIMITATIONS.md) / [`REPLICATION.md`](REPLICATION.md) / [`ROADMAP.md`](ROADMAP.md) | Claims C1–C5, Real-vs-Metaphor, reproducible protocol, roadmap | Audited Rounds 1–2 (synced to 45 entries / 32 submodules / 5 sub-conjectures / RFC 3161 TSA) |
| [`SECURITY.md`](SECURITY.md) / [`CONTRIBUTING.md`](CONTRIBUTING.md) / [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) / [`SUPPORT.md`](SUPPORT.md) | Community & vulnerability governance | Audited Rounds 1–2 |
| [`AGENTS.md`](AGENTS.md) / [`CLAUDE.md`](CLAUDE.md) / [`GEMINI.md`](GEMINI.md) / [`llms.txt`](llms.txt) / [`llms-full.txt`](llms-full.txt) | AI coding-agent instruction & context stack (A32) | Regenerated deterministically via `scripts/generate_llms_full.py` |
| [`repo.yaml`](repo.yaml) / [`repo-standard.schema.json`](repo-standard.schema.json) | Build Standard v1.2.0 Draft 2020-12 validated project manifest | Validated in pytest & CI |
| [`justfile`](justfile) / [`pytest.ini`](pytest.ini) / [`requirements.txt`](requirements.txt) / [`.gitmodules`](.gitmodules) / [`.gitattributes`](.gitattributes) / [`.gitignore`](.gitignore) | Task runner, bracket-safe pytest config, pinned deps, **32 public submodules**, LF enforcement | Audited Rounds 1–2 |
| [`CHECKSUMS.sha256`](CHECKSUMS.sha256) / [`data/MANIFEST.sha256`](data/MANIFEST.sha256) / [`data/RELEASE_FREEZE.sha256`](data/RELEASE_FREEZE.sha256) / [`data/RELEASE_FREEZE.sha256.tsr`](data/RELEASE_FREEZE.sha256.tsr) | Byte-identical SHA-256 manifests + live DigiCert RFC 3161 TSA seal over immutable frozen release artifacts | Verified on 3 OSes (`sha256sum -c`, Python oracle & DER digest check) |

## 2. Canonical Registries, Bridge & Live Mirror (`registry/`)

- [`registry/PAPERS.json`](registry/PAPERS.json) & [`registry/PAPERS.md`](registry/PAPERS.md) — **16 Tier I standalone preprints** (`0TH-2026-001` through `0TH-2026-016`, with `001/002/003/005` clearly marked as archived historical snapshots consolidated into `0TH-2026-009`).
- [`registry/BUILD_PAPERS.json`](registry/BUILD_PAPERS.json) & [`registry/BUILD_PAPERS.md`](registry/BUILD_PAPERS.md) — **17 Tier II public builds & embedded Pure Lean 4.35.0 suites** (`0TH-BUILD-001` through `0TH-BUILD-017`, **1,058 audited Pure Lean 4.35.0 declarations** across 15 Lean-bearing builds).
- [`registry/LAWS_AND_DISCOVERIES.json`](registry/LAWS_AND_DISCOVERIES.json) & [`registry/LAWS_AND_DISCOVERIES.md`](registry/LAWS_AND_DISCOVERIES.md) — **12 Tier III public laws, pre-registered empirical claims, discoveries, synthesis dossiers & open-problem atlases** (`0TH-DISC-001` through `0TH-DISC-012`).
- [`registry/SOLVED_AND_ATLAS_BRIDGE.json`](registry/SOLVED_AND_ATLAS_BRIDGE.json) & [`registry/SOLVED_AND_ATLAS_BRIDGE.md`](registry/SOLVED_AND_ATLAS_BRIDGE.md) — **26 version-checked rows** cross-referencing all 1,900 Mega-Atlas V2 problems (`0 / 1,900` grand problems retired; **5** peer-literature open sub-conjectures/questions proved in Lean 4.35.0).
- [`registry/LIVE_ECOSYSTEM_MIRROR.json`](registry/LIVE_ECOSYSTEM_MIRROR.json) & [`registry/LIVE_ECOSYSTEM_MIRROR.md`](registry/LIVE_ECOSYSTEM_MIRROR.md) — Live upstream commit, release, CI, and Pages status across all **38 unique tracked public non-fork `0thernes/*` repositories**.

## 3. Automation, Verification, Live Sync & Portal Scripts (`scripts/`)

- [`scripts/verify_archive.py`](scripts/verify_archive.py) — Deterministic `--sync` dossier/checksum/release-freeze generator + full verifier (SHA-256, RFC 3161 TSA digest verification, ORCID, Lean axioms, submodule pins, `README.md` table-continuity & count parity, exact bridge-to-registry version parity, mirror count parity, zero broken markdown links, zero unformed LLC strings, `< 5 MB` A24 size guard).
- [`scripts/live_sync.py`](scripts/live_sync.py) — Stdlib GitHub API live mirror, privacy firewall, bridge markdown renderer, and `README.md` live block updater (`--offline` supported, zero-noise idempotent).
- [`scripts/build_site.py`](scripts/build_site.py) — WCAG 2.2 AA searchable 3-tier + Bridge + Live Mirror static GitHub Pages generator.
- [`scripts/generate_llms_full.py`](scripts/generate_llms_full.py) — Deterministic `llms.txt` & `llms-full.txt` builder.
- [`scripts/register_paper.py`](scripts/register_paper.py) — Clean registration helper.
- [`scripts/audit-repo.sh`](scripts/audit-repo.sh) & [`scripts/Audit-Repo.ps1`](scripts/Audit-Repo.ps1) — Cross-platform Build Standard v1.2.0 self-auditors.

## 4. Automated Test Ladder (`tests/`)

- [`tests/test_archive_integrity.py`](tests/test_archive_integrity.py) — Draft 2020-12 schema, version parity, R4 zero banned files, privacy firewall across all 5 registries, zero unformed LLC, zero broken local markdown links, `README.md` table-continuity & negative split-table mutant rejection, bridge-to-registry exact version parity & mutant rejection, RFC 3161 TSA verification, end-to-end `verify_archive.py` + manifest parity, latest consolidated entries (`0TH-2026-013 v1.2.0`, `0TH-2026-014..016`, `0TH-BUILD-012..017`), Mega-Atlas honesty invariants, `live_sync.py` negative & HTTP-500 failure-injection tests, WCAG portal build check, metamorphic `--sync` idempotence (B14), Hypothesis property-based SHA-256 differential check (B10/B11), and surgical mutant-killing tests (B06/B13).

## 5. CI/CD, Live Sync, Pages & Provenance Workflows (`.github/workflows/`)

- [`.github/workflows/archive-audit.yml`](.github/workflows/archive-audit.yml) — 3-OS (`ubuntu`, `windows`, `macos`) cryptographic audit + `pytest` + `build_site.py` + `ruff`/`mypy` + Build Standard v1.2.0 + `gitleaks`.
- [`.github/workflows/live-sync.yml`](.github/workflows/live-sync.yml) — Real-time sync on `repository_dispatch`, 2-hour `cron` (`0 */2 * * *`), and `workflow_dispatch`.
- [`.github/workflows/pages.yml`](.github/workflows/pages.yml) — Static portal build & GitHub Pages deployment.
- [`.github/workflows/release.yml`](.github/workflows/release.yml) — Release tarball, `SHA256SUMS`, and Sigstore SLSA build provenance attestation.

## 6. Frozen Cryptographic Archives (`papers/`, `builds/`, `discoveries/`) & Submodules (`repos/`)

- `papers/` — **16** directories (`0TH-2026-001`..`0TH-2026-016`), each with frozen PDF(s), `METADATA.json`, `EVIDENCE.md`.
- `builds/` — **17** directories (`0TH-BUILD-001`..`0TH-BUILD-017`), including updated [`builds/0TH-BUILD-007_unsolved-problems-mega-atlas/0THERNES_SOLVED_AUDIT_2026-11-25.md`](builds/0TH-BUILD-007_unsolved-problems-mega-atlas/0THERNES_SOLVED_AUDIT_2026-11-25.md).
- `discoveries/` — **12** directories (`0TH-DISC-001`..`0TH-DISC-012`), all `< 5 MB` per file.
- `repos/` — **32** pinned public Git submodules (`160000` gitlinks verified against registry JSONs).

## 7. Architecture, ADRs, Run Logs & 3-Cycle Hardening Dossiers (`docs/`)

- [`docs/index.md`](docs/index.md), [`docs/architecture.md`](docs/architecture.md), [`docs/configuration.md`](docs/configuration.md), [`docs/operations.md`](docs/operations.md), [`docs/threat-model.md`](docs/threat-model.md), [`docs/faq.md`](docs/faq.md), [`docs/glossary.md`](docs/glossary.md), [`docs/run-log.md`](docs/run-log.md).
- [`docs/adr/0001-three-tier-epistemic-archive.md`](docs/adr/0001-three-tier-epistemic-archive.md) & [`docs/adr/0002-canonical-hub-and-live-sync.md`](docs/adr/0002-canonical-hub-and-live-sync.md).
- [`docs/upstream-notify-workflow.yml`](docs/upstream-notify-workflow.yml).
- [`docs/reviews/2026-11-26-overnight-hardening-log.md`](docs/reviews/2026-11-26-overnight-hardening-log.md), [`docs/reviews/2026-11-25-3cycle-hardening-log.md`](docs/reviews/2026-11-25-3cycle-hardening-log.md), and [`docs/reviews/red-team-2026-11-25.md`](docs/reviews/red-team-2026-11-25.md).

## 8. Companion Hardened Releases

- [`0thernes/p-vs-np-frontier-lab`](https://github.com/0thernes/p-vs-np-frontier-lab) (`v1.2.0`, `0TH-2026-013`) — Gold Standard Playbook v1.3 release (25 audited Lean 4.35.0 declarations incl. 5 `NonVacuity` + 5 `AdversarialTests`, 15 Palomar targets across 6 kernels, mandatory live negative Lean kernel rejection CI gate, 27/27 live verified citations / 0 retractions, DigiCert RFC 3161 `.tsr`, 0 `ruff`/0 `mypy`, interactive WCAG Blueprint, 100.0% Build Standard v1.2.0).
- [`0thernes/unsolved-black-hole-problems`](https://github.com/0thernes/unsolved-black-hole-problems) (`0TH-DISC-006`) — Linked to canonical hub in `README.md` with `.github/workflows/notify-archive.yml` dispatch hook.
