# Evidence & Falsification Dossier — `0TH-2026-009`

**Title:** Pauli Contextuality Lab: Unified Lean 4.35.0 Formalization of Spectral Bounds, Disjoint Mermin Configurations, and Sequential Contextuality Evidence  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Quantum Foundations / Quantum Contextuality  
**Version / Date:** `v2.2.0` (2026-11-24)  
**Status:** Consolidated research preprint suite (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 & cross-platform CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/pauli-contextuality-lab |
| Pinned Git Submodule | `repos/pauli-contextuality-lab` @ `9be258afbc1d27cb34f64a8d9a377d91d93da74a` |
| GitHub Release | https://github.com/0thernes/pauli-contextuality-lab/releases/tag/v2.2.0 |
| Frozen Archived PDF | `papers/0TH-2026-009_pauli-contextuality-lab/unified-contextuality.pdf` |
| Frozen PDF SHA-256 | `066dc7bf992769dc1d3934cd1df287fcfd183dec971985ae145f6a7fa1a50c64` |
| arXiv / Source Bundle SHA-256 | `N/A (canonical TeX sources in repo papers/spectral-bounds/unified-contextuality.tex & papers/disjoint-mermin/contextuality-tensor.tex)` |
| CI Verification Run | https://github.com/0thernes/pauli-contextuality-lab/actions/runs/45414259326 |
| Software Heritage SWHID | `swh:1:snp:b416e3a258b457d0f5819a61032f4032c5b524d2` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Consolidates the four archived Pauli/Mermin contextuality repositories (hoggar-bound, hoggar-bound-lab, contextuality-tensor-lab, contextuality-evidence-lab) into one unified Apache-2.0 / CC-BY-4.0 monorepo meeting Build Standard v1.1.0 (100.0%, 68/68 checks) with a single pinned Lean 4.35.0 + Mathlib v4.35.0 workspace, deduplicated third-party stack, interactive Lean Blueprint (/blueprint/), and 3-OS + C11 ASan/UBSan CI (run 45414259879). Track 1 proves the universal spectral floor, Kramers floor, 5-way saturation equivalences, exact degrees (75, 480, 2016, 729344), the infinite non-closed pure-CCZ determinant family |Psi_{3m}>, unconditional N=4..5 bounds d(W(7,2))>=1455 and d(Q+(9,2))>=6444, exact four-qubit C3 binary completion optima (368 vs 344, gap 24), and Jonah's Conjecture E across all 9 vertex cases for every N>=4. Track 2 proves exact arbitrary-k disjoint-copy formulas d_k=(7^k-5^k)/2 (squares) and (6^k-4^k)/2 (pentagrams) addressing Muller & Saniga (arXiv:2609.19862v1 Sec. 6). Track 3 proves finite adaptive-tree sequential evidence bounds and a sharp setting-bias attack on the Peres-Mermin square. All 12 unified comparator targets (43,860-43,863 transitive declarations) passed all 6 independent kernels (lean-paranoid, lean4lean, nanoda, con-leche, con-ron, lean-default) in CI run 45414259326 with Sigstore/Rekor attestation (logIndex 4076483377).

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 / Mathlib v4.35.0 (158 explicit #print axioms + exhaustive 1,920-theorem Lean.collectAxioms audit across HoggarBound, ContextualityTensor, Evidence, PauliContextualityLab; 0 Batteries linter errors; 12 headline targets verified across 6 independent kernels via lake comparator --paranoid in Ubuntu 24.04 CI)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAll.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/HoggarBound/NonVacuity.lean`

## Preserved Component Manuscripts (Historical Provenance)

- **Spectral bounds and their limits in Pauli contextuality: exact configurations and a proof of Jonah's Conjecture E (Track 1, v2.0.0)** (`v2.2.0 (consolidated from hoggar-bound-lab v1.9.0)`, `papers/spectral-bounds/unified-contextuality.pdf`): Primary archived PDF for 0TH-2026-009; recompiled with Tectonic under independent-researcher CC-BY-4.0 header.
- **Exact contextuality degrees for disjoint Mermin configurations (Track 2, v2.0.0)** (`v2.2.0 (consolidated from contextuality-tensor-lab v0.1.0)`, `papers/disjoint-mermin/contextuality-tensor.pdf`): Directly answers Section 6 of Muller & Saniga (arXiv:2609.19862v1); archived alongside Track 1 in papers/0TH-2026-009_pauli-contextuality-lab/contextuality-tensor.pdf.
- **Contextuality Evidence Lab: Exact Sequential Certificates and a Constructive Setting-Bias Attack (Track 3, v1.0.0)** (`v2.2.0 (consolidated from contextuality-evidence-lab v1.0.0)`, `papers/sequential-evidence/whitepaper.pdf`): Freshly typeset XeLaTeX/Tectonic PDF under independent-researcher CC-BY-4.0 header; archived in papers/0TH-2026-009_pauli-contextuality-lab/whitepaper.pdf.

## Verification Boundary (Honest Epistemic Scope)

158 explicit headline declarations plus an exhaustive 1,920-theorem Lean.collectAxioms audit in VerifyAll.lean (zero sorry, zero native_decide, strictly within [propext, Classical.choice, Quot.sound]) and 12 cross-track Challenge/Solution targets are machine-checked in Lean 4.35.0 across 6 independent kernels in CI; 36 pytest suites (property, negative, 6-mutant killing, 300-payload fuzz, integrity), 2 Node web-model tests, 7 track exact verifiers, and C11 ASan/UBSan checks pass across Linux/macOS/Windows CI. Finite C censuses (540.3M N=9 forms, 42-orbit W(5,2) census), Moonlab/QGTL/QRNG simulations, and exploratory floating-point scripts are explicitly separated from Lean kernel proofs (see CLAIMS.md, LIMITATIONS.md, and docs/statement-fidelity.md). No external peer review, hardware experiment, or external DOI is claimed.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/pauli-contextuality-lab && python scripts/verify_all.py && python -m pytest -v tests/ && cd lean && lake exe cache get && lake build HoggarBound ContextualityTensor Evidence Solution && lake env lean VerifyAll.lean && lake comparator --config comparator.json --paranoid
```
