# Evidence & Falsification Dossier — `0TH-2026-013`

**Title:** Anatomy of the P vs. NP Barrier: Zero-Mathlib Lean 4 Formalization of Classical Obstructions, Exact SAT Multiplicative Complexity, and Four Algorithmic Falsifiers  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Computational Complexity / Proof Complexity / Formal Verification  
**Version / Date:** `v1.2.0` (2026-11-26)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0, negative elaboration test & cross-platform CI)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/p-vs-np-frontier-lab |
| Pinned Git Submodule | `repos/p-vs-np-frontier-lab` @ `a70733fc388c24e3789eef9fb7afc8464f1669fe` |
| GitHub Release | https://github.com/0thernes/p-vs-np-frontier-lab/releases/tag/v1.2.0 |
| Frozen Archived PDF | `papers/0TH-2026-013_p-vs-np-frontier-lab/Donahue_2026_p_vs_np_barrier_anatomy.pdf` |
| Frozen PDF SHA-256 | `c82738df5d755b38bf8cff70e33cd39f589eb4f80b407dc2da987ffb33591983` |
| arXiv / Source Bundle SHA-256 | `46ab7262d8b5a85266fba751035df028b39c7dc3e87a937b585731c7abe6d0aa` |
| CI Verification Run | https://github.com/0thernes/p-vs-np-frontier-lab/actions/runs/45829725341 |
| Software Heritage SWHID | `Pending manual Save Code Now` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Machine-checks 25 zero-Mathlib Lean 4.35.0 declarations (14 statements C1-C14 (the Baker-Gill-Solovay theorem, the counting step of natural proofs, and twelve classical supporting lemmas) + prove_all + 5 concrete NonVacuity witnesses NV1-NV5 + 5 AdversarialTests sharpness refutations ADV1-ADV5, with 15 isolated Palomar Challenge/Solution comparator targets and a negative elaboration test in CI (a false statement must fail to compile)): Baker-Gill-Solovay relativization (C1-C2), the counting step of the natural-proofs argument, a telescoping bound and a largeness witness (C3-C5), minimal unsatisfiability of odd-cycle and Mermin-Peres XOR systems (C6-C7), polymorphism facts and projection-only rigidity of {x∨y∨z, ¬x∨¬y∨¬z} (C8-C9), Markov's negation bound and a k-NOT compilation without size bound (C10-C11), AND-count versus F2-degree (C12), permanent = determinant mod 2 (C13), and reversible register programs (C14). Paired with exact CaDiCaL 2.1.2 SAT multiplicative-complexity synthesis cross-checked by exhaustive brute-force enumeration, three exact counterexamples and one numerical illustration against four illustrative SAT heuristics (CTDS ODE blowup, rational LP integrality gaps, 3-adic Hensel non-Boolean root, completely rigid |Aut|=1 3-SAT instance), 27 references (three DOIs in the repository's citation audit resolve to unrelated records; correction pending), DigiCert RFC 3161 TSA timestamp (data/MANIFEST.sha256.tsr) over LF-normalized 21-artifact MANIFEST.sha256, 0 ruff / 0 mypy errors, 12/12 cross-OS pytest+Hypothesis tests, 15-page zero-overfull AMS-LaTeX preprint + standalone arXiv tarball, interactive searchable WCAG 2.2 AA GitHub Pages Proof Blueprint, and 100.0% (63/63) Build Standard v1.2.0 compliance.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 (zero Mathlib, 17 module files / 8,250+ lines, 25 audited declarations: 14 headline statements C1-C14 + prove_all + 5 concrete NonVacuity witnesses NV1-NV5 + 5 AdversarialTests sharpness refutations ADV1-ADV5 [2 strictly zero-axiom], 15 Palomar comparator targets, zero sorry outside the 15 statement stubs in PalomarChallenge.lean, zero native_decide, autoImplicit = false; accepted by six kernel checks (five checker implementations) via lake check --paranoid & lake comparator --paranoid on Ubuntu CI, plus a negative elaboration test)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/PalomarChallenge.lean, lean/PalomarSolution.lean, lean/PVsNP/NonVacuity.lean, lean/PVsNP/AdversarialTests.lean`

## Verification Boundary (Honest Epistemic Scope)

All 25 audited Lean 4.35.0 declarations (14 headline statements, their conjunction, and 10 instantiated corollaries) are kernel-checked in zero-Mathlib Lean 4.35.0 strictly within [propext, Classical.choice, Quot.sound] (with ADV1/ADV2 strictly zero-axiom), accepted by six kernel checks (five checker implementations) on Ubuntu CI, with a negative elaboration test. Explicitly formalizes known barriers and refutes heuristic attacks — makes ZERO claim to resolve P vs NP (Mega-Atlas CS-001) or any open complexity separation. Attack A (CTDS ODE) is explicitly tagged numerical_approximation; no external peer review or external DOI is claimed.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/p-vs-np-frontier-lab && python -m pytest -v tests/test_all.py && python scripts/check_readme_axioms.py && python scripts/check_citations.py && cd lean && lake build && lake build PalomarChallenge && lake env lean VerifyAxioms.lean   # Linux only (bubblewrap): lake comparator --config comparator.json --paranoid
```
