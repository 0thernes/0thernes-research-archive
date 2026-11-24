# Evidence & Falsification Dossier — `0TH-2026-004`

**Title:** Certified exact minima of Kochen-Specker sets inside coordinate pools: 31 and 33 rays in dimension three, 18 in dimension four, 29 in dimension five  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Quantum Foundations / Combinatorial Optimization  
**Version / Date:** `v1.2.0` (2026-11-24)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 repository CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/kochen-specker-extremal-lab |
| Pinned Git Submodule | `repos/kochen-specker-extremal-lab` @ `4a40f7f7f0ecc55a046cf351753ddd38e716c1c0` |
| GitHub Release | https://github.com/0thernes/kochen-specker-extremal-lab/releases/tag/v1.2.0 |
| Frozen Archived PDF | `papers/0TH-2026-004_kochen-specker-extremal-lab/ks-minimum.pdf` |
| Frozen PDF SHA-256 | `5a8166089748df3aa4d24f18a7f1df06a0d97bf97362e83a9b336d3106dccdf0` |
| arXiv / Source Bundle SHA-256 | `1e6d40ab2533ef8a07a3b0c1655d3352e11ec1f15d17ae6e9049efbc30d90907` |
| CI Verification Run | https://github.com/0thernes/kochen-specker-extremal-lab/actions/runs/45376573629 |
| Software Heritage SWHID | `swh:1:snp:27559be8090327ecbc1a0213ad8c1116be34e7f7` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Certifies exact minimum Kochen-Specker set sizes inside finite coordinate pools: 31 in 3D integer pools (|c|<=2,3,4), 33 in 3D N-th roots of unity (N=6,12,18,24), 18 in 4D {0,+1,-1}, and 29 in 5D {0,+1,-1}, using Lean 4 proofs and independently checked DRUP unsatisfiability certificates.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 (zero Mathlib, 6 independent kernels via lake comparator --paranoid in repository CI)
- **Library Entry Point:** `lean/KS.lean`
- **Primary Axiom Audit Script:** `lean/KS/Audit.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/Solution.lean`

## Verification Boundary (Honest Epistemic Scope)

Bound-2 3D minimum (31) and 4D minimum (18), plus non-vacuity 30-ray and 17-ray witnesses, are kernel-checked in pure Lean 4.35.0 without Mathlib and replayed across 6 independent kernels (lean, leanchecker-paranoid, lean4lean, nanoda, con-leche, con-ron) via lake comparator --paranoid in CI; larger pools rest on independently checked DRUP certificates. Upgraded to Apache-2.0 / CC-BY-4.0 and Build Standard v1.1.0 in v1.1.0. Explicitly notes the general unrestricted minimal-KS problem remains open.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/kochen-specker-extremal-lab/lean && lake build && lake env lean KS/Audit.lean && lake comparator --config comparator.json --paranoid
```
