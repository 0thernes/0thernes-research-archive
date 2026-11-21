# Evidence & Falsification Dossier — `0TH-2026-002`

**Title:** Spectral bounds and their limits in Pauli contextuality: exact configurations and a proof of Jonah's Conjecture E  
**Author:** Alexander Stephen Donahue (0thernes LLC, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Quantum Foundations / Quantum Contextuality  
**Version / Date:** `v1.7.0` (2026-11-21)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; listed on ORCID)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/hoggar-bound-lab |
| Pinned Git Submodule | `repos/hoggar-bound-lab` @ `7b0f7690c5a83d436315b7b18f950509078ecc29` |
| GitHub Release | https://github.com/0thernes/hoggar-bound-lab/releases/tag/v1.7.0 |
| Frozen Archived PDF | `papers/0TH-2026-002_hoggar-bound-lab/unified-contextuality.pdf` |
| Frozen PDF SHA-256 | `62fac6aa4c0f83b57b26786318426087bb5be2a53d4b7e9c29791550ab483961` |
| arXiv / Source Bundle SHA-256 | `93d87bbecf73c0127ca92c41093ae192d10272f52aeb396439d6b657fade62e3` |
| CI Verification Run | https://github.com/0thernes/hoggar-bound-lab/actions/runs/44908422882 |
| Software Heritage SWHID | `swh:1:snp:4fb332121197dd97e4d57c082c3cd32457692b41` |
| Wayback Machine Snapshot | https://web.archive.org/web/20261110150849/https://0thernes.github.io/hoggar-bound-lab/paper/unified-contextuality.pdf?v=1.4.0 |
| External DOI | None claimed |

## Core Result

Unified study with complete Lean 4.35.0 formalizations of the spectral floor and its asymptotic 1/2 Filter.Tendsto limits (Theorem 1, Corollary A), Theorem 2 (Kramers / quaternionic floor and elliptic quadrics Q-(2N-1,2)), Theorems 3-4 (5-way saturation equivalences and (2^N-1)|S| = square), quantum-metric and two-character theorems (Propositions 3, 8, 10), exact contextuality degrees (75, 480, 729344) for 4-, 5-, and 7-qubit configurations, a four-qubit cospectral C3 pair with distinct completion spectra (Theorem 14) and tightened two-sided binary completion enclosures 330 <= min_y F(sigma_1, y) <= 344 < 347 <= min_y F(sigma_0, y) <= 368 (Corollary 16 & Proposition 16' via exact zero-sum QUBO SDP dual), general cone lift and case C11 from C3 (Corollary 18), signed-Clifford orbit transport, Lemmas 20-21, Theorem 22 (universal cubic-trace identity) and Table 8 outside character sums, and Theorem 19: a full machine-checked Lean 4 proof of Jonah's Conjecture E at the canonical Hermitian eigenvalue-multiset level across all nine vertex cases (C1, C3, C5, C6, C8, C11, C12, C14, C15) for every N >= 4 (plus N >= 3 for C1, C3, C6, C11), accompanied by 136 exact integer checks of Theorem 22 through six qubits and 15 exact checks of Proposition 16'.

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

As of v1.7.0, the spectral floor and asymptotic 1/2 limits, Kramers quaternionic floor, 5-way saturation equivalences, Propositions 3/8/10, saturated configurations (75, 480, 729344), four-qubit C3 spectral certificate (42 decls) and tightened two-sided binary enclosures [347,368] & [330,344] (Corollary 16 & Proposition 16'), all-qubit C3 family (74 decls), general cone lift and case C11 (Corollary 18), signed-Clifford orbit transport, Lemmas 20-21, Theorem 22 (universal cubic-trace identity), and eigenvalue-multiset Theorem 19 (Jonah's Conjecture E in all 9 vertex cases for every N >= 4) are all kernel-checked in Lean 4.35.0 (77 audited declarations in VerifyNewFormalizations.lean, 9,728 library lines across 7 modules, zero sorry, zero native_decide, strictly standard axioms [propext, Classical.choice, Quot.sound]). Remaining outside Lean: state-to-mask identifications of Table 1, Propositions 4, 6, 9 and 11, exhaustive enumerations of Theorems 12-13, printed C3 factorizations and relaxation gap 32, and the single-orbit group-transitivity classification of Jonah [J3, Theorem B4]. Historical source manuscripts remain preserved inside the repository as component records of this single combined study (see publication/PAPER-MAP.md).

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/hoggar-bound-lab/lean && lake build HoggarBound.Kramers HoggarBound.SaturationTheory HoggarBound.ConjectureE HoggarBound.ConjectureEExtras HoggarBound.AuditUpgrades && lake env lean VerifyNewFormalizations.lean && cd .. && python scripts/conjecture_e_trace_formula.py && python scripts/conjecture_e_trace_formula.py 6 && python scripts/c3_sdp_dual_check.py
```
