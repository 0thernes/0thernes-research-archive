# Evidence & Falsification Dossier — `0TH-2026-029`

**Title:** A Zero-Mathlib, Zero-Classical.choice Lean 4.35.0 Six-Kernel Formalization of the Odd-Length Barker Classification, Order-16 Circulant Hadamard Exclusion, and Reduction to Ryser's Conjecture  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Combinatorics / Number Theory / Coding Theory / Formal Verification  
**Version / Date:** `v1.0.0` (2026-11-27)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 & 100% zero Classical.choice verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/barker-hadamard-frontier |
| Pinned Git Submodule | `repos/barker-hadamard-frontier` @ `28f76669473eb86e43056d19465c3d1b35e23ce1` |
| GitHub Release | https://github.com/0thernes/barker-hadamard-frontier/releases/tag/v1.0.0 |
| Frozen Archived PDF | `papers/0TH-2026-029_barker-hadamard-frontier/Donahue_2026_barker_hadamard_frontier.pdf` |
| Frozen PDF SHA-256 | `3e4906ae957cd7f236ac7e3273fd5399c8ebd3d7a039f1ce3d47f3cfc69c58eb` |
| arXiv / Source Bundle SHA-256 | `d8396de13b50e4c0a3291071afa1d2af9353e821a2693ad721018f7ade5139bb` |
| CI Verification Run | https://github.com/0thernes/barker-hadamard-frontier/actions/runs/46106551162 |
| Software Heritage SWHID | `Pending manual Save Code Now` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Unconditionally classifies all odd-length Barker sequences (n in {1, 3, 5, 7, 11, 13}, T2a-T2f via Turyn-Storer skew-symmetry, doubling law, and Schmidt-Willms run bounds), proves even-length mod-4 elimination, integer Circulant Hadamard reduction M^T M = n I_n, square law n = 4u^2, Turyn 2-coset balance, general d-quotient folding (T1g), and elementary algebraic order-16 Circulant Hadamard impossibility (T1h) pushing the unconditional Barker exclusion to n = 4u^2 >= 36 (refuting all 14 <= n <= 35, T3b), and proves a verbatim biconditional bridge + kernel-checked conditional reduction H_CirculantHadamard -> UpstreamBarkerConjecture (T3a, T3c, T3d) pinned to google-deepmind/formal-conjectures commit 9097e2f90e66, with zero Mathlib and 100% zero Classical.choice (40/40 audited declarations strictly [propext, Quot.sound]).

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Pure Lean 4.35.0 (zero Mathlib, 100% zero Classical.choice: 40/40 audited declarations strictly [propext, Quot.sound] across 210 theorems, 19 Palomar Comparator targets, 7 NonVacuity witnesses, and 14 AdversarialTests refutations; verified across all 6 independent kernels: lean, leanchecker --fresh, leanchecker-paranoid, con-leche --verified, con-ron --verified, nanoda_bin)
- **Library Entry Point:** `lean/PalomarSolution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/PalomarChallenge.lean, lean/BarkerFrontier/FormalConjecturesBridge.lean, lean/BarkerFrontier/WitnessesAndAdversarial.lean`

## Verification Boundary (Honest Epistemic Scope)

All 210 theorems and 40 audited declarations (19 Palomar targets, 7 non-vacuity witnesses, 14 adversarial/sharpness refutations) are kernel-checked in zero-Mathlib, zero-Classical.choice Lean 4.35.0 strictly within [propext, Quot.sound], cross-checked against safe Rust, strict ISO C11 (+ 100k fuzzing), and Python/Hypothesis/mutation suites. Does NOT unconditionally prove Ryser's Circulant Hadamard Conjecture (H_CirculantHadamard) or eliminate even Barker lengths n = 4u^2 >= 36 without H_CirculantHadamard. Retires 0/2,000 Mega-Atlas grand problems unconditionally; not peer reviewed.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/barker-hadamard-frontier && (cd lean && lake build && lake env lean VerifyAxioms.lean) && (cd rust && cargo test --release)
```
