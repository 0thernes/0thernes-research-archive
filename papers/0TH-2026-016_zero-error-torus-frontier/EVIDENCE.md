# Evidence & Falsification Dossier — `0TH-2026-016`

**Title:** Coset-Quotient Compression, Separation-Graph Barriers, and Multi-Kernel Verified Frontiers for Zero-Error Shannon Capacity  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Combinatorics / Information Theory / Graph Theory / Formal Verification  
**Version / Date:** `v1.0.0` (2026-11-25)  
**Status:** Research preprint (not peer reviewed; AI-assisted under human direction; 6-kernel Lean 4.35.0 & cross-platform CI verified)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/zero-error-torus-frontier |
| Pinned Git Submodule | `repos/zero-error-torus-frontier` @ `af343aaa1701637e23733ac0abd7a8f9b2e22b60` |
| GitHub Release | https://github.com/0thernes/zero-error-torus-frontier/releases/tag/v1.0.0 |
| Frozen Archived PDF | `papers/0TH-2026-016_zero-error-torus-frontier/Donahue_2026_zero_error_torus_frontier.pdf` |
| Frozen PDF SHA-256 | `921cf3b9bf31eeddb2994e12c8e874dda124222fe5ff1a1389467b61aa8f105a` |
| arXiv / Source Bundle SHA-256 | `48bab2ff26b21b04d2cdc23bcfcf7c3e242a6b559c8f6b057a29e711beefa3a6` |
| CI Verification Run | https://github.com/0thernes/zero-error-torus-frontier/actions/runs/45762976065 |
| Software Heritage SWHID | `swh:1:snp:6794c5e91c92e22925244c886095bc5d12d9fb63` |
| Wayback Machine Snapshot | Not yet captured |
| External DOI | None claimed |

## Core Result

Establishes four interconnected, six-kernel Lean 4.35.0 verified advances on zero-error Shannon capacity (Mega-Atlas CS-049): (I) algebraic coset-quotient compression for C_n^{boxtimes 4}, exact double-counting ceilings, the H_BPZ (49-ball) intra-coset port obstruction vs. the subgroup H* = <(1,0,0,2),(0,1,0,4)> (unit-shift privacy for all n >= 15; ball sizes 45 versus 49 evaluated at n = 19, 21, 23, 25), two infinite families of coset-union codes that meet the quotient ceiling (helical H_BPZ for C_{4m+1} with m >= 5 and m = 0 or 1 mod 4; staircase H* for C_{8k+1}, k >= 3, whose sizes equal published values: Baumert et al. 1971 for even k, Codenotti-Gerace-Resta 2003 Theorem 1 for odd k; the n^2-port RichPortSystem for odd k is a separate kernel-checked definition outside the 18-target contract), and the locally-injective Baumert pullback homomorphism C_{p+2}^{boxtimes d} -> C_p^{boxtimes d} with exact factored cardinality; (II) four machine-checked lower bounds: Theta(C_25) >= 12.344196091426841 (p=144) and Theta(C_29) >= 14.319949949077991 (alpha(C_29^{boxtimes 4}) >= 42050), which exceed the largest published values found (Codenotti-Gerace-Resta 2003, Table 1: 23125^(1/4), 42017^(1/4)), and Theta(C_27) >= 13.319390984674515, Theta(C_31) >= 15.308776193986504 (p=2048), which are below the values in that table (31522^(1/4), 54934^(1/4)); (III) an induced 5-cycle inside the 7-letter separation graph G_7, and alpha(G_7) >= 3 with alpha(G_7^d) <= 3^d by a 3-clique cover (hence Theta(G_7)=3), general weighted fractional-clique-cover barrier (46875/2 for C_25), and a two-alphabet, two-graph form of the BPZ combining rule (Tandon arXiv:2608.30273, Proposition 1; the two-sided extension of Tandon's Theorem 1 is not addressed) plus pure-kernel admissibility of the BPZ tables T2a/T3c/T3e/C4a/C4b; and (IV) general Haemers rank theorem over any SimpleField, exact integer orthogonal-handle sandwich theorem, exact Z[sqrt(5)] Lovasz pentagon theorem Theta(C_5)=sqrt(5), and a zero-Mathlib six-kernel-checked proof of Haemers's 1979 Schlafli-graph example (Theta(G_27) <= 3 via Z^8 handle, Theta(G_27^c) <= 7 via 27x7 F_2 factorization, Theta(G_27 boxtimes G_27^c) >= 27 > 21). Audited differentially in stdlib Rust (3 OS), ISO C11 (-Werror, ASan+UBSan, 100k fuzz), and 80-digit Python (3 OS, 15/15 pytest + Hypothesis + mutation kills), 19/19 resolvable identifiers live (20 references; Baumert et al. 1971 has no identifier), 13-page 0-warning/0-overfull AMS-LaTeX PDF + clean-room arXiv tarball, interactive GitHub Pages torus/Schlafli/Blueprint explorer, SLSA #72509203 (Rekor 4119482036), Software Heritage snapshot swh:1:snp:6794c5e91c92e22925244c886095bc5d12d9fb63, and 100.0% (68/68) Build Standard v1.2.0 compliance.

## Lean 4 Formal Verification & Axiom Allowlist

- **Framework:** Pure Lean 4.35.0 (zero Mathlib, 12 sorry-free module files plus the statement-only comparator stub PalomarChallenge.lean (18 intentional sorry, excluded from the default build), 32 audited declarations across T1a-T4d + NonVacuity [7] + AdversarialTests [7] + master Palomar bundle strictly within [propext, Classical.choice, Quot.sound], zero native_decide, chunked 81-ball certificates max depth <= 65; all 18 Palomar targets accepted by all 6 independent kernels on Ubuntu CI run 45762976065 via lake check --paranoid & lake comparator --paranoid: Lean paranoid, lean4lean [4,943 decls], nanoda, con-leche --verified [4,946 decls], con-ron --verified [4,946 decls], Lean default; SLSA attestation #72509203 / Rekor 4119482036)
- **Library Entry Point:** `lean/Solution.lean`
- **Primary Axiom Audit Script:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Additional Audit Scripts:** `lean/Challenge.lean, lean/PalomarChallenge.lean, lean/PalomarSolution.lean, lean/ZeroErrorFrontier/NonVacuity.lean, lean/ZeroErrorFrontier/AdversarialTests.lean`

## Verification Boundary (Honest Epistemic Scope)

All 32 audited declarations (T1a-T4d, 7 NonVacuity, 7 AdversarialTests, master Palomar bundle) are kernel-checked in zero-Mathlib Lean 4.35.0 strictly within [propext, Classical.choice, Quot.sound] across all 6 independent proof kernels on Ubuntu CI run 45762976065 (zero sorry, zero native_decide). Claim C-EX1 (exhaustive n^4 2D subgroup scan for n in {19,21,23,25} showing min ball size 45) is tagged [EXACT-COMP] across Rust/Python rather than universally proved in Lean. Determining exact Theta(C_n) for any odd n >= 7 (Mega-Atlas CS-049) remains explicitly OPEN and is NOT claimed solved. Claims no external peer review or external DOI.

## Independent Reproduction & Falsification Protocol

To verify or attempt to falsify this paper from scratch:

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/zero-error-torus-frontier && (cd rust && cargo test --release && cargo run --release -- --verify-all) && make -C native test sanitize fuzz && PYTHONPATH=python pytest tests/test_all.py -v && python scripts/check_readme_axioms.py && (cd lean && lake build && lake env lean VerifyAxioms.lean && lake comparator --config comparator.json --paranoid)
```
