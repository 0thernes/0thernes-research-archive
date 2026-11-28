# Evidence & Falsification Dossier — `0TH-2026-022`

**Title:** The 2-Adic Magic Obstruction, Quaternary Bent-Hyperplane Rupture, Super-MUB Torsion Anomalies, and Divided-Power Characteristic-3 Alltop Constructions Across Product Weyl-Heisenberg Groups  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Quantum Information Theory / Finite Geometry / Combinatorics / Formal Verification  
**Version / Date:** `v1.1.1` (2026-11-27)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 & 3-OS CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/weyl-magic-obstruction-frontier |
| Pinned Git Submodule | `repos/weyl-magic-obstruction-frontier` @ `fbfd12365dfa963421a69f530cf0c97bc866663b` |
| GitHub Release | https://github.com/0thernes/weyl-magic-obstruction-frontier/releases/tag/v1.1.1 |
| Frozen Archived PDF | `papers/0TH-2026-022_weyl-magic-obstruction-frontier/Donahue_2026_weyl_magic_obstruction_frontier.pdf` |
| Frozen PDF SHA-256 | `56fb8f0f781a46277444f4a6e1683aeac54cf1178ba60fee5ea12ca2b43fa17c` |
| arXiv / Source Bundle SHA-256 | `a380307efd79058bc852cf54c14043e7eb07607ed4a3885dce8b31d3751d6b1b` |
| CI Verification Run | https://github.com/0thernes/weyl-magic-obstruction-frontier/actions/runs/46056568188 |
| Software Heritage SWHID | `swh:1:snp:8c1d97bd8c7f23b45d70d4a5750690b9f74e7b97` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | 10.5281/zenodo.24618584 |

## Core Result

