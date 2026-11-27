# Evidence & Falsification Dossier — `0TH-2026-021`

**Title:** Refutation of the SIC-Clifford Stabilizer Conjecture, Trace-Norm Spectral Locking of Mana, All-Prime Alltop Magic Attainment, and Exact Distance Settlement of Projective-Geometry Singer Qudit Codes  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Quantum Information Theory / Quantum Error Correction / Finite Projective Geometry / Formal Verification  
**Version / Date:** `v1.0.0` (2026-11-26)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 & 3-OS 9-language polyglot CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/weyl-magic-stabilizer-frontier |
| Pinned Git Submodule | `repos/weyl-magic-stabilizer-frontier` @ `da2aa5d9e40a7a7e9d54fc18e7ff14a87f6f4617` |
| GitHub Release | https://github.com/0thernes/weyl-magic-stabilizer-frontier/releases/tag/v1.0.0 |
| Frozen Archived PDF | `papers/0TH-2026-021_weyl-magic-stabilizer-frontier/Donahue_2026_weyl_magic_stabilizer_frontier.pdf` |
| Frozen PDF SHA-256 | `e850d5b5423d0ff246b53e19f56bc3fced651734f6c498bb42879792b7539a20` |
| arXiv / Source Bundle SHA-256 | `114ca68ff6a49ed0cc2e166ae8891abd70c3ada63923f1e2a501189a65717a35` |
| CI Verification Run | https://github.com/0thernes/weyl-magic-stabilizer-frontier/actions/runs/45951549479 |
| Software Heritage SWHID | `swh:1:snp:a28a2bfc144bba02e64b2fc69ab5375ec284da07` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Resolves a connected chain of four open 2026 problems across three preprints (arXiv:2512.19657v2, arXiv:2607.07197, arXiv:2610.02392) via 14 machine-checked headline theorems (T1a-T4c) + master conjunction + 8 NonVacuity + 8 AdversarialTests in zero-Mathlib Lean 4.35.0 (31 audited decls, 15 Palomar targets across all 6 independent kernels on Ubuntu CI run 45951549479) and a 9-language polyglot/quantum verification stack: (I) Refutes Conjecture 1 of Erew & Goldstein (arXiv:2512.19657v2) by proving every Pythagorean triple (a,b,c) yields an exact qutrit WH-SIC fiducial v(a,b,c)=(0,c,-(a+bi)) in Z[zeta_12]^3, exhaustively checking all 216 elements of PCliff_3 on v_345 to prove Stab={I,P,P^2} with 2D joint eigenspace span(e_1,e_2) (unit Berry curvature |Omega|=1.0 and Fubini-Study metric diag(1/4,1) confirmed in compiled QGTL C to 0.0 error), proving the universal all-d Zauner trace-multiplicity obstruction m_lambda >= 2 (canonical all d>=4; all three eigenspaces all d>=7), and auditing Scott-Grassl 4a (0/256 isolated fiducials 1D-stabilized); (II) Proves Conjecture 2 of Erew & Goldstein across the high-mana regime Mana(psi) > (1/2) ln(D/2) via universal sign-witness Parseval identity Tr(H_s^2)=D and Trace-Norm Spectral Lock, plus the exact Cubic-Mod-3 Wigner origin dichotomy (W_Alltop(0,0)=0 for p=2 mod 3 via y^((2p-1)/3) vs nonzero 3-to-1 collapse for p=1 mod 3); (III) Addresses Conjecture Eq. (59) of Knipfer et al. (arXiv:2607.07197) by proving universal all-prime d>=5, all-n finite-field Alltop attainment M_2=ln[q^2/(2q-1)], 1D parabolic Clifford unification, exact Welch-MUB gap (D-1)/(D^2(D+1)), exact Gaussian-integer Super-MUB ruptures at 3-qubit Hoggar (D=8, S/8=2/9<15/64, confirmed in Moonlab WASM to 4.02e-16) and composite d=4 (Z_4 x Z_4, D=16, S_int=30,301,769,984), and exact Z[zeta_5] + Eshkol v1.3.6 AD certification that 1-qudit d=5 Alltop is an unstable saddle point; and (IV) Proves Conjecture 24 of Kulhandjian & Hanzo (arXiv:2610.02392) for all d>=2 (M_{Q_e}A = J mod 2, Remark 21 u_+ exception strictly at d=2, exact d_min(Q(2,d))=2), proves the universal odd-prime upper bound d_min(Q(p,2)) <= p+1 via L_line=(tau_H|tau_H) covering both conic orientations, certifies Q(3,2)/Q(5,2)/Q(7,2)/Q(11,2) witnesses in Lean, and settles d_min(Q(7,2))=8 exactly via independent zero-unsafe Rust and strict ISO C11 + dual-ABI x86-64 NASM assembly exhaustive certifications over all 1,827 Q(5,2) orbits and all 1,546,218 Burnside-matched Q(7,2) Singer-Frobenius orbits (0 dependent; 10k ASM diff, ASan/UBSan, 100k libFuzzer-compatible fuzz). Accompanied by Zig 0.17 comptime, ISO C++20 constexpr, Python exact oracle + Hypothesis + 8/8 (100%) mutation kills (0 ruff/0 mypy), 14/14 live Crossref/arXiv citations (0 retractions), 21-page 0-warning/0-overfull AMS-LaTeX PDF + clean-room arXiv tarball, live zero-CDN 3D Observatory & Lean Blueprint, DigiCert RFC 3161 (.tsr) + 3-calendar Bitcoin OTS (.ots), SWH swh:1:snp:a28a2bfc144bba02e64b2fc69ab5375ec284da07, and 71/71 (100.0%, Core 30/30) Build Standard v1.2.0 compliance.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Pure Lean 4.35.0 (zero Mathlib, 13 Lean module files; 12 sorry-free and PalomarChallenge.lean holds the 15 intentional sorry stubs; 31 audited declarations across 14 headline theorems T1a-T4c + master conjunction [= 15 Palomar targets] + 8 NonVacuity witnesses NV01-NV08 [NV08 uses 0 axioms] + 8 AdversarialTests boundary refutations AT01-AT08 strictly within [propext, Classical.choice, Quot.sound], autoImplicit = false, zero native_decide; all 15 Palomar targets passed all 6 independent kernels on Ubuntu CI run 45951549479 via bubblewrap lake check --paranoid [58,611-58,614 decls] & lake comparator --config comparator.json --paranoid [2,438-2,441 decls] + live sorry/custom-axiom tamper rejection: lean, leanchecker-paranoid, lean4lean, nanoda, con-leche --verified, con-ron --verified; CI SLSA #72963755 / Rekor 4143162203, Release v1.0.0 SLSA #72963458 / Rekor 4143155495)
- **Library Entry Point:** `lean/PalomarSolution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/Solution.lean, lean/PalomarChallenge.lean, lean/WeylMagicFrontier/NonVacuity.lean, lean/WeylMagicFrontier/AdversarialTests.lean`

## Verification Boundary (Honest Epistemic Scope)

All 31 audited declarations across Pillars I-IV (15 Palomar targets T1a-T4c + prove_all_frontier_theorems), NonVacuity (NV01-NV08), and AdversarialTests (AT01-AT08) are kernel-checked in zero-Mathlib Lean 4.35.0 strictly within [propext, Classical.choice, Quot.sound] across all 6 independent proof kernels + live sorry/custom-axiom tamper rejection on Ubuntu CI run 45951549479 (zero sorry outside PalomarChallenge.lean, zero native_decide). The exhaustive lower-bound certifications over 1,827 Q(5,2) orbits and 1,546,218 Q(7,2) Singer-Frobenius orbits (C4d) are independently verified in zero-unsafe Rust and ISO C11 + x86-64 NASM assembly and tagged [EXACT-COMP] separately from [LEAN-6K]; Eshkol AD, Moonlab WASM (with explicitly classical deterministic software QRNG mixer SplitMix64+xoshiro256**, zero hardware quantum entropy claimed), QGTL C, and numerical sweeps are tagged [NUM-STACK]. Explicitly affirms 0/2,000 overarching Mega-Atlas grand open problems retired; low-mana Conjecture 2 (Mana <= (1/2) ln(D/2)), the global upper bound on two-qudit prime M_2, Zauner's SIC existence conjecture, and Kulhandjian-Hanzo Conjecture 27's lower bound for p >= 11 remain OPEN. Claims no external peer review or external DOI.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/weyl-magic-stabilizer-frontier && (cd rust && cargo clippy --all-targets -- -D warnings && cargo test --release && cargo run --release -- --json) && (cd zig && zig test src/main.zig && zig run -O ReleaseFast src/main.zig) && make -C c clean test-nasm sanitize fuzz && PYTHONPATH=src:. pytest -v tests/test_all.py && PYTHONPATH=src:. python3 scripts/mutate.py && python3 scripts/check_readme_axioms.py && (cd lean && lake build && lake build PalomarChallenge && lake env lean VerifyAxioms.lean && lake comparator --config comparator.json --paranoid)
```
