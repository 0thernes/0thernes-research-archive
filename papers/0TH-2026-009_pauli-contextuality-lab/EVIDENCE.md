# Evidence & Falsification Dossier — `0TH-2026-009`

**Title:** Pauli Contextuality Lab: Unified Lean 4.35.0 Formalization of Spectral Bounds, Disjoint Mermin Configurations, and Sequential Contextuality Evidence  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Quantum Foundations / Quantum Contextuality  
**Version / Date:** `v3.0.0` (2026-11-26)  
**Status:** Consolidated research preprint suite (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 & cross-platform CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/pauli-contextuality-lab |
| Pinned Git Submodule | `repos/pauli-contextuality-lab` @ `b0f8a180f441674c439840d5125e2c4dcac55a18` |
| GitHub Release | https://github.com/0thernes/pauli-contextuality-lab/releases/tag/v3.0.0 |
| Frozen Archived PDF | `papers/0TH-2026-009_pauli-contextuality-lab/unified-contextuality.pdf` |
| Frozen PDF SHA-256 | `f2e54d74ae02f4072580620e125206981d23dbf973350aac768721a8d3bf60e8` |
| arXiv / Source Bundle SHA-256 | `N/A (canonical TeX sources in repo papers/spectral-bounds/unified-contextuality.tex & papers/disjoint-mermin/contextuality-tensor.tex)` |
| CI Verification Run | https://github.com/0thernes/pauli-contextuality-lab/actions/runs/45826042676 |
| Software Heritage SWHID | `swh:1:snp:54b1005a1e5ebde0c4dd89892c1bff4c3e6845ba` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Consolidates the four archived Pauli/Mermin contextuality repositories (hoggar-bound, hoggar-bound-lab, contextuality-tensor-lab, contextuality-evidence-lab) into one unified Apache-2.0 / CC-BY-4.0 monorepo meeting Build Standard v1.2.0 (100.0%, 68/68 checks, Core 30/30, 10 finding classes, Draft 2020-12 JSON Schema-validated repo.yaml) and Defensible Independent AI Research Playbook v1.3 (ERRATA.md, CRediT & COI disclosures across all 4 manuscripts, 1,900-problem Unsolved Problems Mega-Atlas V2 cross-reference in docs/mega-atlas-cross-reference.md recording 0/1,900 grand problems solved; the results are thematically related to QM-011 (the atlas entry was not checked to list them as sub-cases), BibTeX + Handle + Crossref retraction-free citation audit across 44/44 URLs and 17/17 journal DOIs, cross-track adversarial false-variant Lean rejection tests, repo-wide CDN sha384 SRI guard, and SHA-256-verified gitleaks v8.30.1 + osv-scanner v2.7.1 CI). Ships a single pinned Lean 4.35.0 + Mathlib v4.35.0 workspace (transparent 60-module audit map in lean/README.md), deduplicated third-party stack, searchable 27-node / 162-declaration Lean Blueprint (/blueprint/) with MathJax SRI, explicit Sp(2N,2) witness isomorphism verifier plus Qontextium-ready hyperbolic quasi-quadric (135/1,095/75) exports (/exports/hyperbolic-quasi-quadric-135/), 4 zero-overflow Tectonic PDFs (literal 0.00pt max overfull hbox across all 4 PDFs), and 3-OS + 14-engine zero-warning C11 ASan/UBSan CI (run 45826042756). Track 1 formalizes Jonah's universal spectral floor and Kramers floor (prior work, here for arbitrary supports) and proves 5-way saturation equivalences, an infinite non-closed pure-CCZ family |Psi_{3m}> attaining the floor (degree 2016 at m = 2; contextual for m >= 2), lower bounds d(W(7,2))>=1455 and d(Q+(9,2))>=6444 (below the exact values 1575 and 6975 claimed earlier by Jonah), exact four-qubit C3 binary completion optima (368 vs 344) for one sign pair, and strict-law failure for one explicit representative of each of the 9 vertex cases of Jonah's Conjecture E for every N>=4 (case coverage via Jonah's Theorem B4, outside Lean). The finite degrees 75, 480 and 729344 are in modules not compiled at the pinned commit. Track 2 proves exact arbitrary-k disjoint-copy formulas d_k=(7^k-5^k)/2 (squares) and (6^k-4^k)/2 (pentagrams) addressing Muller & Saniga (arXiv:2609.19862v1 Sec. 6). Track 3 proves finite adaptive-tree sequential evidence bounds and a sharp setting-bias attack on the Peres-Mermin square. Live Ubuntu CI run 45826042676 audited 166 explicit #print axioms (including HoggarBound.Stability) and all 2,206 theorems strictly within standard axioms, refuted 3 cross-track adversarial false-variant Lean theorems, and verified all 12 cross-track comparator targets across all 6 independent kernels (lean-paranoid, lean4lean, nanoda, con-leche, con-ron, lean-default) with Sigstore/Rekor attestation (Lean logIndex 4126960397; Release v3.0.0 run 45830072420 Rekor logIndex 4126969649; DigiCert RFC 3161 TSA + 3-calendar OpenTimestamps verified via OpenSSL X.509 in CI).

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 / Mathlib v4.35.0 (166 explicit #print axioms including HoggarBound.Stability + 2,206-theorem-constant Lean.collectAxioms audit over the 43 modules imported by VerifyAll.lean (1,175 authored theorem/lemma declarations across all 60 files); 0 Batteries linter errors across HoggarBound.Bound, HoggarBound.Stability, ContextualityTensor, Evidence; 12 headline targets verified across 6 independent kernels via lake comparator --paranoid in Ubuntu 24.04 CI)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAll.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/HoggarBound/NonVacuity.lean`

## Preserved Component Manuscripts (Historical Provenance)

- **Spectral bounds and their limits in Pauli contextuality: exact configurations and a proof of Jonah's Conjecture E (Track 1, v3.0.0)** (`v3.0.0 (consolidated from hoggar-bound-lab v1.9.0)`, `papers/spectral-bounds/unified-contextuality.pdf`): Primary archived PDF for 0TH-2026-009; recompiled with Tectonic (literal 0.00pt max overfull hbox) with CRediT, COI, and ERRATA disclosures under CC-BY-4.0.
- **Cospectral Pauli carriers with different completion spectra: an exact four-qubit C3 certificate (Track 1 companion, v3.0.0)** (`v3.0.0 (consolidated from hoggar-bound-lab v0.2.0-c3-certificate)`, `papers/spectral-bounds/c3-spectral-counterexample.pdf`): Track 1 companion C3 certificate PDF archived in papers/0TH-2026-009_pauli-contextuality-lab/c3-spectral-counterexample.pdf (0.00pt max overfull).
- **Exact contextuality degrees for disjoint Mermin configurations (Track 2, v3.0.0)** (`v3.0.0 (consolidated from contextuality-tensor-lab v0.1.0)`, `papers/disjoint-mermin/contextuality-tensor.pdf`): Directly answers Section 6 of Muller & Saniga (arXiv:2609.19862v1); recompiled with Tectonic (literal 0.00pt max overfull hbox) and archived in papers/0TH-2026-009_pauli-contextuality-lab/contextuality-tensor.pdf.
- **Contextuality Evidence Lab: Exact Sequential Certificates and a Constructive Setting-Bias Attack (Track 3, v3.0.0)** (`v3.0.0 (consolidated from contextuality-evidence-lab v1.0.0)`, `papers/sequential-evidence/whitepaper.pdf`): Freshly typeset XeLaTeX/Tectonic PDF (0.00pt max overfull) with unified VerifyAll.lean audit text and CRediT/COI/ERRATA disclosures; archived in papers/0TH-2026-009_pauli-contextuality-lab/whitepaper.pdf.

## Verification Boundary (Honest Epistemic Scope)

166 explicit headline declarations (including all 6 HoggarBound.Stability theorems) plus an exhaustive 2,206-theorem Lean.collectAxioms audit in VerifyAll.lean (zero sorry, zero native_decide, no Lean elaboration warnings besides Lake module-system import notices, strictly within [propext, Classical.choice, Quot.sound]), 3 cross-track adversarial false-variant Lean rejection checks are machine-checked by the Lean kernel in CI, and the 12 cross-track Challenge/Solution targets are additionally re-checked by 6 independent kernels; the Saturated*, C3Certificate, C3Spectra, C3Theorem, FlatData and PhaseData modules are not compiled in that CI run; 52 pytest suites (including DigiCert RFC 3161 TSA + OpenTimestamps + SWHID + submission-packet checks) (+6 subtests, including repo-wide CDN sha384 SRI guard, Draft 2020-12 repo.yaml schema, 10-class labels, _native.* axiom-rejection & Palomar size guards, Sp(2N,2) witness isomorphism & Qontextium export tests, property, negative, 6-mutant killing, 300-payload fuzz, live C3/Blueprint/explorer/monorepo integrity), 2 Node web-model tests, 7 track exact verifiers, and 14 zero-warning C11 ASan/UBSan engines pass across Linux/macOS/Windows CI. Finite C censuses (540.3M N=9 forms, 42-orbit W(5,2) census), Moonlab/QGTL/QRNG simulations, and exploratory floating-point scripts are explicitly separated from Lean kernel proofs (see CLAIMS.md, LIMITATIONS.md, ERRATA.md, and docs/statement-fidelity.md). No external peer review, hardware experiment, or external DOI is claimed. data/MANIFEST.sha256 is cryptographically timestamped by DigiCert RFC 3161 TSA (.tsr, OpenSSL X.509 Verification: OK in CI) and 3-calendar Bitcoin OpenTimestamps (.ots), and an author-automated Python/Node clean-clone check passed on v2.9.0 (17.7s, no Lean step; external human replication remains open).

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/pauli-contextuality-lab && python scripts/verify_all.py && python scripts/stamp_timestamps.py --verify && python -m pytest -v tests/ && cd lean && lake exe cache get && lake build HoggarBound ContextualityTensor Evidence Solution VerifyAll && lake env lean VerifyAll.lean && lake comparator --config comparator.json --paranoid
```
