# Evidence & Falsification Dossier — `0TH-2026-008`

**Title:** Open Hard Problems Across Eleven Neuro-Scientific Disciplines, Deductive-Inductive-Abductive Frontiers of Sentience, and a Six-Class Forensic Audit  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Interdisciplinary Neuroscience / Philosophy of Mind / Open Problems  
**Version / Date:** `v1.2.0` (2026-11-23)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 2x2 algebraic factorization bounds Lean 4.35.0 repository CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/human-synapse-bouton-lab |
| Pinned Git Submodule | `repos/human-synapse-bouton-lab` @ `4539a48c362e473a91f4b2d7c610962e04878b1a` |
| GitHub Release | https://github.com/0thernes/human-synapse-bouton-lab/releases/tag/v1.2.0 |
| Frozen Archived PDF | `papers/0TH-2026-008_open-hard-problems-consciousness-frontier/Donahue_2026_open_hard_problems_consciousness_frontier.pdf` |
| Frozen PDF SHA-256 | `6e744f44ed9b54a05eb87493e7e0c96b011067bbb1bbd6b5988c60850eea2fc7` |
| arXiv / Source Bundle SHA-256 | `a51f1cc281ab6498c9a4b4c328def96f29a17f986b4ea8f78dd778e2486cec5f` |
| CI Verification Run | https://github.com/0thernes/human-synapse-bouton-lab/actions/runs/45277848703 |
| Software Heritage SWHID | `swh:1:snp:8ef70f745fae4f91f040720b28e21560c73deffc` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | 10.5281/zenodo.24484350 |

## Core Result

Synthesizes an explicit 11-discipline open-problems roadmap (Math, Physics, Chemistry, Biology, Neuroscience, Neuropsychology, NeuroCS, NeuroMath, Neurochemistry, Neurobiology, Neurophysics), formally proves exact 2x2 weight-table algebraic factorization (= 0) vs. strict diagonal product dominance (> 0) bounds (T17-T18) in Lean 4.35.0 (6 kernels in repository CI), verifies 23/23 bibliography citations live against Crossref (0 retractions), builds a deductive/inductive/abductive epistemic matrix for consciousness and sentience frontiers, and records a unified six-class forensic audit (F01-F10 core + F11-F20 hardening) synchronized across code, tests, web UI, ERRATA.md, and manuscript.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 (zero Mathlib, positive-domain hardened, 6 independent kernels via lake comparator --paranoid in repository CI)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/NonVacuity.lean`

## Verification Boundary (Honest Epistemic Scope)

Formal Lean 4 theorems T17-T18 apply strictly to observational 2x2 integer weight-table algebraic factorization determinants and explicitly do NOT prove interventional causal disconnection under latent common causes, geometric nanocolumn-to-weight derivations, phenomenal consciousness, subjective experience, or sentience; all philosophical and empirical cross-disciplinary gaps remain explicitly labeled open.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/human-synapse-bouton-lab/lean && lake build --wfail && lake env lean VerifyAxioms.lean && lake env leanchecker Solution
```
