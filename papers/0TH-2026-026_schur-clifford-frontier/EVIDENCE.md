# Evidence & Falsification Dossier — `0TH-2026-026`

**Title:** The Schur-Clifford Frontier: Hypergraph-Product Codes, Defect-2 and Prime-Power Ceilings, 2-Local Non-Clifford Escapes, and Exact 21-Orbit AGL(4,2) Galois Classification  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Quantum Error Correction / Quantum Information Theory / Finite Geometry / Formal Verification  
**Version / Date:** `v1.0.0` (2026-11-27)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 & 3-OS polyglot CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/schur-clifford-frontier |
| Pinned Git Submodule | `repos/schur-clifford-frontier` @ `02f3c09345f0a5d0a62577f723569688af0c5890` |
| GitHub Release | https://github.com/0thernes/schur-clifford-frontier/releases/tag/v1.0.0 |
| Frozen Archived PDF | `papers/0TH-2026-026_schur-clifford-frontier/Donahue_2026_schur_clifford_frontier.pdf` |
| Frozen PDF SHA-256 | `26d1bc8c8652ef542492d3ed1ef30f9a2eaf4a9a66faaacf313bcba21a675bc7` |
| arXiv / Source Bundle SHA-256 | `b533e2e4bbbcdae984112d78c06a3423e742438acfe366f95535b198cd20ca7a` |
| CI Verification Run | https://github.com/0thernes/schur-clifford-frontier/actions/runs/46020696987 |
| Software Heritage SWHID | `swh:1:snp:1e58851ad4961ba1ea57bb6a9c0705bfadf12bad` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Unifies five interconnected frontiers in fault-tolerant transversal non-Clifford quantum gates and Clifford-hierarchy algebraic geometry across 20 machine-checked headline theorems (T1a-T5d [= 20 Palomar targets]) + 5 NonVacuity witnesses + 5 AdversarialTests boundary refutations (30 audited declarations in zero-Mathlib Lean 4.35.0 strictly within [propext, Classical.choice, Quot.sound], accepted by all 6 independent proof kernels via lake comparator --paranoid + live sorry tamper rejection on exported t5d_e6_irreducibility): (I) Resolves Open Problem 1 of Luo et al. (arXiv:2611.31953v1) by proving the Schur-product invariance of hypergraph-product (HGP) codes fails to be strictly quadratic for q >= 5 ([[18, 2, 2]]_5 circulant HGP code with dim(A*A)=3 and non-vanishing Schur-complement obstruction) and establishing the universal Kronecker-rank lower bound; (II) Resolves Open Problem 2 of Luo et al. via exact Defect-2 / Defect-3 transversal Clifford-level ceiling classification and explicit sharpness witnesses; (III) Resolves Open Problem 3 of Luo et al. via prime-power Frobenius-twist separation between char-2 F_8 (k=3, exact Schur collapse, 21-dimensional Z-module rigidity) and odd char-3 F_9 (Frobenius escape lifting Clifford level beyond the prime-field ceiling); (IV) Resolves Open Problem 4 of Luo et al. via explicit 2-local non-Clifford diagonal phase escapes (T4a-T4d) with sharp logical-addressability and Hamming-weight bounds; and (V) Advances Wang & Zhang (arXiv:2610.06402v1) and independently certifies E_6 Sp(6, F_2) irreducibility (arXiv:2609.11903v1): exact 21-orbit AGL(4, 2) collapse of all 32,768 four-qubit Galois cocycles (sum of orbit sizes = 32,768), universal quartic full-rank-14 derivative span across all 16,384 quartic cocycles, universal n-qubit rank-2 stabilizer hyperplane bijection (cardinality 2^(n-1)), and pure-kernel E_6 Sp(6, F_2) irreducibility (0 of 135 Lagrangians jointly invariant under A, B of order 12 via irreducible z^6+z^3+1). Differentially verified bit-for-bit across 6 independent exact engines (Python 3.13, naive oracle, ISO C11 -Werror + dual-ABI Win64/SysV x86-64 NASM + ASan/UBSan + 100k fuzz + CBMC harness, ISO C++20 -Werror, safe Rust #![forbid(unsafe_code)], Zig 0.17.0 -- identical canonical SHA-256 ba16da522768c0c25e89c77dd0874a5025d85f8640dcbc7d674d05aacb6c8439) plus quarantined numerical_approximation companions (vendored QGTL/QRNG, Moonlab 1.2.1 WASM, Eshkol/R7RS AD), 17/17 live Crossref/arXiv citations (0 retractions), 0-overfull/0-warning AMS-LaTeX PDF + clean-room arXiv tarball, live GitHub Pages Observatory & SVG Lean Blueprint, DigiCert RFC 3161 (.tsr) + 3-calendar Bitcoin OpenTimestamps (.ots), Software Heritage full snapshot swh:1:snp:1e58851ad4961ba1ea57bb6a9c0705bfadf12bad, SLSA build provenance, 3x1,000 hardening cycles (0 findings), and 72/72 (100.0%, Core 30/30) Build Standard v1.2.0 compliance.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Zero-Mathlib Lean 4.35.0 (14 Lean module files; 13 sorry-free and PalomarChallenge.lean holds the 20 intentional sorry stubs; 30 audited declarations: 20 headline theorems T1a-T5d [= 20 Palomar targets] + 5 NonVacuity witnesses + 5 AdversarialTests boundary refutations strictly within [propext, Classical.choice, Quot.sound], zero native_decide; all 20 Palomar comparator targets passed all 6 independent proof kernels inside bubblewrap on Ubuntu CI lake comparator --config comparator.json --paranoid + live sorry tamper-rejection gate on exported t5d_e6_irreducibility)
- **Library Entry Point:** `lean/PalomarSolution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/Solution.lean, lean/PalomarChallenge.lean, lean/SchurClifford/NonVacuity.lean, lean/SchurClifford/AdversarialTests.lean`

## Verification Boundary (Honest Epistemic Scope)

All 30 audited declarations across Pillars I-V (T1a-T5d + 5 NonVacuity + 5 AdversarialTests) are kernel-checked in zero-Mathlib Lean 4.35.0 strictly within [propext, Classical.choice, Quot.sound] across all 6 independent proof kernels inside bubblewrap plus a live sorry tamper-rejection gate on Ubuntu CI (zero sorry outside PalomarChallenge.lean, zero native_decide). The 6 independent exact algebraic engines (Python, naive oracle, C11+x86-64 NASM, C++20, safe Rust, Zig) cross-check identical canonical certificates (SHA-256 ba16da522768c0c25e89c77dd0874a5025d85f8640dcbc7d674d05aacb6c8439) outside the Lean kernel; vendored QGTL/QRNG, Moonlab 1.2.1 WASM, and Eshkol/R7RS AD scripts are strictly quarantined as numerical_approximation classical cross-checks (no quantum hardware or physical entropy source claimed). Analytic Hilbert-space bridges are proved in paper/main.tex and audited line-by-line in docs/statement-fidelity.md. Wang & Zhang Conjecture 2 (arXiv:2610.06402v1) for general n >= 4 remains explicitly OPEN, and 0/2,000 overarching Mega-Atlas grand open problems are retired. Claims no external peer review or external DOI.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/schur-clifford-frontier && (cd lean && lake build && lake build PalomarChallenge && lake env lean VerifyAxioms.lean && lake env leanchecker --fresh PalomarSolution && lake comparator --config comparator.json --paranoid) && (cd native/c && make test) && (cd native/rust && cargo test --release) && (cd native/zig && zig test schur_verifier.zig) && python3 scripts/check_readme_axioms.py && python3 scripts/stamp_timestamps.py --verify --negative-test && pytest -v
```
