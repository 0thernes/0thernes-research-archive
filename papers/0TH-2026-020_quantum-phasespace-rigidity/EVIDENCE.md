# Evidence & Falsification Dossier — `0TH-2026-020`

**Title:** Discrete Symplectic Phase-Space Rigidity: Complete Cyclic Stabilizer AME Dichotomy, Maximal-Cardinality Resolvable Quantum Latin Squares, and Stabilizer-Polytope Magic Geometry  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Quantum Information Theory / Combinatorial Design Theory / Formal Verification  
**Version / Date:** `v2.0.0` (2026-11-27)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 & 3-OS polyglot CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/quantum-phasespace-rigidity |
| Pinned Git Submodule | `repos/quantum-phasespace-rigidity` @ `a99f327698a46ecc249f5cc1a98a387969d80d24` |
| GitHub Release | https://github.com/0thernes/quantum-phasespace-rigidity/releases/tag/v2.0.0 |
| Frozen Archived PDF | `papers/0TH-2026-020_quantum-phasespace-rigidity/Donahue_2026_quantum_phasespace_rigidity.pdf` |
| Frozen PDF SHA-256 | `8e8c9be2f0e147126c061c4f01c48e9d429b3ce40f0ed0ef93276cf0c9e06681` |
| arXiv / Source Bundle SHA-256 | `15e676c70e9534a3028f1a5af60399a9c5597e6b3bba98e03a0358c066855f06` |
| CI Verification Run | https://github.com/0thernes/quantum-phasespace-rigidity/actions/runs/46056858766 |
| Software Heritage SWHID | `swh:1:snp:91466bc3ff5dad44fef051db37afc2dcb91aa57b` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | 10.5281/zenodo.24618588 |

## Core Result

