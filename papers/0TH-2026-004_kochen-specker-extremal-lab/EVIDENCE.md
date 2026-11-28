# Evidence & Falsification Dossier — `0TH-2026-004`

**Title:** Certified exact minima of Kochen-Specker sets inside coordinate pools: 31 and 33 rays in dimension three, 18 in dimension four, 29 in dimension five  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Quantum Foundations / Combinatorial Optimization  
**Version / Date:** `v2.3.0` (2026-11-27)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 repository CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/kochen-specker-extremal-lab |
| Pinned Git Submodule | `repos/kochen-specker-extremal-lab` @ `d2ebab5ec0161504eccac1fbacca9e561ae0bc66` |
| GitHub Release | https://github.com/0thernes/kochen-specker-extremal-lab/releases/tag/v2.3.0 |
| Frozen Archived PDF | `papers/0TH-2026-004_kochen-specker-extremal-lab/ks-minimum.pdf` |
| Frozen PDF SHA-256 | `41a02bb957936b2f06b2f0c368b0824f97989405c7cfc85e28b3cde5796601a8` |
| arXiv / Source Bundle SHA-256 | `927e983c6b172917a2abb36e14ce6a0ae3e5c080841ad8308f623caf5e41999a` |
| CI Verification Run | https://github.com/0thernes/kochen-specker-extremal-lab/actions/runs/46055062154 |
| Software Heritage SWHID | `swh:1:snp:4c421f5d8b6cf9d06c224ed7bfafe88bc3392f4f` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | 10.5281/zenodo.24618610 |

## Core Result

Certifies exact minimum Kochen-Specker set sizes inside finite coordinate pools: 31 in 3D integer pools (|c|<=2,3,4), 33 in 3D N-th roots of unity (N=6,12,18,24), 18 in 4D {0,+1,-1}, and 29 in 5D {0,+1,-1}, with zero-Mathlib Lean 4 kernel proofs for the |c|<=2 pool (31) and the 4D pool (18) (including bidirectional KS.isColoringBool_iff soundness/completeness, strengthened explicit-basis + 0/1-colouring non-vacuity, and kernel-proved false-variant refutations); the other seven values rest on SAT unsatisfiability proofs checked by verify/drup_check (cross-checked in Linux CI by pinned drat-trim -> LRAT -> lrat-check and HOL4-formally-verified cake_lpr across 11 UNSAT/uniqueness proofs spanning 6 of 9 pools and ALL 3 dimensions d in {3,4,5}: B(3,2) k=30 & k=31 uniq, B(4,1) k=17 & k=18 uniq, B(3,3) k=30 & k=31 uniq, U(3,6) k=32 & k=33 uniq, U(3,12) k=32 & k=33 uniq, and 5D B(5,1) branch in:0,1,2;out:3,4 k=28), a CNF encoder, and paper lemmas.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 (zero Mathlib, 9/9 Palomar module headers, zero-warning lake build --wfail KS Solution, bidirectional soundness & completeness KS.isColoringBool_iff promoted as Comparator Target 7, 38 explicit #print axioms + 126-theorem-constant Lean.collectAxioms audit in module mode [71 hand-written theorems] in KS/Audit.lean, live CI tamper-injection negative gate, independent lake env leanchecker --fresh Solution, strengthened K1 explicit-basis + 0/1-colouring non-vacuity & K2 kernel-proved false-variant refutations, and 7 comparator targets checked by official Lean kernel (default & paranoid) + lean4lean, nanoda, con-leche, con-ron via lake comparator --paranoid in CI run 46055062154, SLSA attestation #73248201; Release v2.3.0 run 46055716324 SLSA #73248523)
- **Library Entry Point:** `lean/KS.lean`
- **Primary Axiom Audit Script:** `lean/KS/Audit.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/Solution.lean`

## Verification Boundary (Honest Epistemic Scope)

Bound-2 3D minimum (31) and 4D minimum (18), bidirectional soundness & completeness KS.isColoringBool_iff, strengthened K1 non-vacuity theorems (requiring an explicit complete d-ray orthogonal basis inside T plus an explicit 0/1 colouring via KS.isColoringBool), and K2 kernel-proved false-variant refutations (refute_box3h2_all_31_colorable, refute_box4h1_all_18_colorable) are kernel-checked in pure Lean 4.35.0 without Mathlib with 9/9 Palomar module headers under zero-warning lake build --wfail KS Solution (38 explicit #print axioms + 126-theorem-constant KS namespace axiom audit [71 hand-written], 0 disallowed axioms), guarded by a live CI tamper-injection negative gate, replayed independently by lake env leanchecker --fresh Solution, and all 7 comparator targets plus their dependency closure passed 6 independent kernel runs (official Lean default and paranoid, lean4lean, nanoda, con-leche, con-ron) via lake comparator --paranoid in CI (run 46055062154, SLSA #73248201; Release v2.3.0 run 46055716324, SLSA #73248523). Trigger T2 independent UNSAT proof checkers (pinned marijnheule/drat-trim 2e3b2dc -> LRAT -> lrat-check + HOL4-formally-verified tanyongkiam/cake_lpr 033aad5 confirming s VERIFIED UNSAT + truncated-LRAT negative control on both checkers) cross-verify 11 UNSAT/uniqueness proofs across 6 pools spanning ALL 3 dimensions d in {3,4,5} live in Linux CI (B(3,2), B(4,1), B(3,3), U(3,6), U(3,12), and 5D B(5,1) branch in:0,1,2;out:3,4 k=28; B(3,4), U(3,18), U(3,24), and the remaining 82 5D branches rest on verify/drup_check). data/MANIFEST.sha256 is freshly timestamped by DigiCert RFC 3161 TSA (.tsr, OpenSSL X.509 Verification: OK in CI) and 3-calendar Bitcoin OpenTimestamps (.ots), Software Heritage full snapshot swh:1:snp:4c421f5d8b6cf9d06c224ed7bfafe88bc3392f4f (v2.2.0; fresh v2.3.0 Save Code Now gated by Anubis PoW), zero-warning C11 ASan/LSan/UBSan engines, 59/59 Node checks, 128 Python tests (incl. 6/6 AST source-code mutants killed), 33/33 Crossref DOIs (0 retractions), 0.00pt overfull PDF, and Build Standard v1.2.0 98.4% (63/64, A24 partial for pinned >5 MB cut-certificate JSON). Unrestricted minimal-KS in R^3 (QM-011) remains open.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/kochen-specker-extremal-lab && python scripts/stamp_timestamps.py --verify && bash scripts/verify_lrat.sh && cd lean && lake build --wfail KS Solution && lake env lean KS/Audit.lean && lake env leanchecker --fresh Solution && lake comparator --config comparator.json --paranoid
```
