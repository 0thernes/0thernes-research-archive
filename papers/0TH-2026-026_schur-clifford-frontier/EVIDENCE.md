# Evidence & Falsification Dossier — `0TH-2026-026`

**Title:** Breaking and Mapping the Clifford Ceiling: Universal HGP Schur Saturation, Prime-Power Frobenius Obstructions, Two-Local Escape, and the Exact 21-Orbit AGL(4,2) Reduction  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Quantum Error Correction / Quantum Information Theory / Finite Geometry / Formal Verification  
**Version / Date:** `v1.1.0` (2026-11-27)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 & 3-OS polyglot CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/schur-clifford-frontier |
| Pinned Git Submodule | `repos/schur-clifford-frontier` @ `09ea389f20d95d2424524715d9d856517435fd26` |
| GitHub Release | https://github.com/0thernes/schur-clifford-frontier/releases/tag/v1.1.0 |
| Frozen Archived PDF | `papers/0TH-2026-026_schur-clifford-frontier/Donahue_2026_schur_clifford_frontier.pdf` |
| Frozen PDF SHA-256 | `6f43c181d0fc2d031b08cf4da7b1ff731e327bf2c4c1c8d4d96917e83a46ed33` |
| arXiv / Source Bundle SHA-256 | `7575ac179a2757b1837c1a09c06addc3107ceb243c274055b7fb5164aa5c7a3c` |
| CI Verification Run | https://github.com/0thernes/schur-clifford-frontier/actions/runs/46054378237 |
| Software Heritage SWHID | `swh:1:snp:4d16f7077d1ecbc298e024cc6304c83b72d9d422` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | 10.5281/zenodo.24618580 |

## Core Result

Unifies five interconnected frontiers in fault-tolerant transversal non-Clifford quantum gates and Clifford-hierarchy algebraic geometry across 20 machine-checked headline theorems (T1a-T5d [= 20 Palomar targets]) + 7 NonVacuity witnesses + 6 AdversarialTests boundary refutations (33 named audited declarations + exhaustive VerifyAllDecls.lean sweep of all 742 SchurClifford.* declarations in zero-Mathlib Lean 4.35.0 strictly within [propext, Classical.choice, Quot.sound], accepted by all 6 independent proof kernels via full-project lake check --paranoid and lake comparator --paranoid + dual live sorry & custom-axiom tamper rejection on exported t5d_e6_irreducibility): (I) Resolves OP1(a) of Guzman-Vega, Jimenez-Cervantes, & Sarmiento-Rosales (arXiv:2611.31953v1) by proving universal hypergraph-product (HGP) Schur saturation D * D = F^(n1*n2 + r1*r2) over any field F (T1a-T1b), concrete HGP[[13,1,3]]_5 saturation (T1c), 3 sharp hypothesis-drop obstructions (T1d), and LP/BB saturation (12/12, 15/15, 26/26); (II) Resolves OP1(b) via universal automatic strict CSS promotion of the Schur-defect subspace A_d(C_X, D) over any commutative ring R (T2a), cubic non-Clifford criterion 6*F_alpha^(3)(r) != 0 (T2b), and exact separation between logically trivial [[4,1,2]]_5 (kappa_3=2, dim Q_3=0) and non-Clifford RS[[10,1,3]]_11 (kappa_3=4, dim Q_3=1) (T2c); (III) Resolves OP2 over prime-power fields F_8 and F_9 via universal F_8 Frobenius-Schur ceiling D * D^(2) = F_8^n (T3a), Refutation #1: explicit [[12,4,2]]_8 code with classical Schur rank 12 yet Frobenius rank 11 admitting strictly CSS-preserving non-Clifford F(x)=sum x_i^7 (0/262,144 CSS violations, Delta^3 != 0, T3b), reverse F_8 separation on cyclic-7 (classical 5, Frobenius 7, T3c), and universal F_9 disjunction ceiling (D*D=F_9^n) or (D*D^(3)=F_9^n) with two-way witnesses (6,5) and (5,8) (T3d); (IV) Resolves OP3/4 via universal 2-local level-3 (Q_unif <chi,x>, T4a) and level-4 (Q_unif^2, T4b) escape, complete 56/56 individual logical-mode addressability on Q_3* = [[64,56,3]]_5 (T4a-Q3*), universal 3-copy CCZ & 1-local addressability no-go (T4c), and complete 2-local homogeneous cubic rigidity (dim Q_3^(2)=0) on HGP[[13,1,3]]_5 (T4d); and (V) Advances Wang & Zhang (arXiv:2610.06402v1) and independently certifies de Silva & Lautsch (arXiv:2609.11903v1): exact 21-orbit AGL(4,2) collapse of all 32,768 four-qubit Galois cocycles (sum = 32,768, T5a), universal quartic full-rank-14 derivative span across all 7 quartic orbits / 16,384 cocycles (T5b), universal arbitrary-n rank-2 stabilizer hyperplane bijection (T5c), and pure-kernel E_6 <= Sp(6,F_2) irreducibility (0/135 invariant Lagrangians via irreducible z^6+z^3+1, T5d). Differentially verified bit-for-bit across 6 independent exact engines (Python 3.13, naive oracle, ISO C11 -Werror + dual-ABI Win64/SysV x86-64 NASM + ASan/UBSan + 100k fuzz + exhaustive CBMC harness, ISO C++20 -Werror, safe Rust #![forbid(unsafe_code)] #![deny(clippy::all)], Zig 0.17.0 -- identical canonical SHA-256 ba16da522768c0c25e89c77dd0874a5025d85f8640dcbc7d674d05aacb6c8439), isolated 8/8 real code-mutation suite (scripts/mutate.py), quarantined numerical_approximation companions (vendored QGTL/QRNG, Moonlab 1.2.1 WASM, native LLVM JIT eshkol-run v1.3.6-evolve -r), 17/17 live Crossref/arXiv citations (min_title_jaccard=0.8333, 0 retractions), 0-overfull/0-warning AMS-LaTeX PDF + clean-room arXiv tarball, live GitHub Pages Observatory & SVG Lean Blueprint, OpenSSL X.509-verified DigiCert RFC 3161 (.tsr) + 3-calendar Bitcoin OpenTimestamps (.ots), Software Heritage full snapshot swh:1:snp:4d16f7077d1ecbc298e024cc6304c83b72d9d422, SLSA build provenance, 3-cycle forensic hardening (0 open findings), and 72/72 (100.0%, Core 30/30) Build Standard v1.2.0 compliance.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Zero-Mathlib Lean 4.35.0 (15 Lean module files under lake build --wfail with 0 warnings; 14 sorry-free and PalomarChallenge.lean holds the 20 intentional sorry stubs; 33 named audited declarations: 20 headline theorems T1a-T5d [= 20 Palomar targets] + 7 NonVacuity witnesses + 6 AdversarialTests boundary refutations, plus exhaustive Lean.collectAxioms sweep VerifyAllDecls.lean across all 742 SchurClifford.* declarations strictly within [propext, Classical.choice, Quot.sound], zero native_decide; full-project lake check --paranoid and all 20 Palomar comparator targets passed all 6 independent proof kernels inside bubblewrap on Ubuntu CI lake comparator --config comparator.json --paranoid + dual live sorry & custom-axiom tamper-rejection gates on exported t5d_e6_irreducibility)
- **Library Entry Point:** `lean/PalomarSolution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/VerifyAllDecls.lean, lean/Challenge.lean, lean/Solution.lean, lean/PalomarChallenge.lean, lean/SchurClifford/NonVacuity.lean, lean/SchurClifford/AdversarialTests.lean`

