# Changelog

All notable archive registrations, cryptographic pin updates, and hardening releases are logged here.

## [2026.11.25] - 2026-11-25

### Updated & Added
- **Updated `0TH-2026-006` (`multinomial-tv-conjecture` `v1.0.0` → `v2.0.0`):** Pinned submodule to `18d95f0f7446f355f54bf9f6a50189b87e88d7d8`, replaced frozen PDF with v2.0.0 zero-error build and byte-reproducible arXiv tarball digest, recorded 576 exhaustively audited Lean 4.35.0 theorems (0 Batteries linter warnings, 18 `NonVacuity` witnesses), full sandboxed Ubuntu 24.04 **6-kernel `lake comparator --paranoid`** pass (`CI run 45723630668`), Sigstore Rekor log `4114226539`, and GitHub Pages Blueprint (`https://0thernes.github.io/multinomial-tv-conjecture/`).
- **Updated `0TH-BUILD-007` (`unsolved-problems-mega-atlas` `v2.3.0` → `v2.3.1`):** Pinned submodule to `bebe7946a800f6caae515504beef9ac3c2ade040`, archived `0THERNES_SOLVED_AUDIT_2026-11-25.md` recording the honest `0 / 1,900` grand-problem retirement audit, removed R4-banned PR template, and verified 32/32 pytest + 72/72 Lean theorems.
- **Identity Accuracy:** Updated active archive headers (`README.md`, `CITATION.cff`, registry headers) from unformed `"0thernes LLC"` to `Independent Researcher, Spokane, WA, USA` matching ORCID `0009-0006-8168-9648`.
- **Build Standard v1.2.0 Hardening (`18.0% → 100.0%`):** Added `VERSION`, `CHANGELOG.md`, `CLAIMS.md`, `LIMITATIONS.md`, `REPLICATION.md`, `ROADMAP.md`, `SECURITY.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SUPPORT.md`, `NOTICE`, `THIRD_PARTY_NOTICES.md`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.cursor/rules/build-standard.mdc`, `llms.txt`, `llms-full.txt`, `justfile`, `requirements.txt`, `repo.yaml`, `repo-standard.schema.json`, `data/MANIFEST.sha256`, `tests/test_archive_integrity.py`, `docs/` suite, cross-platform CI (`ubuntu`/`windows`/`macos`), static Pages portal (`pages.yml`), and `SHA256SUMS` + Sigstore SLSA release workflow (`release.yml`).

## [2026.11.21] - 2026-11-21

### Added
- Initial three-tier public master vault covering Tier I standalone preprints (`registry/PAPERS.json`), Tier II public build white papers & embedded Pure Lean 4 suites (`registry/BUILD_PAPERS.json`), Tier III laws/discoveries/atlases (`registry/LAWS_AND_DISCOVERIES.json`), 20 pinned public submodules, and `scripts/verify_archive.py`.
