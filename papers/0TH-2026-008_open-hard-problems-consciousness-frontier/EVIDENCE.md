# Evidence & Falsification Dossier — `0TH-2026-008`

**Title:** Open Hard Problems Across Eleven Neuro-Scientific Disciplines, Deductive-Inductive-Abductive Frontiers of Sentience, and a Six-Class Forensic Audit  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Interdisciplinary Neuroscience / Philosophy of Mind / Open Problems  
**Version / Date:** `v1.1.2` (2026-11-23)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; algebraic coupling bounds Lean 4.35.0 & Palomar CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/human-synapse-bouton-lab |
| Pinned Git Submodule | `repos/human-synapse-bouton-lab` @ `dd2ec73793d341d26aaf9fe59f26d4d5519d2b37` |
| GitHub Release | https://github.com/0thernes/human-synapse-bouton-lab/releases/tag/v1.1.2 |
| Frozen Archived PDF | `papers/0TH-2026-008_open-hard-problems-consciousness-frontier/Donahue_2026_open_hard_problems_consciousness_frontier.pdf` |
| Frozen PDF SHA-256 | `a4e2bc65b181e5593ab32bca27f00e84211ce8795a449eae83dad4df405af62f` |
| arXiv / Source Bundle SHA-256 | `8c5b730dab81f2b4ce1053eec36f2fe7d34bc7bc3872a973aa7653507cff51ad` |
| CI Verification Run | https://github.com/0thernes/human-synapse-bouton-lab/actions/runs/45245761763 |
| Software Heritage SWHID | `swh:1:snp:d922faec88e60f6f950f98eb6572b55f7b450bc7` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | 10.5281/zenodo.24478612 |

## Core Result

Synthesizes an explicit 11-discipline open-problems roadmap (Math, Physics, Chemistry, Biology, Neuroscience, Neuropsychology, NeuroCS, NeuroMath, Neurochemistry, Neurobiology, Neurophysics), formally proves discrete bipartite non-factorizability vs. zero-integration boundaries (T17-T18) in Lean 4.35.0 (Palomar module headers, 6 kernels, Palomar CI pass 45241561032), verifies 23/23 bibliography citations live against Crossref (0 retractions), builds a deductive/inductive/abductive epistemic matrix for consciousness and sentience frontiers, and records a unified six-class forensic audit (F01-F10 core + F11-F14 v1.1.2 sweep) synchronized across code, tests, web UI, ERRATA.md, and manuscript.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 (zero Mathlib, Palomar module headers, 6 independent kernels via lake comparator --paranoid)
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
