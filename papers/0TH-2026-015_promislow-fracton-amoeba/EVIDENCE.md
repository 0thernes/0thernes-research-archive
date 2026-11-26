# Evidence & Falsification Dossier — `0TH-2026-015`

**Title:** Hantzsche-Wendt Group Rings, Haah CC1 Curve Algebra, and S4 Permutation Facts: A Zero-Mathlib Six-Kernel Formalization  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Non-Commutative Algebra / Quantum Error Correction / Non-Hermitian Topology / Formal Verification  
**Version / Date:** `v1.0.0` (2026-11-25)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 & cross-platform CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/promislow-fracton-amoeba |
| Pinned Git Submodule | `repos/promislow-fracton-amoeba` @ `c829ab811568a13e2283db2175f684e35b17c816` |
| GitHub Release | https://github.com/0thernes/promislow-fracton-amoeba/releases/tag/v1.0.0 |
| Frozen Archived PDF | `papers/0TH-2026-015_promislow-fracton-amoeba/Donahue_2026_promislow_fracton_amoeba.pdf` |
| Frozen PDF SHA-256 | `bfdd96f71beb6fc132e89e939233e12f09c8775bf789ef3d3ce7140f94b41c78` |
| arXiv / Source Bundle SHA-256 | `caf374d2b698b988f28998dc7bb793047be57e343fbefec068e87ecd2efe1df1` |
| CI Verification Run | https://github.com/0thernes/promislow-fracton-amoeba/actions/runs/45751946493 |
| Software Heritage SWHID | `swh:1:snp:3de955e528951f543794d11b7c4ec43d5869e611` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Connects three topics around the torsion-free Hantzsche-Wendt (Promislow) group P and its standard 4x4 Bloch representation Psi (Passman, arXiv:2108.06570): R[P] -> M_4(R[x^+-1, y^+-1, z^+-1]) across 15 headline theorems (T1a-T3c) + 5 auxiliary/adversarial/master declarations in zero-Mathlib Lean 4.35.0 (6-kernel lake comparator --paranoid verified): (I) torsion-freeness of P, Klein V_4 conjugation of the Bloch matrix (the Lean determinant statement covers only the 8 integer sign points, where the V_4 action is the identity; constancy of unit determinants is argued on paper), exact 8-sign-point factorizations, Gardam's 21-term unit mod-4 congruence (89-term integer det with constant 97 and augmentation 945) (2-adic Hensel lifting: a generic identity in Lean, not instantiated for Gardam's unit; inverse supports computed in Rust/Python), failure of the 8 sign-point determinant test for all 2^21 sign lifts on Gardam's support (a necessary condition for a unit; the unit consequence is implied by Tabei arXiv:2608.00103) (and strengthened arbitrary even-sum p obstruction via quaternionic norm P_1^2 - 31 != +-1 at (1,1,-1)), and P-equivariant bijective 21-neighbor linear CA (ALG-035/ANL-063); (II) universal involutive-ring unit-twisted CSS commutation, complete 64-signed Haah conic discriminant classification (smooth for all p >= 5), an algebraic statement that no nontrivial monomial is constant on a rational parametrization of Haah's CC1 curve over integral domains with 2 != 0 containing roots of three quadratics of discriminant 5, plus one F_4 line (6 Bezout identities); the link to string operators is not formalized, a search showing p=23 is the first odd prime with an F_p-rational odd-order CC1 point (k_23(11)=6 is a Rust/Python computation, not Lean), and Gardam-twisted and intrinsic CSS stabilizer pairs over F_2[P]/Z[P] (no distance, logical-qubit or fracton property is formalized) with exact (52,52)/(52,56) weights and 342-term integer commutator defect (QC-032/CM-016); and (III) a non-strict origin-minimum lemma for midpoint-convex V_4-symmetric functions Q^3 -> Q (no Ronkin function in Lean), integer-point checks of defined amoeba inequality predicates and a nilpotent 2x2 matrix, and generation of S_4 by two permutations observed numerically as monodromies (CM-018/FLD-060). Paired with zero-dependency Rust core (4/4 tests, Ubuntu + Windows), Python exact oracle + Hypothesis + differential tests (9/9), 6/6 (100%) killed mutants, 18/18 live Crossref/arXiv citations (0 retractions), 10-page zero-warning AMS-LaTeX PDF + clean-room arXiv tarball, live 3D WebGL2 Studio & Proof Blueprint on GitHub Pages, SLSA Attestation #72484621 (Rekor 4117699930), Software Heritage full snapshot swh:1:snp:3de955e528951f543794d11b7c4ec43d5869e611, and 90/90 Build Standard v1.2.0 compliance.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Pure Lean 4.35.0 (zero Mathlib, 14 Lean files (PalomarChallenge.lean is the comparator template with sorry bodies; the proof files are sorry-free), 20 audited declarations across T1a-T3c + hensel_geometric_identity + strengthened_no_sign_lift_of_gardam_support + NonVacuity + Adversarial + master Palomar conjunction strictly within [propext, Classical.choice, Quot.sound], autoImplicit = false, zero native_decide; verified across all 6 independent kernels lean/leanchecker-paranoid/lean4lean[3,860 decls]/nanoda_bin/con-leche[3,863 decls]/con-ron[3,863 decls] + lake comparator --paranoid inside bubblewrap on Ubuntu CI with SLSA attestation #72484621 / Rekor 4117699930)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/PalomarChallenge.lean, lean/PalomarSolution.lean, lean/PromislowFracton/NonVacuity.lean, lean/PromislowFracton/AdversarialTests.lean`

## Verification Boundary (Honest Epistemic Scope)

All 20 audited declarations across Pillars I-III, NonVacuity, Adversarial, and Palomar comparator contracts are kernel-checked in zero-Mathlib Lean 4.35.0 strictly within [propext, Classical.choice, Quot.sound] by the Lean kernel; the 16 comparator targets and their dependency closure were also accepted by 6 kernel checks (5 distinct implementations) on Ubuntu CI (run 45751946493). Numerical 3D Ronkin quadrature (O(1/N) nodal-singularity convergence), bipolar skin-effect winding grids (max_err = 0.0), and continuous-loop canonical quartic discriminant braid degrees (-1,-3,-2,+3) are verified differentially between zero-dependency Rust and Python rather than in Lean real analysis. The unit conjecture is false over C (Gardam, arXiv:2312.05240, for this group P). Whether Z[P] or Q[P] has non-trivial units for unrestricted supports, Gottschalk's Surjunctivity Conjecture for non-sofic groups, and distance scaling of HW covers remain OPEN; claims no external peer review or external DOI.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/promislow-fracton-amoeba && (cd rust && cargo test --release) && PYTHONPATH=python pytest tests/test_all.py -v && PYTHONPATH=python python scripts/mutate.py && python scripts/check_readme_axioms.py && python scripts/audit_repo.py && (cd lean && lake build && lake env lean VerifyAxioms.lean && lake comparator --config comparator.json --paranoid)
```
