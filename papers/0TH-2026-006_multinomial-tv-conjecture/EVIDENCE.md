# Evidence & Falsification Dossier — `0TH-2026-006`

**Title:** Resolution and Lean 4 Formal Verification of Conjecture 7.7 on the Second-Order Variance of Multinomial Discrete Total Variation  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Mathematical Statistics / Probability Theory  
**Version / Date:** `v2.0.0` (2026-11-25)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 & cross-platform CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/multinomial-tv-conjecture |
| Pinned Git Submodule | `repos/multinomial-tv-conjecture` @ `18d95f0f7446f355f54bf9f6a50189b87e88d7d8` |
| GitHub Release | https://github.com/0thernes/multinomial-tv-conjecture/releases/tag/v2.0.0 |
| Frozen Archived PDF | `papers/0TH-2026-006_multinomial-tv-conjecture/Donahue_2026_Conjecture_7_7_Multinomial_TV.pdf` |
| Frozen PDF SHA-256 | `02000c0e996ef47aa7ab46bd523bf189bb05371dae33a22fc2f89f8c64a11a86` |
| arXiv / Source Bundle SHA-256 | `76db6bd1a40a5d62b0ebac96616730aa001cb8f596c71ca599084765851fa806` |
| CI Verification Run | https://github.com/0thernes/multinomial-tv-conjecture/actions/runs/45723630668 |
| Software Heritage SWHID | `Pending manual Save Code Now` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Proves Conjecture 7.7 (conj:atriangle) of Banic & Elezovic (arXiv:2610.17046v1, confirmed open in arXiv:2611.14735v1) via an exact 2D-to-1D combinatorial telescoping reduction, sharp non-asymptotic Stirling bounds, and cubic odd-Gaussian Euler-Maclaurin summation, establishing b_0 = 32*sqrt(3)/(81*pi), b_1 = b_2 = -22*sqrt(3)/(81*pi), d_0 = -4*sqrt(3)/(81*pi), a_triangle = 1/32 - 4*sqrt(3)/243, and gamma_2 = -1/(32*pi) - 8*sqrt(3)/(243*pi), rendering linear gamma(n) and cyclic gamma_c(n) unconditional for n >= 5. Hardened in v2.0.0 with Palomar Challenge/Solution isolation, 18 NonVacuity witnesses, exhaustive 576-theorem axiom audit, 6-kernel Ubuntu bubblewrap CI replay, 24/24 pytest (Hypothesis, negative, mutant-killing, multi-precision 50/80/120 dps), 18/18 live HTTP-200 citations, deterministic standalone arXiv tarball with vector figures, interactive Lean Blueprint, Sigstore Rekor attestation (4114226539), and 100.0% (64/64) Build Standard v1.2.0 compliance.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 / Mathlib v4.35.0 (autoImplicit = false, 10 files, 5,445 lines, 43 explicit #print axioms + exhaustive 576-theorem Lean.collectAxioms audit across MultinomialTV, 18 NonVacuity witnesses, 0 Batteries linter warnings; all 6 independent kernels passed on sandboxed Ubuntu 24.04 CI run 45723630668 via lake comparator --paranoid: Lean paranoid, lean4lean 41,718 decls, Rust nanoda, con-leche 41,721 decls, con-ron 41,721 decls, Lean default; Sigstore Rekor logIndex 4114226539 / GitHub attestation 72417729; interactive Lean Blueprint at /blueprint/)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/MultinomialTVConjecture/NonVacuity.lean`

## Verification Boundary (Honest Epistemic Scope)

Entire proof of Conjecture 7.7, exact nested-sum fidelity check (hAdj_eq_nested_sum), 18 NonVacuity witnesses, and unconditional gamma(n) & gamma_c(n) closed forms are 100% kernel-checked in Lean 4.35.0 (5,445 lines, autoImplicit = false, 576 exhaustively audited theorems, 0 sorry, 0 Batteries warnings, strictly [propext, Classical.choice, Quot.sound]) and replayed across all 6 independent kernels on sandboxed Ubuntu CI (run 45723630668), independently verified in exact rational arithmetic (L=3..45, 0/1 error) and 80-digit 28-point Richardson extrapolation (< 2.67e-55 error). Claims no external peer review or external DOI; Software Heritage Save Code Now awaits manual browser PoW completion.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/multinomial-tv-conjecture/lean && lake exe cache get && lake build && lake env lean VerifyAxioms.lean && lake exe runLinter MultinomialTVConjecture && lake comparator --config comparator.json --paranoid && cd .. && python scripts/verify_conjecture.py && pytest -v tests/
```
