# Evidence & Falsification Dossier — `0TH-2026-008`

**Title:** Open Hard Problems Across Eleven Neuro-Scientific Disciplines, Deductive-Inductive-Abductive Frontiers of Sentience, and a Six-Class Forensic Audit  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Interdisciplinary Neuroscience / Philosophy of Mind / Open Problems  
**Version / Date:** `v1.3.0` (2026-11-25)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 2x2 algebraic factorization bounds Lean 4.35.0 repository CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/human-synapse-bouton-lab |
| Pinned Git Submodule | `repos/human-synapse-bouton-lab` @ `06e0dcdd5fc4cb406e9fe21d260ff94b68a414d4` |
| GitHub Release | https://github.com/0thernes/human-synapse-bouton-lab/releases/tag/v1.3.0 |
| Frozen Archived PDF | `papers/0TH-2026-008_open-hard-problems-consciousness-frontier/Donahue_2026_open_hard_problems_consciousness_frontier.pdf` |
| Frozen PDF SHA-256 | `13e9a949f6541844d31769e87e591f9ed0ae80afb9b455322663d066482f301d` |
| arXiv / Source Bundle SHA-256 | `bdd27fca048f13640c45058e42917f07d68072aca446ce72ccef66488fbf5036` |
| CI Verification Run | https://github.com/0thernes/human-synapse-bouton-lab/actions/runs/45747272478 |
| Software Heritage SWHID | `swh:1:snp:8ef70f745fae4f91f040720b28e21560c73deffc` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | 10.5281/zenodo.24548051 |

## Core Result

Synthesizes an explicit 11-discipline open-problems roadmap (Math, Physics, Chemistry, Biology, Neuroscience, Neuropsychology, NeuroCS, NeuroMath, Neurochemistry, Neurobiology, Neurophysics), publishes an honest ID-by-ID crosswalk against all 1,900 entries of 0thernes/unsolved-problems-mega-atlas (explicitly reporting 0 / 1,900 grand open problems solved while mapping verified partial bounds across 18 high-CSS Atlas IDs), formally proves exact 2x2 weight-table algebraic factorization (= 0), diagonal product dominance (> 0), and diagonal excess implication (T22-T24) paired with a machine-proved common-cause counterexample (A05 in AdversarialChecks.lean) across 6 CI kernels, compiles with literal 0 LaTeX warnings, resolves 21 DOIs on Crossref (one, xu2016dnaorigami, points to an unrelated paper; titles and authors are not compared; the retraction check does not read Crossref updated-by), and records 3-cycle forensic hardening findings (F01-F34) across HARDENING_LOG.md and ERRATA.md.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 (zero Mathlib, zero Classical.choice, 24 theorems + 26 non-vacuity witnesses + 6 adversarial counterexamples incl. A05 common-cause counterexample, 6 independent kernels via lake comparator --paranoid in CI run 45747272478)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/NonVacuity.lean, lean/AdversarialChecks.lean`

## Verification Boundary (Honest Epistemic Scope)

Explicitly reports 0 / 1,900 Mega-Atlas open problems solved. Formal Lean 4 theorems T22-T24 apply strictly to observational 2x2 integer weight-table algebraic factorization determinants and (as machine-proved by counterexample A05) explicitly do NOT prove interventional causal disconnection under latent common causes, phenomenal consciousness, subjective experience, or sentience.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/human-synapse-bouton-lab/lean && lake build --wfail && lake env lean VerifyAxioms.lean && lake env leanchecker Solution && lake env leanchecker AdversarialChecks
```
