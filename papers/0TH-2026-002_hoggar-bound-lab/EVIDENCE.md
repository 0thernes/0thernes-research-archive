# Evidence & Falsification Dossier — `0TH-2026-002`

**Title:** Spectral bounds and their limits in Pauli contextuality: exact configurations and a proof of Jonah's Conjecture E  
**Author:** Alexander Stephen Donahue (0thernes LLC, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Quantum Foundations / Quantum Contextuality  
**Version / Date:** `v1.8.0` (2026-11-21)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; listed on ORCID)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/hoggar-bound-lab |
| Pinned Git Submodule | `repos/hoggar-bound-lab` @ `eb2d83ef72f882b33a89d81bead66def2ab5283d` |
| GitHub Release | https://github.com/0thernes/hoggar-bound-lab/releases/tag/v1.8.0 |
| Frozen Archived PDF | `papers/0TH-2026-002_hoggar-bound-lab/unified-contextuality.pdf` |
| Frozen PDF SHA-256 | `6d963d6da3381c91acae602a049b28c60d366b97d6d4fbd4553adb97a15b4ac1` |
| arXiv / Source Bundle SHA-256 | `980bbdc2ad84235bae87820379981e704e3ea90ccefbedc4062467d830183e2c` |
| CI Verification Run | https://github.com/0thernes/hoggar-bound-lab/actions/runs/44959312365 |
| Software Heritage SWHID | `swh:1:snp:f8afa748054409dffbad57b721d07eb57a545757` |
| Wayback Machine Snapshot | https://web.archive.org/web/20261110150849/https://0thernes.github.io/hoggar-bound-lab/paper/unified-contextuality.pdf?v=1.4.0 |
| External DOI | None claimed |

## Core Result

Unified study with complete Lean 4.35.0 formalizations (100 newly audited declarations across 12 modules, 13,910 library lines, plus retained audits) of the spectral floor and its asymptotic 1/2 Filter.Tendsto limits (Theorem 1, Corollary A), Theorem 2 (Kramers / quaternionic floor and elliptic quadrics Q-(2N-1,2)), Theorems 3-4 (5-way saturation equivalences and (2^N-1)|S| = square), Propositions 3, 8, 10, exact degrees 75 (4 qubits), 480 (5 qubits), 2016 (6 qubits) and 729344 (7 qubits), Theorem 13b (infinite non-closed contextual floor-saturating pure-CCZ determinant family |Psi_{3m}> for every m >= 1 proved directly from the state vector, plus a 540.3M-form N=9 cyclic-symmetry rank-8 C census), symplectic transvection invariance, CSS witnesses (315, 1575, 6975), exact double-counting ladders, unconditional bounds d(W(7,2)) >= 1455 and d(Q+(9,2)) >= 6444, Lemmas L1/L4 and master reduction paired with an independent 42-orbit W(5,2) C census and pure-integer dual check reproducing Jonah [J1]'s (315, 1575, 6975), a four-qubit cospectral C3 pair with distinct completion spectra (Theorem 14) and EXACT global binary completion optima min_y F(sigma_0, y) = 368 and min_y F(sigma_1, y) = 344 with exact gap 24 (Theorem 16'' via kernel-checked pure-integer MET-SDP duals), general cone lift and case C11 from C3 (Corollary 18), signed-Clifford orbit transport, Lemmas 20-21, Theorem 22 (universal cubic-trace identity) and Table 8 outside character sums, and Theorem 19: a full machine-checked Lean 4 proof of Jonah's Conjecture E at the canonical Hermitian eigenvalue-multiset level across all nine vertex cases (C1, C3, C5, C6, C8, C11, C12, C14, C15) for every N >= 4 (plus N >= 3 for C1, C3, C6, C11), accompanied by 202/202 exact verifier checks on Ubuntu 24.04 CI.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 / Mathlib v4.35.0
- **Library Entry Point:** `lean/HoggarBound.lean`
- **Primary Axiom Audit Script:** `lean/VerifyNewFormalizations.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/C3Verification.lean, lean/IndependentVerification.lean, lean/SaturatedVerification.lean, lean/SaturatedSevenVerification.lean, lean/StabilityVerification.lean`

