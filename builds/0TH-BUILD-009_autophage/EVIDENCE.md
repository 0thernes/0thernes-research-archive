# Build White Paper & Proof Evidence Dossier — `0TH-BUILD-009`

**Title:** AUTOPHAGE v1.4.0: A Bare-Metal Polymorphic x86-64 Galois-Field Genetic Engine with 48 Pure Six-Kernel Lean 4.35.0 Proofs and 18-Gate Silicon Falsification  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Systems Architecture / Coding Theory / Artificial Life / Formal Methods  
**Version / Date:** `v1.4.0` (2026-11-26)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/autophage |
| Pinned Git Submodule | `repos/autophage` @ `1956c2cc54845ebadc54b2a5276cbc66bf031a8b` |
| Archived Artifact | `builds/0TH-BUILD-009_autophage/Donahue_2026_autophage.pdf` (from `dist/Donahue_2026_autophage.pdf`) |
| Artifact SHA-256 | `2d11a5a3cf292c090063572bba09d0a2daed0a77d93fe97523dfda7a2fb2684c` |
| Archived Artifact | `builds/0TH-BUILD-009_autophage/arxiv_submission.tar.gz` (from `dist/arxiv_submission.tar.gz`) |
| Artifact SHA-256 | `7dcacb8aede1e7674c0019ef74351ad42f60ec7843b86e1d6e84bd0358f549b3` |
| Archived Artifact | `builds/0TH-BUILD-009_autophage/VERIFICATION.md` (from `VERIFICATION.md`) |
| Artifact SHA-256 | `08351f877caa7b1b60f530568a6f757348451ee034d8d07bdd01fb92b0c82b7f` |
| Archived Artifact | `builds/0TH-BUILD-009_autophage/ARCHITECTURE.md` (from `ARCHITECTURE.md`) |
| Artifact SHA-256 | `8678eafcf2e719bead98d49948553127d968adb9884604223d8412d9870eea3d` |
| Archived Artifact | `builds/0TH-BUILD-009_autophage/README.md` (from `README.md`) |
| Artifact SHA-256 | `900f2bb60bc63179a7c7fed63293af260949ea5b656eb715afe4815b2062bbc5` |
| Archived Artifact | `builds/0TH-BUILD-009_autophage/CLAIMS.md` (from `CLAIMS.md`) |
| Artifact SHA-256 | `c73864a2e712699ccc71439de657d692f4b77cae1ad44fb4d03803ca302a4a89` |
| Archived Artifact | `builds/0TH-BUILD-009_autophage/HARDENING_LOG.md` (from `HARDENING_LOG.md`) |
| Artifact SHA-256 | `158033193ed64ae27c6a8eff17efc5e97532a46d929025badceb7a701e37f842` |
| Archived Artifact | `builds/0TH-BUILD-009_autophage/MEGA_ATLAS_CROSSCHECK.md` (from `docs/MEGA_ATLAS_CROSSCHECK.md`) |
| Artifact SHA-256 | `f1c00a8d281b8604937dbc11ec49d26e7af4a241cffaf817f97ee6e6497412ef` |
| Archived Artifact | `builds/0TH-BUILD-009_autophage/lean4-audit.txt` (from `results/lean4-audit.txt`) |
| Artifact SHA-256 | `4c25a572d3626c26c554918e567ce20c82030451e884162afa8354ec471b5617` |
| Archived Artifact | `builds/0TH-BUILD-009_autophage/lean4-multi-kernel.txt` (from `results/lean4-multi-kernel.txt`) |
| Artifact SHA-256 | `57724cd2161990236ab00b769a3c00fbfb3256f7d38f806b1628bf29913800e5` |

## Summary

Hardened through 3 full audit cycles under dual Apache-2.0 / CC-BY-4.0 licenses and 100.0% (76/76, 33/33 Core) Build Standard v1.2.0 compliance: zero-dependency C11 bare-metal polymorphic x86-64 RWX genetic engine where each 256-byte organism translates a 64-byte germline through an evolvable 8x8 F_2 affine ribosome (VGF2P8AFFINEQB), recombines over F_2[x]/(x^8+p) (PCLMULQDQ), repairs via 2x2 Cauchy MDS codes over F_{2^8}, executes reversible Toffoli/Fredkin gates with exact POPCNT Landauer accounting, and computes 2-adic ultrametric kin distance (TZCNT). Verified by 48 pure zero-bv_decide Lean 4.35.0 Palomar theorems across all 6 independent kernels, 18/18 gates + 6/6 mutants, 0-bit SHA-256 JIT==Scalar parity across Win64 & Linux, 1M RWX fuzzing, N=24 locked Holm-Bonferroni stats (24/24 wins, p_Holm=0.00030), 8-page zero-overflow AMS-LaTeX PDF (17/17 live refs), SLSA #72482726, and honest 0/1,900 Mega-Atlas non-retirement audit.

## Embedded Lean 4 Proof Suite Audit

- **Framework:** Pure Lean 4.35.0 (Palomar module headers, zero Mathlib, autoImplicit = false, zero bv_decide, zero native_decide, 6-kernel bubblewrap lake check --paranoid & 48-theorem lake comparator --paranoid)
- **Lean Modules / Lines:** 5 files / 1792 lines
- **Audited Theorems (`#print axioms`):** 48
- **Entry Point:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Live Audit Status:** GitHub Actions CI GREEN (run #45751051356, 5/5 jobs: Windows C11 + Linux C11 -Werror ASan/UBSan 18/18 gates + 6/6 mutants + 1M RWX fuzz + prop_check + 8-page 0-overfull Tectonic AMS-LaTeX PDF & clean-room arXiv tarball with 17/17 live citations + SLSA provenance #72482726 / Rekor 4117522487 + 100.0% 76/76 Build Standard v1.2.0 + 6-kernel bubblewrap lake check --paranoid & lake comparator --paranoid across lean4, leanchecker-paranoid, lean4lean, nanoda_bin, con-leche, con-ron); Release v1.4.0 & SWH snapshot swh:1:snp:6ea23803655df1f9679deb98d44efbf53321a393 archived; 48/48 audited theorems (T01-T30, T39-T48 incl. 6 concrete NonVacuity & boundary refutations) strictly within [propext, Classical.choice, Quot.sound], 0 sorryAx outside isolated Challenge.lean, 0 bv_decide, 0 warnings

## Verification Boundary

All 48 Lean 4.35.0 theorems (T01-T48 incl. 6 NonVacuity/refutation witnesses across 5 files / 1,792 lines) compile cleanly with zero Mathlib, zero bv_decide, zero native_decide, zero sorry outside isolated Challenge.lean, and strictly [propext, Classical.choice, Quot.sound], verified across all 6 independent kernels on Ubuntu CI (#45751051356, SLSA #72482726 / Rekor 4117522487). Raw x86-64 machine-code emission, FP64 Kahan-Neumaier drift, 1M RWX fuzzing, 18 gates + 6 mutants, and N=24 empirical stats are program-audited outside the Lean kernel. Explicitly retires 0/1,900 overarching open problems in unsolved-problems-mega-atlas and makes no claims of biological life or peer review.

## Independent Reproduction & Falsification Protocol

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/autophage && SKIP_LEAN=1 ./build_linux.sh && python3 scripts/prop_check.py && python3 scripts/check_readme_axioms.py && (cd lean && lake build && lake build Challenge && lake env lean VerifyAxioms.lean && lake check --paranoid && lake comparator --config comparator.json --paranoid)
```
