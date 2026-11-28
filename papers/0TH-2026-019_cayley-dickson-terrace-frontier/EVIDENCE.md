# Evidence & Falsification Dossier — `0TH-2026-019`

**Title:** The Dyadic-Palindromic Terrace Law, Nilpotent Mirror Conservation, and Coordinate Norm-Multiplicativity Ruptures Across Cayley-Dickson Algebras  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Non-Associative Algebra / Hypercomplex Algebras / Combinatorial Number Theory / Formal Verification  
**Version / Date:** `v2.1.0` (2026-11-27)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 & 3-OS CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/cayley-dickson-terrace-frontier |
| Pinned Git Submodule | `repos/cayley-dickson-terrace-frontier` @ `0ea58439e9f98b4f44f13fa484c5ee4b50badb10` |
| GitHub Release | https://github.com/0thernes/cayley-dickson-terrace-frontier/releases/tag/v2.1.0 |
| Frozen Archived PDF | `papers/0TH-2026-019_cayley-dickson-terrace-frontier/Donahue_2026_cayley_dickson_terrace_frontier.pdf` |
| Frozen PDF SHA-256 | `ca99318ae699d5fb3140e41557a7887558608bf4afc95dc33d9463a3fdf69146` |
| arXiv / Source Bundle SHA-256 | `dbc49151c74e8e9633828d94a6b256b0454f2e350f40615be2bd0e0369947029` |
| CI Verification Run | https://github.com/0thernes/cayley-dickson-terrace-frontier/actions/runs/46055543755 |
| Software Heritage SWHID | `swh:1:snp:a8698046c6b39a1531cfb5a74c6fa17c36a5d981` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | 10.5281/zenodo.24618590 |

## Core Result

