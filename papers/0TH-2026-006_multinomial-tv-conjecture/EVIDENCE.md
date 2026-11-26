# Evidence & Falsification Dossier — `0TH-2026-006`

**Title:** Resolution and Lean 4 Formal Verification of Conjecture 7.7 on the Second-Order Variance of Multinomial Discrete Total Variation  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Mathematical Statistics / Probability Theory  
**Version / Date:** `v2.2.0` (2026-11-25)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0, Palomar module headers, live negative kernel rejection & cross-platform CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/multinomial-tv-conjecture |
| Pinned Git Submodule | `repos/multinomial-tv-conjecture` @ `5ceae10ee73d2c6e4d23c9ce40724f6cfc1f55d1` |
| GitHub Release | https://github.com/0thernes/multinomial-tv-conjecture/releases/tag/v2.2.0 |
| Frozen Archived PDF | `papers/0TH-2026-006_multinomial-tv-conjecture/Donahue_2026_Conjecture_7_7_Multinomial_TV.pdf` |
| Frozen PDF SHA-256 | `4b3a53cce5b5784eda641eeabd08f18413d3ea97c5ff3e4d5e2b4f214be5850d` |
| arXiv / Source Bundle SHA-256 | `021cc60cee16b698cedf5030d1e74ce5fa9cad490cb7d0d2734ddc6fe030e11c` |
| CI Verification Run | https://github.com/0thernes/multinomial-tv-conjecture/actions/runs/45747471704 |
| Software Heritage SWHID | `Pending manual Save Code Now` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Proves Conjecture 7.7 (conj:atriangle) of Banic & Elezovic (arXiv:2610.17046v1, confirmed open in arXiv:2611.14735v1) via an exact 2D-to-1D combinatorial telescoping reduction, sharp non-asymptotic Stirling bounds, and cubic odd-Gaussian Euler-Maclaurin summation, establishing b_0 = 32*sqrt(3)/(81*pi), b_1 = b_2 = -22*sqrt(3)/(81*pi), d_0 = -4*sqrt(3)/(81*pi), a_triangle = 1/32 - 4*sqrt(3)/243, and gamma_2 = -1/(32*pi) - 8*sqrt(3)/(243*pi), rendering linear gamma(n) and cyclic gamma_c(n) unconditional for n >= 5. Hardened in v2.2.0 across 44 cumulative classified findings (F-01..F-44 & Playbook v1.3 10-pass scorecard) with Palomar Lean 4.35.0 module headers across all 10 files (Challenge.lean 122 lines), REUSE SPDX headers, 18 NonVacuity witnesses, exhaustive 723-theorem named+private axiom audit, live negative Lean kernel rejection check + 6-kernel Ubuntu bubblewrap CI replay (run 45747471704, Rekor 4117130014; Release Rekor 4116986681), 31/31 pytest across 3 OSes (including E-2026-009 120-dps dynamic precision regression, CFF/lockfile parity, Hypothesis L=3..45, negative, mutant-killing, and path-leak guards), 16/16 live HTTP-200 Crossref/arXiv 0-retraction clickable plainurl citations with bidirectional \cite parity, 0.00pt max-overfull 20-page AMS-LaTeX PDF (with C1-C6 ledger, EAR/ITAR export-control self-screen, and deterministic standalone arXiv tarball), WCAG AA interactive 16-node/47-decl Lean Blueprint, dual DigiCert RFC 3161 (.tsr) + 3-calendar Bitcoin OpenTimestamps (.ots) proofs on 30-artifact MANIFEST.sha256, and 100.0% (66/66, Core 29/29) Build Standard v1.2.0 compliance.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 / Mathlib v4.35.0 (autoImplicit = false, Palomar module headers on all 10 files, 5,626 lines = 5,216 library + 410 root/bridge/audit, REUSE SPDX headers, 43 explicit #print axioms + exhaustive 723-theorem Lean.collectAxioms audit across named & module-private MultinomialTV decls, 18 NonVacuity witnesses, 0 Batteries linter warnings; live negative Lean kernel rejection of false aTriangle = 1/32 + all 6 independent kernels passed on sandboxed Ubuntu 24.04 CI run 45747471704 via lake comparator --paranoid: Lean paranoid, lean4lean, Rust nanoda, con-leche 41,721 decls, con-ron 41,721 decls, Lean default; Sigstore Rekor logIndex 4117130014 / GitHub attestation 72475662 & Release v2.2.0 Rekor 4116986681 / attestation 72474325; dual DigiCert RFC 3161 TSA (.tsr) + 3-calendar Bitcoin OpenTimestamps (.ots) on 30-artifact MANIFEST.sha256; WCAG AA interactive Lean Blueprint at /blueprint/)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/MultinomialTVConjecture/NonVacuity.lean`

## Verification Boundary (Honest Epistemic Scope)

Entire proof of Conjecture 7.7, exact nested-sum fidelity check (hAdj_eq_nested_sum), 18 NonVacuity witnesses, and unconditional gamma(n) & gamma_c(n) closed forms are 100% kernel-checked in Lean 4.35.0 (5,626 lines across 10 Palomar module-header files, autoImplicit = false, 723 exhaustively audited named & private theorems, 0 sorry, 0 Batteries warnings, strictly [propext, Classical.choice, Quot.sound]) and replayed across all 6 independent kernels plus a live negative kernel-rejection check on sandboxed Ubuntu CI (run 45747471704), independently verified in exact rational arithmetic (L=3..45, 0/1 error) and 80-digit 28-point Richardson extrapolation (< 2.67e-55 error) plus 120-dps stability. Claims no external peer review or external DOI; independent human line-by-line review of Challenge.lean remains open, and Software Heritage Save Code Now awaits manual browser PoW completion.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/multinomial-tv-conjecture/lean && lake exe cache get && lake build && lake env lean VerifyAxioms.lean && lake exe runLinter MultinomialTVConjecture && lake comparator --config comparator.json --paranoid && cd .. && python scripts/verify_conjecture.py && python scripts/stamp_timestamps.py --verify && pytest -v tests/
```
