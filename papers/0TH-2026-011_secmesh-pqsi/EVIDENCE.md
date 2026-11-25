# Evidence & Falsification Dossier — `0TH-2026-011`

**Title:** SecMesh-PQSI: Formal Algebraic and Information-Theoretic Foundations and Cryptographic Defense Engine for Post-Quantum and Post-Super-Intelligence Meshes  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Cryptography / Post-Quantum Security / Information Theory / Quantum Geometry  
**Version / Date:** `v2.2.0` (2026-11-25)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 & cross-platform CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/secmesh-pqsi |
| Pinned Git Submodule | `repos/secmesh-pqsi` @ `f90d518569a8cbe176efbf3a9a5b98057b85b12e` |
| GitHub Release | https://github.com/0thernes/secmesh-pqsi/releases/tag/v2.2.0 |
| Frozen Archived PDF | `papers/0TH-2026-011_secmesh-pqsi/Donahue_2026_secmesh_pqsi_formal_foundations.pdf` |
| Frozen PDF SHA-256 | `7c66c628e9cf69b1ba816bc72f3aa07f4ee45e515180990b2c6869c73eeb9ff8` |
| arXiv / Source Bundle SHA-256 | `4c6604fac74682c42807160746506e868f22c7d72821e92e8dbd1007149f5b4d` |
| CI Verification Run | https://github.com/0thernes/secmesh-pqsi/actions/runs/45721046640 |
| Software Heritage SWHID | `Pending manual Save Code Now` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Clean-room cryptographic refactoring of legacy BoogerCheeseOnRye/SecMesh@aff7dc6 rebuilt atop Tsotchke's MIT/Apache-2.0 stack (full live-API audit of all 27 public repos: 17 tsotchke + 10 Tsotchke-Corporation) into a Post-Quantum + Post-Super-Intelligence (information-theoretic) defense engine. Uncovers and resolves 10 defects in legacy SecMesh v1 and machine-checks 27 zero-Mathlib Lean 4.35.0 theorems across 7 families plus 4 zero-axiom adversarial counterexamples: (T1) finite-key DI-QKD forensics (S=354/125 > 2*sqrt(2) excess 316, 4x range-2 Hoeffding error, quarter-circle duality u^2+v^2=1 with max H_vN-H_min gap +0.235703 at S=2.699192, 93/256 deNoise bias & 70/256 weight-4 fragility, 5-lane composable epsilon); (T2) unconditional PSI triad (Shannon OTP bijection, k-factor XOR dual-survivability, constructive Toeplitz 2-universality, Cauchy-Schwarz LHL, general-field Carter-Wegman degree-d bound); (T3) Shamir (t,n) exact secrecy, Byzantine Singleton tightness n >= t + 2b, and CS-053 PIR capacity gap T^2 > 0; (T4) D-dim QGT PSD Lagrange/trace uncertainty, exact QGT Concurrence Surplus identity det(g) - (1/4)Omega^2 = (C^2/4)sin^2(theta/2) (60-digit residual 3.3e-60), Bravyi [[144,12,12]] Gross BB qLDPC certification (5,184 CSS checks, weight 6, k=12), exact topological Chern-Concurrence-Entropy Conservation Law c_eff^2 + C^2 = 1 proving H_min^DI(S_max) = 1 - log2(1 + |c_eff|) (T4d, 60-digit residual 1e-59), and libirrep SU(2) spin-j GHZ Heisenberg QFI scaling F_Q = N^2*tau_N > N <-> N*tau_N > 1 (T4e); (T5) FIPS 203 q=3329 / zeta=17 NTT invariants, zero-overflow Montgomery reduction, exact Compress_1 margin |e| <= 831 (tight at +832), and K_N bandwidth ceiling (<1.75% IT-MAC hedge); (T6) Discrete Laplacian PSD, Ising ground-state optimality & Cheeger expander contagion work barrier (T6a), plus Simmons deterministic zero-subliminal capacity, 2^k kleptographic bijection & threshold-hedged XOR signing nonce dual-closure (T6b); and (T7) first-principles Toner quantum CHSH monogamy S_AB^2 + S_AE^2 <= 8 with CKW tripartite Berry-monopole Eve isolation (T7a, zero Classical.choice) and exact Hiding-Binding Conservation Law TV(P0,P1) + Overlap(P0,P1) = 1 proving unconditional bit-commitment impossibility and hybrid PQ+PSI architectural necessity (T7b, zero Classical.choice in both Solution & PalomarSolution). Accompanied by bit-exact C11 Moonlab <-> OpenSSL 3.5.5 FIPS 203 ML-KEM-768 interop, Shamir duplicate-x/NaN/LE64/NULL C11 hardening, RFC-6479 bounded sliding-window anti-replay CW-128 framing, live execution of all 4 Eshkol v1.3.6 forward-mode dual-number AD modules (<1e-12), 58/58 C11 + ASan/UBSan + 500/500 fuzz, 16/16 Node 25, 13/13 pytest (incl. negative Lean kernel rejection), automated README axiom drift audit, 42/42 live HTTP-200 citations with 32/32 DOIs Crossref-verified not retracted, 100.0% Build Standard v1.2.0 compliance (76/76), interactive Proof Blueprint DAG, and two zero-overfull AMS-LaTeX white papers (18 pp. WP1 with 5 vector PDF figures + 5 pp. WP2 with bounded 10,000-resample nonparametric bootstrap 95% CIs).

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 (zero Mathlib, 15 files, 4,573 lines, 27 exported theorems T1a-T7b + prove_all + concrete SimpleField (Fin 5) & finite-graph NonVacuity + 4 zero-axiom AdversarialTests = 60 audited Solution/Palomar/Adversarial declarations, Palomar.t7b zero Classical.choice matching Solution.t7b; all 6 independent kernels passed on Ubuntu CI run 45721046640 via lake comparator --paranoid: Lean paranoid, lean4lean, nanoda, con-leche --verified 3,694 decls, con-ron --verified 3,694 decls, Lean default, plus live negative rejection of false Compress_1 claim; interactive SVG Proof Blueprint published at https://0thernes.github.io/secmesh-pqsi/blueprint.html; Sigstore SLSA build provenance attested)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/PalomarChallenge.lean, lean/PalomarSolution.lean, lean/SecMeshPQSI/NonVacuity.lean, lean/SecMeshPQSI/AdversarialTests.lean`

## Preserved Component Manuscripts (Historical Provenance)

- **SecMesh-PQSI: Cryptographic Systems Architecture, Tsotchke Stack Integration, Threat Model, and Pre-Registered Empirical Defense Evaluation (White Paper II, v2.2.0)** (`v2.2.0`, `dist/Donahue_2026_secmesh_pqsi_architecture.pdf`): Companion 5-page systems architecture, live-API-verified Tsotchke 27-repo audit (17+10), STRIDE+PQ+PSI threat model, RFC-6479 bounded sliding-window anti-replay CW-128 & live Eshkol AD runtime, and pre-registered 30-seed simulation white paper with bounded nonparametric bootstrap 95% CIs (0 overfull hboxes); archived in papers/0TH-2026-011_secmesh-pqsi/Donahue_2026_secmesh_pqsi_architecture.pdf.

## Verification Boundary (Honest Epistemic Scope)

All 27 algebraic, combinatorial, topological, and information-theoretic theorems (T1a-T7b), SimpleField (Fin 5) and finite-graph NonVacuity, and 4 zero-axiom adversarial boundary counterexamples are 100% kernel-checked in zero-Mathlib Lean 4.35.0 across all 6 independent kernels on Ubuntu CI run 45721046640 (zero sorry, zero native_decide, zero warnings, all 60 declarations strictly within [propext, Classical.choice, Quot.sound], plus live negative kernel rejection of a false Compress_1 claim); transcendental curves are cross-verified to 60-digit Decimal precision in Python and differentially across C11, Node 25, and live Eshkol dual-number AD (<1e-11). Explicitly disclaims physical photonic loophole-free QKD (software E91 is a mathematical finite-key simulator), requires an independent physical/pre-shared pad for unconditional PSI confidentiality, strictly separates verbatim-verified open Mega Atlas v2 conjectures (QC-021, CS-002, CS-026, CS-028, CS-030, CS-053, CS-061, QC-004, QC-018, QC-030, QC-042, STAT-014, SYS-024) from proved theorems, and claims no external peer review, FIPS 140-3 certification, or external DOI. Software Heritage Save Code Now awaits manual browser PoW completion.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/secmesh-pqsi && make -C native test && node node/tests/test_secmesh_v2.mjs && python scripts/check_readme_axioms.py && cd lean && lake build && lake env lean VerifyAxioms.lean && lake comparator --config palomar_comparator.json --paranoid
```
