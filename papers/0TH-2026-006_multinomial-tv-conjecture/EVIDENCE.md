# Evidence & Falsification Dossier — `0TH-2026-006`

**Title:** Resolution and Lean 4 Formal Verification of Conjecture 7.7 on the Second-Order Variance of Multinomial Discrete Total Variation  
**Author:** Alexander Stephen Donahue (0thernes LLC, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Mathematical Statistics / Probability Theory  
**Version / Date:** `v1.0.0` (2026-11-20)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 100% Lean 4 kernel-verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/multinomial-tv-conjecture |
| Pinned Git Submodule | `repos/multinomial-tv-conjecture` @ `df6cab4b2b6cef7910f1990234741a328e52ea40` |
| GitHub Release | https://github.com/0thernes/multinomial-tv-conjecture/releases/tag/v1.0.0 |
| Frozen Archived PDF | `papers/0TH-2026-006_multinomial-tv-conjecture/Donahue_2026_Conjecture_7_7_Multinomial_TV.pdf` |
| Frozen PDF SHA-256 | `1a2f98651fd5fbd5a88a64b8162612ab841ba368fe4fcb112897073f9f15bd16` |
| arXiv / Source Bundle SHA-256 | `f5b5a415c4d2fa1631708574264837dae61ea672a987586676580910796ebac9` |
| CI Verification Run | https://github.com/0thernes/multinomial-tv-conjecture/actions/runs/44862576204 |
| Software Heritage SWHID | `Pending manual Save Code Now` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Proves Conjecture 7.7 (conj:atriangle) of Banic & Elezovic (arXiv:2610.17046v1, confirmed open in arXiv:2611.14735v1) via an exact 2D-to-1D combinatorial telescoping reduction, sharp non-asymptotic Stirling bounds, and cubic odd-Gaussian Euler-Maclaurin summation, establishing b_0 = 32*sqrt(3)/(81*pi), b_1 = b_2 = -22*sqrt(3)/(81*pi), d_0 = -4*sqrt(3)/(81*pi), a_triangle = 1/32 - 4*sqrt(3)/243, and gamma_2 = -1/(32*pi) - 8*sqrt(3)/(243*pi), rendering linear gamma(n) and cyclic gamma_c(n) unconditional for n >= 5.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 / Mathlib v4.35.0
- **Library Entry Point:** `lean/MultinomialTVConjecture.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`

## Verification Boundary (Honest Epistemic Scope)

Entire proof of Conjecture 7.7, exact nested-sum fidelity check (hAdj_eq_nested_sum), and unconditional gamma(n) & gamma_c(n) closed forms are 100% kernel-checked in Lean 4 (4,960 lines, 0 sorry, standard axioms only), independently verified in exact rational arithmetic (L=3..45, 0/1 error) and 80-digit Richardson extrapolation (< 3e-55 error).

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/multinomial-tv-conjecture/lean && lake build && lake env lean VerifyAxioms.lean && cd .. && python scripts/verify_conjecture.py
```
