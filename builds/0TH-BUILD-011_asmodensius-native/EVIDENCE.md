# Build White Paper & Proof Evidence Dossier — `0TH-BUILD-011`

**Title:** Asmodensius Native: Bare-Metal C11/Vulkan Organism Runtime with 20 Pure Lean 4.35.0 Discrete Invariants (A01-A20)  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Artificial Life / Systems Engineering / Formal Methods  
**Version / Date:** `main-snapshot` (2026-11-22)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/asmodensius-native |
| Pinned Git Submodule | `repos/asmodensius-native` @ `782cd0ed5f2aa06383c6b6279ac6ff22b42e8f47` |
| Archived Artifact | `builds/0TH-BUILD-011_asmodensius-native/AsmodensiusProofs.lean` (from `lean/AsmodensiusProofs.lean`) |
| Artifact SHA-256 | `c29ebfc856ea241ab71b016e0b54c03597216777329dedc5bca8065f818bac8a` |
| Archived Artifact | `builds/0TH-BUILD-011_asmodensius-native/AGENTS.md` (from `AGENTS.md`) |
| Artifact SHA-256 | `6ce72bfe1eeea640bed2bd5fd9d2073b82141a882d9927c55dbdca30db1594e8` |

## Summary

Native runtime component of the A-Life Singularity Omega stack carrying 20 Pure Lean 4.35.0 declarations (AsmodensiusProofs.lean, A01-A20) covering mass/energy conservation, species cap refusal boundaries, arena rollback, observer hash invariance, Philox RNG key equivalence, and CPU/GPU twin hash parity.

## Embedded Lean 4 Proof Suite Audit

- **Framework:** Pure Lean 4.35.0 Core (zero Mathlib, zero native_decide)
- **Lean Modules / Lines:** 1 files / 155 lines
- **Audited Theorems (`#print axioms`):** 20
- **Entry Point:** `lean/AsmodensiusProofs.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Live Audit Status:** 20 Pure Lean 4 declarations (A01-A20, zero sorry, explicit #print axioms strictly standard); NOTE: A15, A16, and A20 are disclosed arithmetic rfl accounting witnesses rather than deep behavioral proofs

## Verification Boundary

Certifies discrete arithmetic, state-transition, and hash-parity invariants of the native simulation runtime; explicitly discloses that A15, A16, and A20 are trivial arithmetic rfl accounting witnesses and makes zero claims of sentience, consciousness, or resolving any open mathematical/scientific problem.

## Independent Reproduction & Falsification Protocol

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/asmodensius-native/lean && lean AsmodensiusProofs.lean
```
