# Evidence & Falsification Dossier — `0TH-2026-009`

**Title:** Pauli Contextuality Lab: Unified Lean 4.35.0 Formalization of Spectral Bounds, Disjoint Mermin Configurations, and Sequential Contextuality Evidence  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Quantum Foundations / Quantum Contextuality  
**Version / Date:** `v3.3.0` (2026-11-27)  
**Status:** Consolidated research preprint suite (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 & cross-platform CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/pauli-contextuality-lab |
| Pinned Git Submodule | `repos/pauli-contextuality-lab` @ `53e987595dc434e81dd393463e2587b4eb23eda5` |
| GitHub Release | https://github.com/0thernes/pauli-contextuality-lab/releases/tag/v3.3.0 |
| Frozen Archived PDF | `papers/0TH-2026-009_pauli-contextuality-lab/unified-contextuality.pdf` |
| Frozen PDF SHA-256 | `e210881efaed4dce60a530d6bdc2c81463fb2cf8174d2ebbbe7e2107e6231895` |
| arXiv / Source Bundle SHA-256 | `N/A (canonical TeX sources in repo papers/spectral-bounds/unified-contextuality.tex & papers/disjoint-mermin/contextuality-tensor.tex)` |
| CI Verification Run | https://github.com/0thernes/pauli-contextuality-lab/actions/runs/46055695985 |
| Software Heritage SWHID | `swh:1:snp:cf9ae7bd108e9556e79d4c0c81c8de92632b91c1` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Consolidates the four archived Pauli/Mermin contextuality repositories into one unified Apache-2.0 / CC-BY-4.0 monorepo meeting Build Standard v1.2.0 (100.0%, 68/68 checks, Core 30/30) and Playbook v1.3, closing all six Track 1/2 formal-code errata AND 100% of Track 2 Eqs. 1-16 in Lean 4.35.0. Ships a pinned Lean 4.35.0 + Mathlib v4.35.0 workspace (65 .lean files; all 9 standalone Track 1 finite-certificate modules compiled and axiom-audited live in parallel CI via VerifyStandalone.lean and VerifyPhaseSeven.lean), searchable 29-node / 213-declaration Lean Blueprint with MathJax SRI, explicit Sp(2N,2) witness isomorphism verifier & hyperbolic quasi-quadric (135/1,095/75) Qontextium exports, 4 zero-overflow Tectonic PDFs (0.00pt max overfull), 7/7 AST source-code mutation suite (100% kill rate), and 3-OS + 14-engine C11 ASan/UBSan CI (run 46055696084). Track 1 formalizes Jonah's universal and Kramers spectral floors (arbitrary supports), two-sided asymptotic 1/2 limits, five-way saturation equivalences, finite flat degrees 75, 480, 2016 and 729344 (live-audited in CI), infinite non-closed pure-CCZ family |Psi_{3m}> (m>=1, contextual m>=2), lower bounds d(W(7,2))>=1455 and d(Q+(9,2))>=6444 (below Jonah's earlier 1575/6975 claims), exact four-qubit C3 binary completion optima (368 vs 344), formal geometric vertex-case membership predicates IsCaseC1-IsCaseC15 (ConjectureECases.lean) + strict-law failure for one representative per case for all N>=4 (whole-case transfer via Jonah's Theorem B4 outside Lean), and 8 kernel-proved perturbed-bound refutations. Track 2 (ContextualityTensor/GeneralTheory.lean + ActualModel.lean + SeedSupport.lean) formalizes 100% of Eqs. 1-16: exact degrees (7^k-5^k)/2 (squares), (6^k-4^k)/2 (pentagrams), mixed (7^s 6^t - 5^s 4^t)/2 (s squares + t pentagrams), heterogeneous endpoint reduction (Theorem 2), universal general-seed asymptotics eps_k(G) -> 1 for every finite contextual signed seed (Theorem 5), arbitrary-k 2k- and 3k-qubit literal Pauli realizations (Eq. 5), kernel-decided HS(L(K_{3,3})) / HS(Petersen) support equality, and k-independent independent-readout noise thresholds with noisy score decay to 0 (Eqs. 14-16). Track 3 proves finite adaptive-tree sequential evidence bounds and a sharp Peres-Mermin setting-bias attack. All 3 parallel Lean CI jobs (run 46055695985) passed 100% green: 217 explicit + 2,452 exhaustive axioms, live tamper gate, 15-module Batteries linter, 24 targets across 6 independent kernels (SLSA #73255989), VerifyStandalone (SLSA #73261704), VerifyPhaseSeven (SLSA #73249231), and Release v3.3.0 (run 46062140725, SLSA #73263415).

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 / Mathlib v4.35.0 (217 explicit #print axioms + 2,452-theorem-constant Lean.collectAxioms audit over the 45 modules imported by VerifyAll.lean [1,275 non-Challenge authored declarations across 65 files]; complete 100% formalization of Track 2 Eqs. 1-16 in ContextualityTensor/GeneralTheory.lean; dedicated parallel CI jobs lean-verify-standalone [VerifyStandalone.lean, 8 standalone Track 1 modules incl. C3Certificate/C3Spectra, 16 explicit, SLSA #73261704] and lean-verify-phase7 [VerifyPhaseSeven.lean, 7-qubit SaturatedPhaseSeven degree 729,344, 5 explicit, SLSA #73249231]; live CI tamper-injection negative gate; 0 Batteries linter errors across 15 modules; 24 cross-track targets verified across 6 independent kernels via lake comparator --paranoid in Ubuntu CI run 46055695985, SLSA #73255989; Release v3.3.0 run 46062140725 SLSA #73263415)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAll.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/HoggarBound/NonVacuity.lean, lean/VerifyStandalone.lean, lean/VerifyPhaseSeven.lean`

## Preserved Component Manuscripts (Historical Provenance)

- **Spectral bounds and their limits in Pauli contextuality: exact configurations and a proof of Jonah's Conjecture E (Track 1, v3.3.0)** (`v3.3.0 (consolidated from hoggar-bound-lab v1.9.0)`, `papers/spectral-bounds/unified-contextuality.pdf`): Primary archived PDF for 0TH-2026-009; recompiled with Tectonic (literal 0.00pt max overfull hbox) with CRediT, COI, and ERRATA disclosures under CC-BY-4.0.
- **Cospectral Pauli carriers with different completion spectra: an exact four-qubit C3 certificate (Track 1 companion, v3.3.0)** (`v3.3.0 (consolidated from hoggar-bound-lab v0.2.0-c3-certificate)`, `papers/spectral-bounds/c3-spectral-counterexample.pdf`): Track 1 companion C3 certificate PDF archived in papers/0TH-2026-009_pauli-contextuality-lab/c3-spectral-counterexample.pdf (0.00pt max overfull).
- **Exact contextuality degrees for disjoint Mermin configurations (Track 2, v3.3.0)** (`v3.3.0 (consolidated from contextuality-tensor-lab v0.1.0)`, `papers/disjoint-mermin/contextuality-tensor.pdf`): Directly answers Section 6 of Muller & Saniga (arXiv:2609.19862v1); recompiled with Tectonic (literal 0.00pt max overfull hbox) and archived in papers/0TH-2026-009_pauli-contextuality-lab/contextuality-tensor.pdf.
- **Contextuality Evidence Lab: Exact Sequential Certificates and a Constructive Setting-Bias Attack (Track 3, v3.3.0)** (`v3.3.0 (consolidated from contextuality-evidence-lab v1.0.0)`, `papers/sequential-evidence/whitepaper.pdf`): Freshly typeset XeLaTeX/Tectonic PDF (0.00pt max overfull) with unified VerifyAll.lean audit text and CRediT/COI/ERRATA disclosures; archived in papers/0TH-2026-009_pauli-contextuality-lab/whitepaper.pdf.

## Verification Boundary (Honest Epistemic Scope)

All 65 .lean files in the workspace are live-compiled and axiom-audited strictly within [propext, Classical.choice, Quot.sound] across three parallel Ubuntu CI jobs in run 46055695985: VerifyAll.lean (217 explicit #print axioms + 2,452 kernel theorem constants across 45 modules / 1,275 non-Challenge authored declarations, live CI tamper-injection negative gate, 0 Batteries linter errors across 15 modules, 24 cross-track Challenge/Solution targets accepted by all 6 independent kernels via lake comparator --paranoid, SLSA #73255989), VerifyStandalone.lean (8 standalone Track 1 modules including C3Certificate/C3Spectra and 4-/5-qubit saturated degrees, 16 explicit, SLSA #73261704), and VerifyPhaseSeven.lean (7-qubit SaturatedPhaseSeven degree 729,344, 5 explicit, SLSA #73249231). 53 pytest suites (+13 subtests incl. 7/7 AST source-code mutants killed), 2 Node tests, 7 exact verifiers, and 14 zero-warning C11 ASan/UBSan engines pass across Linux/macOS/Windows CI (run 46055696084). Remaining outside Lean: whole-case single-orbit transitivity via Jonah's Theorem B4, finite C censuses (540.3M N=9 forms, 42-orbit W(5,2) census), Moonlab/QGTL/QRNG simulations, and exploratory floating-point scripts (100% of Track 2 Eqs. 1-16 are now kernel-proved inside Lean 4.35.0). No external peer review, hardware experiment, or external DOI is claimed; DigiCert RFC 3161 TSA + 3-calendar OpenTimestamps verified in CI; SWH swh:1:snp:cf9ae7bd108e9556e79d4c0c81c8de92632b91c1 (v3.2.0; fresh v3.3.0 Save Code Now gated by Anubis PoW).

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/pauli-contextuality-lab && python scripts/verify_all.py && python scripts/stamp_timestamps.py --verify && python -m pytest -v tests/ && cd lean && lake exe cache get && lake build HoggarBound ContextualityTensor Evidence Solution VerifyAll && lake env lean VerifyAll.lean && lake comparator --config comparator.json --paranoid
```
