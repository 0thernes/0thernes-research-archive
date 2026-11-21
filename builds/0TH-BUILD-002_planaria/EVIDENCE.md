# Build White Paper & Proof Evidence Dossier — `0TH-BUILD-002`

**Title:** PLANARIA: Progressive Holographic Executable Architecture (.hbin), Multi-Stratum Compilation, Autonomous Control-Flow Anastomosis, and Cryptographic Cellular Quorum  
**Author:** Alexander Stephen Donahue (0thernes LLC, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Systems Architecture / Coding Theory / Formal Methods  
**Version / Date:** `v2.2.0` (2026-11-21)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/planaria |
| Pinned Git Submodule | `repos/planaria` @ `b4eaf7cfc88ccc12191f86e910448db43b42c993` |
| Archived Artifact | `builds/0TH-BUILD-002_planaria/Donahue_2026_planaria.pdf` (from `dist/Donahue_2026_planaria.pdf`) |
| Artifact SHA-256 | `a7d24c36cf82b398cc850232f34f0775bc2efc925341e4558f3352813be0dfbd` |
| Archived Artifact | `builds/0TH-BUILD-002_planaria/WHITE_PAPER.md` (from `paper/WHITE_PAPER.md`) |
| Artifact SHA-256 | `c5ad237b447249fffb2737fa5ad09aad24daad62ac56eb43fa8cfc39d250a29c` |
| Archived Artifact | `builds/0TH-BUILD-002_planaria/VERIFICATION.md` (from `VERIFICATION.md`) |
| Artifact SHA-256 | `eb8cd6058f417c2431900048701f529e3a8ffb5cf6e2e8a8c86abc8d3b47d675` |
| Archived Artifact | `builds/0TH-BUILD-002_planaria/lean4-audit.txt` (from `results/lean4-audit.txt`) |
| Artifact SHA-256 | `736c60670a2b88945f8aea0d879d1a459e05c078108d4e201b7c8fb12705489c` |
| Archived Artifact | `builds/0TH-BUILD-002_planaria/arxiv_submission.tar.gz` (from `dist/arxiv_submission.tar.gz`) |
| Artifact SHA-256 | `dedf23610126025f99361b818ad8888c0b9c58932b0c5641b1a4d82e4eb944f7` |

## Summary

Progressive Holographic Instruction Stratification (.hbin) architecture hardened by a 5-layer adversarial audit (v2.2.0): Overlap-Eclipse-resistant byte-granular sync scanning, canonical header invariants, GF(2^8) RS(254,238)/Cauchy MDS coding, Depth-8 0x00/0x01/0x02 SHA-256-128 Merkle authentication, exact integer low-discrepancy placement schedule, strict Plang compiler, caller-windowed PVM-32 anastomosis VM, 4 compiled living .hbin species with SPECIES_MAGIC logic Xenografts, WebGL2 3D temporal-quantum engine (4-qubit Horodecki CHSH & Mermin GHZ, O(1) 360-frame RingBuffer rewind, PolyBLEP 48 kHz AudioWorklet, exact 6,421,059,993,600 reachable discrete combinations), hardened CSP/realpathSync Studio server, 24-suite falsification & security harness, 44-file Ed25519 self-consistency seal, frozen 8-page AMS-LaTeX PDF + standalone arXiv bundle, and 62 pure Lean 4 (v4.35.0) machine-checked proofs.

## Embedded Lean 4 Proof Suite Audit

- **Framework:** Pure Lean 4.35.0 (zero Mathlib, zero native_decide)
- **Lean Modules / Lines:** 7 files / 1772 lines
- **Audited Theorems (`#print axioms`):** 62
- **Entry Point:** `lean/PlanariaProofs.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Live Audit Status:** Build completed successfully (9 jobs); 0 warnings; 0 sorry; all 62 #print axioms strictly within [propext, Classical.choice, Quot.sound] (10 zero-axiom constructive); GitHub CI #44910075875 (3/3 jobs GREEN); GitHub Release v2.2.0; prior Software Heritage save #2675014 (v2.2.0 public Save Code Now gated by Anubis PoW)

## Verification Boundary

All 62 Lean 4.35.0 theorems (1,772 lines across 7 files, covering full 65,536-pair/16,777,216-triple GF(256) field axioms & concrete Char2Field Cauchy invertibility, exact integer placement schedule zero-tie halves, 7-bundle anastomosis vs RS(40,16) and equal-storage RS(192,48), byte-list Hamming/tight 16B-18B bursts/8-level Merkle & unpinned Sybil counterexample, signed BitVec 32 sandboxing & non-vacuous B0/B6 sovereignty, full 4-qubit 16-amplitude complex unitarity, bounded 360-frame RingBuffer rewind, and exact 6,421,059,993,600 combinatorial count) compile cleanly in pure Lean 4.35.0 with zero Mathlib, zero native_decide, and zero sorry, strictly within [propext, Classical.choice, Quot.sound]. Runtime JS implementation, Monte Carlo survival curves, CLI/HTTP security, and WebGL2 3D engine are separately tested by the 24-suite falsification & security harness (npm test) and Ubuntu CI.

## Independent Reproduction & Falsification Protocol

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/planaria && npm run build && npm test && cd lean && lake clean && lake build
```
