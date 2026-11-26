# Evidence & Falsification Dossier — `0TH-2026-007`

**Title:** Formally Verified Biophysical Invariants, Multi-Language Differential Oracles, and Pre-Registered Monte Carlo Simulation of the Human Synaptic Bouton  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Computational Neuroscience / Biophysical Verification  
**Version / Date:** `v1.3.0` (2026-11-25)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 repository CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/human-synapse-bouton-lab |
| Pinned Git Submodule | `repos/human-synapse-bouton-lab` @ `06e0dcdd5fc4cb406e9fe21d260ff94b68a414d4` |
| GitHub Release | https://github.com/0thernes/human-synapse-bouton-lab/releases/tag/v1.3.0 |
| Frozen Archived PDF | `papers/0TH-2026-007_human-synaptic-bouton-verification/Donahue_2026_human_synaptic_bouton_verification.pdf` |
| Frozen PDF SHA-256 | `7fd56d4c0c3358663270effd7a4fce9bb280eb20bd82d22732b34f220b4d65ed` |
| arXiv / Source Bundle SHA-256 | `adc66d2e34b102733b20260404c9352717d2e324f409f726be4e301bd436a0e3` |
| CI Verification Run | https://github.com/0thernes/human-synapse-bouton-lab/actions/runs/45747272478 |
| Software Heritage SWHID | `swh:1:snp:8ef70f745fae4f91f040720b28e21560c73deffc` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | 10.5281/zenodo.24548051 |

## Core Result

Proves 24 elementary algebraic and discrete-dynamical biophysical invariants with explicit positive-domain guarantees across 6 synaptic domains in pure Lean 4.35.0 (incl. Hill n=4 vs. n=1 sigmoidal crossover T06, fixed-point Tsodyks-Markram STP bounds T07, Jahr-Stevens NMDAR Mg2+ unblock monotonicity T11, structural-induction multi-step vesicle conservation T13, and exact discrete ATP depletion hitting-time bound T15 certifying H3 depletion at t=3 s; 26 non-vacuity witnesses + 6 adversarial counterexamples in AdversarialChecks.lean; replayed across 6 independent kernels in CI run 45747272478 with live README axiom drift checking & interactive /blueprint/ DAG), validates TypeScript and Rust kernels against a 50-digit NaN/Inf-guarded mpmath oracle over 1,000 random inputs (0 mismatches within 1e-10), kills 6/6 core mutants, verifies 23/23 live Crossref citations (0 retractions), compiles with literal 0 LaTeX warnings, seals 47-artifact MANIFEST.sha256 with DigiCert RFC 3161 + OpenTimestamps + SLSA v4 attestations + Croissant 1.0 metadata, achieves 100.0% (79/79) Build Standard v1.1.0, confirms H1 & H2 (p_Holm=0.0005), and honestly reports pre-registered 40 Hz H3 refutation alongside exploratory 20 Hz H3b.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 (zero Mathlib, zero Classical.choice, 24 theorems + 26 non-vacuity witnesses + 6 adversarial counterexamples, 6 independent kernels via lake comparator --paranoid in CI run 45747272478, interactive /blueprint/ DAG)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/NonVacuity.lean, lean/AdversarialChecks.lean`

## Verification Boundary (Honest Epistemic Scope)

All 24 algebraic/inductive invariants, 26 concrete physiological witnesses, and 6 adversarial counterexample checks are 100% kernel-checked in pure Lean 4.35.0 (zero sorry, zero Classical.choice, zero _native) across 6 independent kernels in CI; RK4 Hodgkin-Huxley ODE and ChaCha8Rng Monte Carlo trajectories are explicitly labeled numerical_approximation; pre-registered H3 (40 Hz) is reported as refuted and H3b (20 Hz) as post-hoc exploratory. Software Heritage v1.3.0 snapshot awaits browser PoW (prior v1.2.0 SWHID preserved).

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/human-synapse-bouton-lab/lean && lake build --wfail && lake env lean VerifyAxioms.lean && lake env leanchecker Solution && lake env leanchecker NonVacuity && lake env leanchecker AdversarialChecks && cd .. && npm ci && npm run build && npm test && cargo test --locked && uv run pytest -v python/tests/ && uv run python scripts/check_readme_axioms.py
```
