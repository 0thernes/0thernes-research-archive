# Build White Paper & Proof Evidence Dossier — `0TH-BUILD-003`

**Title:** ULTRAMETRICA: Exact Non-Archimedean Holography, Recursive Adelic Valuation-Residue Symmetries, Multi-Edge Curved Gauss-Bonnet Curvature, Holographic Strong Subadditivity, and 6-Kernel Lean 4 Verification  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Mathematical Physics / Non-Archimedean Analysis / Formal Methods  
**Version / Date:** `v1.4.1` (2026-11-25)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/ultrametrica |
| Pinned Git Submodule | `repos/ultrametrica` @ `f11ddc5ceff1a696c5677449d4dd59df608a535b` |
| Archived Artifact | `builds/0TH-BUILD-003_ultrametrica/Donahue_2026_Ultrametrica.pdf` (from `dist/Donahue_2026_Ultrametrica.pdf`) |
| Artifact SHA-256 | `8ed1c87cd39d458e3adc9c43e2043f9b0909cec84c5effb1c15e32b5aee54007` |
| Archived Artifact | `builds/0TH-BUILD-003_ultrametrica/WHITE_PAPER.md` (from `paper/WHITE_PAPER.md`) |
| Artifact SHA-256 | `58811b08af5e9ad39eaa51bdea98000d7b92a130bf40cca752fa3b35581a9192` |
| Archived Artifact | `builds/0TH-BUILD-003_ultrametrica/arxiv_submission.tar.gz` (from `dist/arxiv_submission.tar.gz`) |
| Artifact SHA-256 | `ec49d31199f8602a16eb4905a4c4dd126d326f83d39c4e2cef4b643916f9a25b` |
| Archived Artifact | `builds/0TH-BUILD-003_ultrametrica/CLAIMS.md` (from `CLAIMS.md`) |
| Artifact SHA-256 | `c71dbb1a6811cf9ed999454a78a65c0bbe20638548cdf4cd6f3aba64f687642b` |
| Archived Artifact | `builds/0TH-BUILD-003_ultrametrica/MEGA_ATLAS_CROSSCHECK.md` (from `docs/MEGA_ATLAS_CROSSCHECK.md`) |
| Artifact SHA-256 | `844dab244a02cb6b3c68cf76d9bcc4240a2853cd56ab387fda3edc70bb55e4e6` |
| Archived Artifact | `builds/0TH-BUILD-003_ultrametrica/2026-11-25-hardening-cycles.md` (from `docs/reviews/2026-11-25-hardening-cycles.md`) |
| Artifact SHA-256 | `5a39422b22024ccac14b9cd2286bdc8ed405a97583f94dc600f8661740cfa3bb` |
| Archived Artifact | `builds/0TH-BUILD-003_ultrametrica/AUDIT_AND_CONTRAST_ANALYSIS.md` (from `docs/AUDIT_AND_CONTRAST_ANALYSIS.md`) |
| Artifact SHA-256 | `76b23fbeac229714254bc9fb4dcbc27d394e9563925cbc3ba77b4f38adbeed28` |
| Archived Artifact | `builds/0TH-BUILD-003_ultrametrica/lean4-audit.txt` (from `results/lean4-audit.txt`) |
| Artifact SHA-256 | `819c2a8e58fe6f8a49b035547ab3d71b2233588ea25240e57ad135df8086afc8` |

## Summary

Zero-dependency computational laboratory, responsive WCAG 2.2 AA live GitHub Pages WebGL2 + 48 kHz AudioWorklet observatory (https://0thernes.github.io/ultrametrica/), zero-warning 19-page AMS-LaTeX preprint PDF (5 vector figures, 21/21 verified refs), standalone arXiv bundle, 1-to-1 CLAIMS.md falsification ledger, honest 0/1,900 Mega-Atlas cross-check (discrete sub-results on SUB-032), 3-cycle hardening dossier (28 findings F01-F28 across 10 classes), 100.0% (80/80) Build Standard v1.2.0 compliance (0 ruff, 0 mypy, 0 gitleaks), and 120 pure Lean 4.35.0 declarations + 8 isolated Spec/Challenge/Solution comparator targets verified across all 6 independent kernels (Lean 4.35.0, leanchecker-paranoid, lean4lean, nanoda, con-leche, con-ron) covering Theorems I-VI (including Theorem V-Global arbitrary multi-edge curved AdS Gauss-Bonnet and Theorem VI universal weighted-graph holographic RT Strong Subadditivity), paired with exact-rational Fraction/Q(i)/brute-force checks (69 curved trees, 4,352 SSA partitions), git-sealed pre-registered 20-seed Experiment I (4/4 confirmed at p_holm = 0.0004), 26/26 Node suites (8/8 mutants killed, 3,200+ properties, HTTP EIO failure injection), and 1,000+ Python differential oracle checks.

## Embedded Lean 4 Proof Suite Audit

- **Framework:** Pure Lean 4.35.0 (zero Mathlib, autoImplicit = false, zero native_decide, 6-kernel lake comparator --paranoid)
- **Lean Modules / Lines:** 9 files / 3218 lines
- **Audited Theorems (`#print axioms`):** 120
- **Entry Point:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Live Audit Status:** GitHub Actions CI GREEN (run #45740525070, 6/6 jobs: ubuntu-24.04/macos/windows 26/26 Node tests + 3/3 examples + 1,000+ Python oracle + 79-file sha256sum + Tectonic zero-warning 19-page PDF/arXiv with 21/21 refs + 0 ruff / 0 mypy / 0 gitleaks + 100.0% 80/80 Build Standard v1.2.0 + 6-kernel bubblewrap lake comparator --paranoid PASS, SLSA attestation 72456984), Pages GREEN (#45740525069), Release v1.4.1 SLSA attested (#45740529180, attestation 72456429); 120/120 audited declarations + 8/8 isolated Challenge/Solution targets strictly within [propext, Classical.choice, Quot.sound]

## Verification Boundary

All 120 audited Lean 4.35.0 declarations and 8 isolated Challenge/Solution targets compile cleanly with zero Mathlib, autoImplicit = false, zero native_decide, zero sorry, and strictly [propext, Classical.choice, Quot.sound], verified across all 6 independent kernels via sandboxed lake comparator --paranoid on Ubuntu CI (SLSA attestation 72456984). Exact-rational Python checks verify 7,033 conjugate Adelic pairs, 45 BTZ horizons, 69 single/multi-edge curved AdS trees, 4,352 exhaustive RT SSA partitions, exact Q(i) solves, and 79 SHA-256 digests; floating-point FFT/PDE/Jacobi checks, 20-seed Experiment I statistics, and 26 Node suites lie outside the Lean kernel boundary and are separated explicitly in CLAIMS.md, LIMITATIONS.md, and docs/statement-fidelity.md. Claims 0/1,900 full Mega-Atlas solutions and no empirical discovery of new physical laws of nature.

## Independent Reproduction & Falsification Protocol

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/ultrametrica && npm run verify:all && npm run examples && python3 reference/padic_oracle.py && python3 scripts/check_readme_axioms.py && python3 scripts/verify_exact.py --check-checksums && (cd lean && lake clean && lake build UltrametricaProofs Challenge Solution && lake env lean VerifyAxioms.lean && lake comparator --config comparator.json --paranoid)
```
