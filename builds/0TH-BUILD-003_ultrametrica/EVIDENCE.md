# Build White Paper & Proof Evidence Dossier — `0TH-BUILD-003`

**Title:** ULTRAMETRICA: Exact Non-Archimedean Holography, Recursive Adelic Valuation-Residue Symmetries, Tate-Curve BTZ & Curved Gauss-Bonnet Curvature, and Lean 4 Formal Verification  
**Author:** Alexander Stephen Donahue (0thernes LLC, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Mathematical Physics / Non-Archimedean Analysis / Formal Methods  
**Version / Date:** `v1.3.0` (2026-11-21)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/ultrametrica |
| Pinned Git Submodule | `repos/ultrametrica` @ `e42e6affdce172dc72cdbd8f2ffbd5f211d234f5` |
| Archived Artifact | `builds/0TH-BUILD-003_ultrametrica/Donahue_2026_Ultrametrica.pdf` (from `dist/Donahue_2026_Ultrametrica.pdf`) |
| Artifact SHA-256 | `d56f2ec54d3d04fecc885c1d010fd2045a12c4c05f3bacc444a452be263f1395` |
| Archived Artifact | `builds/0TH-BUILD-003_ultrametrica/WHITE_PAPER.md` (from `paper/WHITE_PAPER.md`) |
| Artifact SHA-256 | `8f5aa748e3ad50c99a495ddcc92fef226598ae52893f26e186078c8954684c95` |
| Archived Artifact | `builds/0TH-BUILD-003_ultrametrica/arxiv_submission.tar.gz` (from `dist/arxiv_submission.tar.gz`) |
| Artifact SHA-256 | `aae1420e8947c69fd3511e8c6bc2419cabc1528b44b99f48b591bbd6931dca55` |
| Archived Artifact | `builds/0TH-BUILD-003_ultrametrica/CLAIMS.md` (from `docs/CLAIMS.md`) |
| Artifact SHA-256 | `352c533c500dd3bd90093f4fede7af06c78961cb26ed42b163e059b99f1648a5` |
| Archived Artifact | `builds/0TH-BUILD-003_ultrametrica/AUDIT_AND_CONTRAST_ANALYSIS.md` (from `docs/AUDIT_AND_CONTRAST_ANALYSIS.md`) |
| Artifact SHA-256 | `7a52b15d4242da361c37f5a971f28e9c9b9e8308bf067a8cce7fedf5c3fac438` |
| Archived Artifact | `builds/0TH-BUILD-003_ultrametrica/lean4-audit.txt` (from `results/lean4-audit.txt`) |
| Artifact SHA-256 | `832d293b298ccb88bbbc5724d864666f3131b08d2d8dbd5502ad3cc4e94afd1f` |

## Summary

Zero-dependency computational laboratory, live GitHub Pages WebGL2 + 48 kHz AudioWorklet observatory (https://0thernes.github.io/ultrametrica/), zero-warning 15-page AMS-LaTeX white paper PDF (5 vector figures), standalone arXiv bundle, 1-to-1 CLAIMS.md ledger, 7-layer AUDIT_AND_CONTRAST_ANALYSIS.md dossier (resolving 16 code/UI/audio/security/doc issues), 55-file CHECKSUMS.sha256 manifest, and formal framework coupling discrete p-adic QFT on Z_p/p^n Z_p to Bruhat-Tits tree and rotating Tate-curve BTZ holography, verified by 101 pure Lean 4.35.0 universal & first-principles proofs (universal Monna bijectivity & ball contiguity, concrete Bruhat-Tits Ultrametric instance, subtree cyclic-shift ultrametric isometry, universal Proposition 4.2 modular picket-fence law, cycle-graph metric bridge + Kantorovich primal-dual 1-Wasserstein optimality for AdS and BTZ, Euler characteristics chi=1,0, Theorem V non-perturbative curved AdS discrete Gauss-Bonnet conservation & supercritical pinch deficit, arbitrary K-ball compacton-solitons, complex Hermitian Sherman-Morrison exactness, and Kerr flux parity), an independent exact-rational (Fraction & Q(i)) Python falsifier (45 BTZ horizons + 60 curved Gauss-Bonnet plans), 8/8 planted negative mutants killed, and 8 reproducible experiments (Exp A-H up to N = 625 across alpha in [0.5, 2.0] and BF margin Delta = 0.5001).

## Embedded Lean 4 Proof Suite Audit

- **Framework:** Pure Lean 4.35.0 (zero Mathlib, zero native_decide)
- **Lean Modules / Lines:** 6 files / 2267 lines
- **Audited Theorems (`#print axioms`):** 101
- **Entry Point:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Live Audit Status:** GitHub Actions CI GREEN (run #44905696592, 4/4 jobs incl. sha256sum 55/55 + 8/8 mutants + Exp A-H + Tectonic standalone arXiv) & Pages deploy GREEN (#44905696484); local lake clean && lake build EXIT 0 (7 jobs, 0 warnings); 101/101 #print axioms strictly within [propext, Classical.choice, Quot.sound] (8 zero-axiom constructive)

## Verification Boundary

All 101 audited Lean 4.35.0 declarations (2,267 lines) compile cleanly in pure Lean 4 core with zero Mathlib, zero native_decide, zero sorry, and strictly standard axioms ([propext, Classical.choice, Quot.sound] or empty). Independent exact-rational Python checks verify 7,033 conjugate Adelic pairs, 18 modular picket-fence sectors, 45 BTZ optimal-transport horizons, 60 curved AdS Gauss-Bonnet transport plans, exact Q(i) Rank-1 Sherman-Morrison solves, and all 55 SHA-256 digests; floating-point FFT/PDE simulations, large-N Hermitian Jacobi spectra (alpha in [0.5, 2.0]), BF margin tests, and 8/8 planted negative mutants lie outside the Lean kernel boundary and are mapped 1-to-1 in docs/CLAIMS.md and docs/AUDIT_AND_CONTRAST_ANALYSIS.md. No empirical discovery of new physical laws of nature is claimed.

## Independent Reproduction & Falsification Protocol

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/ultrametrica && npm run verify:all && python3 scripts/verify_exact.py --check-checksums && sha256sum -c CHECKSUMS.sha256 && (cd lean && lake clean && lake build && lake env lean VerifyAxioms.lean)
```