Unifies three 2025-2026 frontiers in discrete symplectic quantum phase-space geometry across 13 machine-checked headline theorems (T1a-T3d) + master conjunction + 3 NonVacuity witnesses + 6 AdversarialTests boundary refutations (23 explicit + 311 exhaustively axiom-audited declarations via SweepAllAxioms.lean in zero-Mathlib Lean 4.35.0 with warningAsError = true, all 14 Palomar targets verified across all 6 independent kernels on Ubuntu CI run 46056858766): (I) Classification of cyclic Weyl-Heisenberg Z_{2l}-stabilizer AME(N, 2l) states across all N >= 2 and all even d = 2l >= 2 (torsion Singleton p-rank forcing, radical divisor descent, universal unimodular lifts K_2/K_3/C_5/Prism_6/20-case W_5 for all d >= 2, Pless obstructions, Rains shadows at N in {4,7,9,11}, and exported additive F_4-MDS non-existence A_6=-21 at N=7 and odd N>=9): exists iff N in {2,3,5,6}, extending Wojcik et al. (arXiv:2603.18193v3) with an explicit Ring-vs-Field separation at (4,4) (Z_4 impossible vs F_4 realizable); (II) Maximal-cardinality t-resolvable quantum Latin squares extending Zhang & Cao (arXiv:2608.29201v2) beyond t <= 2 via two-frequency Fourier lifts of Megyesi-Redei permutations: explicit ((p-5)/2)-RQLS(p) for all odd primes p >= 7 (3-RQLS(11), 4-RQLS(13), 6-RQLS(17)), prime-power constructions 2-RQLS(9) and char-2 3-RQLS(16) (198,820 zero-float Z[zeta_p] state pairs, 0 off-diagonal collinear in C++20), both untwisted Q_1 x Q_2 (3-RQLS(143)) and twist-separated Q_1 x_D C_2 (3-RQLS(55)) direct-product lifting, and exhaustive F_8 orthomorphism linearity (0/4,872 nonlinear perms in Lean & Zig); and (III) Basis-independent stabilizer/magic polytope geometry addressing Zurel & Davis (arXiv:2602.22336v2 Sec. V.3) via Gurvits-Barnum Cor. 3 collapse ASTAB_{2,d} subset AWP_{2,d} subseteq ASEP_{2,d} (odd prime d >= 3, all-bipartition biseparability for all n >= 2), 2-qubit rational incomparability witnesses rho_ent=(11,3,3,3)/20 & rho_sep=(8,7,4,1)/20, universal global polytope circumradii R^2(ASTAB_{2,2})=3(13+4*sqrt(3))/484 > 1/12 in Z[sqrt(3)] and R^2(ASTAB_{1,3})=(7-3*sqrt(5))/6 in Z[sqrt(5)], finite uniform-cover Symplectic Marginal Descent strengthening Liu et al. (arXiv:2512.16777v2 Thm 10) to C_n <= (7*4^n+8)/(15*2^n) (exact 15/7x squared-inball gain for all n >= 2), and first-principles multivariate polynomial Clifford-Reynolds Degree-2 RLT+SOS Barrier (M >= 4^n - 1). Verified across unified 7-engine CI (REQUIRE_ALL_ENGINES=1: Lean 4, Rust 1.94 #![forbid(unsafe_code)] 3-OS [1,770 Lambda_2 facet pairs, 240 CNC vertices, 336 n=3 subspaces], Zig comptime, C++20 Z[zeta_p], ISO C11 + x86-64 NASM + vendored MIT Moonlab/QGTL/QRNG + ASan/UBSan + 100k fuzz, Eshkol Dual-AD err <= 2.78e-17 with explicit numerical_approximation tags, Python 3.12 exact oracle + Hypothesis + Draft 2020-12 schema + 12/12 100% mutation kill + gitleaks/osv-scanner), 25/25 live arXiv/Crossref citations (0 retractions), 0-overfull/0-warning 16-page AMS-LaTeX PDF + clean-room arXiv tarball, live GitHub Pages Observatory & Blueprint, DigiCert RFC 3161 (.tsr) + 3-calendar Bitcoin OpenTimestamps (.ots), Software Heritage v1.0.0 snapshot swh:1:snp:91466bc3ff5dad44fef051db37afc2dcb91aa57b, zero-padding 1,000/1,000 hardening audit, and 100.0% (69/69, Core 29/29) Build Standard v1.2.0 compliance.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Pure Lean 4.35.0 (zero Mathlib, warningAsError = true, 12 Lean module files; 11 sorry-free and PalomarChallenge.lean holds the 14 intentional sorry stubs; 23 explicit audited declarations across T1a-T3d + master conjunction + 3 NonVacuity witnesses + 6 AdversarialTests boundary refutations PLUS 311 exhaustively audited project declarations via SweepAllAxioms.lean using Lean.collectAxioms strictly within [propext, Classical.choice, Quot.sound], zero native_decide; all 14 Palomar comparator targets passed all 6 independent proof kernels on Ubuntu CI run 46056858766 via bubblewrap lake check --paranoid & lake comparator --config comparator.json --paranoid + live negative custom-axiom rejection)
- **Library Entry Point:** `lean/PalomarSolution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/SweepAllAxioms.lean, lean/Challenge.lean, lean/Solution.lean, lean/PalomarChallenge.lean, lean/QPRigidity/NonVacuity.lean, lean/QPRigidity/AdversarialTests.lean`

## Verification Boundary (Honest Epistemic Scope)

All 23 explicit audited declarations across Pillars I-III (T1a-T3d + master conjunction + 3 NonVacuity witnesses + 6 AdversarialTests refutations) plus all 311 project declarations (SweepAllAxioms.lean) are kernel-checked in zero-Mathlib Lean 4.35.0 (warningAsError = true) strictly within [propext, Classical.choice, Quot.sound] across all 6 independent proof kernels on Ubuntu CI run 46056858766 (zero sorry outside PalomarChallenge.lean, zero native_decide). Character-sum orthogonality over C^q (198,820 pairs in Z[zeta_p]), all 1,770 Lambda_2 facet pairs (min overlap -1), all 240 CNC m=1 vertices (33/60 facets, C_2=2), all 336 4D symplectic subspaces of F_2^6 (uniform cover r=80), QGTL Fubini-Study metric & Berry curvature (explicitly tagged numerical_approximation), and NIST SP 800-90B QRNG auditing are verified across Rust, Zig, C++20, C11+NASM+Moonlab, Eshkol AD, and Python exact arithmetic; analytic Hilbert-space bridges and the generic diagonal phase twist D_phi for Q_1 x_D C_2 are proved in paper/main.tex and audited line-by-line in docs/statement-fidelity.md. Software Heritage full snapshot swh:1:snp:91466bc3ff5dad44fef051db37afc2dcb91aa57b covers v1.0.0 (automated Save Code Now for v2.0.0 was gated by Software Heritage's Anubis PoW bot challenge). Explicitly affirms 0/2,000 (and 0/1,900 in upstream v1 audit) overarching Mega-Atlas grand open problems retired; non-stabilizer even-d AME(N,d), Zhang-Cao's 17 sporadic 1-RQLS orders (starting at v=10), Zurel-Davis Conjectures 1-2 for n >= 3, and odd-prime multipartite bound-entangled AWP remain OPEN. Claims no external peer review or external DOI.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/quantum-phasespace-rigidity && (cd rust && cargo clippy --all-targets -- -D warnings && cargo test --release && cargo run --release -- --verify-all) && (cd zig && zig test src/main.zig) && (cd cpp && make test) && (cd c && make test) && python3 eshkol/run_eshkol_ad.py --verify-all && REQUIRE_ALL_ENGINES=1 PYTHONPATH=src:. pytest -v tests/test_all.py && python3 scripts/mutate.py && python3 scripts/check_readme_axioms.py && python3 scripts/hardening_audit.py && (cd lean && lake build && lake build PalomarChallenge && lake env lean VerifyAxioms.lean && lake env lean SweepAllAxioms.lean && lake comparator --config comparator.json --paranoid)
```
