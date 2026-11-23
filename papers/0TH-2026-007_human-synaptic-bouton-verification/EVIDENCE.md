# Evidence & Falsification Dossier — `0TH-2026-007`

**Title:** Formally Verified Biophysical Invariants, Multi-Language Differential Oracles, and Pre-Registered Monte Carlo Simulation of the Human Synaptic Bouton  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Computational Neuroscience / Biophysical Verification  
**Version / Date:** `v1.0.0` (2026-11-23)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/human-synapse-bouton-lab |
| Pinned Git Submodule | `repos/human-synapse-bouton-lab` @ `6bdb7d5d0517cbf154f599e981cdf77b58ff9f15` |
| GitHub Release | https://github.com/0thernes/human-synapse-bouton-lab/releases/tag/v1.0.0 |
| Frozen Archived PDF | `papers/0TH-2026-007_human-synaptic-bouton-verification/Donahue_2026_human_synaptic_bouton_verification.pdf` |
| Frozen PDF SHA-256 | `4ef364f105162e5bf21facbb80483be687b2d2d4641a19ccdffc9823163b1170` |
| arXiv / Source Bundle SHA-256 | `e42fa09b656a08b68fd0d0ac0e01a1b29706a35e5d0ee3d6e722165ec8fe667b` |
| CI Verification Run | https://github.com/0thernes/human-synapse-bouton-lab/actions/runs/45218417682 |
| Software Heritage SWHID | `swh:1:snp:1a278fff55465dbe8d0b870408b6468822eb3e8b` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Proves 18 exact algebraic biophysical invariants across 6 synaptic domains in pure Lean 4.35.0 (replayed by 6 independent kernels: lean, leanchecker-paranoid, lean4lean, nanoda, con-leche, con-ron), validates TypeScript and Rust kernels against a 50-digit mpmath oracle over 1,000 random inputs (0 mismatches within 1e-10), confirms pre-registered nanocolumn and Ca2+ nanodomain hypotheses (p_Holm=0.0005), and honestly refutes pre-registered 40 Hz mitochondrial ATP sustainability (burn 1,284,000 > supply 950,000 ATP/s; f_crit=29.5625 Hz).

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 (zero Mathlib, 6 independent kernels via lake comparator --paranoid)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/NonVacuity.lean`

## Verification Boundary (Honest Epistemic Scope)

The 18 algebraic invariants and 19 non-vacuity witnesses are 100% kernel-checked in pure Lean 4.35.0 (zero sorry, zero Classical.choice); RK4 Hodgkin-Huxley ODE and ChaCha8Rng Monte Carlo trajectories are explicitly labeled numerical_approximation; pre-registered H3 (40 Hz) is reported as refuted and H3b (20 Hz) as post-hoc exploratory.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/human-synapse-bouton-lab/lean && lake build --wfail && lake env lean VerifyAxioms.lean && lake env leanchecker Solution && cd .. && npm ci && npm run build && npm test && cargo test --locked && uv run pytest -v python/tests/
```
