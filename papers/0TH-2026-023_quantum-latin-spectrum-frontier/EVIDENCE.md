# Evidence & Falsification Dossier — `0TH-2026-023`

**Title:** Exact Closure of the Quantum Latin Square Cardinality Spectrum for All Orders v >= 8 and Resolution of Maximal Idempotent Symmetric Quantum Latin Squares Across All Congruence Classes Modulo 4  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Quantum Information Theory / Combinatorial Design Theory / Formal Verification  
**Version / Date:** `v2.0.0` (2026-11-27)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0, CBMC, 101/101 zero-float symbolic & 3-OS CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/quantum-latin-spectrum-frontier |
| Pinned Git Submodule | `repos/quantum-latin-spectrum-frontier` @ `728c1536f96c1f4a8404b71abd89a6778602f297` |
| GitHub Release | https://github.com/0thernes/quantum-latin-spectrum-frontier/releases/tag/v2.0.0 |
| Frozen Archived PDF | `papers/0TH-2026-023_quantum-latin-spectrum-frontier/Donahue_2026_Quantum_Latin_Spectrum_Frontier.pdf` |
| Frozen PDF SHA-256 | `0f4c97d955b4a7ab09a4915ea1448e632a0a7c1336549e3c6c4f4fb0d00af02c` |
| arXiv / Source Bundle SHA-256 | `0a7b1732caa517eeb64b63228b58c21df78f2611e6fbb5b6b13fc978f0791361` |
| CI Verification Run | https://github.com/0thernes/quantum-latin-spectrum-frontier/actions/runs/46057897837 |
| Software Heritage SWHID | `swh:1:snp:a13ad420f794605f15f7eb1f1c81cb82a38ca0c2` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Resolves two interlocked open-problem families from the July-September 2026 quantum Latin square literature, backed by zero-Mathlib Lean 4.35.0 proofs (28 Palomar targets, 8 NonVacuity witnesses incl. RatQ : ExactField, 7 AdversarialTests refutations = 43 audited declarations strictly within [propext, Classical.choice, Quot.sound], verified across all 6 independent proof kernels on Ubuntu CI runs 46057897837 & 46059370281 + live tamper-injecting negative comparator gate, SLSA #73254433 / Rekor 4150978936) and 10 additional polyglot engines: (I) Complete zero-float exact closure of the QLS(v) cardinality spectrum for all orders v >= 8 (87/87 open cases from Zhang-Lv-Cao arXiv:2607.19969 closed exactly + 14/19 exact at v=7 = 101/101 zero-float recipes verified over Q(i,sqrt(2),sqrt(3),sqrt(5)) + exact SymPy Das-Kumar POA(6,28) arXiv:2608.12607: 1/1 at v=23 via deterministic cyclic-Venn Bjorck C_23 giving QLS(23,528) and exact p^2-1 for p in {11,19,23,31,43,47} backed by literal alpha^k != 1 in any ExactScalarRing + Paley autocorrelation + Hadamard Schur-product IsQLS; 13/13 at v=9 and 73/73 at v=11 via Dual-Punctured Odd-Order Decomposition with subspace ray disjointness, Lean-verified Golden-Ratio POA(5,20) over (1/4)Z[sqrt(5)] and Sparse QLS(5,25) over (1/(2*sqrt(6)))Z[sqrt(6),sqrt(10)], and exact rational rotation W_R=(5/13,12/13) closing c=108; plus Bjorck C_7 QLS(7,41) and Petrescu BH(7,6) QLS(7,45)); (II) Resolution of MCISQLS(n) across all three open congruence classes n == 0, 1, 3 (mod 4) from Zhang-Cao arXiv:2609.24653: exact impossibility of ISQLS(4) over any positive-definite field, Group-Translation Covariant reduction, unrestricted Quantum Direct Product proving literal IsMCISQLS(nm) over any ExactField (all n, m >= 1, removing odd-n parity restriction), CP^(n-1) equal-norm real-ray bridge, two infinite 1-parameter rational curves MCISQLS(7)(t) and MCISQLS(11)(t), and ALL SEVEN exact closed-form witnesses spanning n in {7, 8, 9, 11, 16, 17, 19} now kernel-checked in Lean 4.35.0 (incl. MCISQLS(16) 136/136 rays over ZBiQuad2_113). Differentially verified across 11 engines (Lean 4.35.0, dual Win64/ELF64 x86-64 NASM 128-bit dot kernel, ISO C11 -Werror + ASan/UBSan + 100k fuzz + 72/72 mutants + CBMC bounded model checking, C++20 -Werror, safe Rust #![forbid(unsafe_code)] 3-OS, Zig, Eshkol 1681-pt tangent check, dynamic Python stdlib Fraction oracle + 10/10 surgical mutation kill + zero-float symbolic verifier, plus explicitly labelled classical CPU simulations via Moonlab 3-qubit WASM 64-op UEB, QGTL Fubini-Study metric g_tt err 1.29e-8, and C11/JS-BigInt QRNG mixers), 0 open Dependabot alerts (pytest 9.2.0), 13/13 live arXiv+Crossref title/author-verified citations (0 retractions), 0-warning AMS-LaTeX PDF + clean-room arXiv tarball, WCAG 2.2 AA strict-CSP interactive SVG Proof DAG site, DigiCert RFC 3161 (.tsr) + 3-calendar Bitcoin (.ots), SWH swh:1:snp:a13ad420f794605f15f7eb1f1c81cb82a38ca0c2, zero-padding 3x1,000 hardening (1,000/1,000 PASS, unique_titles=1000), and 72/72 (100.0%, Core 30/30) Build Standard v1.2.0 compliance.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Pure Lean 4.35.0 (zero Mathlib, 15 Lean module files [14 sorry-free; PalomarChallenge.lean is the intentional statement-only sorry stub] + formalization.yaml, 43 audited declarations: 28 Palomar targets [incl. 6 statement-fidelity bridges & MCISQLS(16) over ZBiQuad2_113] + 8 NonVacuity witnesses [incl. quotient division field RatQ : ExactField] + 7 AdversarialTests boundary/tamper refutations strictly within [propext, Classical.choice, Quot.sound], autoImplicit = false, zero native_decide; all 28 targets passed all 6 independent kernels on Ubuntu CI runs 46057897837 & 46059370281 via bubblewrap-sandboxed lake check --paranoid & lake comparator --config comparator.json --paranoid + live tamper-injecting negative comparator gate: lean, leanchecker-paranoid, lean4lean, nanoda, con-leche --verified, con-ron --verified; SLSA #73254433 / Rekor 4150978936)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/PalomarChallenge.lean, lean/PalomarSolution.lean, lean/QlsFrontier/NonVacuity.lean, lean/QlsFrontier/AdversarialTests.lean`

## Verification Boundary (Honest Epistemic Scope)

All 43 audited declarations (28 Palomar targets, 8 NonVacuity witnesses incl. RatQ : ExactField, 7 AdversarialTests refutations) are kernel-checked in zero-Mathlib Lean 4.35.0 strictly within [propext, Classical.choice, Quot.sound] across all 6 independent kernels plus a live tamper-injecting negative gate on Ubuntu CI runs 46057897837 & 46059370281 (zero sorry outside PalomarChallenge.lean, zero native_decide), covering ALL SEVEN MCISQLS(7,8,9,11,16,17,19) witnesses and all 6 general statement-fidelity theorems. The 101 individual spectrum recipes for QLS(9) (13/13), QLS(11) (73/73), QLS(23) (1/1), and QLS(7) (14/19) are verified with ZERO floating-point arithmetic ([EXACT-COMP]) over Q(i,sqrt(2),sqrt(3),sqrt(5)) + exact SymPy POA(6,28) in python/verify_spectrum_exact_symbolic.py. Moonlab 3-qubit WASM, QGTL differential geometry, QRNG integer mixers, and Eshkol stages are strictly classical deterministic CPU computations outside the Lean proof trust base (no quantum hardware claimed). Five QLS(7) values {37,38,39,40,42} (1e-15 residual, 5 tangent syzygies) and 2-unitary OQLS pairs (25/81,18/81) and (16/64,8/64) are strictly [NUMERICAL]; exact algebraic closure of QLS(7) {37..40,42}, sporadic MCISQLS(5,12,13,15,20,32), MCIQLS(6), and MCOQLS(d<64) remain explicitly OPEN. Claims no external peer review or external DOI.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/quantum-latin-spectrum-frontier && (cd lean && lake build && lake build PalomarChallenge && lake env lean VerifyAxioms.lean && lake check --paranoid && lake comparator --config comparator.json --paranoid) && (cd rust && cargo clippy --all-targets -- -D warnings && cargo test --release && cargo run --release) && (cd zig && zig test verify_qls.zig && zig run verify_qls.zig) && (cd asm && make test) && (cd c && make test && make cbmc) && (cd cpp && make test) && (cd stack && node qls_moonlab.cjs) && python python/verify_spectrum_exact_symbolic.py && python scripts/mutation_check.py && python tests/test_all.py && python scripts/check_readme_axioms.py
```
