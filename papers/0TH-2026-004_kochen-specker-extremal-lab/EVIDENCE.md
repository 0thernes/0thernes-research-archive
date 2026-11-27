# Evidence & Falsification Dossier — `0TH-2026-004`

**Title:** Certified exact minima of Kochen-Specker sets inside coordinate pools: 31 and 33 rays in dimension three, 18 in dimension four, 29 in dimension five  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Quantum Foundations / Combinatorial Optimization  
**Version / Date:** `v2.1.0` (2026-11-26)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 repository CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/kochen-specker-extremal-lab |
| Pinned Git Submodule | `repos/kochen-specker-extremal-lab` @ `888ee434e68f180e5fa397bcf64448b641a5fb99` |
| GitHub Release | https://github.com/0thernes/kochen-specker-extremal-lab/releases/tag/v2.1.0 |
| Frozen Archived PDF | `papers/0TH-2026-004_kochen-specker-extremal-lab/ks-minimum.pdf` |
| Frozen PDF SHA-256 | `24dea28431537fa3d5ff550b807061f142d62655e1d58c5da07655704e5cc9a7` |
| arXiv / Source Bundle SHA-256 | `0bfef1667f38d2efa334bdffa5361be10805fafd2912d4fb726fe80b9d5bf115` |
| CI Verification Run | https://github.com/0thernes/kochen-specker-extremal-lab/actions/runs/45939136064 |
| Software Heritage SWHID | `swh:1:snp:68ed4cd5af45b8fa4ed21a82f8f3dfd69ac901ae` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Certifies exact minimum Kochen-Specker set sizes inside finite coordinate pools: 31 in 3D integer pools (|c|<=2,3,4), 33 in 3D N-th roots of unity (N=6,12,18,24), 18 in 4D {0,+1,-1}, and 29 in 5D {0,+1,-1}, with Lean 4 kernel proofs for the |c|<=2 pool (31) and the 4D pool (18) only; the other seven values rest on SAT unsatisfiability proofs checked by the project's own DRUP checker (cross-checked by pinned drat-trim -> LRAT -> lrat-check and HOL4-formally-verified cake_lpr for |c|<=2, 4D and |c|<=3), a CNF encoder and paper lemmas.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 (zero Mathlib, 9/9 Palomar module headers, zero-warning lake build --wfail KS Solution, 30 explicit #print axioms + 116-theorem-constant Lean.collectAxioms audit in module mode (62 hand-written theorems) in KS/Audit.lean, independent lake env leanchecker --fresh Solution, 3 negative sanity checks (decide rejects pool sizes 48 and 39 and a wrong bit count), and official Lean kernel (default & paranoid) + lean4lean, nanoda, con-leche, con-ron via lake comparator --paranoid in repository CI run 45939136064, Sigstore Rekor logIndex 4141357381)
- **Library Entry Point:** `lean/KS.lean`
- **Primary Axiom Audit Script:** `lean/KS/Audit.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/Solution.lean`

## Verification Boundary (Honest Epistemic Scope)

Bound-2 3D minimum (31) and 4D minimum (18), plus two corollaries (the first 30 rays of B(3,2) and the first 17 rays of B(4,1) are colourable; the latter contain no basis), are kernel-checked in pure Lean 4.35.0 without Mathlib with 9/9 Palomar module headers under zero-warning lake build --wfail KS Solution (exhaustive 116-theorem-constant KS namespace axiom audit in module mode, 62 hand-written, + 30 explicit #print axioms, 0 disallowed axioms), replayed independently by lake env leanchecker --fresh Solution, tested against 3 negative sanity checks (decide rejects pool sizes 48 and 39 and a wrong bit count), and its 4 comparator targets and their dependency closure were checked by 6 kernel runs (official Lean default and paranoid, lean4lean, nanoda, con-leche, con-ron) via lake comparator --paranoid in CI (run 45939136064, Sigstore Rekor logIndex 4141357381; Release v2.1.0 run 45940283452 Rekor logIndex 4141517398). Trigger T2 independent UNSAT proof checkers (pinned marijnheule/drat-trim 2e3b2dc -> LRAT -> lrat-check + HOL4-formally-verified tanyongkiam/cake_lpr 033aad5 confirming s VERIFIED UNSAT + truncated-LRAT negative control on both checkers, SHA-256 verified) cross-verify B(3,2) k=30, B(4,1) k=17, and B(3,3) k=30 in Linux CI alongside verify/drup_check; the 2026-11-26 statement-audit errata P1-P6, O1-O4, K2, and K3 are closed in place. data/MANIFEST.sha256 is cryptographically timestamped by DigiCert RFC 3161 TSA (.tsr, OpenSSL X.509 DigiCert chain Verification: OK in CI) and 3-calendar Bitcoin OpenTimestamps (.ots); zero-warning C11 DRUP/QGTL/QRNG engines pass ASan/LSan/UBSan, 59/59 Node verifier checks pass, 12/12 Python integrity/fuzz/brute-force-CNF tests pass, mypy reports 0/47 errors, 33/33 Crossref DOIs have 0 retractions, ks-minimum.pdf compiles with literal 0.00pt overfull hboxes, author-automated zero-cache clean-clone replication passed (76.8s; external human replication remains open), and Build Standard v1.2.0 scores 98.4% (63/64, A24 honestly partial for pinned >5 MB cut-certificate JSON). Explicitly notes the general unrestricted minimal-KS problem (QM-011) remains open (0/1,900 Mega-Atlas grand problems solved).

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/kochen-specker-extremal-lab && python scripts/stamp_timestamps.py --verify && bash scripts/verify_lrat.sh && cd lean && lake build --wfail KS Solution && lake env lean KS/Audit.lean && lake env leanchecker --fresh Solution && lake comparator --config comparator.json --paranoid
```
