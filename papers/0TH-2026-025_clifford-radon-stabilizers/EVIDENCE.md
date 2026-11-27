# Evidence & Falsification Dossier — `0TH-2026-025`

**Title:** Clifford-Radon Stabilizers: Universal Finite-Field Radon Inversion, Modulo-3 Ancilla Phase Transitions, Canonical Type-I Twisted Quantum Double Obstructions, and Exact Quantum Geometry  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Quantum Information Theory / Topological Quantum Matter / Finite Geometry / Formal Verification  
**Version / Date:** `v1.1.0` (2026-11-27)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 & 3-OS CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/clifford-radon-stabilizers |
| Pinned Git Submodule | `repos/clifford-radon-stabilizers` @ `6fde4054f2445da9c3f81c9d82930c9834470b5c` |
| GitHub Release | https://github.com/0thernes/clifford-radon-stabilizers/releases/tag/v1.1.0 |
| Frozen Archived PDF | `papers/0TH-2026-025_clifford-radon-stabilizers/Donahue_2026_clifford_radon_stabilizers.pdf` |
| Frozen PDF SHA-256 | `248d0a1d87607fb183105cb65e474d06f6bd94378c4be28b2aa17b071960d611` |
| arXiv / Source Bundle SHA-256 | `02247e0b99d5a93f7c93e7f41e5e6eca372f081cc722674338cbc1283ba475ef` |
| CI Verification Run | https://github.com/0thernes/clifford-radon-stabilizers/actions/runs/46063758501 |
| Software Heritage SWHID | `swh:1:snp:d8ed231796b86384a1b8ff11c1fcf1d38cd93db2` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Machine-checks 22 headline theorems (T1a-T6c, incl. T3e/T3f/T3g) + master conjunction (= 23 Palomar targets), 6 NonVacuity witnesses (explicit quotient faithfulPhaseRing, faithful-character Z[Q/Z] group-algebra faithfulMomentRing with F(chi 0)=1 and chi(1/2)!=chi 0, and nontrivial ccz2_strict_level3), and 8 AdversarialTests refutations (37 named + exhaustive 929/929 VerifyAllDecls.lean sweep in zero-Mathlib Lean 4.35.0, all 6 independent proof kernels verified inside bubblewrap on Ubuntu CI run 46063758501 + live negative tamper rejection, SLSA #73267069) across four linked problems rooted in Fechisin et al. (arXiv:2610.00464v1): (I) Universal resolution of Conjecture B.5 (Eqs. 118-119) for all primes p and all m >= 2 via p-adic orbit-sum drop (T1a-T1b), hyperplane Radon drop (T1c), Newton-binomial CGK lift (T1d), and projective Radon inversion with zero affine shifts (T2a-T2c); (II) Complete exact ancilla dichotomy for EVERY prime p (even permitting arbitrary affine shifts N_b.x + d_b): qubit Walsh-Hadamard r_ab(C^{l-1} Z) = 2^l - 1 - l (T3a), universal 6-qudit non-abelian level-2 r_nonab(CCZ_p) = 3 (T3b), DFT-3 collapse r_ab(CCZ_p) = 3 iff p == 1 (mod 3) (T3c, T3f), and exact r_ab(CCZ_p) = 4 for p = 3 (newly discovered ternary Z/9Z cubic inclusion-exclusion identity T3e) and all p == 2 (mod 3) (T3d, T3e, T3g); (III) Canonical Type-I TQD tetrahedron phase exact Clifford level p + 1 vs. Type-III level 3 (T4), exponent-p collapse (T5a), phase stripping (T5b), 1D Else-Nayak Type-I/II boundary-anomaly vanishing for k <= p - 1 (T5c), and sharp carry SPT saturation at k = p (T5d, exact L = 2 2-gon cancellation to p - 1); and (IV) Exact Fubini-Study QGT-covariance law with zero Berry curvature (T6a), PSD metric (T6b), and exact Weyl-Heisenberg 2*alpha-moment / SRE invariance (T6c, M_2(|CCZ_2>) = log_2(32/11)). Differentially verified across 10 polyglot engines (Rust #![forbid(unsafe_code)] 3-OS, Zig 0.17, ISO C11 ASan/UBSan + 100k fuzz + CBMC 6.6.0 --z3 126/126 properties verified, C++23 ASan/UBSan, x86-64 NASM Assembly, Python exact Fraction + 1,000-ex Hypothesis + 9/9 100% mutation kill + 0 ruff/0 mypy, Moonlab WASM, QGTL, QRNG 128-state codeword sampler + 10k negative control + 20-seed Holm-Bonferroni statistical study [H1/H2 p_holm=3e-4, true-null H0 p_holm=0.695], Native Eshkol LLVM AD), TLA+ 24/24 BFS + mutant check, 19/19 bijective live non-retracted citations, 0-warning/0.00pt AMS-LaTeX PDF + clean-room arXiv tarball, live GitHub Pages Observatory & 23-target Proof Blueprint, OpenSSL-verified DigiCert RFC 3161 (.tsr) + 3-calendar OTS (.ots), Software Heritage snapshot swh:1:snp:d8ed231796b86384a1b8ff11c1fcf1d38cd93db2, and Draft 2020-12 Build Standard v1.2.0 audit.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Pure Lean 4.35.0 (zero Mathlib, 15 Lean module files [14 sorry-free; PalomarChallenge.lean is the intentional statement-only sorry stub], 37 audited named declarations across 22 headline theorems T1a-T6c [incl. T3e/T3f/T3g] + master conjunction [= 23 Palomar targets] + 6 NonVacuity witnesses [incl. faithful Z[Q/Z] group-algebra MomentRing and ccz2_strict_level3] + 8 AdversarialTests refutations, plus exhaustive metaprogrammatic VerifyAllDecls.lean sweep of ALL 929/929 project declarations strictly within [propext, Classical.choice, Quot.sound], autoImplicit = false, zero native_decide; all 23 Palomar targets passed all 6 independent proof kernels inside bubblewrap on Ubuntu CI run 46063758501 via lake check --paranoid [60,108-60,111 decls] & lake comparator --config comparator.json --paranoid [5,961-5,964 decls] + live tamper-injecting negative comparator & axiom gate: lean, leanchecker-paranoid, lean4lean, nanoda, con-leche --verified, con-ron --verified; SLSA #73267069)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/PalomarChallenge.lean, lean/PalomarSolution.lean, lean/CliffordRadon/NonVacuity.lean, lean/CliffordRadon/AdversarialTests.lean, lean/VerifyAllDecls.lean, lean/STATEMENT_FIDELITY.md`

## Verification Boundary (Honest Epistemic Scope)

All 37 named declarations and all 929/929 project declarations (VerifyAllDecls.lean) are kernel-checked in zero-Mathlib Lean 4.35.0 strictly within [propext, Classical.choice, Quot.sound] across all 6 independent kernels inside bubblewrap plus a live tamper-injecting negative gate on Ubuntu CI run 46063758501 (zero sorry outside PalomarChallenge.lean, zero native_decide). Multi-engine computations (Rust, Zig, ISO C11 + CBMC 6.6 --z3 126/126, C++23, NASM x86-64, Python Fraction + 9/9 mutation, Moonlab WASM CPU statevector simulation, QGTL, deterministic seeded QRNG + 20-seed Holm-Bonferroni study, Eshkol LLVM AD, TLA+ 24-state BFS) are strictly classical deterministic cross-checks outside the Lean kernel (no quantum hardware or physical entropy source claimed). Bulk 2D phase Conjecture V.4 of Fechisin et al. (arXiv:2610.00464v1) remains explicitly [OPEN], 0/2,000 overarching Mega-Atlas grand open problems are retired, and external third-party human replication remains partial. Claims no external peer review or external DOI.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/clifford-radon-stabilizers && (cd lean && lake build && lake build PalomarChallenge CliffordRadon.NonVacuity CliffordRadon.AdversarialTests && lake env lean VerifyAxioms.lean && lake env lean VerifyAllDecls.lean && lake check --paranoid && lake comparator --config comparator.json --paranoid) && (cd engines/rust && cargo clippy --all-targets -- -D warnings && cargo test --release) && (cd engines/zig && zig build test) && node engines/quantum/moonlab_radon_verify.mjs && pytest -v engines/python/test_oracle.py tests/test_repo_integrity.py && python3 engines/python/mutation_test.py && python3 scripts/check_tla_model.py && python3 scripts/check_readme_axioms.py --run-tamper-test && python3 scripts/generate_manifests.py --verify-only && python3 scripts/stamp_timestamps.py --verify --negative-test
```
