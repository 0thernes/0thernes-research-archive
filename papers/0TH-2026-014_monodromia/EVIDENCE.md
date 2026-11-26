# Evidence & Falsification Dossier — `0TH-2026-014`

**Title:** MONODROMIA: Machine-Checked Non-Hermitian Spectral Knots, Higher-Order Exceptional-Point Petermann Cancellation, Generalized Brillouin Zone Collapse, Non-Reciprocal Critical Matter, and Plastic-Squared Dipole Scars  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Mathematical Physics / Non-Hermitian Topology / Knot Theory / Formal Verification  
**Version / Date:** `v1.0.0` (2026-11-25)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 & cross-platform CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/monodromia |
| Pinned Git Submodule | `repos/monodromia` @ `153792bdaee2b01f9a56afbcb60af7d2957d5669` |
| GitHub Release | https://github.com/0thernes/monodromia/releases/tag/v1.0.0 |
| Frozen Archived PDF | `papers/0TH-2026-014_monodromia/Donahue_2026_Monodromia.pdf` |
| Frozen PDF SHA-256 | `057da9c86d8fbc4c9cda46b436857868d713254bcd4adf741bcf5844e057f144` |
| arXiv / Source Bundle SHA-256 | `ffca74cc005aebd7b42cdee0949cb9081ef74f37c757180135ad75df0a141e8f` |
| CI Verification Run | https://github.com/0thernes/monodromia/actions/runs/45749048047 |
| Software Heritage SWHID | `swh:1:snp:c2071e6233ff31c36dab1392682036763a15c851` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Unifies six coupled non-Hermitian and topological frontiers across 98 zero-Mathlib Lean 4.35.0 declarations (6-kernel lake comparator --paranoid verified): (I) arbitrary-N Hatano-Nelson cleared-denominator imaginary-gauge similarity, zero-energy Chebyshev parity, literal 3x3/4x4 dual-corner determinant bridge, and exact exponential corner-perturbation catastrophe (CM-018); (II) arbitrary-order EP_n nilpotency, strict 1D coalescence, cyclic Puiseux eigenvectors, and Universal Petermann-Sensitivity Exact Cancellation SNR_Pet^2(n,q) = 1/S_n(q)^2 < 1 strictly decreasing in n; (III) 2-band R=1 Zero-Knot obstruction, the infinite 3-band Gerono-Turk's-Head spectral-knot and Borromean-link family with universal gap >= sqrt(3), uniform half-plane discriminant barrier Re(Delta) <= -783/4 < 0 forcing identically zero discriminant winding nu(Delta) = 0 for all p >= 1, strictly increasing Lucas knot determinant tower L_{2p}-2, 5-adic Fox-Milnor non-sliceness for all even p (GEOM-038), exact TL_3 Kauffman-Jones separation of Unknot/4_1/6_2^3/8_18 and chiral 3_1 (GEOM-039), and Fox Trapezoidal Law for all (2,2m+1) torus knots and alternating twist knots K_p (GEOM-046); (IV) anti-Newtonian CEP necessity (J_AB J_BA < 0), CEP Jordan defectiveness, exact chiral quadrature time-crystal rotation Omega = -sJ, static equal-amplitude impossibility, and non-variational curl (FLD-060/CM-043); (V) exact Gaussian-integer PT intertwining metric eta = [[k, -i*g],[i*g, k]], unbroken positivity, EP_2 null collapse (1,-i), universal pseudo-Hermitian reality, and broken-PT metric impossibility; and (VI) 4-site dipole conservation (0110 <-> 1001), exact 4-state DFA delayed-Tribonacci recurrence Z(L)=Z(L-1)+Z(L-2)+Z(L-4), Plastic-Constant-Squared (rho^2 ~ 1.754878) factorization, exponential shattering 2Z(L)<Z(L+4), and unconditional NHSE immunity (CM-045/QM-017). Paired with safe native Rust (#![forbid(unsafe_code)], 512 fuzz), Python exact Fraction oracle, 15 Node tests + 2,400 property checks + 8/8 killed mutants + 7 STRIDE/EIO HTTP tests, pre-registered 20-seed exact 2^20 permutation study (4/4 confirmed, p_Holm = 7.63e-6), 5/5 hardware-tagged latency budgets, 16-page zero-warning PDF (27/27 live Crossref DOIs) + standalone arXiv bundle, live 3D WebGL2 + 48 kHz AudioWorklet observatory + Lean Blueprint on GitHub Pages, Software Heritage full snapshot swh:1:snp:c2071e6233ff31c36dab1392682036763a15c851, and 100.0% (80/80) Build Standard v1.2.0 compliance.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Pure Lean 4.35.0 (zero Mathlib, 14 sorry-free files, 98 audited declarations strictly within [propext, Classical.choice, Quot.sound], autoImplicit = false, zero native_decide, 7 NonVacuity witnesses, 7 AdversarialTests refutations, 9 Palomar comparator targets verified across all 6 independent kernels via lake comparator --config comparator.json --paranoid inside bubblewrap on Ubuntu 24.04 CI with SLSA attestation)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/PalomarChallenge.lean, lean/PalomarSolution.lean, lean/MonodromiaProofs/NonVacuity.lean, lean/MonodromiaProofs/AdversarialTests.lean`

## Verification Boundary (Honest Epistemic Scope)

All 98 exported declarations across Pillars I-VI, NonVacuity (7), AdversarialTests (7), and Palomar comparator contracts (9) are kernel-checked in zero-Mathlib Lean 4.35.0 strictly within [propext, Classical.choice, Quot.sound] across all 6 independent kernels on Ubuntu 24.04 CI. Continuous-parameter QR eigensolves, 2D Chase PDE evolution, and 20-seed confirmatory statistics are verified numerically, differentially against safe Rust, and statistically rather than in Lean real analysis. Explicitly records 0/1,900 full solutions to overarching problems in 0thernes/unsolved-problems-mega-atlas (docs/MEGA_ATLAS_CROSSCHECK.md); claims no external peer review or external DOI.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/monodromia && npm run verify:all && npm run examples && (cd native && cargo test --release && cargo run --release -- fuzz 512) && python scripts/verify_exact.py --check-checksums && python scripts/check_readme_axioms.py && (cd lean && lake build && lake env lean VerifyAxioms.lean && lake comparator --config comparator.json --paranoid)
```
