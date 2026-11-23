# Evidence & Falsification Dossier — `0TH-2026-008`

**Title:** Open Hard Problems Across Eleven Neuro-Scientific Disciplines, Deductive-Inductive-Abductive Frontiers of Sentience, and a Six-Class Forensic Audit  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Interdisciplinary Neuroscience / Philosophy of Mind / Open Problems  
**Version / Date:** `v1.0.0` (2026-11-23)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; algebraic coupling bounds Lean 4.35.0 verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/human-synapse-bouton-lab |
| Pinned Git Submodule | `repos/human-synapse-bouton-lab` @ `6bdb7d5d0517cbf154f599e981cdf77b58ff9f15` |
| GitHub Release | https://github.com/0thernes/human-synapse-bouton-lab/releases/tag/v1.0.0 |
| Frozen Archived PDF | `papers/0TH-2026-008_open-hard-problems-consciousness-frontier/Donahue_2026_open_hard_problems_consciousness_frontier.pdf` |
| Frozen PDF SHA-256 | `69fd84374eedd70f089daf02dffa48fbb63799db5fec32b6c0563b391d39005a` |
| arXiv / Source Bundle SHA-256 | `2beaacbfacc5d4f36562110211bddad15638ecd695cac725b656e32e0d6affb0` |
| CI Verification Run | https://github.com/0thernes/human-synapse-bouton-lab/actions/runs/45218417682 |
| Software Heritage SWHID | `swh:1:snp:1a278fff55465dbe8d0b870408b6468822eb3e8b` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Synthesizes an explicit 11-discipline open-problems roadmap (Math, Physics, Chemistry, Biology, Neuroscience, Neuropsychology, NeuroCS, NeuroMath, Neurochemistry, Neurobiology, Neurophysics), formally proves discrete bipartite non-factorizability vs. zero-integration boundaries (T17-T18) in Lean 4.35.0, builds a deductive/inductive/abductive epistemic matrix for consciousness and sentience frontiers, and records a complete six-class forensic audit (F01-F10) of bugs, errors, issues, problems, dilemmas, conflicts, and epistemic blind spots.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 (zero Mathlib, 6 independent kernels via lake comparator --paranoid)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/NonVacuity.lean`

## Verification Boundary (Honest Epistemic Scope)

Formal Lean 4 theorems T17-T18 apply solely to discrete finite-state bipartite coupling determinants and explicitly do NOT prove, measure, or detect phenomenal consciousness, subjective experience, or sentience; all philosophical and empirical cross-disciplinary gaps remain explicitly labeled open.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/human-synapse-bouton-lab/lean && lake build --wfail && lake env lean VerifyAxioms.lean && lake env leanchecker Solution
```
