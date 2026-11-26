# Build White Paper & Proof Evidence Dossier — `0TH-BUILD-004`

**Title:** The Unsolved Mathematics Atlas (v0.5.0): Eight-Domain Multi-Kernel Lean 4.35.0 Structural Core (69 Declarations), 10-Page Monograph, and Adversarial Collatz Case Study  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Mathematics / Open Problems / Adversarial Verification / Formal Methods  
**Version / Date:** `v0.5.0` (2026-11-25)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/unsolved-mathematics |
| Pinned Git Submodule | `repos/unsolved-mathematics` @ `0604df5c70c850df44f3fdd20519e46c82925224` |
| Archived Artifact | `builds/0TH-BUILD-004_unsolved-mathematics/Donahue_2026_unsolved_mathematics_atlas-v0.5.0.pdf` (from `releases/v0.5.0/Donahue_2026_unsolved_mathematics_atlas-v0.5.0.pdf`) |
| Artifact SHA-256 | `6e1e2dfd804ac43a92e2513a967260867f6fa48962e35fcd37a73ef2a407bed6` |
| Archived Artifact | `builds/0TH-BUILD-004_unsolved-mathematics/arxiv_submission-v0.5.0.tar.gz` (from `releases/v0.5.0/arxiv_submission-v0.5.0.tar.gz`) |
| Artifact SHA-256 | `8fac8e524b06bdda7f6bca732c4a5daece812ceffbc7a60b13c8fed054414f44` |
| Archived Artifact | `builds/0TH-BUILD-004_unsolved-mathematics/six_kernel_audit.txt` (from `lean/six_kernel_audit.txt`) |
| Artifact SHA-256 | `a15373ee6d68cfeedd76df0050be8d494b17496c666bc2307d81c5632e298408` |
| Archived Artifact | `builds/0TH-BUILD-004_unsolved-mathematics/formalization.yaml` (from `lean/formalization.yaml`) |
| Artifact SHA-256 | `da2982fb7fe7c99e71e732a347acfdd63a143159570df0887a514e1dc8614b51` |
| Archived Artifact | `builds/0TH-BUILD-004_unsolved-mathematics/WHITEPAPER-COLLATZ-MULTI-MODEL-CASE-STUDY-2026-07-01.md` (from `docs/WHITEPAPER-COLLATZ-MULTI-MODEL-CASE-STUDY-2026-07-01.md`) |
| Artifact SHA-256 | `30a5b117b5aa5eab3a6d38cf44fb19be9392f7f2ab4630d53dc140f87e864f96` |
| Archived Artifact | `builds/0TH-BUILD-004_unsolved-mathematics/WHITEPAPER-COLLATZ-MULTI-MODEL-CASE-STUDY-2026-07-01-QA-AUDIT-2026-07-02.md` (from `docs/WHITEPAPER-COLLATZ-MULTI-MODEL-CASE-STUDY-2026-07-01-QA-AUDIT-2026-07-02.md`) |
| Artifact SHA-256 | `1bc3917ee115edf6b70dd2025f4ec2efd3140b3e4d7605b2f56ecfcc196c4b5d` |
| Archived Artifact | `builds/0TH-BUILD-004_unsolved-mathematics/EDITORIAL-REVIEW-WHITEPAPER-2026-07-01.md` (from `docs/EDITORIAL-REVIEW-WHITEPAPER-2026-07-01.md`) |
| Artifact SHA-256 | `fb3f01099f3a092e7d11caba8ba8b1c7f2e3fb55ca5a8b0eb30e9976e22c7eed` |

## Summary

Specialist open-mathematics research atlas upgraded to v0.5.0 with an 8-domain zero-Mathlib Lean 4.35.0 structural core (45 theorems + 10 concrete non-vacuity witnesses + 14 adversarial false-variant refutations = 69 audited declarations verified across all 6 independent kernels) covering Collatz, Erdos-Straus, Lonely Runner, Brocard, Primes/Twin Primes, Goldbach, Odd Perfect/Mersenne Primes, and Ramsey R(3,3)=6, paired with a 10-page AMS-LaTeX monograph PDF, standalone arXiv source bundle, FAIR metadata, live GitHub Pages site, and the preserved July 2026 adversarial Collatz multi-model case study.

## Embedded Lean 4 Proof Suite Audit

- **Framework:** Pure Lean 4.35.0 (zero Mathlib, Palomar Challenge/Solution/NonVacuity/Adversarial, 6-kernel lake comparator --paranoid)
- **Lean Modules / Lines:** 15 files / 2964 lines
- **Audited Theorems (`#print axioms`):** 69
- **Entry Point:** `lean/Solution.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Live Audit Status:** GitHub Actions CI GREEN (run #45742865067, workflow CI, v0.5.0); 69 audited declarations (45 headline theorems + 10 concrete NonVacuity witnesses + 14 adversarial false-variant refutations) verified across all 6 independent kernels (lean, leanchecker-paranoid, comparator in CI run 45742865067: lean4lean 2,737 decls, con-leche 2,740, con-ron 2,740; lake check --paranoid 58,545–58,548 decls) strictly within [propext, Classical.choice, Quot.sound]

## Verification Boundary

All 69 Lean 4.35.0 declarations compile with zero Mathlib, zero sorry, and strictly standard axioms across 6 independent kernels (CI #45742865067). Explicitly proves ZERO open conjectures (Collatz, Erdos-Straus, Lonely Runner, Brocard, Twin Primes, Goldbach, Odd Perfect Numbers, Mersenne infinitude all remain OPEN); formalizes classical foundations, modular reductions, sharpness bounds, and adversarial refutations only.

## Independent Reproduction & Falsification Protocol

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/unsolved-mathematics/lean && lake build && lake env lean VerifyAxioms.lean && lake comparator --config comparator.json --paranoid
```
