# Evidence & Falsification Dossier — `0TH-2026-012`

**Title:** Koszul-Veronese Byzantine Private Information Retrieval, MLWE Reduction Tightness, and Machine-Checked Complexity-Barrier Bridges  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Information Theory / Post-Quantum Cryptography / Computational Complexity  
**Version / Date:** `v5.2.0` (2026-11-26)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0, live negative tamper gate & cross-platform CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/coded-pir-mlwe-complexity-lab |
| Pinned Git Submodule | `repos/coded-pir-mlwe-complexity-lab` @ `29a63e7cc8ae9d62584813e07c1d27b981a9768b` |
| GitHub Release | https://github.com/0thernes/coded-pir-mlwe-complexity-lab/releases/tag/v5.2.0 |
| Frozen Archived PDF | `papers/0TH-2026-012_coded-pir-mlwe-complexity-lab/Donahue_2026_coded_pir_mlwe_complexity_frontier.pdf` |
| Frozen PDF SHA-256 | `b8af9b801cf482601daa2de579e06287e293d56149d4601cf92acc859fcf77fd` |
| arXiv / Source Bundle SHA-256 | `2a7d8e0332d4e9b69571fe93d5b01986b1e37ebcd0d9091098cf4f5788e38c78` |
| CI Verification Run | https://github.com/0thernes/coded-pir-mlwe-complexity-lab/actions/runs/46018229865 |
| Software Heritage SWHID | `Pending manual Save Code Now` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Zero-Mathlib Lean 4.35.0 suite (23 files, 16,679 lines, 35 audited declarations + 1,656 TriadFrontier.* axiom-swept declarations under module, six kernels in CI run 46018229865) of formalized PIR/MLWE/complexity results alongside exact multi-precision computational verifiers. Kernel-checked: Koszul-Veronese moment annihilation, Pascal binomial identity, and (6,3,3) arithmetic (T1a); symmetric coded/Byzantine PIR rate inequalities (T1b-T1d); scale-128 polymatroid and 6-subspace F_2^64 retrieval realization at 8/13 > 3/5 (T1e-T1j) upgraded in v5.2.0 by T1k proving standard vector-space HasSpanDim & Steinitz soundness for matRankModP (F_2, F_3) and gf2RankSparse (closing ERRATA L02) plus field-universal 2-file N-server K-MDS flag-private PIR exact zero-error decoding and two-sided colluder-transcript bijection Psi_I (closing S01/A02); ring-universal anti-periodic & m-twisted DFT cancellation, diagonal q^m determinant, and pure-Nat moment/Renyi-2 DPI/tensorization/R_infty inequalities for CBD_eta & 8/9/10/14-bit branchless dyadic samplers (T2a-T2i); exact NIST FIPS 203 Eq. (4.7) Compress_1 margins (T3d, L01 fixed); and characteristic-free rank_F(<2,2,2>)=7 (T3h), substitution bound 2m^2-m (T3i, weaker than Brockett-Dobkin's 2m^2-1), Schwartz-Zippel & Strassen bounds (T3k), Haemers & Lovasz Theta(C_5)=sqrt(5) (T3j), and conditional Z[sqrt(4k+1)] conference-graph capacity instantiated for P_5, P_13, P_17 (T3l). Instantiated outside Lean in Python & ISO C11: explicit F_101 (6,3,3) rate-10/17 witness verified across 20/20 colluding triples (GL_20 flag isos & bit-for-bit bijections) and 10/10 live encode/decode trials; and exact coupled FIPS 203 DFR convolution e^T r - s^T(e_1+c_u) + e_2 + c_v cross-verified by a 90-digit Kronecker exact interval oracle (width < 1e-30 bits, closing S02) matching all three NIST FIPS 203 Table 1 baselines within 0.04 bits (2^-138.77, 2^-164.81, 2^-174.76).

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Lean 4.35.0 (zero Mathlib, 23 files, 16,679 lines, 32 exported theorems T1a-T3l & T1k + prove_all_triad_theorems + non-degenerate concurrent/coplanar P^3(F_5), char-2 & Fin 11 NonVacuity + 10 universal AdversarialTests = 35 audited declarations + programmatic 1,656-declaration Lean.collectAxioms sweep under module via AuditExhaustiveAxioms.lean, zero sorry, zero native_decide; v5.2.0 closes ERRATA L02/L06/L07/S01/A02/S02/H39-H45 with standard vector-space HasSpanDim & Steinitz rank soundness for matRankModP (F_2, F_3) and gf2RankSparse (PivotTrie, all 63 nonempty subsets of T1j) plus field-universal 2-file N-server K-MDS flag-private PIR exact zero-error decoding and two-sided colluder-transcript bijection Psi_I; all 6 independent kernels passed on Ubuntu CI run 46018229865 via lake comparator --config comparator.json --paranoid inside bubblewrap: Lean paranoid, lean4lean (4,691 decls), nanoda, con-leche --verified 4,745 standalone / 4,694 comparator decls, con-ron --verified 4,745 standalone / 4,694 comparator decls, Lean default + live negative kernel-rejection tamper gate rejecting false mlkemCompress1 (1665 + 832) = 1; interactive CSP/WCAG-AA 32-theorem SVG Proof Blueprint deployed on GitHub Pages run 46018229775; Sigstore Rekor logIndex 4149914735 / GitHub attestation 73154309; DigiCert RFC 3161 TSA Serial 0x2BC2018402DCA39EEE29F9AF8293E2ED + 3-calendar Bitcoin OpenTimestamps .ots on MANIFEST.sha256)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/PalomarChallenge.lean, lean/PalomarSolution.lean, lean/TriadFrontier/PIRLinearCerts.lean, lean/TriadFrontier/KoszulTensor.lean, lean/TriadFrontier/StrassenWinograd.lean, lean/TriadFrontier/BrockettDobkin.lean, lean/TriadFrontier/ShannonCapacity.lean, lean/TriadFrontier/AlgebraicComplexity.lean, lean/TriadFrontier/PaleyCapacity.lean, lean/TriadFrontier/NonVacuity.lean, lean/TriadFrontier/AdversarialTests.lean, lean/AuditExhaustiveAxioms.lean, lean/TriadFrontier/LinearRankSoundness.lean, lean/TriadFrontier/PIRProtocol.lean`

## Verification Boundary (Honest Epistemic Scope)

All 32 headline theorems (T1a-T3l & T1k), master conjunction, non-degenerate P^3(F_5)/char-2/Fin 11 NonVacuity witnesses (L06 closed), and 10 universal AdversarialTests boundary refutations (L07 closed) (35 audited declarations + 1,656 TriadFrontier.* declarations swept under module by AuditExhaustiveAxioms.lean, H39 closed) are kernel-checked in zero-Mathlib Lean 4.35.0; all 33 comparator targets and their dependency closure passed 6 kernel checks (5 distinct implementations) via lake comparator --paranoid plus a live negative tamper gate rejecting false mlkemCompress1 (1665 + 832) = 1 on Ubuntu CI run 46018229865 (zero sorry, zero native_decide, lake build --wfail 0 warnings, strictly within [propext, Classical.choice, Quot.sound]; T1e and T2f use [propext] alone). Explicit F_101 (6,3,3) rate-10/17 witness (20/20 GL_20 flag isos, 20/20 bijections, 10/10 live trials), transcendental 60-digit Renyi-2 curves, overflow-free Bai et al. (2018) alpha-sigma optima, exact coupled FIPS 203 DFR convolutions cross-verified by a 90-digit Kronecker exact interval oracle (width < 1e-30 bits; matching NIST Table 1 within 0.04 bits), trigonometric Lovasz theta(C_7) ~ 3.3177, and continuous DFT/QGTL spectra are verified in Tier-2 Python (0 ruff / 0 mypy, 25/25 pytest incl. Draft 2020-12 repo.yaml schema & 16/16 mutants), hardened ISO C11 (88/88 unit + 1,024 fuzz, ASan/UBSan), and Eshkol dual-number AD (<2e-13, 3/3 + 7 negative guards), with 36/36 live HTTP-200 + 30/30 Crossref 0-retraction citations and dual DigiCert RFC 3161 + 3-calendar Bitcoin OTS timestamps. Explicitly affirms that P != NP & explicit circuit lower bounds (CS-001/CS-010), matrix multiplication exponent omega = 2 (CS-004), Valiant VP != VNP (CS-012), non-linear C(2,4,2,2) in [3/5, 8/13] (inequalities in 5 or more variables involving individual storage symbols remain possible), Sun-Tao-Xu-Zhang max-redundancy, general M >= 3 non-LFSR PIR capacity, general T >= 4 zero-error schemes, exact Shannon capacity Theta(C_7) in [sqrt(10), theta(C_7)] (CS-CMP-012), and worst-case quantum MLWE lower bounds (CS-026/QC-042) remain completely OPEN. Claims no external peer review or external DOI; Software Heritage Save Code Now request #2700669 accepted.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/coded-pir-mlwe-complexity-lab && make -C native clean test && ./native/build/triad_cli f101-t3k3 && node eshkol/run_eshkol_ad.mjs && PYTHONPATH=python pytest tests/test_all.py -v && ruff check python tests scripts examples && mypy python/triad_verify scripts --ignore-missing-imports && python scripts/check_readme_axioms.py && python scripts/stamp_timestamps.py --verify && cd lean && lake build --wfail && lake env lean VerifyAxioms.lean && lake env lean AuditExhaustiveAxioms.lean && lake comparator --config comparator.json --paranoid
```
