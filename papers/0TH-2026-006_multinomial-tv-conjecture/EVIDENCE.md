# Evidence & Falsification Dossier — `0TH-2026-006`

**Title:** Resolution and Lean 4 Formal Verification of Conjecture 7.7 on the Second-Order Variance of Multinomial Discrete Total Variation  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Mathematical Statistics / Probability Theory  
**Version / Date:** `v2.1.0` (2026-11-25)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0, live negative kernel rejection & cross-platform CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/multinomial-tv-conjecture |
| Pinned Git Submodule | `repos/multinomial-tv-conjecture` @ `6b0bca3a1f4b94851a60dd7f95c3ef9a1d228a3f` |
| GitHub Release | https://github.com/0thernes/multinomial-tv-conjecture/releases/tag/v2.1.0 |
| Frozen Archived PDF | `papers/0TH-2026-006_multinomial-tv-conjecture/Donahue_2026_Conjecture_7_7_Multinomial_TV.pdf` |
| Frozen PDF SHA-256 | `6ef5ad0bce4a5e7e00b207d6af76edfb444a3a9a3a3c65ffc06e43f249385ccf` |
| arXiv / Source Bundle SHA-256 | `2893a10972180bcd69919d9d7184c9064b989a2ceefd856cd9fda875ce79e2ba` |
| CI Verification Run | https://github.com/0thernes/multinomial-tv-conjecture/actions/runs/45741323731 |
| Software Heritage SWHID | `Pending manual Save Code Now` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Proves Conjecture 7.7 (conj:atriangle) of Banic & Elezovic (arXiv:2610.17046v1, confirmed open in arXiv:2611.14735v1) via an exact 2D-to-1D combinatorial telescoping reduction, sharp non-asymptotic Stirling bounds, and cubic odd-Gaussian Euler-Maclaurin summation, establishing b_0 = 32*sqrt(3)/(81*pi), b_1 = b_2 = -22*sqrt(3)/(81*pi), d_0 = -4*sqrt(3)/(81*pi), a_triangle = 1/32 - 4*sqrt(3)/243, and gamma_2 = -1/(32*pi) - 8*sqrt(3)/(243*pi), rendering linear gamma(n) and cyclic gamma_c(n) unconditional for n >= 5. Hardened in v2.1.0 across 3 full red-team cycles (29 classified findings F-01..F-29 & Playbook v1.3 10-pass scorecard) with Palomar Challenge/Solution isolation (108 lines), 18 NonVacuity witnesses, exhaustive 576-theorem axiom audit, live negative Lean kernel rejection check + 6-kernel Ubuntu bubblewrap CI replay (run 45741323731, Rekor 4116347212), 28/28 pytest across 3 OSes (Hypothesis L=3..45, negative, mutant-killing, 50/80/120 dps stability, path-leak & Table-1 parity guards), 18/18 live HTTP-200 Crossref 0-retraction citations, 0.00pt max-overfull AMS-LaTeX PDF + deterministic standalone arXiv tarball, interactive 16-node/47-decl Lean Blueprint with dependency-cone highlighting, DigiCert RFC 3161 TSA timestamp on 30-artifact MANIFEST.sha256, and 100.0% (64/64) Build Standard v1.2.0 compliance.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 / Mathlib v4.35.0 (autoImplicit = false, 10 files, 5,445 lines, 43 explicit #print axioms + exhaustive 576-theorem Lean.collectAxioms audit across MultinomialTV, 18 NonVacuity witnesses, 0 Batteries linter warnings; live negative Lean kernel rejection of false aTriangle = 1/32 + all 6 independent kernels passed on sandboxed Ubuntu 24.04 CI run 45741323731 via lake comparator --paranoid: Lean paranoid, lean4lean 41,718 decls, Rust nanoda, con-leche 41,721 decls, con-ron 41,721 decls, Lean default; Sigstore Rekor logIndex 4116347212 / GitHub attestation 72460023; DigiCert RFC 3161 TSA timestamp on 30-artifact MANIFEST.sha256; interactive Lean Blueprint with search & dependency-cone highlighting at /blueprint/)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/MultinomialTVConjecture/NonVacuity.lean`

## Verification Boundary (Honest Epistemic Scope)

Entire proof of Conjecture 7.7, exact nested-sum fidelity check (hAdj_eq_nested_sum), 18 NonVacuity witnesses, and unconditional gamma(n) & gamma_c(n) closed forms are 100% kernel-checked in Lean 4.35.0 (5,445 lines, autoImplicit = false, 576 exhaustively audited theorems, 0 sorry, 0 Batteries warnings, strictly [propext, Classical.choice, Quot.sound]) and replayed across all 6 independent kernels plus a live negative kernel-rejection check on sandboxed Ubuntu CI (run 45741323731), independently verified in exact rational arithmetic (L=3..45, 0/1 error) and 80-digit 28-point Richardson extrapolation (< 2.67e-55 error). Claims no external peer review or external DOI; independent human line-by-line review of Challenge.lean remains open, and Software Heritage Save Code Now awaits manual browser PoW completion.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/multinomial-tv-conjecture/lean && lake exe cache get && lake build && lake env lean VerifyAxioms.lean && lake exe runLinter MultinomialTVConjecture && lake comparator --config comparator.json --paranoid && cd .. && python scripts/verify_conjecture.py && pytest -v tests/
```
