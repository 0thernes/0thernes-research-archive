# Build White Paper & Proof Evidence Dossier — `0TH-BUILD-006`

**Title:** Black Hole Simulation Lab: Exact Schwarzschild Lean 4 Certificates (ClassicalGR.lean) & Kerr Shadow Asymmetry Analytic Anchors  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** General Relativity / Computational Astrophysics / Formal Methods  
**Version / Date:** `main+research-branch` (2026-11-10)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/black-hole-simulation-lab |
| Pinned Git Submodule | `repos/black-hole-simulation-lab` @ `050455db866d32eb115d0cd1a39f9b90a76fdd6f` |
| Additional Branch Ref | `cursor/research-archive-and-starfield-b952 @ 9114db2f0876ea5acbe539acac77570e76da2d1c` |
| Archived Artifact | `builds/0TH-BUILD-006_black-hole-simulation-lab/ClassicalGR.lean` (from `proofs/ClassicalGR.lean (branch cursor/research-archive-and-starfield-b952)`) |
| Artifact SHA-256 | `ba61fa1c955601872c6ca6a91d43dfabc7fa5987dab1d1170fdf3eb5780352cd` |
| Archived Artifact | `builds/0TH-BUILD-006_black-hole-simulation-lab/M5_SHADOW_ASYMMETRY.md` (from `docs/research/M5_SHADOW_ASYMMETRY.md`) |
| Artifact SHA-256 | `a56a672d018de67694e41afea6e5f4fdf3119c94d007986e0adf9cb66d6e4b6b` |
| Archived Artifact | `builds/0TH-BUILD-006_black-hole-simulation-lab/RESEARCH_PROGRAM.md` (from `docs/research/RESEARCH_PROGRAM.md`) |
| Artifact SHA-256 | `51190094d2519142b452504364261a436ec4534383d8f85ba21b3298bb5ab44e` |

## Summary

GR-exact Schwarzschild/Kerr geodesic simulation lab with an 8-theorem zero-axiom Lean 4 certificate (proofs/ClassicalGR.lean on branch cursor/research-archive-and-starfield-b952) verifying photon-sphere u=1/3, critical potential 1/27, b_crit^2=27, ISCO E^2=8/9 & L^2=12, and BPT a=0 -> r=6, paired with exact Bardeen Kerr shadow asymmetry anchors (M5_SHADOW_ASYMMETRY.md) and 20+ GR source cards.

## Embedded Lean 4 Proof Suite Audit

- **Framework:** Pure Lean 4.35.0 Core (zero Mathlib, zero axioms)
- **Lean Modules / Lines:** 1 files / 34 lines
- **Audited Theorems (`#print axioms`):** 8
- **Entry Point:** `builds/0TH-BUILD-006_black-hole-simulation-lab/ClassicalGR.lean`
- **Permitted Axioms:** `NONE (zero axioms)`
- **Live Audit Status:** Live lean 4.35.0 EXIT 0; all 8 rfl theorems depend on ZERO axioms (does not depend on any axioms)

## Verification Boundary

ClassicalGR.lean certifies exact rational Schwarzschild algebraic limits by pure kernel definitional reduction (rfl, zero axioms); it explicitly disclaims proving the full Einstein field equations. Kerr shadow asymmetry anchors are closed-form analytic_classical checks.

## Independent Reproduction & Falsification Protocol

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
lean builds/0TH-BUILD-006_black-hole-simulation-lab/ClassicalGR.lean
```
