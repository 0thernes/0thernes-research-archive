# Evidence & Falsification Dossier — `0TH-2026-002`

**Title:** Spectral bounds and their limits in Pauli contextuality: exact configurations and a proof of Jonah's Conjecture E  
**Author:** Alexander Stephen Donahue (0thernes LLC, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Quantum Foundations / Quantum Contextuality  
**Version / Date:** `v1.5.0` (2026-11-21)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; listed on ORCID)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/hoggar-bound-lab |
| Pinned Git Submodule | `repos/hoggar-bound-lab` @ `5d4f48901812b0265d292ba5db7b76eba657e5a7` |
| GitHub Release | https://github.com/0thernes/hoggar-bound-lab/releases/tag/v1.5.0 |
| Frozen Archived PDF | `papers/0TH-2026-002_hoggar-bound-lab/unified-contextuality.pdf` |
| Frozen PDF SHA-256 | `89532166e85088b98b157d5521785955c501f1b75e33f53e4d199a4ce58ea203` |
| arXiv / Source Bundle SHA-256 | `5ce9058b78640a2ecadeac8c1259b67f9dd3d0764594a15b77b05d5a94849a73` |
| CI Verification Run | https://github.com/0thernes/hoggar-bound-lab/actions/runs/44888403135 |
| Software Heritage SWHID | `swh:1:snp:eae8dd29885ec4075b4a30e2edac1fea28d9d998` |
| Wayback Machine Snapshot | https://web.archive.org/web/20261110150849/https://0thernes.github.io/hoggar-bound-lab/paper/unified-contextuality.pdf?v=1.4.0 |
| External DOI | None claimed |

## Core Result

Unified study with complete Lean 4.35.0 formalizations of the spectral floor, Theorem 2 (Kramers / quaternionic floor and elliptic quadrics Q-(2N-1,2)), Theorems 3-4 (5-way saturation equivalences and (2^N-1)|S| = square), exact contextuality degrees (75, 480, 729344) for 4-, 5-, and 7-qubit configurations, a four-qubit cospectral C3 pair with distinct completion spectra, Lemmas 20-21 (Jordan restriction and universal cubic-trace identity), and Theorem 19: a full machine-checked Lean 4 proof of Jonah's Conjecture E across all nine vertex cases (C1, C3, C5, C6, C8, C11, C12, C14, C15) for every N >= 4.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 / Mathlib v4.35.0
- **Library Entry Point:** `lean/HoggarBound.lean`
- **Primary Axiom Audit Script:** `lean/VerifyNewFormalizations.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/C3Verification.lean, lean/IndependentVerification.lean, lean/SaturatedVerification.lean, lean/SaturatedSevenVerification.lean, lean/StabilityVerification.lean`

## Preserved Component Manuscripts (Historical Provenance)

- **A machine-checked spectral floor for Pauli contextuality, and new configurations that attain it** (`v1.1.0 / v1.1.1`, `paper/spectral-floor.pdf`): Historical source study folded into unified-contextuality.pdf (not a separate journal submission).
- **Cospectral Pauli carriers with different completion spectra: an exact four-qubit C3 certificate** (`v0.2.0-c3-certificate`, `paper/c3-spectral-counterexample.pdf`): Historical 42-declaration C3 study folded into unified-contextuality.pdf.
- **A verified spectral bound for Pauli contextuality: independent validation and critical synthesis** (`v0.1.0-independent-verification`, `paper/independent-research-note.pdf`): Historical independent validation companion folded into unified-contextuality.pdf.

## Verification Boundary (Honest Epistemic Scope)

As of v1.5.0, the spectral floor, Kramers quaternionic floor, 5-way saturation equivalences, saturated configurations, four-qubit C3 certificate, all-qubit C3 family, Lemmas 20-21, and Theorem 19 (Jonah's Conjecture E in all 9 vertex cases for every N >= 4) are all kernel-checked in Lean 4.35.0 with zero sorry, zero native_decide, and strictly standard axioms [propext, Classical.choice, Quot.sound]. Historical source manuscripts remain preserved inside the repository as component records of this single combined study (see publication/PAPER-MAP.md).

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/hoggar-bound-lab/lean && lake build HoggarBound.Kramers HoggarBound.SaturationTheory HoggarBound.ConjectureE && lake env lean VerifyNewFormalizations.lean && cd .. && bash scripts/run_all.sh
```
