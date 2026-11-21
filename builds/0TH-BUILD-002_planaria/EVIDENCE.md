# Build White Paper & Proof Evidence Dossier — `0TH-BUILD-002`

**Title:** PLANARIA: Progressive Holographic Executable Architecture (.hbin), Multi-Stratum Compilation, Autonomous Control-Flow Anastomosis, and Cryptographic Cellular Quorum  
**Author:** Alexander Stephen Donahue (0thernes LLC, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Systems Architecture / Coding Theory / Formal Methods  
**Version / Date:** `v2.1.0` (2026-11-21)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/planaria |
| Pinned Git Submodule | `repos/planaria` @ `b12a1c997161d7fab635d056688276ae048bb308` |
| Archived Artifact | `builds/0TH-BUILD-002_planaria/Donahue_2026_planaria.pdf` (from `dist/Donahue_2026_planaria.pdf`) |
| Artifact SHA-256 | `4ace7864d3c5b119691d29ab2507afa22399e3a8a3c86ed3ee8f43e5c09306ae` |
| Archived Artifact | `builds/0TH-BUILD-002_planaria/WHITE_PAPER.md` (from `paper/WHITE_PAPER.md`) |
| Artifact SHA-256 | `91b82b1a94639cdc5bd4893297516dd7d8c5acf079acdaa1ee9b6576fbe57d3b` |

## Summary

Progressive Holographic Instruction Stratification (.hbin) architecture integrating GF(2^8) Reed-Solomon/Cauchy erasure coding, Depth-8 SHA-256-128 Merkle cellular authentication, Plang compiler, PVM-32 anastomosis VM, 4 compiled living .hbin species, WebGL2 3D temporal-quantum engine, 16-suite falsification harness, Ed25519 attestation, frozen 7-page AMS-LaTeX white paper PDF + standalone arXiv bundle, and 38 pure Lean 4 (v4.35.0) machine-checked proofs.

## Embedded Lean 4 Proof Suite Audit

- **Framework:** Pure Lean 4.35.0 (zero Mathlib, zero native_decide)
- **Lean Modules / Lines:** 7 files / 976 lines
- **Audited Theorems (`#print axioms`):** 38
- **Entry Point:** `lean/PlanariaProofs.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Live Audit Status:** Build completed successfully (9 jobs); 0 warnings; 0 sorry; all 38 #print axioms within [propext, Classical.choice, Quot.sound] (7 zero-axiom constructive); GitHub CI #44890541291 (3/3 jobs GREEN); Software Heritage save #2675014

## Verification Boundary

All 38 Lean 4 theorems (covering GF(256) arithmetic, Byzantine quorum thresholds, mitosis bounds, stratum anastomosis, xenograft ABI, and quantum-temporal norm/rewind/combinatorial invariants) compile cleanly in pure Lean 4.35.0 with zero Mathlib, zero native_decide, and zero sorry, strictly within [propext, Classical.choice, Quot.sound]. Runtime JS implementation, Monte Carlo survival curves, and WebGL2 3D engine are separately tested by the 16-suite falsification harness (npm test) and Ubuntu CI.

## Independent Reproduction & Falsification Protocol

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/planaria && npm run build && npm test && cd lean && lake clean && lake build
```
