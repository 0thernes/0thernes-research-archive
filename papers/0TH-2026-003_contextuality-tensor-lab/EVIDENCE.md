# Evidence & Falsification Dossier — `0TH-2026-003`

**Title:** Exact contextuality degrees for disjoint Mermin configurations  
**Author:** Alexander Stephen Donahue (0thernes LLC, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Quantum Foundations / Quantum Contextuality  
**Version / Date:** `v0.1.0` (2026-11-10)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/contextuality-tensor-lab |
| Pinned Git Submodule | `repos/contextuality-tensor-lab` @ `f7a1e6e74f8590d9cee0aa4c01f9ea3800f7fe87` |
| GitHub Release | https://github.com/0thernes/contextuality-tensor-lab/releases/tag/v0.1.0 |
| Frozen Archived PDF | `papers/0TH-2026-003_contextuality-tensor-lab/contextuality-tensor.pdf` |
| Frozen PDF SHA-256 | `2d0f0d2af4177a48d5691286b470b7b14d709646e1d1c4874ce04795408e8b6f` |
| arXiv / Source Bundle SHA-256 | `e7a592bbf563928246ae05e0bbba194cd7b8646a725c020ea61aa9f78ee2b054` |
| CI Verification Run | https://github.com/0thernes/contextuality-tensor-lab/actions/runs/42751584064 |
| Software Heritage SWHID | `swh:1:rev:de48ed9002e930825f1cf5f140c8dc8cbfdc1ea0` |
| Wayback Machine Snapshot | https://web.archive.org/web/20261110040209/https://0thernes.github.io/contextuality-tensor-lab/paper/contextuality-tensor.pdf |
| External DOI | None claimed |

## Core Result

Proves exact arbitrary-copy contextuality degree formulas d_k = (7^k - 5^k)/2 for k disjoint Peres-Mermin squares and (6^k - 4^k)/2 for k Mermin pentagrams under full nonempty-union context families, answering Section 6 of Muller & Saniga (arXiv:2609.19862v1).

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4
- **Library Entry Point:** `lean/ContextualityTensor.lean`
- **Primary Axiom Audit Script:** `lean/Verification.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`

## Verification Boundary (Honest Epistemic Scope)

Exact multiplicative identity and attaining assignments are machine-checked in Lean 4 (153-declaration axiom audit strictly within standard axioms), paired with independent Python and JavaScript exact enumeration.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/contextuality-tensor-lab/lean && lake build && lake env lean Verification.lean
```
