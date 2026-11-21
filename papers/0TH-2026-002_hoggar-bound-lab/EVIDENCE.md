# Evidence & Falsification Dossier — `0TH-2026-002`

**Title:** Spectral bounds and their limits in Pauli contextuality: exact configurations and a proof of Jonah's Conjecture E  
**Author:** Alexander Stephen Donahue (0thernes LLC, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Quantum Foundations / Quantum Contextuality  
**Version / Date:** `v1.4.0` (2026-11-10)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; listed on ORCID)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/hoggar-bound-lab |
| Pinned Git Submodule | `repos/hoggar-bound-lab` @ `2149cbfc5475efbd8e791547ddd9b040954cb8ed` |
| GitHub Release | https://github.com/0thernes/hoggar-bound-lab/releases/tag/v1.4.0 |
| Frozen Archived PDF | `papers/0TH-2026-002_hoggar-bound-lab/unified-contextuality.pdf` |
| Frozen PDF SHA-256 | `89532166e85088b98b157d5521785955c501f1b75e33f53e4d199a4ce58ea203` |
| arXiv / Source Bundle SHA-256 | `5ce9058b78640a2ecadeac8c1259b67f9dd3d0764594a15b77b05d5a94849a73` |
| CI Verification Run | https://github.com/0thernes/hoggar-bound-lab/actions/runs/42834831332 |
| Software Heritage SWHID | `swh:1:snp:eae8dd29885ec4075b4a30e2edac1fea28d9d998` |
| Wayback Machine Snapshot | https://web.archive.org/web/20261110150849/https://0thernes.github.io/hoggar-bound-lab/paper/unified-contextuality.pdf?v=1.4.0 |
| External DOI | None claimed |

## Core Result

Unified study combining Lean 4 verification of the spectral floor, exact contextuality degrees (75, 480, 729344) for new 4-, 5-, and 7-qubit configurations, a four-qubit cospectral C3 pair with distinct completion spectra, an all-qubit (N >= 4) Lean-checked C3 family, and a self-contained proof settling all nine vertex cases of Jonah's Conjecture E.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0
- **Library Entry Point:** `lean/HoggarBound.lean`
- **Axiom Audit Script:** `lean/C3Verification.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`

## Verification Boundary (Honest Epistemic Scope)

Spectral floor, saturated configurations, and all-qubit C3 family are kernel-checked in Lean 4; non-C3 vertex cases of Conjecture E have self-contained paper proofs checked by exact computation and seven automated adversarial review passes.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/hoggar-bound-lab && bash scripts/run_all.sh
```
