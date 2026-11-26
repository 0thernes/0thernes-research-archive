# Evidence & Falsification Dossier — `0TH-2026-004`

**Title:** Certified exact minima of Kochen-Specker sets inside coordinate pools: 31 and 33 rays in dimension three, 18 in dimension four, 29 in dimension five  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Quantum Foundations / Combinatorial Optimization  
**Version / Date:** `v1.9.0` (2026-11-25)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 repository CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/kochen-specker-extremal-lab |
| Pinned Git Submodule | `repos/kochen-specker-extremal-lab` @ `03c8910e5abce13b8dcfcb6974c69ca1fd709c8f` |
| GitHub Release | https://github.com/0thernes/kochen-specker-extremal-lab/releases/tag/v1.9.0 |
| Frozen Archived PDF | `papers/0TH-2026-004_kochen-specker-extremal-lab/ks-minimum.pdf` |
| Frozen PDF SHA-256 | `122e838544b75bef5cb7d23c5c6765938417ad798d4300b623eae8001aa47f72` |
| arXiv / Source Bundle SHA-256 | `c7e3342842679b19ac51ad713168e5641372e92a78288380fe24240b176f8aae` |
| CI Verification Run | https://github.com/0thernes/kochen-specker-extremal-lab/actions/runs/45741815040 |
| Software Heritage SWHID | `swh:1:snp:6df0f79e042201d9490512cc8dda65471db9fafb` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Certifies exact minimum Kochen-Specker set sizes inside finite coordinate pools: 31 in 3D integer pools (|c|<=2,3,4), 33 in 3D N-th roots of unity (N=6,12,18,24), 18 in 4D {0,+1,-1}, and 29 in 5D {0,+1,-1}, using Lean 4 proofs and independently checked DRUP unsatisfiability certificates.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 (zero Mathlib, 30 explicit #print axioms + exhaustive 149-theorem Lean.collectAxioms audit in KS/Audit.lean, independent lake env leanchecker --fresh Solution, 3 adversarial false-variant Lean refutations, and 6 independent kernels via lake comparator --paranoid in repository CI run 45741815040, Sigstore Rekor logIndex 4116355625)
- **Library Entry Point:** `lean/KS.lean`
- **Primary Axiom Audit Script:** `lean/KS/Audit.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/Solution.lean`

## Verification Boundary (Honest Epistemic Scope)

Bound-2 3D minimum (31) and 4D minimum (18), plus non-vacuity 30-ray and 17-ray witnesses, are kernel-checked in pure Lean 4.35.0 without Mathlib (exhaustive 149-theorem KS namespace axiom audit + 30 explicit #print axioms, 0 disallowed axioms), replayed independently by lake env leanchecker --fresh Solution, tested against 3 adversarial false-variant Lean refutations, and verified across 6 independent kernels (lean, leanchecker-paranoid, lean4lean, nanoda, con-leche, con-ron) via lake comparator --paranoid in CI (run 45741815040, Sigstore Rekor logIndex 4116355625; Release v1.9.0 run 45744236042 Rekor logIndex 4116572137); zero-warning C11 DRUP/QGTL/QRNG engines pass ASan/LSan/UBSan, 59/59 Node verifier checks pass, 33/33 Crossref DOIs have 0 retractions, ks-minimum.pdf compiles with literal 0.00pt overfull hboxes (with CRediT & ERRATA.md), Build Standard v1.2.0 (10 finding classes, Draft 2020-12 schema-valid repo.yaml) scores 98.4% (63/64, A24 honestly partial for 2 pinned cut-certificate JSONs >5 MB), and SHA-256-verified gitleaks v8.30.1 + osv-scanner v2.7.1 report zero leaks; larger pools rest on independently checked DRUP certificates. Explicitly notes the general unrestricted minimal-KS problem (QM-011) remains open (0/1,900 Mega-Atlas grand problems solved).

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/kochen-specker-extremal-lab/lean && lake build KS Solution && lake env lean KS/Audit.lean && lake env leanchecker --fresh Solution && lake comparator --config comparator.json --paranoid
```
