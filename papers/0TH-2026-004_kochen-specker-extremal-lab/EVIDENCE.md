# Evidence & Falsification Dossier — `0TH-2026-004`

**Title:** Certified exact minima of Kochen-Specker sets inside coordinate pools: 31 and 33 rays in dimension three, 18 in dimension four, 29 in dimension five  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Quantum Foundations / Combinatorial Optimization  
**Version / Date:** `v1.7.0` (2026-11-24)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 repository CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/kochen-specker-extremal-lab |
| Pinned Git Submodule | `repos/kochen-specker-extremal-lab` @ `19805b6fb7e4816afaf6457c5993b74bda17b433` |
| GitHub Release | https://github.com/0thernes/kochen-specker-extremal-lab/releases/tag/v1.7.0 |
| Frozen Archived PDF | `papers/0TH-2026-004_kochen-specker-extremal-lab/ks-minimum.pdf` |
| Frozen PDF SHA-256 | `8c1b47a6e3fac9afa74efcb59e1f2f94d06af74ccabc9497d23fedf1f80f7d53` |
| arXiv / Source Bundle SHA-256 | `1e6d40ab2533ef8a07a3b0c1655d3352e11ec1f15d17ae6e9049efbc30d90907` |
| CI Verification Run | https://github.com/0thernes/kochen-specker-extremal-lab/actions/runs/45508431897 |
| Software Heritage SWHID | `swh:1:snp:0b0d9e6f2e47f0f16d7c4c0f6373d39f96220cb4` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Certifies exact minimum Kochen-Specker set sizes inside finite coordinate pools: 31 in 3D integer pools (|c|<=2,3,4), 33 in 3D N-th roots of unity (N=6,12,18,24), 18 in 4D {0,+1,-1}, and 29 in 5D {0,+1,-1}, using Lean 4 proofs and independently checked DRUP unsatisfiability certificates.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 (zero Mathlib, 30 explicit #print axioms + exhaustive 149-theorem Lean.collectAxioms audit in KS/Audit.lean, 6 independent kernels via lake comparator --paranoid in repository CI, Sigstore Rekor logIndex 4088100409)
- **Library Entry Point:** `lean/KS.lean`
- **Primary Axiom Audit Script:** `lean/KS/Audit.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/Solution.lean`

## Verification Boundary (Honest Epistemic Scope)

Bound-2 3D minimum (31) and 4D minimum (18), plus non-vacuity 30-ray and 17-ray witnesses, are kernel-checked in pure Lean 4.35.0 without Mathlib (exhaustive 149-theorem KS namespace axiom audit + 30 explicit #print axioms, 0 disallowed axioms) and replayed across 6 independent kernels (lean, leanchecker-paranoid, lean4lean, nanoda, con-leche, con-ron) via lake comparator --paranoid in CI (run 45508431897, Sigstore Rekor logIndex 4088100409; Release v1.7.0 Rekor logIndex 4088073090); zero-warning C11 DRUP/QGTL/QRNG engines pass ASan/LSan/UBSan, ruff finds 0 bugbears, and gitleaks reports zero leaks; larger pools rest on independently checked DRUP certificates. Explicitly notes the general unrestricted minimal-KS problem remains open.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/kochen-specker-extremal-lab/lean && lake build && lake env lean KS/Audit.lean && lake comparator --config comparator.json --paranoid
```