Machine-checks 22 numbered theorem groups (T1a-T5d) + arbitrary-bent n=4 kernel bridge n4_z4_bent_hyperplane_rupture_arbitrary_bent + master conjunction prove_all_weyl_magic_theorems (23 Palomar comparator targets, 3 strictly zero-axiom) plus 6 NonVacuity witnesses (including nontrivial n=2 nonvacuity_pillar1_n2_mub_spectrum) and 8 AdversarialTests sharpness refutations (38 audited declarations, zero Mathlib, zero native_decide, all 6 independent Lean 4.35.0 proof kernels verified inside bubblewrap on Ubuntu CI 12/12 green) across five linked pillars governing extremal Stabilizer Renyi Entropy across product Weyl-Heisenberg groups: (I) Universal 2-Adic Odd-Qubit Obstruction (T1a-T1d): for all odd n >= 3, v_2(2^n(2^n-2)^2) = n+2 is odd, unconditionally ruling out any n-qubit pure state with WH-MUB Pauli spectrum |c_P|^2 in {0, 2^{-n}} (zero subgroup or equimodularity assumptions), sharp at n=1 and n=2 ((1,1,1,i)/2, Phi_4 = 7/4); (II) Quaternary Bent-Hyperplane Rupture at n=4 (T2a-T2e + arbitrary-bent kernel bridge): universal symplectic rigidity H^perp subseteq H, Fermat Gaussian-square phase locking R^2+I^2 = 4^m -> u_x in Z_4, universal Rothaus (1976) degree bound deg_ANF(f) <= m for all m >= 2, exhaustive F_2^4 classification (all 896 bent functions are quadratic, 0 of degree > 2), and universal 3-hyperplane zero-sum parity obstruction ruling out equimodular n=4 WH-MUB states directly inside the Lean kernel for arbitrary IsBent 2 f; (III) Super-MUB Torsion Anomalies & alpha-Dependence (T3a-T3e): exact Z[zeta_8] WH-MUB fiducials in W(4)xW(2) (norm2=8) and W(4)xW(4) (norm2=320) alongside exact Z[i] Super-MUB witnesses v42 (norm2=1001) and v44 (norm2=1596) strictly beating WH-MUB at alpha=2 and alpha=3 while crossing above WH-MUB at alpha=4, paired with C++20 L-BFGS numerical evidence that direct alpha=4 re-optimization still beats WH-MUB; (IV) Two-Stabilizer Tower, n=5 SOS Rupture & AME Ceilings (T4a-T4d): universal 3-stratum Parseval unifying n=1,2,3 (4/3, 7/4, 16/9), exact n=4 cubic 453t^3-651t^2+311t-49=0 (t* = 0.37745680..., Phi_4* = 2.15052015..., M_2* = 2.00687898...), exact n=5 SOS floor Phi_4(Psi_5) >= 3 ruptured by exact Z[i]^32 witness (Phi_4 = 693568064/260144641 ~= 2.666086 < 3), and universal k-uniform/AME Cauchy-Schwarz ceilings (AME(2,2) >= 2, AME(5,2) >= 1879/918, AME(6,2) >= 13/6); and (V) Divided-Power Char-3 Alltop, Char-5 & Exact QGT (T5a-T5d): elementary Z_9 carry-quadratic formulation (explicitly crediting Damski et al. arXiv:2603.15550 for GR(9,n) existence), universal bilinear Gauss-sum flat-modulus theorem, exact radix-3 FFT Z[zeta_9] certificates for W(3)^tensor-{1,2,3} (extended to n=4, D=81 in Rust/C11), Z[zeta_5] certificates for W(5)^tensor-{1,2}, and exact Fubini-Study QGT metric g_{theta,theta} = (1-D^{-1})/(2+2D^{-1/2}cos theta)^2. Differentially cross-verified across 8 executed polyglot engines (Lean 4.35.0, safe Rust 3-OS, Zig comptime, strict ISO C11 + dual Win64/ELF64 x86-64 NASM 1.56x FWHT + ASan/UBSan + 100k fuzz + CBMC harness, C++20 L-BFGS, Python exact Fraction/Decimal + textbook O(D^3) oracle with 16/16 3-OS pytest [3 Hypothesis suites + Draft 2020-12 repo.yaml schema] & 9/9 real isolated source-code mutation kills & 0 ruff/mypy --strict, plus explicitly labelled classical cross-checks via QGTL and Moonlab WASM + tsotchke/quantum_rng splitmix64/hadamard_mix) and 1 source-level Eshkol AD companion spec (not compiled/executed in CI), 17/17 live title/author/retraction-verified Crossref/arXiv citations (0 retractions; Leone2022SRE fixed to arXiv:2106.12587), line-by-line statement-fidelity audit (docs/statement-fidelity.md), 18-finding 3-cycle hostile red-team audit, 14-page 0-warning AMS-LaTeX PDF + clean-room arXiv tarball, live zero-CDN WebGL2+2D-fallback Observatory & 38-declaration WCAG 2.2 AA Blueprint, DigiCert RFC 3161 (.tsr) + Bitcoin (.ots), SWH swh:1:snp:8c1d97bd8c7f23b45d70d4a5750690b9f74e7b97, and 75/75 (100.0%, Core 31/31; B44 honestly partial) Build Standard v1.2.0 compliance.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Pure Lean 4.35.0 (zero Mathlib, 14 Lean module files [13 sorry-free; PalomarChallenge.lean is the intentional statement-only sorry stub], 38 audited declarations across 22 numbered theorem groups T1a-T5d + n4_z4_bent_hyperplane_rupture_arbitrary_bent [arbitrary-bent n=4 kernel bridge] + prove_all_weyl_magic_theorems [= 23 Palomar targets + arbitrary-bent bridge, 3 zero-axiom] + 6 NonVacuity witnesses [incl. nontrivial n=2 Pauli-MUB witness nonvacuity_pillar1_n2_mub_spectrum] + 8 AdversarialTests boundary refutations strictly within [propext, Classical.choice, Quot.sound], autoImplicit = false, zero native_decide; all 6 independent kernels passed on Ubuntu CI via bubblewrap-sandboxed lake check --paranoid & lake comparator --config comparator.json --paranoid [3,664-3,667 decls] + live tamper-injecting negative comparator gate: lean, leanchecker-paranoid, lean4lean, nanoda, con-leche --verified, con-ron --verified; Sigstore Rekor 4150923477 / 4150923691)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/PalomarChallenge.lean, lean/PalomarSolution.lean, lean/WeylMagic/NonVacuity.lean, lean/WeylMagic/AdversarialTests.lean`

## Verification Boundary (Honest Epistemic Scope)

All 38 audited declarations across Pillars I-V (23 Palomar targets T1a-T5d + prove_all_weyl_magic_theorems + n4_z4_bent_hyperplane_rupture_arbitrary_bent, 6 NonVacuity witnesses incl. nontrivial n=2 Pauli-MUB spectrum, 8 AdversarialTests refutations) are kernel-checked in zero-Mathlib Lean 4.35.0 strictly within [propext, Classical.choice, Quot.sound] across all 6 independent kernels plus a live tamper-injecting negative gate on Ubuntu CI 12/12 green (zero sorry outside PalomarChallenge.lean, zero native_decide). docs/statement-fidelity.md maps all 38 Lean declarations line-by-line to manuscript claims and explicit bridges. W(3)^tensor-4 (D=81) is verified in exact Z[zeta_9] in Rust and C11 ([EXACT-COMP], outside Lean). C++20 multi-start L-BFGS landscapes (including direct alpha=4 re-optimization), QGTL Richardson QGT cross-checks (max_rel_err 1.224e-8), Moonlab WASM CPU simulation (max_err 1.33e-14), and the vendored tsotchke/quantum_rng splitmix64/hadamard_mix PRNG are strictly classical deterministic [NUMERICAL-APPROX] cross-checks (no quantum hardware or physical entropy source); eshkol/magic_qgt_ad.esk is a source-level companion AD specification (not compiled/executed in CI). Build Standard B44 is honestly marked partial (author self-replication + clean-room 3-OS CI pass; independent third-party human replication open). Explicitly affirms 0/2,000 overarching Mega-Atlas grand open problems retired; non-equimodular global optimality of |Psi_4(theta*)> over C^16, strong form for even n >= 6 qubits, and non-cyclic WH-SIC exclusion in W(4)xW(2) and W(4)xW(4) remain OPEN. Claims no external peer review or external DOI.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/weyl-magic-obstruction-frontier && (cd rust && cargo clippy --all-targets -- -D warnings && cargo test --release) && (cd zig && zig test src/main.zig && zig run -OReleaseFast src/main.zig) && node node/moonlab_crosscheck.cjs && PYTHONPATH=src:. pytest -v tests/test_all.py && PYTHONPATH=src:. python scripts/mutation_check.py && python scripts/check_readme_axioms.py && (cd lean && lake build && lake build PalomarChallenge && lake env lean VerifyAxioms.lean && lake check --paranoid && lake comparator --config comparator.json --paranoid)
```
