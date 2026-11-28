# Evidence & Falsification Dossier — `0TH-2026-021`

**Title:** Refutation of the SIC-Clifford Stabilizer Conjecture, Trace-Norm Spectral Locking of Mana, All-Prime Alltop Magic Attainment, and Exact Distance Settlement of Projective-Geometry Singer Qudit Codes  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Quantum Information Theory / Quantum Error Correction / Finite Projective Geometry / Formal Verification  
**Version / Date:** `v2.0.0` (2026-11-27)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 & 3-OS 9-language polyglot CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/weyl-magic-stabilizer-frontier |
| Pinned Git Submodule | `repos/weyl-magic-stabilizer-frontier` @ `ab70ad2e7c5c4c037e794b1e6944c12c98ff237d` |
| GitHub Release | https://github.com/0thernes/weyl-magic-stabilizer-frontier/releases/tag/v2.0.0 |
| Frozen Archived PDF | `papers/0TH-2026-021_weyl-magic-stabilizer-frontier/Donahue_2026_weyl_magic_stabilizer_frontier.pdf` |
| Frozen PDF SHA-256 | `eeccd42a3776700ab33dcbf74dd334b0b15270aab35f8476ba87d52013cd8681` |
| arXiv / Source Bundle SHA-256 | `8c111e66e45d19b5e97f5f4ead5bb3a8fed81d627b8e04ef149c3bbec9050e6b` |
| CI Verification Run | https://github.com/0thernes/weyl-magic-stabilizer-frontier/actions/runs/46055745811 |
| Software Heritage SWHID | `swh:1:snp:f5d459ee8888a15fc0310532d3c6ba402835c939` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | 10.5281/zenodo.24618582 |

## Core Result