Machine-checks 22 headline theorems (T1a-T1f, T2a-T2f, T3a-T3d, T4a-T4f) + master conjunction prove_all_terrace_theorems (23 Palomar targets) plus 4 NonVacuity witnesses and 8 AdversarialTests sharpness refutations (35 audited decls) in zero-Mathlib Lean 4.35.0, resolving 23/23 ERRATA.md entries from v1.0.0 and 34/34 Cycle 1-3 forensic hardening findings in v2.1.0: (I) Nilpotent Mirror Conservation & Full Bilinear Kernel Basis across all 2^n signatures CD_n(gamma) (T1a-T1f): exact multiplicative cocycle factorization, k-independent 2x2 block-sign flip law, full bilinear square (e_i+e_j)^2 with cross-term cancellation, mirror dichotomy, mirror-pair sum invariance H(v)+H(2^(n-1)-v), and T1f explicit Z-basis isomorphism for ker L_{e_i+e_j} under cdMulCoordGamma; (II) Dyadic-Palindromic Terrace Law & Sharp BDI Separation (T2a-T2f): four-branch doubling recurrence, 4|nu and attained ceiling 2^(n-1)-4 with uniqueness of BDI equality at n=4 (strict separation for all n>=5), closed mass 8(2^(n-1)-1)(2^(n-2)-1)(2^(n-3)-1), non-ZD count (6n-9)*2^(n-2)+3, interior palindrome, top terrace bin 2H_n(0), and Universal All-Signature Midpoint 42 Law H_n^gamma(2^(n-2)) = 42*2^(n-4); (III) Coordinate right-multiplier families in Euclidean CD_n (T3a-T3d): exact doubling of G_n^comp & unique universal right-multipliers {e_0, e_{2^(n-1)}}, exact clique number omega(G_n^comp)=n+5 (n>=3), arithmetic comparison vs classical rho(2^n) saturating at n in {3,4,5} and falling short with deficit >= n-5 for all n>=6 (Euclidean coordinate scope), and constructive [2^n,n+5,2^n] & [2^(n-1),2(n+4),2^n] pairs; and (IV) Complete Finite Certificates, Pure-Kernel Pathion r_max=14 (7+7 Rigidity) & Dim-64 Gap (T4a-T4f): Sedenion Triple-42 & Fano 7+28+7=42 + 2+2 bad-plane splitting across all 2^16 subsets with 0 at >=11D (T4a), non-circular vanishing-product re-verification of de Marrais 7xK_{2,2,2} box-kites & 9D O+Re_8 (T4b), CD_4/CD_5 split phases (T4c), [14,14,32] & [16,16,64] witnesses + unfactored c^2=1 => c=+-1 in Z[i] (T4d), pure-kernel exhaustion over all 2^32 Pathion subsets & duplicate-free lists proving r_max(CD_5)=14 and strict 7+7 half-balance rigidity retiring HiGHS MILP from the proof trust base (T4e), and pure-kernel 9-bin histogram at CD_6(flip=56) certifying the dimension-64 interior spectral gap H_6^56(20)=0 (T4f). Differentially audited across all 496 algebras CD_4(gamma)-CD_8(gamma) and all 280 Pathion 14D subspaces in Rust (#![forbid(unsafe_code)], 4/4 tests incl. T1f Z-basis, 3-OS CI), strict ISO C11 (-Werror -Wconversion -Wshadow, ASan/UBSan, 100k CD_1..CD_7 fuzz, zero-stride 496 algebras), and exact Q Python oracle (3-OS CI, 15/15 pytest incl. T1f Z-basis, strict repo.yaml Draft 2020-12 schema, real-symbol statement-fidelity audit, Hypothesis + 8/8 surgical mutants killed + 0 ruff / 0 mypy), accompanied by 30 bibliography entries (28/28 live Crossref/arXiv title+author+year+retraction verified + 2 print-only classics + programmatic docs/literature-search-log.md + 100% bijective cite), 43-item Gold Standard checklist, 21-page 0-warning AMS-LaTeX PDF + clean-room arXiv tarball, OpenSSL-verified DigiCert RFC 3161 .tsr + 3-calendar Bitcoin .ots timestamps, strict-CSP zero-CDN WCAG keyboard-accessible 3D Canvas Observatory & 26-node Blueprint on GitHub Pages, 1280x640 social preview, and 100.0% (71/71) Build Standard v1.2.0 compliance.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Pure Lean 4.35.0 (zero Mathlib, 14 Lean module files (13 sorry-free; PalomarChallenge.lean is the intentional 23-target sorry stub), 35 audited declarations across 23 Palomar targets T1a-T4f + prove_all_terrace_theorems + 4 NonVacuity witnesses + 8 AdversarialTests boundary refutations strictly within [propext, Classical.choice, Quot.sound], autoImplicit = false, zero native_decide, zero maxRecDepth/maxHeartbeats overrides, full Palomar formalization.yaml metadata; all 6 independent kernels passed on Ubuntu CI run 46055543755 [10/10 green, zero deprecation warnings] via lake check --paranoid [60,087-60,090 decls] & lake comparator --config comparator.json --paranoid [4,482-4,485 decls]: lean, leanchecker-paranoid, lean4lean, nanoda, con-leche --verified, con-ron --verified, plus a real tamper-injecting negative comparator & axiom-gate test on PalomarSolution.lean rejecting both injected sorry and injected public axiom; SLSA attestation #73248368 / Rekor 4150903219; OpenSSL-verified DigiCert RFC 3161 .tsr [Nov 27 18:19:18 2026 GMT] + 3-calendar Bitcoin .ots)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/PalomarChallenge.lean, lean/PalomarSolution.lean, lean/CDTerrace/NonVacuity.lean, lean/CDTerrace/AdversarialTests.lean`

## Verification Boundary (Honest Epistemic Scope)

All 35 audited declarations across Pillars I-IV (23 Palomar targets T1a-T4f + prove_all_terrace_theorems), NonVacuity (4), and AdversarialTests (8) are kernel-checked in zero-Mathlib Lean 4.35.0 strictly within [propext, Classical.choice, Quot.sound] across all 6 independent kernels plus a real tamper-injecting negative comparator/axiom gate on Ubuntu CI run 46055543755 (zero sorry outside PalomarChallenge.lean, zero native_decide, zero overrides; all 23 headline targets mapped 1-to-1 in docs/statement-fidelity.md with zero ghost Lean identifiers). T1f formally bridges twobladeNullityGamma to the exact Z-basis dimension of ker L_{e_i+e_j} under cdMulCoordGamma, T4e proves r_max(CD_5)=14 and strict 7+7 rigidity purely inside the Lean kernel over all 2^32 subsets (retiring HiGHS MILP from the proof trust base), and T4f certifies the CD_6(56) interior spectral gap H_6^56(20)=0 in Lean. Complete 448-algebra split-phase tables for CD_6(gamma)-CD_8(gamma) (C1) and the exhaustive count of 280 Pathion 14D subspaces (C2) are verified differentially across Rust, ISO C11, and exact Q Python and tagged [EXACT-COMP]. Explicitly affirms that 0/1,900 overarching Mega-Atlas grand open problems are retired (adjacent ALG-035, ALG-039, XGEOM-031, COMB-040 and general non-coordinate composition-pair/Hurwitz-Radon problems remain OPEN). Claims no external peer review or external DOI; Software Heritage Save Code Now awaits manual browser submission past Anubis PoW.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/cayley-dickson-terrace-frontier && (cd rust && cargo clippy --all-targets -- -D warnings && cargo test --release && cargo run --release -- --verify-all) && make -C c test sanitize fuzz && PYTHONPATH=src:. pytest -v tests/test_all.py && python scripts/check_readme_axioms.py && python scripts/stamp_timestamps.py --verify --negative-test && (cd lean && lake build && lake build PalomarChallenge && lake env lean VerifyAxioms.lean && lake comparator --config comparator.json --paranoid)
```
