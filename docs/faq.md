# Frequently Asked Questions (`docs/faq.md`)

### 1. Why are entries split into Tier I, Tier II, and Tier III?
To enforce epistemic honesty: Tier I holds standalone formalized research preprints (`PAPERS.json`), Tier II holds public software/engineering builds with embedded white papers and Pure Lean 4 invariant suites (`BUILD_PAPERS.json`), and Tier III holds architectural laws, pre-registered empirical claims (including null results), finite certificates, and open-problem atlases (`LAWS_AND_DISCOVERIES.json`).

### 2. Have any papers in this archive retired one of the 1,900 Mega-Atlas problems?
**No (`0 / 1,900` grand Mega-Atlas problems retired).** Specialized open conjectures such as Conjecture 7.7 of Banić & Elezović (`0TH-2026-006`) and Jonah's Conjecture E (`0TH-2026-009`) are formally proved in Lean 4 within their exact published scopes; see [`builds/0TH-BUILD-007_unsolved-problems-mega-atlas/0THERNES_SOLVED_AUDIT_2026-11-25.md`](../builds/0TH-BUILD-007_unsolved-problems-mega-atlas/0THERNES_SOLVED_AUDIT_2026-11-25.md).

### 3. How do I verify every archived PDF and submodule pin locally?
Run `python3 scripts/verify_archive.py` and `sha256sum -c CHECKSUMS.sha256`. Every hash and Git submodule pin is verified in under 2 seconds.
