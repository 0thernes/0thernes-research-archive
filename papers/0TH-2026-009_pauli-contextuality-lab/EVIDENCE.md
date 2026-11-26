# Evidence & Falsification Dossier — `0TH-2026-009`

**Title:** Pauli Contextuality Lab: Unified Lean 4.35.0 Formalization of Spectral Bounds, Disjoint Mermin Configurations, and Sequential Contextuality Evidence  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Quantum Foundations / Quantum Contextuality  
**Version / Date:** `v2.9.0` (2026-11-25)  
**Status:** Consolidated research preprint suite (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 & cross-platform CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/pauli-contextuality-lab |
| Pinned Git Submodule | `repos/pauli-contextuality-lab` @ `cbf384a47db065f0aed7d0b5fce6d3ec72b03794` |
| GitHub Release | https://github.com/0thernes/pauli-contextuality-lab/releases/tag/v2.9.0 |
| Frozen Archived PDF | `papers/0TH-2026-009_pauli-contextuality-lab/unified-contextuality.pdf` |
| Frozen PDF SHA-256 | `340b0c001b8934098711b2539c6d1b3ede88e03ccedf439815d52ca5205e1264` |
| arXiv / Source Bundle SHA-256 | `N/A (canonical TeX sources in repo papers/spectral-bounds/unified-contextuality.tex & papers/disjoint-mermin/contextuality-tensor.tex)` |
| CI Verification Run | https://github.com/0thernes/pauli-contextuality-lab/actions/runs/45741807525 |
| Software Heritage SWHID | `swh:1:snp:0d84f85d8dc6b9c703784c655998864acee6c98d` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Consolidates the four archived Pauli/Mermin contextuality repositories (hoggar-bound, hoggar-bound-lab, contextuality-tensor-lab, contextuality-evidence-lab) into one unified Apache-2.0 / CC-BY-4.0 monorepo meeting Build Standard v1.2.0 (100.0%, 68/68 checks, Core 30/30, 10 finding classes, Draft 2020-12 JSON Schema-validated repo.yaml) and Defensible Independent AI Research Playbook v1.3 (ERRATA.md, CRediT & COI disclosures across all 4 manuscripts, 1,900-problem Unsolved Problems Mega-Atlas V2 cross-reference in docs/mega-atlas-cross-reference.md honestly recording 0/1,900 grand problems solved with bounded QM-011 finite-dimensional Pauli subcases settled in Lean 4.35.0, BibTeX + Handle + Crossref retraction-free citation audit across 44/44 URLs and 17/17 journal DOIs, cross-track adversarial false-variant Lean rejection tests, repo-wide CDN sha384 SRI guard, and SHA-256-verified gitleaks v8.30.1 + osv-scanner v2.7.1 CI). Ships a single pinned Lean 4.35.0 + Mathlib v4.35.0 workspace (transparent 60-module audit map in lean/README.md), deduplicated third-party stack, searchable 27-node / 162-declaration Lean Blueprint (/blueprint/) with MathJax SRI, explicit Sp(2N,2) witness isomorphism verifier plus Qontextium-ready hyperbolic quasi-quadric (135/1,095/75) exports (/exports/hyperbolic-quasi-quadric-135/), 4 zero-overflow Tectonic PDFs (literal 0.00pt max overfull hbox across all 4 PDFs), and 3-OS + 14-engine zero-warning C11 ASan/UBSan CI (run 45741807429). Track 1 proves the universal spectral floor, Kramers floor, 5-way saturation equivalences, exact degrees (75, 480, 2016, 729344), infinite non-closed pure-CCZ determinant family |Psi_{3m}>, unconditional N=4..5 bounds d(W(7,2))>=1455 and d(Q+(9,2))>=6444, exact four-qubit C3 binary completion optima (368 vs 344, gap 24), and Jonah's Conjecture E across all 9 vertex cases for every N>=4. Track 2 proves exact arbitrary-k disjoint-copy formulas d_k=(7^k-5^k)/2 (squares) and (6^k-4^k)/2 (pentagrams) addressing Muller & Saniga (arXiv:2609.19862v1 Sec. 6). Track 3 proves finite adaptive-tree sequential evidence bounds and a sharp setting-bias attack on the Peres-Mermin square. Live Ubuntu CI run 45741807525 audited 160 explicit #print axioms and all 2,206 theorems strictly within standard axioms, refuted 3 cross-track adversarial false-variant Lean theorems, and verified all 12 cross-track comparator targets across all 6 independent kernels (lean-paranoid, lean4lean, nanoda, con-leche, con-ron, lean-default) with Sigstore/Rekor attestation (Lean logIndex 4116592110; Release v2.9.0 run 45744521481 Rekor logIndex 4116605402).

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 / Mathlib v4.35.0 (160 explicit #print axioms + exhaustive 2,206-theorem Lean.collectAxioms audit across HoggarBound, ContextualityTensor, Evidence, PauliContextualityLab; 0 Batteries linter errors; 12 headline targets verified across 6 independent kernels via lake comparator --paranoid in Ubuntu 24.04 CI)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAll.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/HoggarBound/NonVacuity.lean`

## Preserved Component Manuscripts (Historical Provenance)

- **Spectral bounds and their limits in Pauli contextuality: exact configurations and a proof of Jonah's Conjecture E (Track 1, v2.9.0)** (`v2.9.0 (consolidated from hoggar-bound-lab v1.9.0)`, `papers/spectral-bounds/unified-contextuality.pdf`): Primary archived PDF for 0TH-2026-009; recompiled with Tectonic (literal 0.00pt max overfull hbox) with CRediT, COI, and ERRATA disclosures under CC-BY-4.0.
- **Cospectral Pauli carriers with different completion spectra: an exact four-qubit C3 certificate (Track 1 companion, v2.9.0)** (`v2.9.0 (consolidated from hoggar-bound-lab v0.2.0-c3-certificate)`, `papers/spectral-bounds/c3-spectral-counterexample.pdf`): Track 1 companion C3 certificate PDF archived in papers/0TH-2026-009_pauli-contextuality-lab/c3-spectral-counterexample.pdf (0.00pt max overfull).
- **Exact contextuality degrees for disjoint Mermin configurations (Track 2, v2.9.0)** (`v2.9.0 (consolidated from contextuality-tensor-lab v0.1.0)`, `papers/disjoint-mermin/contextuality-tensor.pdf`): Directly answers Section 6 of Muller & Saniga (arXiv:2609.19862v1); recompiled with Tectonic (literal 0.00pt max overfull hbox) and archived in papers/0TH-2026-009_pauli-contextuality-lab/contextuality-tensor.pdf.
- **Contextuality Evidence Lab: Exact Sequential Certificates and a Constructive Setting-Bias Attack (Track 3, v2.9.0)** (`v2.9.0 (consolidated from contextuality-evidence-lab v1.0.0)`, `papers/sequential-evidence/whitepaper.pdf`): Freshly typeset XeLaTeX/Tectonic PDF (0.00pt max overfull) with unified VerifyAll.lean audit text and CRediT/COI/ERRATA disclosures; archived in papers/0TH-2026-009_pauli-contextuality-lab/whitepaper.pdf.

## Verification Boundary (Honest Epistemic Scope)

160 explicit headline declarations plus an exhaustive 2,206-theorem Lean.collectAxioms audit in VerifyAll.lean (zero sorry, zero native_decide, zero warnings, strictly within [propext, Classical.choice, Quot.sound]), 3 cross-track adversarial false-variant Lean rejection checks, and 12 cross-track Challenge/Solution targets are machine-checked in Lean 4.35.0 across 6 independent kernels in CI; 51 pytest suites (+6 subtests, including repo-wide CDN sha384 SRI guard, Draft 2020-12 repo.yaml schema, 10-class labels, _native.* axiom-rejection & Palomar size guards, Sp(2N,2) witness isomorphism & Qontextium export tests, property, negative, 6-mutant killing, 300-payload fuzz, live C3/Blueprint/explorer/monorepo integrity), 2 Node web-model tests, 7 track exact verifiers, and 14 zero-warning C11 ASan/UBSan engines pass across Linux/macOS/Windows CI. Finite C censuses (540.3M N=9 forms, 42-orbit W(5,2) census), Moonlab/QGTL/QRNG simulations, and exploratory floating-point scripts are explicitly separated from Lean kernel proofs (see CLAIMS.md, LIMITATIONS.md, ERRATA.md, and docs/statement-fidelity.md). No external peer review, hardware experiment, or external DOI is claimed.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/pauli-contextuality-lab && python scripts/verify_all.py && python -m pytest -v tests/ && cd lean && lake exe cache get && lake build HoggarBound ContextualityTensor Evidence Solution && lake env lean VerifyAll.lean && lake comparator --config comparator.json --paranoid
```
