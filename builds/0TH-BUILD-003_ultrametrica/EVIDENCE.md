# Build White Paper & Proof Evidence Dossier — `0TH-BUILD-003`

**Title:** ULTRAMETRICA: Exact Non-Archimedean Holography, Recursive Adelic Valuation-Residue Symmetries, Tate-Curve BTZ Ollivier-Ricci Curvature, and Real-Time p-adic Quantum Gravity  
**Author:** Alexander Stephen Donahue (0thernes LLC, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Mathematical Physics / Non-Archimedean Analysis / Formal Methods  
**Version / Date:** `v1.0.0` (2026-11-18)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/ultrametrica |
| Pinned Git Submodule | `repos/ultrametrica` @ `68b0fcdf827905a0f7b179561041adf247c7a1fa` |
| Archived Artifact | `builds/0TH-BUILD-003_ultrametrica/WHITE_PAPER.md` (from `paper/WHITE_PAPER.md`) |
| Artifact SHA-256 | `43258869c2f907eae0d787cf1370ddf41ec1b738cb0371ccb0c385b46cc66185` |

## Summary

Zero-dependency computational laboratory and formal framework for discrete p-adic QFT on Z_p/p^n Z_p coupled to Bruhat-Tits tree and rotating Tate-curve BTZ holography, with 24 pure Lean 4 (v4.35.0) machine-checked proofs covering adelic symmetry, holography curvature, exact Kozyrev nonlinear solitons, and Sherman-Morrison PSD bounds.

## Embedded Lean 4 Proof Suite Audit

- **Framework:** Pure Lean 4.35.0 (zero Mathlib)
- **Lean Modules / Lines:** 5 files / 614 lines
- **Audited Theorems (`#print axioms`):** 24
- **Entry Point:** `lean/UltrametricaProofs.lean`
- **Permitted Axioms:** `propext, Quot.sound`
- **Live Audit Status:** Build completed successfully (7 jobs); 0 sorry; all 24 #print axioms within [propext, Quot.sound] or empty

## Verification Boundary

All 24 audited Lean 4 declarations compile cleanly in pure Lean 4.35.0 with zero Mathlib and zero sorry, strictly within [propext, Quot.sound]. Machine-precision numerical simulations complement the discrete algebraic theorems.

## Independent Reproduction & Falsification Protocol

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/ultrametrica/lean && lake build
```
