# Evidence & Falsification Dossier — `0TH-2026-004`

**Title:** Certified exact minima of Kochen-Specker sets inside coordinate pools: 31 and 33 rays in dimension three, 18 in dimension four, 29 in dimension five  
**Author:** Alexander Stephen Donahue (0thernes LLC, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Quantum Foundations / Combinatorial Optimization  
**Version / Date:** `v1.0.0` (2026-11-10)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/kochen-specker-extremal-lab |
| Pinned Git Submodule | `repos/kochen-specker-extremal-lab` @ `38108d26776a3356e56fe54b6338902602bf31e1` |
| GitHub Release | https://github.com/0thernes/kochen-specker-extremal-lab/releases/tag/v1.0.0 |
| Frozen Archived PDF | `papers/0TH-2026-004_kochen-specker-extremal-lab/ks-minimum.pdf` |
| Frozen PDF SHA-256 | `8063949e478c41b93913bfd9ff39b2d598c07ed7f0e539af300aa7375f5ae967` |
| arXiv / Source Bundle SHA-256 | `1e6d40ab2533ef8a07a3b0c1655d3352e11ec1f15d17ae6e9049efbc30d90907` |
| CI Verification Run | https://github.com/0thernes/kochen-specker-extremal-lab/actions/runs/42811596518 |
| Software Heritage SWHID | `Pending manual Save Code Now` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Certifies exact minimum Kochen-Specker set sizes inside finite coordinate pools: 31 in 3D integer pools (|c|<=2,3,4), 33 in 3D N-th roots of unity (N=6,12,18,24), 18 in 4D {0,+1,-1}, and 29 in 5D {0,+1,-1}, using Lean 4 proofs and independently checked DRUP unsatisfiability certificates.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4 (zero Mathlib)
- **Library Entry Point:** `lean/KS.lean`
- **Primary Axiom Audit Script:** `lean/KS/Audit.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`

## Verification Boundary (Honest Epistemic Scope)

Bound-2 3D minimum (31) and 4D minimum (18) are kernel-checked in pure Lean 4 without Mathlib; larger pools rest on independently checked DRUP certificates. Explicitly notes the general unrestricted minimal-KS problem remains open.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/kochen-specker-extremal-lab/lean && lake build && lake env lean KS/Audit.lean
```