## Preserved Component Manuscripts (Historical Provenance)

- **A machine-checked spectral floor for Pauli contextuality, and new configurations that attain it** (`v1.1.0 / v1.1.1`, `paper/spectral-floor.pdf`): Historical source study folded into unified-contextuality.pdf (not a separate journal submission).
- **Cospectral Pauli carriers with different completion spectra: an exact four-qubit C3 certificate** (`v0.2.0-c3-certificate`, `paper/c3-spectral-counterexample.pdf`): Historical 42-declaration C3 study folded into unified-contextuality.pdf.
- **A verified spectral bound for Pauli contextuality: independent validation and critical synthesis** (`v0.1.0-independent-verification`, `paper/independent-research-note.pdf`): Historical independent validation companion folded into unified-contextuality.pdf.

## Verification Boundary (Honest Epistemic Scope)

As of v1.8.0, the spectral floor and asymptotic 1/2 limits, Kramers quaternionic floor, 5-way saturation equivalences, Propositions 3/8/10, saturated configurations (75, 480, 2016, 729344), Theorem 13b infinite pure-CCZ determinant family |Psi_{3m}> for all m >= 1 directly from the state vector, symplectic transvection invariance, CSS witnesses (315, 1575, 6975), exact double-counting ladders, unconditional Kramers-lifted bounds d(W(7,2)) >= 1455 and d(Q+(9,2)) >= 6444, Lemmas L1/L4 and master reduction, four-qubit C3 spectral certificate (42 decls) and EXACT global binary completion optima min F(sigma_0) = 368 and min F(sigma_1) = 344 with exact gap 24 (Theorem 16'' via pure-integer MET-SDP duals, plus Corollary 16 & Proposition 16'), all-qubit C3 family (74 decls), general cone lift and case C11 (Corollary 18), signed-Clifford orbit transport, Lemmas 20-21, Theorem 22, and eigenvalue-multiset Theorem 19 (Jonah's Conjecture E in all 9 vertex cases for every N >= 4) are all kernel-checked in Lean 4.35.0 (100 audited declarations in VerifyNewFormalizations.lean, 13,910 library lines across 12 modules, zero sorry, zero native_decide, strictly standard axioms [propext, Classical.choice, Quot.sound]). Remaining outside Lean: state-to-mask identifications of finite Table 1 rows other than |Psi_{3m}>, Propositions 4, 6, 9 and 11, exhaustive enumerations of Theorems 12-13, the 540.3M-form N=9 rank-8 cyclic census, the independent 42-orbit W(5,2) C census and 42 pure-integer certificates reproducing Jonah [J1], printed C3 factorizations and spherical relaxation gap 32, and the single-orbit group-transitivity classification of Jonah [J3, Theorem B4]. Historical source manuscripts remain preserved inside the repository as component records of this single combined study (see publication/PAPER-MAP.md). Superseded GitHub repository archived read-only on 2026-11-24 and consolidated into 0TH-2026-009 (0thernes/pauli-contextuality-lab); this historical snapshot remains cryptographically pinned.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/hoggar-bound-lab/lean && lake build HoggarBound.Kramers HoggarBound.SaturationTheory HoggarBound.ConjectureE HoggarBound.ConjectureEExtras HoggarBound.AuditUpgrades HoggarBound.C3ExactOptima HoggarBound.SaturatedPhaseSix HoggarBound.NormPhaseFamily HoggarBound.ExactDegreesN4N5 && lake env lean VerifyNewFormalizations.lean && cd .. && python scripts/conjecture_e_trace_formula.py && python scripts/conjecture_e_trace_formula.py 6 && python scripts/c3_sdp_dual_check.py && python scripts/c3_exact_optima_check.py && python scripts/norm_phase_family.py && python scripts/exact_degrees_n4_n5.py
```
