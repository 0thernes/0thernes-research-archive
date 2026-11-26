# Frequently Asked Questions (`docs/faq.md`)

### 1. Which repository is the single canonical master archive of everything `0thernes` has solved or verified?
**This repository (`0thernes/0thernes-research-archive`)** — along with its live GitHub Pages portal at [`https://0thernes.github.io/0thernes-research-archive/`](https://0thernes.github.io/0thernes-research-archive/). Specialist open-problem catalogues (`unsolved-problems-mega-atlas`, `unsolved-mathematics`, `unsolved-black-hole-problems`) remain focused domain spokes indexed inside this hub and kept live-synced via [`.github/workflows/live-sync.yml`](../.github/workflows/live-sync.yml) (see [ADR 0002](adr/0002-canonical-hub-and-live-sync.md)).

### 2. Why are entries split into Tier I, Tier II, and Tier III?
To enforce epistemic honesty: Tier I holds standalone formalized research preprints (`PAPERS.json`), Tier II holds public software/engineering builds with embedded white papers and Pure Lean 4 invariant suites (`BUILD_PAPERS.json`), and Tier III holds architectural laws, pre-registered empirical claims (including null results), finite certificates, synthesis dossiers, and open-problem atlases (`LAWS_AND_DISCOVERIES.json`).

### 3. Have any papers in this archive retired one of the 1,900 Mega-Atlas problems?
**No (`0 / 1,900` grand Mega-Atlas problems retired).** Five peer-literature open sub-conjectures/questions (`0TH-2026-006` Conjecture 7.7, `0TH-2026-010` Vinciguerra Sec. 6, `0TH-2026-009` Track 2 Muller–Saniga Sec. 6, `0TH-2026-012` Sun–Tao–Xu–Zhang Schur-syzygy rank, `0TH-2026-016` Tandon `arXiv:2608.30273` Open Problem #2 + 4 odd-cycle Shannon capacity world records) plus Jonah's Conjecture E (`0TH-2026-009` Track 1, with cited Theorem B4 outside Lean) are formally proved in Lean 4.35.0 within their exact published scopes; see [`registry/SOLVED_AND_ATLAS_BRIDGE.md`](../registry/SOLVED_AND_ATLAS_BRIDGE.md) and [`builds/0TH-BUILD-007_unsolved-problems-mega-atlas/0THERNES_SOLVED_AUDIT_2026-11-25.md`](../builds/0TH-BUILD-007_unsolved-problems-mega-atlas/0THERNES_SOLVED_AUDIT_2026-11-25.md).

### 4. How does real-time live synchronization work across upstream repos?
Every 2 hours (and immediately whenever an upstream repo dispatches `upstream-repo-updated` via `.github/workflows/notify-archive.yml`), `.github/workflows/live-sync.yml` runs `scripts/live_sync.py`, updates `registry/LIVE_ECOSYSTEM_MIRROR.json/.md` and the bounded live status block in `README.md`, re-verifies SHA-256 digests and `pytest`, and redeploys GitHub Pages automatically.

### 5. How do I verify every archived PDF, link, and submodule pin locally?
Run `python3 scripts/verify_archive.py`, `sha256sum -c CHECKSUMS.sha256`, and `python3 -m pytest -v tests/`. Every hash, relative link, privacy-firewall invariant, and Git submodule pin is verified in seconds.
