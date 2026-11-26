# Evidence & Falsification Dossier — `0TH-2026-013`

**Title:** Anatomy of the P vs. NP Barrier: Zero-Mathlib Lean 4 Formalization of Classical Obstructions, Exact SAT Multiplicative Complexity, and Four Algorithmic Falsifiers  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Computational Complexity / Proof Complexity / Formal Verification  
**Version / Date:** `v1.1.0` (2026-11-25)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 & cross-platform CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/p-vs-np-frontier-lab |
| Pinned Git Submodule | `repos/p-vs-np-frontier-lab` @ `01e56da105db4ec7cabb8aa19b8c7f6dfd48ac67` |
| GitHub Release | https://github.com/0thernes/p-vs-np-frontier-lab/releases/tag/v1.1.0 |
| Frozen Archived PDF | `papers/0TH-2026-013_p-vs-np-frontier-lab/Donahue_2026_p_vs_np_barrier_anatomy.pdf` |
| Frozen PDF SHA-256 | `c82738df5d755b38bf8cff70e33cd39f589eb4f80b407dc2da987ffb33591983` |
| arXiv / Source Bundle SHA-256 | `46ab7262d8b5a85266fba751035df028b39c7dc3e87a937b585731c7abe6d0aa` |
| CI Verification Run | https://github.com/0thernes/p-vs-np-frontier-lab/actions/runs/45743257383 |
| Software Heritage SWHID | `Pending manual Save Code Now` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Machine-checks 14 classical complexity-barrier theorems (C1-C14) in zero-Mathlib Lean 4.35.0 with Palomar Challenge/Solution isolation (15 comparator targets): Baker-Gill-Solovay relativization (C1-C2), Markov-Fischer bounded-negation theorem & slice monotonicity (C3-C5), Razborov-Rudich natural proofs obstruction (C6), Schaefer polymorphism rigidity (C7-C9), algebraic/multiplicative & catalytic complexity bounds (C10-C13), and permanent-vs-determinant characteristic-2 collapse (C14). Paired with exact CaDiCaL 2.1.2 SAT multiplicative-complexity synthesis cross-checked by exhaustive brute-force enumeration, 4 rigorous falsifiers of aggressive P=NP heuristics (CTDS ODE blowup, rational LP integrality gaps, 3-adic Hensel non-Boolean root, completely rigid |Aut|=1 3-SAT instance), 12/12 cross-OS pytest+Hypothesis tests, 15-page zero-overfull AMS-LaTeX preprint + standalone arXiv tarball, live GitHub Pages Proof Blueprint, and 100.0% (63/63) Build Standard v1.2.0 compliance.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 (zero Mathlib, 15 module files / 8,078+ lines, 14 headline barrier theorems C1-C14 + prove_all = 15 Palomar comparator targets, zero sorry, zero native_decide, autoImplicit = false; verified across 6 independent kernels via lake check --paranoid & lake comparator --paranoid on Ubuntu CI)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/PalomarChallenge.lean, lean/PalomarSolution.lean`

## Verification Boundary (Honest Epistemic Scope)

All 14 classical barrier theorems plus master conjunction (15 audited targets) are 100% kernel-checked in zero-Mathlib Lean 4.35.0 strictly within [propext, Classical.choice, Quot.sound]. Explicitly formalizes known barriers and refutes heuristic attacks — makes ZERO claim to resolve P vs NP (Mega-Atlas CS-001) or any open complexity separation. Attack A (CTDS ODE) is explicitly tagged numerical_approximation; no external peer review or external DOI is claimed.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/p-vs-np-frontier-lab && python -m pytest -v tests/test_all.py && python scripts/check_readme_axioms.py && cd lean && lake build && lake build PalomarChallenge && lake env lean VerifyAxioms.lean && lake comparator --config comparator.json --paranoid
```
