# Evidence & Falsification Dossier — `0TH-2026-018`

**Title:** Thin Vieta Reflection Groups, Apollonian-Octahedral Reciprocity Obstructions, Integer-Superharmonic Sandpile Envelopes, and Markov-Hurwitz Geodesic Spectra: A Zero-Mathlib Six-Kernel Formalization  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Arithmetic Geometry / Number Theory / Statistical Mechanics / Algebraic Combinatorics / Formal Verification  
**Version / Date:** `v2.1.0` (2026-11-26)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 & cross-platform CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/apollonian-sandpile-markov |
| Pinned Git Submodule | `repos/apollonian-sandpile-markov` @ `94ece6a8dce9c9a30c6a2ada2eb335cb0501f770` |
| GitHub Release | https://github.com/0thernes/apollonian-sandpile-markov/releases/tag/v2.1.0 |
| Frozen Archived PDF | `papers/0TH-2026-018_apollonian-sandpile-markov/Donahue_2026_apollonian_sandpile_markov.pdf` |
| Frozen PDF SHA-256 | `4d3a296d7ceea64e3e288a9d4c225817046b8a5b3094eb28075362c1afc76df1` |
| arXiv / Source Bundle SHA-256 | `eeed90fce4b795f4aab385a77da579c20aafaf2bf9d6998f8af434e512a3f6d4` |
| CI Verification Run | https://github.com/0thernes/apollonian-sandpile-markov/actions/runs/46009124568 |
| Software Heritage SWHID | `swh:1:snp:392d116f12dbe6820df783848373d27bbf138c55` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Unifies three quadratic-Vieta-involution frontiers across 16 machine-checked headline theorems (T1a-T3e + T2f) + master conjunction + expanded NonVacuity + 9 Adversarial refutations in zero-Mathlib Lean 4.35.0 (19 exported decls, 818 declarations exhaustively audited via VerifyAllDecls.lean, full project accepted by lake check --paranoid [59,868-59,871 decls] and all 17 Palomar targets by lake comparator --paranoid [5,231-5,234 decls] + live negative tamper rejection on Ubuntu CI run 46009124568, SLSA #73128469), resolving all 13 paper/doc and 9 Lean findings of the 2026-11-26 statement audit (ERRATA.md) plus 28 additional v2.1.0 three-cycle hardening findings (HARDENING_LOG.md): (I) Descartes Lorentzian form, Gaussian norm (a+b)(a+c)=a^2+k^2 & BQF (T1a), self-contained zero-Mathlib Eisenstein (1844) Gauss Quadratic Reciprocity & supplementary laws (T1b), zero-Mathlib formalization of the HKRS (Annals of Math. 2024) square obstruction for (-3,5,8,8), (-7,17,12,20), (-11,21,24,28), contrasted with rootSquareContrast=(-4,8,9,9) which hits 9 (HKRS list 3n^2, 6n^2, n^4, 4n^4 obstructions for it) (T1c), octahedral 8-reflection mod-8 residue locking on (-6,10,17,40,24,17) excluding squares at b1,b2 and twice-squares at b3,b6 by congruence vs. strip (0,0,1,2,2,1) (T1d; citing Shi et al., arXiv:2510.21702), and Soddy dimension dichotomy (d-1) | 2 <=> d in {2,3} + all five 3D Soddy reflection invariances & square hit 25=5^2 (T1e); (II) Abelian sandpile toppling commutativity, least action bound and uniqueness of legal stabilizing traces without a termination theorem (T2a), direct zero-Mathlib n x n Laplace determinant detMat proving det4 (gridLap 2) = 192 and detMat 9 (gridLap 3) = 100,352 plus legal Dhar traces (T2b; Matrix-Tree link outside Lean), isotropic Z^2 obstruction for 4u = 3(x^2+y^2) + periodic with Laplacian <= 3 via torus summation (T2c), elementary A2 parity lemma with no prior statement found (T2d: M*u = quadratic + periodic with A2 Laplacian <= K = (4A-2B+4C)/M forces K even, excluding K=5 in this class; K=4,2 attained), lattice-polygon edge-normal closure identity (T2e; Kalinin-Shkolnikov theorem not formalized), and direct zero-Mathlib detMat proofs det4 (a2GridLap 2) = 1,092 and detMat 9 (a2GridLap 3) = 5,393,920 plus legal A2 Dhar traces (T2f); and (III) SL2(Z) Fricke-Cohn correspondence with explicit 3 | tr divisibility exported (T3a), pairwise coprimality, odd-prime p = 1 (mod 4) obstruction, and zero-Mathlib formalization of Zhang's theorem (Acta Arith. 128 (2007), arXiv:math/0612620) that every even Markov number is 2 mod 32 with 2 and 34 mod 64 (T3b), universal Hensel sqrt(-1) mod p^k uniqueness (T3c), exchange identities along one 5-step Markov-quiver mutation sequence with subtraction-free numerators and two non-monomial divisions P1, P2 specializing at (1,1,1) to (2,5,29,433,37666) (T3d), and the classical (Hurwitz 1907) n=4 admissible coefficient classification a in {1,4} with parity constraints (T3e). Paired with zero-dependency Rust (Ubuntu/Windows, 6/6 tests, Markov <= 10^7), ISO C11 ASan/UBSan + 100k 7-law fuzz + 7-law coverage-guided libFuzzer, Python exact oracle (`python -m asm_verify`) + 600+ Hypothesis trials + Rust-Python differential + 12/12 pytest + 10/10 (100%) killed mutants (0 ruff, 0 mypy across 10 files, 0 Dependabot alerts), 23/23 live Crossref (update-to & updated-by + title/author overlap) & arXiv citations (0 retractions), 14-page zero-warning AMS-LaTeX PDF with clickable plainurl DOIs + clean-room arXiv tarball + OpenSSL-verified DigiCert RFC 3161 (.tsr) + 3-calendar Bitcoin OpenTimestamps (.ots), live 4-mode GitHub Pages Observatory & Blueprint (safe DOM / WCAG a11y / strict CSP), Software Heritage snapshot swh:1:snp:392d116f12dbe6820df783848373d27bbf138c55 (v2.0.0; Save Code Now API currently gated by Anubis PoW), and 76/76 (100.0%, Core 31/31) Build Standard v1.2.0 compliance.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Pure Lean 4.35.0 (zero Mathlib, 13 Lean module files (12 sorry-free; PalomarChallenge.lean holds 17 intentional sorry stubs), 19 exported audited declarations across T1a-T3e + T2f + master conjunction + NonVacuity + Adversarial (9 refutations) AND all 818 ApollonianSandpileMarkov.* declarations exhaustively axiom-audited via VerifyAllDecls.lean (Lean.collectAxioms) strictly within [propext, Classical.choice, Quot.sound], zero native_decide; entire project accepted by lake check --paranoid inside bubblewrap (lean4lean 59,868 decls, nanoda, con-leche --verified 59,871 decls, con-ron --verified 59,871 decls) AND all 17 Palomar targets accepted by lake comparator --paranoid (lean4lean 5,231 decls, con-leche/con-ron 5,234 decls) + live negative kernel rejection gate on Ubuntu CI run 46009124568; SLSA attestation #73128469)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/PalomarChallenge.lean, lean/PalomarSolution.lean, lean/ApollonianSandpileMarkov/NonVacuity.lean, lean/ApollonianSandpileMarkov/Adversarial.lean`

## Verification Boundary (Honest Epistemic Scope)

All 19 exported audited declarations across Pillars I-III (T1a-T3e + T2f), master conjunction, expanded NonVacuity (incl. all three HKRS roots, lapZ2 <= 3, joint T2d bundle, stabilizing-odometer witnesses, Cohn seed dets), and 9 Adversarial refutations (incl. T2d mean-equation & T2a LegalTrace necessity) — plus all 818 declarations under ApollonianSandpileMarkov.* checked exhaustively by VerifyAllDecls.lean — are kernel-checked in zero-Mathlib Lean 4.35.0 strictly within [propext, Classical.choice, Quot.sound]; the entire project passed lake check --paranoid (lean4lean 59,868 decls, nanoda, con-leche --verified 59,871 decls, con-ron --verified 59,871 decls) and all 17 Palomar targets passed lake comparator --paranoid (5,231-5,234 decls) plus a live negative kernel rejection gate on Ubuntu CI run 46009124568 (zero sorry outside PalomarChallenge.lean, zero native_decide). Finite BFS orbit statistics, 65x65 sandpile identities, and Markov uniqueness up to 10^7 are verified differentially across Rust, ISO C11 (ASan/UBSan + 7-law libFuzzer), and Python. Explicitly affirms that full Apollonian local-global classification, the Matrix-Tree / sandpile-group-order link, the continuum PDE scaling limit of STAT-058, general-composite Markov Uniqueness (NT-083), all-depth cluster formalization, and Hurwitz n >= 5 asymptotics remain OPEN. Claims no external peer review or external DOI.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/apollonian-sandpile-markov && (cd rust && cargo test --release) && PYTHONPATH=python pytest tests/test_all.py -v && PYTHONPATH=python python scripts/mutate.py && python scripts/check_readme_axioms.py && python scripts/audit_repo.py && (cd lean && lake build && lake env lean VerifyAxioms.lean && lake comparator --config comparator.json --paranoid)
```
