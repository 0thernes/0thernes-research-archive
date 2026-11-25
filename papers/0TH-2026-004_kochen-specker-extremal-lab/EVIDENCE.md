# Evidence & Falsification Dossier — `0TH-2026-004`

**Title:** Certified exact minima of Kochen-Specker sets inside coordinate pools: 31 and 33 rays in dimension three, 18 in dimension four, 29 in dimension five  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Quantum Foundations / Combinatorial Optimization  
**Version / Date:** `v1.8.0` (2026-11-24)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 repository CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/kochen-specker-extremal-lab |
| Pinned Git Submodule | `repos/kochen-specker-extremal-lab` @ `b18eda33a80c1c07cd0c44e5f760f520ac2d26d4` |
| GitHub Release | https://github.com/0thernes/kochen-specker-extremal-lab/releases/tag/v1.8.0 |
| Frozen Archived PDF | `papers/0TH-2026-004_kochen-specker-extremal-lab/ks-minimum.pdf` |
| Frozen PDF SHA-256 | `0877cee7436a21ab9c579e174c01c4961b32576141b4df9c195d54b9d3cb43b6` |
| arXiv / Source Bundle SHA-256 | `1e6d40ab2533ef8a07a3b0c1655d3352e11ec1f15d17ae6e9049efbc30d90907` |
| CI Verification Run | https://github.com/0thernes/kochen-specker-extremal-lab/actions/runs/45516972182 |
| Software Heritage SWHID | `swh:1:snp:5a8db3249ec69c37f3c415913fc62f51d800cafb` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Certifies exact minimum Kochen-Specker set sizes inside finite coordinate pools: 31 in 3D integer pools (|c|<=2,3,4), 33 in 3D N-th roots of unity (N=6,12,18,24), 18 in 4D {0,+1,-1}, and 29 in 5D {0,+1,-1}, using Lean 4 proofs and independently checked DRUP unsatisfiability certificates.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 (zero Mathlib, 30 explicit #print axioms + exhaustive 149-theorem Lean.collectAxioms audit in KS/Audit.lean, 6 independent kernels via lake comparator --paranoid in repository CI, Sigstore Rekor logIndex 4089101395)
- **Library Entry Point:** `lean/KS.lean`
- **Primary Axiom Audit Script:** `lean/KS/Audit.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/Solution.lean`

## Verification Boundary (Honest Epistemic Scope)

Bound-2 3D minimum (31) and 4D minimum (18), plus non-vacuity 30-ray and 17-ray witnesses, are kernel-checked in pure Lean 4.35.0 without Mathlib (exhaustive 149-theorem KS namespace axiom audit + 30 explicit #print axioms, 0 disallowed axioms) and replayed across 6 independent kernels (lean, leanchecker-paranoid, lean4lean, nanoda, con-leche, con-ron) via lake comparator --paranoid in CI (run 45516972182, Sigstore Rekor logIndex 4089101395; Release v1.8.0 Rekor logIndex 4089066116); zero-warning C11 DRUP/QGTL/QRNG engines pass ASan/LSan/UBSan, ruff finds 0 bugbears/SIM115 resource leaks in build scripts, Build Standard v1.1.0 scores 98.4% (63/64), and gitleaks reports zero leaks; larger pools rest on independently checked DRUP certificates. Explicitly notes the general unrestricted minimal-KS problem remains open.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/kochen-specker-extremal-lab/lean && lake build && lake env lean KS/Audit.lean && lake comparator --config comparator.json --paranoid
```
