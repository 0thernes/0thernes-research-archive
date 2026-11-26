# Evidence & Falsification Dossier — `0TH-2026-001`

**Title:** A third-moment bound on the contextuality degree of multiqubit Pauli configurations  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Quantum Foundations / Quantum Contextuality  
**Version / Date:** `v1.0.0` (2026-11-09)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/hoggar-bound |
| Pinned Git Submodule | `repos/hoggar-bound` @ `c74135c429a0ef827c757df5fc76139aed62a819` |
| GitHub Release | https://github.com/0thernes/hoggar-bound/releases/tag/v1.0.0 |
| Frozen Archived PDF | `papers/0TH-2026-001_hoggar-bound/main.pdf` |
| Frozen PDF SHA-256 | `df01bbbd97f9d1d1a270d9e90b7cbbb848c8b449fe6107a54fd5b77bf764a1c3` |
| arXiv / Source Bundle SHA-256 | `35de9d7084f2e6704246c61070d2f45b8b25ac656abc9c8e01ec7180e4fbaa64` |
| CI Verification Run | Local verification (see repository) |
| Software Heritage SWHID | `Pending manual Save Code Now` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Proves a third-moment spectral lower bound on the contextuality degree of N-qubit Pauli configurations with a Kramers refinement for elliptic quadrics, attained on W(5,2) by the Hoggar SIC fiducial, with Lean 4 proofs, independent Python/C verification, and a Moonlab WASM demo.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4 / Mathlib
- **Library Entry Point:** `lean/HoggarBound.lean`
- **Primary Axiom Audit Script:** `lean/Audit/Axioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`

## Verification Boundary (Honest Epistemic Scope)

Core spectral bound and numerical corollaries are machine-checked in Lean 4; independent Python/C suites verify finite configurations; superseded/extended into the unified manuscript in 0TH-2026-002 (hoggar-bound-lab). Superseded GitHub repository archived read-only on 2026-11-24 and consolidated into 0TH-2026-009 (0thernes/pauli-contextuality-lab); this historical snapshot remains cryptographically pinned.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/hoggar-bound/lean && lake build && lake env lean Audit/Axioms.lean
```
