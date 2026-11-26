# Evidence & Falsification Dossier — `0TH-2026-015`

**Title:** Hantzsche-Wendt Group Rings, All-Prime Type-II Fracton Codes, and 3D Non-Hermitian B4 Monodromy: A Zero-Mathlib Six-Kernel Formalization  
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

Unites three algebraic, arithmetic, and topological frontiers around the torsion-free Hantzsche-Wendt (Promislow) group P and its faithful 4-band Bloch embedding Psi: R[P] -> M_4(R[x^+-1, y^+-1, z^+-1]) across 15 headline theorems (T1a-T3c) + 5 auxiliary/adversarial/master declarations in zero-Mathlib Lean 4.35.0 (6-kernel lake comparator --paranoid verified): (I) torsion-freeness of P, universal Klein V_4-invariance of det(Psi(u)-EI_4) forcing constant determinant for every unit over an integral domain, exact 8-sign-point factorizations, Gardam's 21-term unit mod-4 congruence (89-term integer det with constant 97 and augmentation 945) + all-m 2-adic Hensel tower, exhaustive 2^21 support-preserving sign-lift impossibility (and strengthened arbitrary even-sum p obstruction via quaternionic norm P_1^2 - 31 != +-1 at (1,1,-1)), and P-equivariant bijective 21-neighbor linear CA (ALG-035/ANL-063); (II) universal involutive-ring unit-twisted CSS commutation, complete 64-signed Haah conic discriminant classification (smooth for all p >= 5), universal all-prime & char-0 no-string-operator proof for Haah CC1 via rational parametrization and 6 pairwise linear Bezout identities, exact odd-prime torsion threshold p=23, L=11 (k_23(11)=6), and Gardam-twisted vs. intrinsic non-Abelian HW fracton codes with exact (52,52)/(52,56) weights and 342-term integer commutator defect (QC-032/CM-016); and (III) global origin minimum for every V_4-symmetric midpoint-convex Ronkin function, Haah double-amoeba quadrilateral bounds & single-generator algebraic EP_2 Jordan defectiveness, and Artin B_4 braid relations + full S_4 (order 24) monodromy generation (CM-018/FLD-060). Paired with zero-dependency Rust core (4/4 tests, Ubuntu + Windows), Python exact oracle + Hypothesis + differential tests (9/9), 6/6 (100%) killed mutants, 18/18 live Crossref/arXiv citations (0 retractions), 10-page zero-warning AMS-LaTeX PDF + clean-room arXiv tarball, live 3D WebGL2 Studio & Proof Blueprint on GitHub Pages, SLSA Attestation #72484621 (Rekor 4117699930), Software Heritage full snapshot swh:1:snp:3de955e528951f543794d11b7c4ec43d5869e611, and 90/90 Build Standard v1.2.0 compliance.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Pure Lean 4.35.0 (zero Mathlib, 17 sorry-free Palomar module files, 20 audited declarations across T1a-T3c + hensel_geometric_identity + strengthened_no_sign_lift_of_gardam_support + NonVacuity + Adversarial + master Palomar conjunction strictly within [propext, Classical.choice, Quot.sound], autoImplicit = false, zero native_decide; verified across all 6 independent kernels lean/leanchecker-paranoid/lean4lean[3,860 decls]/nanoda_bin/con-leche[3,863 decls]/con-ron[3,863 decls] + lake comparator --paranoid inside bubblewrap on Ubuntu 24.04 CI with SLSA attestation #72484621 / Rekor 4117699930)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/PalomarChallenge.lean, lean/PalomarSolution.lean, lean/PromislowFracton/NonVacuity.lean, lean/PromislowFracton/Adversarial.lean`

## Verification Boundary (Honest Epistemic Scope)

All 20 audited declarations across Pillars I-III, NonVacuity, Adversarial, and Palomar comparator contracts are kernel-checked in zero-Mathlib Lean 4.35.0 strictly within [propext, Classical.choice, Quot.sound] across all 6 independent kernels on Ubuntu 24.04 CI (run 45751946493). Numerical 3D Ronkin quadrature (O(1/N) nodal-singularity convergence), bipolar skin-effect winding grids (max_err = 0.0), and continuous-loop canonical quartic discriminant braid degrees (-1,-3,-2,+3) are verified differentially between zero-dependency Rust and Python rather than in Lean real analysis. Overarching conjectures (Kaplansky's Unit Conjecture over C[G] or Z[P] for unrestricted supports, Gottschalk's Surjunctivity Conjecture for non-sofic groups, and asymptotic distance scaling of HW fracton covers) remain explicitly OPEN; claims no external peer review or external DOI.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/promislow-fracton-amoeba && (cd rust && cargo test --release) && PYTHONPATH=python pytest tests/test_all.py -v && PYTHONPATH=python python scripts/mutate.py && python scripts/check_readme_axioms.py && python scripts/audit_repo.py && (cd lean && lake build && lake env lean VerifyAxioms.lean && lake comparator --config comparator.json --paranoid)
```
