# Evidence & Falsification Dossier — `0TH-2026-005`

**Title:** Contextuality Evidence Lab: Exact Sequential Certificates and a Constructive Setting-Bias Attack  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Quantum Foundations / Statistical Hypothesis Testing  
**Version / Date:** `v1.0.0` (2026-11-10)  
**Status:** Research methods artifact & preprint (not peer reviewed; AI-assisted under human direction)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/contextuality-evidence-lab |
| Pinned Git Submodule | `repos/contextuality-evidence-lab` @ `ef0682cd24ca248c5e502731c462272a4ac93432` |
| GitHub Release | https://github.com/0thernes/contextuality-evidence-lab/releases/tag/v1.0.0 |
| Frozen Archived PDF | `papers/0TH-2026-005_contextuality-evidence-lab/whitepaper.pdf` |
| Frozen PDF SHA-256 | `8e34d2911a7cc5dc5a02176515364729118fe07cca54d8d9be16e4a818e95743` |
| arXiv / Source Bundle SHA-256 | `5024173ca403642b8f6d1a46b60ae44e432c2f0616470784d92c0d68f1bf9000` |
| CI Verification Run | https://github.com/0thernes/contextuality-evidence-lab/actions/runs/42815130874 |
| Software Heritage SWHID | `Pending manual Save Code Now` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Proves a finite adaptive-tree sequential contextuality evidence theorem and a sharp setting-bias bound for the Peres-Mermin square, constructing an explicit classical adversary causing a miscalibrated 1% test to reject 97.24% of the time while the bias-aware test stays below 1%.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4
- **Library Entry Point:** `lean/Evidence.lean`
- **Primary Axiom Audit Script:** `lean/Verification.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`

## Verification Boundary (Honest Epistemic Scope)

Adaptive-tree evidence bound, biased-setting classical cap (11/12), and counterexample are formally verified in Lean 4; paired with reproducible Moonlab/QGTL/QRNG/Eshkol simulation. Explicitly disclaims hardware contextuality or certified randomness. Superseded GitHub repository archived read-only on 2026-11-24 and consolidated into 0TH-2026-009 (0thernes/pauli-contextuality-lab); this historical snapshot remains cryptographically pinned.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/contextuality-evidence-lab/lean && lake build && lake env lean Verification.lean
```
