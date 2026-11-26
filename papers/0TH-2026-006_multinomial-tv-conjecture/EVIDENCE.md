# Evidence & Falsification Dossier — `0TH-2026-006`

**Title:** Resolution and Lean 4 Formal Verification of Conjecture 7.7 on the Second-Order Variance of Multinomial Discrete Total Variation  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Mathematical Statistics / Probability Theory  
**Version / Date:** `v2.3.0` (2026-11-26)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0, Palomar module headers, Mathlib style linters, live negative kernel rejection & cross-platform CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/multinomial-tv-conjecture |
| Pinned Git Submodule | `repos/multinomial-tv-conjecture` @ `0a69443e1b663f0874b547481b7395fdd24732c4` |
| GitHub Release | https://github.com/0thernes/multinomial-tv-conjecture/releases/tag/v2.3.0 |
| Frozen Archived PDF | `papers/0TH-2026-006_multinomial-tv-conjecture/Donahue_2026_Conjecture_7_7_Multinomial_TV.pdf` |
| Frozen PDF SHA-256 | `8fec1bf551c89a3e1f3eb9c82cda8f4a2f2fb2c6d4585546bec2289bce4e3623` |
| arXiv / Source Bundle SHA-256 | `670c3812d41ace3e787ff11392946ed1159cb92f049b107be04f30a59f0c80e2` |
| CI Verification Run | https://github.com/0thernes/multinomial-tv-conjecture/actions/runs/45832736228 |
| Software Heritage SWHID | `Pending manual Save Code Now` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Proves Conjecture 7.7 (conj:atriangle) of Banic & Elezovic (arXiv:2610.17046v1, confirmed open in arXiv:2611.14735v1) via an exact 2D-to-1D combinatorial telescoping reduction, sharp non-asymptotic Stirling bounds, and cubic odd-Gaussian Euler-Maclaurin summation, establishing b_0 = 32*sqrt(3)/(81*pi), b_1 = b_2 = -22*sqrt(3)/(81*pi), d_0 = -4*sqrt(3)/(81*pi), a_triangle = 1/32 - 4*sqrt(3)/243, and gamma_2 = -1/(32*pi) - 8*sqrt(3)/(243*pi), rendering linear gamma(n), cyclic gamma_c(n) (n >= 5), and degenerate small-bin gamma(3;N) and gamma(4;N) (Corollary 1.2(i)-(iii)) unconditional. Hardened in v2.3.0 across 54 cumulative classified findings (F-01..F-54 & Playbook v1.3 10-pass scorecard) with Palomar Lean 4.35.0 module headers & weak.linter.mathlibStandardSet = true across all 10 files (Challenge.lean 143 lines, 8 targets, 0 warnings), REUSE SPDX headers, 20 NonVacuity witnesses, exhaustive 730-theorem named+private axiom audit, live negative Lean kernel rejection check + 6-kernel Ubuntu bubblewrap CI replay (run 45832736228, Rekor 4127343821; Release Rekor 4127013616), 34/34 pytest across 3 OSes (CI 45832736195; strict CSP/SRI, LF manifest guard, Markdown link audit, 120-dps precision regression, Hypothesis L=3..45, mutant-killing), SHA-256-verified osv-scanner v2.7.1 (0 CVEs with pygments==2.20.0) + gitleaks, disabled R4 automated-security-fixes, 16/16 live HTTP-200 Crossref/arXiv 0-retraction clickable plainurl citations, 0.00pt max-overfull 20-page AMS-LaTeX PDF + deterministic standalone arXiv tarball, strict-CSP WCAG AA interactive 16-node/53-decl Lean Blueprint, dual DigiCert RFC 3161 (.tsr) + 3-calendar Bitcoin OpenTimestamps (.ots) proofs on 30-artifact LF MANIFEST.sha256, and 100.0% (66/66, Core 29/29) Build Standard v1.2.0 compliance.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 / Mathlib v4.35.0 (autoImplicit = false, weak.linter.mathlibStandardSet = true, Palomar module headers on all 10 files, 5,749 lines = 5,287 library + 462 root/bridge/audit, REUSE SPDX headers, 49 explicit #print axioms + exhaustive 730-theorem Lean.collectAxioms audit across named & module-private MultinomialTV decls, 20 NonVacuity witnesses, 0 compiler/Batteries/Mathlib style-linter warnings; live negative Lean kernel rejection of false aTriangle = 1/32 + all 6 independent kernels passed across 8 isolated Challenge/Solution targets on sandboxed Ubuntu 24.04 CI run 45832736228 via lake comparator --paranoid: Lean paranoid, lean4lean 41,726 decls, Rust nanoda, con-leche 41,729 decls, con-ron 41,729 decls, Lean default; Sigstore Rekor logIndex 4127343821 / GitHub attestation 72689977 & Release v2.3.0 Rekor 4127013616 / attestation 72681720; dual DigiCert RFC 3161 TSA (.tsr) + 3-calendar Bitcoin OpenTimestamps (.ots) on 30-artifact LF MANIFEST.sha256; strict-CSP/SRI WCAG AA interactive Lean Blueprint 53 decls at /blueprint/)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/MultinomialTVConjecture/NonVacuity.lean`

## Verification Boundary (Honest Epistemic Scope)

Entire proof of Conjecture 7.7, exact nested-sum fidelity check (hAdj_eq_nested_sum), 20 NonVacuity witnesses, and unconditional gamma(n), gamma_c(n), gamma(3;N), and gamma(4;N) closed forms (Corollary 1.2(i)-(iii)) are 100% kernel-checked in Lean 4.35.0 (5,749 lines across 10 Palomar module-header files, autoImplicit = false, weak.linter.mathlibStandardSet = true, 730 exhaustively audited named & private theorems, 0 sorry, 0 compiler/Batteries/Mathlib warnings, strictly [propext, Classical.choice, Quot.sound]) and replayed across all 6 independent kernels on all 8 targets plus a live negative kernel-rejection check on sandboxed Ubuntu CI (run 45832736228), independently verified in exact rational arithmetic (L=3..45, 0/1 error) and 80-digit 28-point Richardson extrapolation (< 2.67e-55 error) plus 120-dps stability. Claims no external peer review or external DOI; independent human line-by-line review of Challenge.lean remains open, and Software Heritage Save Code Now awaits manual browser PoW completion.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/multinomial-tv-conjecture/lean && lake exe cache get && lake build && lake env lean VerifyAxioms.lean && lake exe runLinter MultinomialTVConjecture && lake comparator --config comparator.json --paranoid && cd .. && python scripts/verify_conjecture.py && python scripts/stamp_timestamps.py --verify && pytest -v tests/
```
