# Evidence & Falsification Dossier — `0TH-2026-018`

**Title:** Thin Vieta Reflection Groups, Apollonian-Octahedral Reciprocity Obstructions, Integer-Superharmonic Sandpile Envelopes, and Markov-Hurwitz Geodesic Spectra: A Zero-Mathlib Six-Kernel Formalization  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Arithmetic Geometry / Number Theory / Statistical Mechanics / Algebraic Combinatorics / Formal Verification  
**Version / Date:** `v1.0.0` (2026-11-26)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 & cross-platform CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/apollonian-sandpile-markov |
| Pinned Git Submodule | `repos/apollonian-sandpile-markov` @ `0cf60c5cc6fec86dd9ab8a029abb3acf6fc6f317` |
| GitHub Release | https://github.com/0thernes/apollonian-sandpile-markov/releases/tag/v1.0.0 |
| Frozen Archived PDF | `papers/0TH-2026-018_apollonian-sandpile-markov/Donahue_2026_apollonian_sandpile_markov.pdf` |
| Frozen PDF SHA-256 | `b16780594dedd844daf8c1e28f09274a9337261b19f299f4320d30ffc8f74b4b` |
| arXiv / Source Bundle SHA-256 | `0fc6fdfae0b0bdb4e4927fd2cd893ced227c140a9665993a10eba69b1bd84164` |
| CI Verification Run | https://github.com/0thernes/apollonian-sandpile-markov/actions/runs/45849166650 |
| Software Heritage SWHID | `swh:1:snp:5dac6e269ff3c673fa6ee9b7520365de44109a16` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Unifies three quadratic-Vieta-involution frontiers across 15 machine-checked headline theorems (T1a-T3e) + master conjunction + NonVacuity + Adversarial in zero-Mathlib Lean 4.35.0 (18 audited decls, all 6 independent kernels accepted 5,012 exported decls via lake comparator --paranoid, SLSA #72728455 / Rekor 4128618149): (I) Descartes Lorentzian form, Gaussian norm (a+b)(a+c)=a^2+k^2 & BQF (T1a), self-contained zero-Mathlib Eisenstein (1844) Gauss Quadratic Reciprocity & supplementary laws (T1b), zero-GCD-exception parabolic Dehn-twist CRT proof of the HKRS (Annals of Math. 2024) global square obstruction on (-3,5,8,8), (-7,17,12,20), (-11,21,24,28) vs. unobstructed (-4,8,9,9) sharing mod-24 set {0,8,9,12,17,20} (T1c), generalized Octahedral Q(sqrt(-2)) 8-reflection mod-8 locking & Jacobi obstruction on (-6,10,17,40,24,17) vs. strip (0,0,1,2,2,1) (T1d), and exact Soddy dimension dichotomy (d-1) | 2 <=> d in {2,3} + 3D square hit 25=5^2 (T1e); (II) universal Abelian sandpile confluence & Discrete Least Action (T2a), exact Matrix-Tree dets 192 & 100,352 via integer Kronecker block-diagonalization + legal Dhar traces (T2b, with Rust/Python Bareiss det(L_{A2,2x2})=1,092, det(L_{A2,3x3})=5,393,920), Levine-Pegden-Smart Z^2 torus Green's First Identity & isotropic K=3 obstruction (T2c), our original Triangular Lattice A2 Even-Laplacian Rigidity Theorem (T2d: every periodic integer superharmonic envelope on A2 satisfies K % 2 = 0, universally obstructing maximal stable height K=5 while certifying K=4,2), and Kalinin-Shkolnikov tropical balancing (T2e; STAT-058); and (III) SL2(Z) Fricke-Cohn tr/3 correspondence (T3a), pairwise coprimality, odd-prime p = 1 (mod 4) obstruction, and our Exact Mod-32 Theorem (T3b: every even Markov number satisfies m % 32 = 2, sharp mod 64 at 2 and 34), universal Hensel sqrt(-1) mod p^k uniqueness (T3c), symbolic 3-variable 5-step Fomin-Zelevinsky Markov cluster Laurent positivity through consecutive non-monomial cancellations P1 and P2 specializing at (1,1,1) to (2,5,29,433,37666) (T3d), and complete Markov-Hurwitz n=4 classification via well-founded Vieta descent (T3e; NT-083). Paired with zero-dependency Rust (Ubuntu/Windows, Markov <= 10^7), ISO C11 ASan/UBSan + 100k fuzz, Python exact oracle + 600+ Hypothesis trials + Rust-Python differential + 8/8 (100%) killed mutants, 20/20 live Crossref/arXiv citations (0 retractions), 13-page zero-warning AMS-LaTeX PDF + clean-room arXiv tarball, live 4-mode GitHub Pages Observatory & Blueprint, Software Heritage full snapshot swh:1:snp:5dac6e269ff3c673fa6ee9b7520365de44109a16, and 90/90 Build Standard v1.2.0 compliance.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Pure Lean 4.35.0 (zero Mathlib, 11 sorry-free Palomar module files, 18 audited declarations across T1a-T3e + master conjunction + NonVacuity + Adversarial strictly within [propext, Classical.choice, Quot.sound], zero native_decide; all 6 independent kernels passed on Ubuntu 24.04 CI run 45849166650 via lake comparator --config comparator.json --paranoid inside bubblewrap: lean, leanchecker, leanchecker-paranoid/lean4lean, nanoda_bin, con-leche --verified [5,012 decls], con-ron --verified [5,012 decls]; SLSA attestation #72728455 / Rekor 4128618149)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/PalomarChallenge.lean, lean/PalomarSolution.lean, lean/ApollonianSandpileMarkov/NonVacuity.lean, lean/ApollonianSandpileMarkov/Adversarial.lean`

## Verification Boundary (Honest Epistemic Scope)

All 18 audited declarations across Pillars I-III, NonVacuity, Adversarial, and Palomar comparator contracts are kernel-checked in zero-Mathlib Lean 4.35.0 strictly within [propext, Classical.choice, Quot.sound] across all 6 independent kernels on Ubuntu CI run 45849166650 (zero sorry, zero native_decide). Finite BFS orbit statistics, A2 Bareiss determinants, 65x65 sandpile identities, and Markov uniqueness up to 10^7 are verified differentially across Rust, ISO C11, and Python. Explicitly affirms that full Apollonian local-global classification, the continuum PDE scaling limit of STAT-058, general-composite Markov Uniqueness (NT-083), all-depth cluster formalization, and Hurwitz n >= 5 asymptotics remain OPEN (0/1,900 overarching Mega-Atlas grand open problems retired). Claims no external peer review or external DOI.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/apollonian-sandpile-markov && (cd rust && cargo test --release) && PYTHONPATH=python pytest tests/test_all.py -v && PYTHONPATH=python python scripts/mutate.py && python scripts/check_readme_axioms.py && python scripts/audit_repo.py && (cd lean && lake build && lake env lean VerifyAxioms.lean && lake comparator --config comparator.json --paranoid)
```
