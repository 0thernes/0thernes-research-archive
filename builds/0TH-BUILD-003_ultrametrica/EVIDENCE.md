# Build White Paper & Proof Evidence Dossier — `0TH-BUILD-003`

**Title:** ULTRAMETRICA: Exact Non-Archimedean Holography, Recursive Adelic Valuation-Residue Symmetries, Tate-Curve BTZ Ollivier-Ricci Curvature, and Lean 4 Formal Verification  
**Author:** Alexander Stephen Donahue (0thernes LLC, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Mathematical Physics / Non-Archimedean Analysis / Formal Methods  
**Version / Date:** `v1.1.0` (2026-11-21)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/ultrametrica |
| Pinned Git Submodule | `repos/ultrametrica` @ `3fe39163a838f6d6b9dab3d75cedb4aea9b3bf0f` |
| Archived Artifact | `builds/0TH-BUILD-003_ultrametrica/Donahue_2026_Ultrametrica.pdf` (from `dist/Donahue_2026_Ultrametrica.pdf`) |
| Artifact SHA-256 | `7ce392ff2c772c6714d67737fc0c1d14e19a2a891193b71cb65de2f6aefb653c` |
| Archived Artifact | `builds/0TH-BUILD-003_ultrametrica/WHITE_PAPER.md` (from `paper/WHITE_PAPER.md`) |
| Artifact SHA-256 | `43258869c2f907eae0d787cf1370ddf41ec1b738cb0371ccb0c385b46cc66185` |
| Archived Artifact | `builds/0TH-BUILD-003_ultrametrica/arxiv_submission.tar.gz` (from `dist/arxiv_submission.tar.gz`) |
| Artifact SHA-256 | `d53caf2d51ca5434ca072b70d9de4acda2e06d43f90c36676096c02dd371a269` |

## Summary

Zero-dependency computational laboratory, zero-warning AMS-LaTeX white paper PDF, standalone arXiv bundle, and formal framework coupling discrete p-adic QFT on Z_p/p^n Z_p to Bruhat-Tits tree and rotating Tate-curve BTZ holography, verified by 36 pure Lean 4 (v4.35.0) machine-checked proofs and an independent exact-rational (fractions.Fraction & Q(i)) Python falsifier.

## Embedded Lean 4 Proof Suite Audit

- **Framework:** Pure Lean 4.35.0 (zero Mathlib)
- **Lean Modules / Lines:** 6 files / 642 lines
- **Audited Theorems (`#print axioms`):** 36
- **Entry Point:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Live Audit Status:** Build completed successfully (7 jobs); 0 sorry; all 36 #print axioms in VerifyAxioms.lean strictly within [propext, Classical.choice, Quot.sound] (14 zero-axiom)

## Verification Boundary

All 36 audited Lean 4 declarations compile cleanly in pure Lean 4.35.0 with zero Mathlib and zero sorry, strictly within [propext, Classical.choice, Quot.sound] (14 zero-axiom). Independent exact-rational Python checks verify 7,033 conjugate Adelic pairs, 45 BTZ optimal-transport horizons, and exact Q(i) Rank-1 Sherman-Morrison solves with zero rounding error; floating-point FFT/PDE simulations complement the exact discrete algebraic theorems. No empirical discovery of new physical laws of nature is claimed.

## Independent Reproduction & Falsification Protocol

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/ultrametrica && npm test && python3 scripts/verify_exact.py && (cd lean && lake build && lake env lean VerifyAxioms.lean)
```