Three-cycle hardened v2.0.0 resolution of a connected chain of four open 2026 problems across three preprints (arXiv:2512.19657v2, arXiv:2607.07197, arXiv:2610.02392) via 14 machine-checked headline theorems (T1a-T4c) + master conjunction + 8 NonVacuity + 8 AdversarialTests in zero-Mathlib Lean 4.35.0 (31 flagship #print axioms + 471-decl exhaustive AuditAllDecls.lean sweep with 0 violations; 15 Palomar targets across all 6 independent kernels on Ubuntu CI run 46055745811) and a 9-language polyglot/quantum verification stack: (I) Refutes Conjecture 1 of Erew & Goldstein (arXiv:2512.19657v2) via Pythagorean rational qutrit WH-SIC fiducials v(a,b,c)=(0,c,-(a+bi)) in Z[zeta_12]^3, exhaustive duplicate-free 216-element PCliff_3 audit on v_345 proving Stab={I,P,P^2} with 2D joint eigenspace span(e_1,e_2) (unit Berry curvature |Omega|=1.0 and Fubini-Study metric diag(1/4,1) confirmed in -Werror QGTL C to 0.0 error), universal all-d Zauner trace-multiplicity obstruction m_lambda >= 2 (canonical all d>=4; all three eigenspaces all d>=7), and reproducible PCliff_4..7 audits (0/256 isolated Scott-Grassl 4a fiducials); (II) Proves Conjecture 2 of Erew & Goldstein across the high-mana regime Mana(psi) > (1/2) ln(D/2) via Tr(H_s^2)=D and Trace-Norm Spectral Lock, establishes the Cubic-Mod-3 Wigner origin dichotomy, and audits 15,566 single-qudit + 2,678 two-qutrit eigenstates plus an explicit locally maximal low-mana 3-qutrit witness at D=27; (III) Addresses Knipfer et al. (arXiv:2607.07197) Eq. (59) via universal all-prime d>=5, all-n Alltop attainment M_2=ln[q^2/(2q-1)], 1D parabolic Clifford unification, Welch-MUB gap (D-1)/(D^2(D+1)), exact Gaussian-integer Super-MUB ruptures at 3-qubit Hoggar (D=8, S/8=2/9<15/64, Moonlab WASM 20,750 gates / 4,096 shots to 4.02e-16) and composite d=4 (Z_4 x Z_4, D=16, S_int=30,301,769,984), exact Z[zeta_5] + Eshkol v1.3.6 9-term WH AD certification of the 1-qudit d=5 Alltop saddle, and complete 8-cluster multiplicity-6 Hessian verification on 2-qudit d=5 Alltop (err 1.42e-14); and (IV) Proves Kulhandjian & Hanzo (arXiv:2610.02392) Conjecture 24 and d_min(Q(2,d))=2 for all d>=2 (inside T4aStmt), proves the universal odd-prime bound d_min(Q(p,2)) <= p+1 with internal circulant commutation (T4bStmt), certifies Q(3,2)/Q(5,2)/Q(7,2)/Q(11,2) in Lean, and settles d_min(Q(7,2))=8 exactly via independent zero-unsafe Rust and strict ISO C11 + dual-ABI x86-64 NASM assembly exhaustive certifications over all 1,827 Q(5,2) and all 1,546,218 Burnside-matched Q(7,2) orbits (0 dependent; 10k ASM diff, ASan/UBSan, 100k fuzz). Accompanied by Zig 0.17, ISO C++20, standalone zero-import reference/oracle.py, 1,000-case Hypothesis, Draft 2020-12 repo.yaml schema validation, 8/8 (-B) mutation kills (0 ruff/0 mypy), 14/14 live author/year/title Crossref/arXiv citations (0 retractions), 21-page 0-warning/0-overfull PDF + clean-room arXiv tarball, WCAG 2.2 AA zero-CDN Interactive 3D Canvas Observatory & Lean Blueprint, OpenSSL X.509 CMS-verified DigiCert RFC 3161 (.tsr) + 3-calendar Bitcoin OTS (.ots), pinned gitleaks + osv-scanner, SWH swh:1:snp:f5d459ee8888a15fc0310532d3c6ba402835c939, and 71/71 (100.0%, Core 30/30) Build Standard v1.2.0 compliance.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Pure Lean 4.35.0 (zero Mathlib, 14 Lean module files; 13 sorry-free and PalomarChallenge.lean holds the 15 intentional sorry stubs; 31 flagship #print axioms audits across 14 headline theorems T1a-T4c + master conjunction [= 15 Palomar targets] + 8 NonVacuity witnesses NV01-NV08 [NV07/NV08 constructively inhabiting universal Pillar IV theorems] + 8 AdversarialTests boundary refutations AT01-AT08 PLUS exhaustive metaprogramming AuditAllDecls.lean sweeping all 471 constants in WeylMagicFrontier.* with 0 violations strictly within [propext, Classical.choice, Quot.sound], autoImplicit = false, zero native_decide; strengthened v2.0.0 Palomar contract includes binary_singer_exact_distance_two in T4aStmt, internal universal circulant commutation eliminating 2 hypotheses from T4bStmt, allPCliff3_nodup/mem_allPCliff3_iff/isCollinear_of_scale in T1bStmt, and sqrt5Elem_sq in T3dStmt; all 15 Palomar targets passed all 6 independent kernels on Ubuntu CI run 46055745811 via bubblewrap lake check --paranoid & lake comparator --config comparator.json --paranoid + live sorry/custom-axiom tamper rejection: lean, leanchecker-paranoid, lean4lean, nanoda, con-leche, con-ron)
- **Library Entry Point:** `lean/PalomarSolution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/AuditAllDecls.lean, lean/Challenge.lean, lean/Solution.lean, lean/PalomarChallenge.lean, lean/WeylMagicFrontier/NonVacuity.lean, lean/WeylMagicFrontier/AdversarialTests.lean`

## Verification Boundary (Honest Epistemic Scope)

All 31 flagship declarations in VerifyAxioms.lean AND all 471 constants in WeylMagicFrontier.* swept by AuditAllDecls.lean (0 violations) are kernel-checked in zero-Mathlib Lean 4.35.0 strictly within [propext, Classical.choice, Quot.sound] across all 6 independent proof kernels + live sorry/custom-axiom tamper rejection on Ubuntu CI run 46055745811 (zero sorry outside PalomarChallenge.lean, zero native_decide). The exhaustive lower-bound certifications over 1,827 Q(5,2) orbits and 1,546,218 Q(7,2) Singer-Frobenius orbits (C4d) are independently verified in zero-unsafe Rust and ISO C11 + x86-64 NASM assembly and tagged [EXACT-COMP] separately from [LEAN-6K]; Eshkol AD, Moonlab WASM (with explicitly classical deterministic software QRNG mixer SplitMix64+xoshiro256**, zero hardware quantum entropy claimed), QGTL C, and scripts/verify_numerical_claims.py are tagged [NUM-STACK]. Explicitly affirms 0/2,000 overarching Mega-Atlas grand open problems retired; low-mana Conjecture 2 (Mana <= (1/2) ln(D/2)), the global upper bound on two-qudit prime M_2, Zauner's SIC existence conjecture, and Kulhandjian-Hanzo Conjecture 27's lower bound for p >= 11 remain OPEN. Claims no external peer review or external DOI.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/weyl-magic-stabilizer-frontier && (cd rust && cargo clippy --all-targets -- -D warnings && cargo test --release && cargo run --release -- --json) && (cd zig && zig test src/main.zig && zig run -O ReleaseFast src/main.zig) && make -C c clean test-nasm sanitize fuzz && PYTHONPATH=src:. pytest -v tests/test_all.py && PYTHONPATH=src:. python3 scripts/mutate.py && python3 scripts/check_readme_axioms.py && (cd lean && lake build && lake build PalomarChallenge && lake env lean VerifyAxioms.lean && lake env lean AuditAllDecls.lean && lake comparator --config comparator.json --paranoid)
```
