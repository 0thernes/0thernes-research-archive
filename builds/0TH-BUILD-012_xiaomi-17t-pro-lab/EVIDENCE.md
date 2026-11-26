# Build White Paper & Proof Evidence Dossier — `0TH-BUILD-012`

**Title:** Xiaomi 17T Pro Lab: Formally Verified Silicon-to-Quantum Modeling, Six-Kernel Lean 4.35.0 Proofs, and Sharded In-Browser Neural Verification of the Dimensity 9500  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Computer Architecture / Semiconductor Physics / EUV Lithography / Quantum Contextuality / Formal Methods  
**Version / Date:** `v3.0.0` (2026-11-25)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/xiaomi-17t-pro-lab |
| Pinned Git Submodule | `repos/xiaomi-17t-pro-lab` @ `267b5a6a79f37396ec99d9dd3e70327b2df80afe` |
| Archived Artifact | `builds/0TH-BUILD-012_xiaomi-17t-pro-lab/Donahue_2026_Xiaomi_17T_Pro_Lab.pdf` (from `dist/Donahue_2026_Xiaomi_17T_Pro_Lab.pdf`) |
| Artifact SHA-256 | `1e59972ac2c4355d38cd0387347e3a8007d90b2dee06294cc78785ce27445d91` |
| Archived Artifact | `builds/0TH-BUILD-012_xiaomi-17t-pro-lab/lean4-audit.txt` (from `results/lean4-audit.txt`) |
| Artifact SHA-256 | `5cff7235963b3dee80e0c0983dfde0c8be04c485b371a0595f1a572e544eec3d` |
| Archived Artifact | `builds/0TH-BUILD-012_xiaomi-17t-pro-lab/VERIFICATION.md` (from `VERIFICATION.md`) |
| Artifact SHA-256 | `ff250c79b880bf6153418a6a4e4f3cb75c49295d538baed273d4cfa07012857a` |
| Archived Artifact | `builds/0TH-BUILD-012_xiaomi-17t-pro-lab/CLAIMS.md` (from `CLAIMS.md`) |
| Artifact SHA-256 | `f7d715d4c32900fe8eca4f9416ca077c57e1af35f8f53e11c748f14d65cbb080` |
| Archived Artifact | `builds/0TH-BUILD-012_xiaomi-17t-pro-lab/mega-atlas-cross-reference.md` (from `docs/mega-atlas-cross-reference.md`) |
| Artifact SHA-256 | `d038aa6f349af5adc6e82814d67bf0309daddccf8908263e2ff691bac38cbe00` |
| Archived Artifact | `builds/0TH-BUILD-012_xiaomi-17t-pro-lab/2026-11-25-3-cycle-hardening-audit.md` (from `docs/reviews/2026-11-25-3-cycle-hardening-audit.md`) |
| Artifact SHA-256 | `d1b53f607db11d1d61ab6a517b442dcb3b1ba6488ceac4d345e86acbc41ac961` |
| Archived Artifact | `builds/0TH-BUILD-012_xiaomi-17t-pro-lab/README.md` (from `README.md`) |
| Artifact SHA-256 | `a08286f7bf4aca5fcbd0465a4f39cd0373208f4b10808ca32dd7a7bac1fd2e21` |

## Summary

Zero-build interactive silicon-to-quantum engineering workbench and 7-page AMS-LaTeX white paper (0 overfull/underfull hboxes) modeling the Xiaomi 17T Pro and MediaTek Dimensity 9500 across 19 interactive routes with 59 Pure Lean 4.35.0 Palomar module declarations verified by 6 independent kernels (hardware floorplan & roofline, EUV Rayleigh/DOF/shot-noise, Crank-Nicolson Cayley unitarity & WKB/Dirac transport, 2D thermal FDTD CFL discrete maximum principle, CHSH & Peres-Mermin contextuality, plus AdversarialTests), a 54-check 60-digit Decimal/Fraction reference oracle (max rel err 2.159e-14), 8/8 killed mutants (100%), 50/50 3-OS Node tests, 8/8 Playwright CSP/E2E specs, 9-shard SHA-256-verified TinyStories-8M in-browser transformer, 100.0% (82/82, 35/35 Core) Build Standard v1.2.0 compliance, and an honest 0/1,900 Mega-Atlas V2 cross-reference.

## Embedded Lean 4 Proof Suite Audit

- **Framework:** Pure Lean 4.35.0 Palomar module core (zero Mathlib, zero native_decide, 6-kernel lake comparator --paranoid)
- **Lean Modules / Lines:** 11 files / 1015 lines
- **Audited Theorems (`#print axioms`):** 59
- **Entry Point:** `lean/XiaomiLabProofs.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Live Audit Status:** Ubuntu CI GREEN (run #45748904789, Sigstore Rekor 4117264287, Release run #45748910920 Rekor 4117247168); 59/59 audited declarations strictly within [propext, Classical.choice, Quot.sound] or zero axioms, zero sorry outside isolated Challenge.lean, leanchecker --fresh PASS, all 6 independent kernels passed via lake comparator --config comparator.json --paranoid in bubblewrap sandbox

## Verification Boundary

Lean 4.35.0 kernels verify algebraic, discrete-PDE stability, unitary-operator, and finite contextuality theorems of the mathematical models with zero sorry and standard axioms; physical hardware leaves distinguish cited facts, computed models, live browser timings, and null UNKNOWN fields (no browser access to MediaTek NPU 990); A-Life routes are purely deterministic software simulations with zero sentience claims; honest Mega-Atlas V2 audit confirms 0 / 1,900 grand open problems retired.

## Independent Reproduction & Falsification Protocol

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/xiaomi-17t-pro-lab && npm ci && npm run verify:all && python3 reference/physics_oracle.py --check-checksums && (cd lean && lake build XiaomiLabProofs Challenge Solution && lake env lean VerifyAxioms.lean && lake comparator --config comparator.json --paranoid)
```
