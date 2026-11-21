# Build White Paper & Proof Evidence Dossier — `0TH-BUILD-003`

**Title:** ULTRAMETRICA: Exact Non-Archimedean Holography, Recursive Adelic Valuation-Residue Symmetries, Tate-Curve BTZ Ollivier-Ricci Curvature, and Lean 4 Formal Verification  
**Author:** Alexander Stephen Donahue (0thernes LLC, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Mathematical Physics / Non-Archimedean Analysis / Formal Methods  
**Version / Date:** `v1.2.0` (2026-11-21)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/ultrametrica |
| Pinned Git Submodule | `repos/ultrametrica` @ `1465bd1fd7e5e172a3f99cc53802cda2136e37b1` |
| Archived Artifact | `builds/0TH-BUILD-003_ultrametrica/Donahue_2026_Ultrametrica.pdf` (from `dist/Donahue_2026_Ultrametrica.pdf`) |
| Artifact SHA-256 | `2a6f73a8ace4b30b2feebea64acd94be1c75e5b663e739d12aae57cec26e8b5e` |
| Archived Artifact | `builds/0TH-BUILD-003_ultrametrica/WHITE_PAPER.md` (from `paper/WHITE_PAPER.md`) |
| Artifact SHA-256 | `009b30f25171d94e311a48c1afe0ed6a518e779d104eab7c40b9efb36a099674` |
| Archived Artifact | `builds/0TH-BUILD-003_ultrametrica/arxiv_submission.tar.gz` (from `dist/arxiv_submission.tar.gz`) |
| Artifact SHA-256 | `9d361cae2f948b5a72451f925d73d9155b50faddc9466645eb5deb9599623a22` |
| Archived Artifact | `builds/0TH-BUILD-003_ultrametrica/CLAIMS.md` (from `docs/CLAIMS.md`) |
| Artifact SHA-256 | `6f9a7948810286f18f17a3af9880d95f7f100fee7bbc08e1595fb227ec4e041f` |
| Archived Artifact | `builds/0TH-BUILD-003_ultrametrica/lean4-audit.txt` (from `results/lean4-audit.txt`) |
| Artifact SHA-256 | `00537c534bd9f7c597c5c0a91f0cdaaf6df29b10fc766c99985c889f83fc72b9` |

## Summary

Zero-dependency computational laboratory, live GitHub Pages WebGL2 + 48 kHz AudioWorklet observatory (https://0thernes.github.io/ultrametrica/), zero-warning 13-page AMS-LaTeX white paper PDF (4 vector figures), standalone arXiv bundle, 1-to-1 CLAIMS.md ledger, 53-file CHECKSUMS.sha256 manifest, and formal framework coupling discrete p-adic QFT on Z_p/p^n Z_p to Bruhat-Tits tree and rotating Tate-curve BTZ holography, verified by 71 pure Lean 4.35.0 universal & first-principles proofs (universal Monna involution & ball contiguity, subtree cyclic-shift ultrametric isometry, Kantorovich primal-dual 1-Wasserstein optimality for AdS and BTZ, arbitrary K-ball compacton-solitons, complex Hermitian Sherman-Morrison exactness, and Kerr flux parity), an independent exact-rational (Fraction & Q(i)) Python falsifier, 6/6 planted negative mutants killed, and large-N (N <= 625) intra-sector spectral falsification of GOE/GUE thermalization (modular picket-fence law).

## Embedded Lean 4 Proof Suite Audit

- **Framework:** Pure Lean 4.35.0 (zero Mathlib, zero native_decide)
- **Lean Modules / Lines:** 6 files / 1706 lines
- **Audited Theorems (`#print axioms`):** 71
- **Entry Point:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Live Audit Status:** GitHub Actions CI GREEN (run #44897905339, 4/4 jobs incl. sha256sum + 6/6 mutants + Tectonic standalone arXiv) & Pages deploy GREEN (#44897991574); local lake clean && lake build EXIT 0 (7 jobs, 0 warnings); 71/71 #print axioms strictly within [propext, Classical.choice, Quot.sound] (7 zero-axiom constructive)

## Verification Boundary

All 71 audited Lean 4.35.0 declarations (1,706 lines) compile cleanly in pure Lean 4 core with zero Mathlib, zero native_decide, zero sorry, and strictly standard axioms ([propext, Classical.choice, Quot.sound] or empty). Independent exact-rational Python checks verify 7,033 conjugate Adelic pairs, 18 modular picket-fence sectors, 45 BTZ optimal-transport horizons, exact Q(i) Rank-1 Sherman-Morrison solves, and all 53 SHA-256 digests; floating-point FFT/PDE simulations, large-N Hermitian Jacobi spectra, and 6/6 planted negative mutants lie outside the Lean kernel boundary and are mapped 1-to-1 in docs/CLAIMS.md. No empirical discovery of new physical laws of nature is claimed.

## Independent Reproduction & Falsification Protocol

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/ultrametrica && npm run verify:all && python3 scripts/verify_exact.py --check-checksums && sha256sum -c CHECKSUMS.sha256 && (cd lean && lake clean && lake build && lake env lean VerifyAxioms.lean)
```
