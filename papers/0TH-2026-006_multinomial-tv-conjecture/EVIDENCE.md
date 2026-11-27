# Evidence & Falsification Dossier — `0TH-2026-006`

**Title:** Resolution and Lean 4 Formal Verification of Conjecture 7.7 on the Second-Order Variance of Multinomial Discrete Total Variation  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Mathematical Statistics / Probability Theory  
**Version / Date:** `v2.6.0` (2026-11-27)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; Lean 4.35.0, Palomar module headers, Mathlib style linters, leanchecker NonVacuity replay, six comparator checker runs & cross-platform CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/multinomial-tv-conjecture |
| Pinned Git Submodule | `repos/multinomial-tv-conjecture` @ `4d8321fde585821b1aa04864c1c2490380eb4f4f` |
| GitHub Release | https://github.com/0thernes/multinomial-tv-conjecture/releases/tag/v2.6.0 |
| Frozen Archived PDF | `papers/0TH-2026-006_multinomial-tv-conjecture/Donahue_2026_Conjecture_7_7_Multinomial_TV.pdf` |
| Frozen PDF SHA-256 | `7f883fc12dbf9a58fc56828456abbf78a146089ffbdae73ded96e8107992b072` |
| arXiv / Source Bundle SHA-256 | `9cf78415ebd51b0b034da31a725ddeb10b47ee06b9ab92a0bfc3ae8de6ef9d7b` |
| CI Verification Run | https://github.com/0thernes/multinomial-tv-conjecture/actions/runs/45951940106 |
| Software Heritage SWHID | `Pending manual Save Code Now` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Proves Conjecture 7.7 (conj:atriangle), the complete quantitative O(L^-2) remainder of Lemma 7.3 (lemma_7_3_O_inv_sq), and the literal Part 2 Sec. 7.2 n=3 source-expression bridge (gamma3_source_form: q_1(3) - d_0 = -7/(96*pi)) of Banic & Elezovic (unrefereed arXiv v1 preprint arXiv:2610.17046v1, confirmed open in arXiv:2611.14735v1) via an exact 2D-to-1D combinatorial telescoping reduction, sharp non-asymptotic Stirling bounds, and 3rd-/4th-order odd-Gaussian Euler-Maclaurin summation, establishing b_0 = 32*sqrt(3)/(81*pi), b_1 = b_2 = -22*sqrt(3)/(81*pi), d_0 = -4*sqrt(3)/(81*pi), a_triangle = 1/32 - 4*sqrt(3)/243, gamma_2 = -1/(32*pi) - 8*sqrt(3)/(243*pi), and |h_adj(L) - c_L*L - a_* - b_{L mod 3}/L| <= C/L^2 for all L >= 1, removing the sole conjectural input from the Banic-Elezovic formulas for linear gamma(n), cyclic gamma_c(n) (n >= 5), and small-bin gamma(3;N) and gamma(4;N); those variance statements still rest on unformalized theorems of the same unrefereed preprints (Part 2 Thm 7.6, Lemmas 7.2 & 7.5, Sec. 7.2/8; Part 5 Thm 3.10). Hardened in v2.6.0 across 72 cumulative classified findings (F-01..F-72, E-2026-001..019): Palomar Lean 4.35.0 module headers & weak.linter.mathlibStandardSet = true across all 10 files (8,138 lines; Challenge.lean 164 lines, 10 targets incl. Target 9 target_lemma_7_3_O_inv_sq & Target 10 target_gamma3_source_form), 189 author-written theorems and lemmas (894 audited theorem constants, 57 explicit #print axioms), standalone CI leanchecker replay of NonVacuity.lean, six comparator checker runs on Ubuntu bubblewrap CI (run 45951940106, Rekor 4143298863; Release v2.6.0 Rekor 4143181508 verified live via gh attestation verify), 43/43 pytest across 3 OSes (3,000+ Hypothesis examples, 1,140-input p3q_exact vs mpmath.loggamma differential oracle, isolated AST code-mutation runner killing 22/22 mutants across 6 scripts), 16/16 live HTTP-200 Crossref updated-by/title/author & arXiv Atom XML 0-retraction citations, deterministic PDF figures, 0.00pt max-overfull 22-page AMS-LaTeX PDF + clean-room verified arXiv tarball, dual DigiCert RFC 3161 (.tsr) + Bitcoin OpenTimestamps (.ots) on 31-artifact LF MANIFEST.sha256, and non-inflated Audit-Repo scoring honoring B44: partial (98.5% 65/66; Core 100.0% 29/29) pending independent outside human operator replication.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 / Mathlib v4.35.0 (autoImplicit = false, weak.linter.mathlibStandardSet = true, Palomar module headers on all 10 files, 8,138 lines = 7,624 library + 514 root/bridge/audit, REUSE SPDX headers, 57 explicit #print axioms + exhaustive Lean.collectAxioms audit across 189 author-written theorems and lemmas / 894 audited theorem constants, 20 NonVacuity theorems [6 direct hAdj 0..5 definition checks + 14 closed-form corollaries/refutations] replayed standalone via lake env leanchecker MultinomialTVConjecture.NonVacuity, no warnings outside the 10 intentional sorry warnings of statement-only Challenge.lean [164 lines]; all six comparator checker runs passed across 10 isolated Challenge/Solution targets [incl. Target 9 quantitative O(L^-2) Lemma 7.3 target_lemma_7_3_O_inv_sq and Target 10 literal Part 2 Sec. 7.2 n=3 bridge target_gamma3_source_form] on sandboxed Ubuntu CI run 45951940106 at tag v2.6.0 [729416c] via lake comparator --paranoid: Lean paranoid, lean4lean 41,899 decls, Rust nanoda, con-leche 41,902 decls, con-ron 41,902 decls, Lean default; Sigstore Rekor logIndex 4143298863 / GitHub attestation 72967371 & Release v2.6.0 Rekor 4143181508 / attestation 72964668 verified live via gh attestation verify; dual DigiCert RFC 3161 TSA (.tsr) + 3-calendar Bitcoin OpenTimestamps (.ots) on 31-artifact LF MANIFEST.sha256; strict-CSP/SRI WCAG AA interactive Lean Blueprint 17 nodes / 61 decls at /blueprint/; pinned commit 4d8321f is the immediate follow-up recording the verbatim 10-target CI comparator log with byte-identical Lean, PDF, and arXiv tarball)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/MultinomialTVConjecture/NonVacuity.lean`

## Verification Boundary (Honest Epistemic Scope)

Entire proof of Conjecture 7.7, quantitative O(L^-2) Lemma 7.3 remainder (lemma_7_3_O_inv_sq), literal Part 2 Sec. 7.2 n=3 bridge (gamma3_source_form), exact nested-sum fidelity check (hAdj_eq_nested_sum), 20 NonVacuity theorems (6 direct hAdj 0..5 definition checks + 14 closed-form corollaries and proved false-constant refutations incl. adversarial_aTriangle_ne_one_div_32, replayed standalone via lake env leanchecker MultinomialTVConjecture.NonVacuity in CI), and the four algebraic identities behind gamma(n), gamma_c(n), gamma(3;N), and gamma(4;N) (not the variance statements of Corollary 1.2(i)-(iii), which rest on cited, unformalized theorems of unrefereed preprints arXiv:2610.17046v1 and arXiv:2611.14735v1) are kernel-checked in Lean 4.35.0 (8,138 lines across 10 Palomar module-header files, autoImplicit = false, weak.linter.mathlibStandardSet = true, 189 author-written theorems and lemmas / 894 axiom-audited theorem constants, 0 sorry/admit/axiom/native_decide in proof modules, no warnings outside the 10 intentional sorry stubs of statement-only Challenge.lean, strictly [propext, Classical.choice, Quot.sound]) and replayed by the six checker runs of lake comparator --paranoid (Lean kernel in paranoid and default mode, lean4lean 41,899 decls, nanoda, con-leche 41,902 decls, con-ron 41,902 decls) across all 10 targets on sandboxed Ubuntu CI (run 45951940106 at tag v2.6.0 729416c; pinned commit 4d8321f records the verbatim 10-target CI log with identical Lean, PDF, and arXiv tarball), cross-checked in exact rational arithmetic (L=3..45, 0/1 error), 80-digit 28-point Richardson extrapolation (< 2.67e-55 error), 120-dps stability, and 22/22 isolated source-code mutants killed. Claims no external peer review or external DOI; independent human line-by-line review of Challenge.lean and external operator replication (B44: partial, reflected honestly as 98.5% 65/66 in Audit-Repo) remain open, independent session re-audit of the v2.6.0 pin in RESULTS_LEDGER.json is pending, and Software Heritage unauthenticated Save Code Now is currently gated by Anubis PoW (awaiting manual browser submission).

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/multinomial-tv-conjecture/lean && lake exe cache get && lake build && lake env lean VerifyAxioms.lean && lake env leanchecker MultinomialTVConjecture.NonVacuity && lake exe runLinter MultinomialTVConjecture && cd .. && python scripts/verify_conjecture.py && python scripts/check_citations.py && python scripts/stamp_timestamps.py --verify && pytest -v tests/   # Linux only (bubblewrap): cd lean && lake comparator --config comparator.json --paranoid
```
