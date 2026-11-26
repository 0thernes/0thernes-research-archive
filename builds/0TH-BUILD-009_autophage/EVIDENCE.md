# Build White Paper & Proof Evidence Dossier — `0TH-BUILD-009`

**Title:** AUTOPHAGE v1.0: Bare-Metal Polymorphic x86-64 Galois-Field Genetic Engine with 31 Lean 4.35.0 Formal Theorems  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Systems Architecture / Coding Theory / Artificial Life / Formal Methods  
**Version / Date:** `v1.0.0` (2026-11-21)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/autophage |
| Pinned Git Submodule | `repos/autophage` @ `185bd16c9c2dfcfacc1a7ef3caf99b78c1c0f44a` |
| Archived Artifact | `builds/0TH-BUILD-009_autophage/VERIFICATION.md` (from `VERIFICATION.md`) |
| Artifact SHA-256 | `e4655c7e9b6a81a58be611a82aeeed8d4a6771d84c40b39035dcebc92b0a5285` |
| Archived Artifact | `builds/0TH-BUILD-009_autophage/ARCHITECTURE.md` (from `ARCHITECTURE.md`) |
| Artifact SHA-256 | `7f2d694d0ef1a9dfc63592aa6fa507930aeeece9fac4abfe2c0ef5ab7c8a0c80` |
| Archived Artifact | `builds/0TH-BUILD-009_autophage/README.md` (from `README.md`) |
| Artifact SHA-256 | `9f457c4271a75e037156ff3336a43850d0b14c155ed0ff7c57bfec78287c1285` |

## Summary

Bare-metal polymorphic x86-64 Galois-field genetic engine with 31 Lean 4.35.0 theorems covering GFNI affine involutions, Weismann roundtrip, GF(256)/Cauchy ECC recovery, 64-bit Toffoli/Fredkin symplectic reversibility and Landauer erasure, 2-adic Strong Triangle Inequality, JIT bounds, and thermodynamic monotonicity.

## Embedded Lean 4 Proof Suite Audit

- **Framework:** Lean 4.35.0 Core + built-in bv_decide bitvector solver (zero Mathlib)
- **Lean Modules / Lines:** 1 files / 394 lines
- **Audited Theorems (`#print axioms`):** 31
- **Entry Point:** `lean/AutophageProofs.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Live Audit Status:** Ubuntu CI GREEN (run 44887958546) & local lean EXIT 0; 31/31 theorems (T01-T30 + T05a), 0 sorry (uses built-in bv_decide reflection on BitVec identities)
- **Reflection Axiom Disclosure:** BitVec identities invoke Lean 4's built-in bv_decide SAT reflection axioms (._native.bv_decide.*); explicitly separated from pure kernel-only proofs.

## Verification Boundary

Compiles cleanly in Lean 4.35.0 on Ubuntu CI with 0 sorry and 0 custom user axioms; transparently discloses reliance on Lean 4's built-in bv_decide native bitvector reflection axioms for finite BitVec theorems. Runtime verified by 18 silicon falsification gates and 6 planted negative mutants on Win64 and Linux.

## Independent Reproduction & Falsification Protocol

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/autophage/lean && lean AutophageProofs.lean
```