## Verification Boundary (Honest Epistemic Scope)

All 33 named audited declarations across Pillars I-V (T1a-T5d + 7 NonVacuity + 6 AdversarialTests) and all 742 SchurClifford.* declarations swept by VerifyAllDecls.lean are kernel-checked in zero-Mathlib Lean 4.35.0 strictly within [propext, Classical.choice, Quot.sound] across all 6 independent proof kernels via full-project lake check --paranoid and lake comparator --paranoid inside bubblewrap plus dual live sorry & custom-axiom tamper-rejection gates on Ubuntu CI (zero warnings under --wfail, zero sorry outside PalomarChallenge.lean, zero native_decide). The 6 independent exact algebraic engines (Python, naive oracle, C11+x86-64 NASM, C++20, safe Rust, Zig) cross-check identical canonical certificates (SHA-256 ba16da522768c0c25e89c77dd0874a5025d85f8640dcbc7d674d05aacb6c8439) outside the Lean kernel alongside an isolated 8/8 code-mutation harness; vendored QGTL/QRNG, Moonlab 1.2.1 WASM, and native Eshkol/R7RS AD scripts are strictly quarantined as numerical_approximation classical cross-checks (no quantum hardware or physical entropy source claimed). Analytic Hilbert-space bridges are proved in paper/main.tex and audited line-by-line in docs/statement-fidelity.md. Wang & Zhang Conjecture 2 (arXiv:2610.06402v1) for n=4, k>=5 remains explicitly OPEN, and 0/2,000 overarching Mega-Atlas grand open problems are retired. Claims no external peer review or external DOI.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/schur-clifford-frontier && (cd lean && lake build --wfail && lake build PalomarChallenge && lake env lean VerifyAxioms.lean && lake env lean VerifyAllDecls.lean && lake env leanchecker --fresh PalomarSolution && lake check --paranoid && lake comparator --config comparator.json --paranoid) && (cd native/c && make test) && (cd native/rust && cargo clippy --all-targets -- -D warnings && cargo test --release) && (cd native/zig && zig test schur_verifier.zig) && python3 scripts/check_readme_axioms.py && python3 scripts/mutate.py && python3 scripts/stamp_timestamps.py --verify --negative-test && pytest -v
```
