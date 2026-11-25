# Evidence & Falsification Dossier — `0TH-2026-011`

**Title:** SecMesh-PQSI: Formal Algebraic and Information-Theoretic Foundations and Cryptographic Defense Engine for Post-Quantum and Post-Super-Intelligence Meshes  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Cryptography / Post-Quantum Security / Information Theory / Quantum Geometry  
**Version / Date:** `v1.0.1` (2026-11-25)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 & cross-platform CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/secmesh-pqsi |
| Pinned Git Submodule | `repos/secmesh-pqsi` @ `a5ec809751b2f90197b4af8bf874ad9120b76573` |
| GitHub Release | https://github.com/0thernes/secmesh-pqsi/releases/tag/v1.0.1 |
| Frozen Archived PDF | `papers/0TH-2026-011_secmesh-pqsi/Donahue_2026_secmesh_pqsi_formal_foundations.pdf` |
| Frozen PDF SHA-256 | `5b39a8bd2e45235e0d016d02cf4de4f680a5a2ac66fffd710ec0fb13dcccd9f4` |
| arXiv / Source Bundle SHA-256 | `7761b855cd6c1aefc40e5591352cb129faf5a5c58f84e0e518b2bb258365b78d` |
| CI Verification Run | https://github.com/0thernes/secmesh-pqsi/actions/runs/45673196390 |
| Software Heritage SWHID | `Pending manual Save Code Now` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Clean-room cryptographic refactoring of legacy BoogerCheeseOnRye/SecMesh@aff7dc6 rebuilt atop Tsotchke's MIT/Apache-2.0 stack (moonlab, quantum_geometric_tensor, eshkol, rosette-wire, pq-consensus-bandwidth, libirrep) into a Post-Quantum + Post-Super-Intelligence (information-theoretic) defense engine. Uncovers and resolves 10 defects in legacy SecMesh v1 and machine-checks 21 zero-Mathlib Lean 4.35.0 theorems across 5 families: (T1) finite-key DI-QKD forensics (S=354/125 > 2*sqrt(2) excess 316, 4x range-2 Hoeffding error, quarter-circle duality u^2+v^2=1 with max H_vN-H_min gap +0.235703 at S=2.699192, 93/256 deNoise bias & 70/256 weight-4 fragility, 5-lane composable epsilon); (T2) unconditional PSI triad (Shannon OTP bijection, k-factor XOR dual-survivability, constructive Toeplitz 2-universality, Cauchy-Schwarz LHL, general-field Carter-Wegman degree-d bound); (T3) Shamir (t,n) exact secrecy, Byzantine Singleton tightness n >= t + 2b, and CS-053 PIR capacity gap T^2 > 0; (T4) D-dim QGT PSD Lagrange/trace uncertainty, a new exact closed-form QGT Concurrence Surplus identity det(g) - (1/4)Omega^2 = (C^2/4)sin^2(theta/2) bridging QGTL to Horodecki CHSH (60-digit residual 3.3e-60), and general group-algebra involution proof certifying Bravyi [[144,12,12]] Gross BB qLDPC (5,184 CSS checks, weight 6, k=12); and (T5) FIPS 203 q=3329 / zeta=17 NTT invariants, zero-overflow Montgomery reduction, exact Compress_1 margin |e| <= 831 (tight at +832), and complete-graph K_N bandwidth ceiling optimality (<1.75% IT-MAC hedge overhead). Accompanied by bit-exact C11 Moonlab <-> OpenSSL 3.5.5 FIPS 203 ML-KEM-768 interop (40/40 C11 + ASan/UBSan + 500/500 fuzz, 12/12 Node 25, 11/11 pytest, 32/32 live HTTP-200 citations), 100.0% Build Standard v1.2.0 compliance (76/76), and two zero-overfull AMS-LaTeX white papers.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 (zero Mathlib, 12 files, 3,501 lines, 21 exported theorems T1a-T5d + prove_all + concrete SimpleField (Fin 5) NonVacuity = 44 audited Solution/Palomar declarations; all 6 independent kernels passed on Ubuntu CI run 45673196390 via lake comparator --paranoid: Lean paranoid, lean4lean 3,549 decls, nanoda, con-leche 3,552 decls, con-ron 3,552 decls, Lean default; Sigstore SLSA build provenance attested)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/PalomarChallenge.lean, lean/PalomarSolution.lean, lean/SecMeshPQSI/NonVacuity.lean`

## Preserved Component Manuscripts (Historical Provenance)

- **SecMesh-PQSI: Cryptographic Systems Architecture, Tsotchke Stack Integration, Threat Model, and Pre-Registered Empirical Defense Evaluation (White Paper II, v1.0.1)** (`v1.0.1`, `dist/Donahue_2026_secmesh_pqsi_architecture.pdf`): Companion 5-page systems architecture, Tsotchke 30-repo audit, STRIDE+PQ+PSI threat model, and pre-registered 30-seed simulation white paper (0 overfull hboxes); archived in papers/0TH-2026-011_secmesh-pqsi/Donahue_2026_secmesh_pqsi_architecture.pdf.

## Verification Boundary (Honest Epistemic Scope)

All 21 algebraic, combinatorial, and information-theoretic theorems (T1a-T5d) plus SimpleField (Fin 5) NonVacuity are 100% kernel-checked in zero-Mathlib Lean 4.35.0 across all 6 independent kernels on Ubuntu CI run 45673196390 (zero sorry, zero native_decide, zero warnings, strictly within [propext, Classical.choice, Quot.sound]); transcendental curves are cross-verified to 60-digit Decimal precision in Python and differentially across C11 and Node 25 (<1e-11). Explicitly disclaims physical photonic loophole-free QKD (software E91 is a mathematical finite-key simulator), requires an independent physical/pre-shared pad for unconditional PSI confidentiality, separates open Mega Atlas conjectures (QC-021, CS-026/028/031/050/053/054/061, QC-034/042) from proved theorems, and claims no external peer review, FIPS 140-3 certification, or external DOI. Software Heritage Save Code Now awaits manual browser PoW completion.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/secmesh-pqsi && make -C native test && node node/tests/test_secmesh_v2.mjs && cd lean && lake build && lake env lean VerifyAxioms.lean && lake comparator --config palomar_comparator.json --paranoid
```
