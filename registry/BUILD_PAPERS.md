# Tier II — Public Build White Papers & Embedded Lean 4 Proof Suites

**Author:** Alexander Stephen Donahue (0thernes LLC) · **ORCID:** [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648)  
**Public Embedded Pure Lean 4.35.0 Proofs Audited:** 290 theorems across 5,498 lines (zero Mathlib, zero `sorry`)  
**Updated:** `2026-11-21T10:36:00Z`

| ID | Date | Repo / Version | Embedded Lean 4 Proofs | Frozen White Paper / Audit | Dossier |
|---|---|---|---|---|---|
| `0TH-BUILD-001` | 2026-11-21 | [`cellulogonic-mecha`](https://github.com/0thernes/cellulogonic-mecha) `v1.2.1` | 58 theorems (8 files, 1438 lines) | [WHITE_PAPER.md](../builds/0TH-BUILD-001_cellulogonic-mecha/WHITE_PAPER.md) | [Evidence](../builds/0TH-BUILD-001_cellulogonic-mecha/EVIDENCE.md) |
| `0TH-BUILD-002` | 2026-11-21 | [`planaria`](https://github.com/0thernes/planaria) `v2.1.0` | 38 theorems (7 files, 976 lines) | [Donahue_2026_planaria.pdf](../builds/0TH-BUILD-002_planaria/Donahue_2026_planaria.pdf) | [Evidence](../builds/0TH-BUILD-002_planaria/EVIDENCE.md) |
| `0TH-BUILD-003` | 2026-11-21 | [`ultrametrica`](https://github.com/0thernes/ultrametrica) `v1.1.0` | 36 theorems (6 files, 642 lines) | [Donahue_2026_Ultrametrica.pdf](../builds/0TH-BUILD-003_ultrametrica/Donahue_2026_Ultrametrica.pdf) | [Evidence](../builds/0TH-BUILD-003_ultrametrica/EVIDENCE.md) |
| `0TH-BUILD-004` | 2026-07-01 | [`unsolved-mathematics`](https://github.com/0thernes/unsolved-mathematics) `2026-07-02-qa` | Audit / Methodology (non-Lean) | [WHITEPAPER-COLLATZ-MULTI-MODEL-CASE-STUDY-2026-07-01.md](../builds/0TH-BUILD-004_unsolved-mathematics/WHITEPAPER-COLLATZ-MULTI-MODEL-CASE-STUDY-2026-07-01.md) | [Evidence](../builds/0TH-BUILD-004_unsolved-mathematics/EVIDENCE.md) |
| `0TH-BUILD-005` | 2026-06-27 | [`cosmogonic-quantum-mechalogodrom`](https://github.com/0thernes/cosmogonic-quantum-mechalogodrom) `v0.14.3` | Audit / Methodology (non-Lean) | [cqm-alife-audit.pdf](../builds/0TH-BUILD-005_cosmogonic-quantum-mechalogodrom/cqm-alife-audit.pdf) | [Evidence](../builds/0TH-BUILD-005_cosmogonic-quantum-mechalogodrom/EVIDENCE.md) |
| `0TH-BUILD-006` | 2026-11-10 | [`black-hole-simulation-lab`](https://github.com/0thernes/black-hole-simulation-lab) `main+research-branch` | 8 theorems (1 files, 34 lines) | [ClassicalGR.lean](../builds/0TH-BUILD-006_black-hole-simulation-lab/ClassicalGR.lean) | [Evidence](../builds/0TH-BUILD-006_black-hole-simulation-lab/EVIDENCE.md) |
| `0TH-BUILD-007` | 2026-11-21 | [`unsolved-problems-mega-atlas`](https://github.com/0thernes/unsolved-problems-mega-atlas) `v2.2.0` | 58 theorems (7 files, 817 lines) | [WHITE_PAPER.md](../builds/0TH-BUILD-007_unsolved-problems-mega-atlas/WHITE_PAPER.md) | [Evidence](../builds/0TH-BUILD-007_unsolved-problems-mega-atlas/EVIDENCE.md) |
| `0TH-BUILD-008` | 2026-11-21 | [`cellular-engine-omega`](https://github.com/0thernes/cellular-engine-omega) `v4.2.0` | 61 theorems (12 files, 1197 lines) | [CELLULAR_BLEEDING_EDGE_THEOREMS_CONJECTURES_AND_HARD_PROBLEMS.md](../builds/0TH-BUILD-008_cellular-engine-omega/CELLULAR_BLEEDING_EDGE_THEOREMS_CONJECTURES_AND_HARD_PROBLEMS.md) | [Evidence](../builds/0TH-BUILD-008_cellular-engine-omega/EVIDENCE.md) |
| `0TH-BUILD-009` | 2026-11-21 | [`autophage`](https://github.com/0thernes/autophage) `v1.0.0` | 31 theorems (1 files, 394 lines) | [VERIFICATION.md](../builds/0TH-BUILD-009_autophage/VERIFICATION.md) | [Evidence](../builds/0TH-BUILD-009_autophage/EVIDENCE.md) |

---

## 0TH-BUILD-001 — CELLULOGONIC MECHA v1.2.1: Non-Equilibrium Chemiosmotic, Elastic-Membrane, Endosymbiotic, Bioelectric & Morphogenetic-GRN Cellular Artificial Life Laboratory with 58 Pure Lean 4.35.0 Proofs

- **Repository:** https://github.com/0thernes/cellulogonic-mecha (`v1.2.1`, pinned `75661bb1b901` at `repos/cellulogonic-mecha`)
- **Lean 4 Audit:** GitHub Actions CI GREEN (run #44894602931, lean4-formal-verify + linux-c11-verify) & local lake build EXIT 0; 58/58 theorems (T01-T58), 0 sorryAx, 0 custom axioms, 0 warnings, strictly within [propext, Classical.choice, Quot.sound]; Software Heritage save #2675182
- **Summary:** Clean-room zero-dependency C11+AVX2 continuous 3D off-lattice cellular artificial life and zero-blueprint developmental embryogenesis laboratory (Build 2 of the 4-build AUTOPHAGE -> Cellulogonic Mecha -> Asmodensius stack). Couples 8-species Chemoton stoichiometry, Canham-Helfrich elastic vesicles (Global Minimax Theorem T16), Mitchell chemiosmosis across 4 planetary solvents, nested serial endosymbiosis, Levin bioelectric colonies, Tardigrade TDP bioglass anhydrobiosis, ATP-pumped GHz Fröhlich-Pokorný microtubules, and 6 developmental embryogenesis mechanisms (3D Wnt/BMP/Shh GPS, conditional GRNs, Steinberg cadherin sorting, Netrin/Slit axon guidance + Hebbian pruning, Hippo + eutelic arrest, ATP-coupled CPG waves), accompanied by 58 pure Lean 4.35.0 theorems, 4-way cross-OS Win64/Linux AVX2/Scalar 0-bit SHA-256 parity (f20e16ec...4f26e918), 24/24 falsification gates + 8/8 planted mutants, N=24 Holm-Bonferroni paired stats, and a 60 FPS WebGL2 3D Observatory.
- **Verification Boundary:** All 58 Lean 4.35.0 theorems (T01-T58) compile cleanly in pure Lean 4 with zero Mathlib, zero native_decide, zero sorry, and strictly standard axioms ([propext, Classical.choice, Quot.sound]). Lean theorems certify exact algebraic/combinatorial invariants of the discrete equations; runtime C11+AVX2 simulation, 4-way Win64/Linux SHA-256 bit-exactness, SHA-256-authenticated .cmbin snapshots, 24 falsification gates + 8 planted mutants, and N=24 paired permutation statistics (p_Holm <= 0.00080) are independently verified by the compiled test suite and Ubuntu CI. Models coarse-grained discrete quanta rather than atomistic wet-lab molecular dynamics; claims no new law of nature.
- **Dossier:** [`EVIDENCE.md`](../builds/0TH-BUILD-001_cellulogonic-mecha/EVIDENCE.md) · [`METADATA.json`](../builds/0TH-BUILD-001_cellulogonic-mecha/METADATA.json)

## 0TH-BUILD-002 — PLANARIA: Progressive Holographic Executable Architecture (.hbin), Multi-Stratum Compilation, Autonomous Control-Flow Anastomosis, and Cryptographic Cellular Quorum

- **Repository:** https://github.com/0thernes/planaria (`v2.1.0`, pinned `b12a1c997161` at `repos/planaria`)
- **Lean 4 Audit:** Build completed successfully (9 jobs); 0 warnings; 0 sorry; all 38 #print axioms within [propext, Classical.choice, Quot.sound] (7 zero-axiom constructive); GitHub CI #44890541291 (3/3 jobs GREEN); Software Heritage save #2675014
- **Summary:** Progressive Holographic Instruction Stratification (.hbin) architecture integrating GF(2^8) Reed-Solomon/Cauchy erasure coding, Depth-8 SHA-256-128 Merkle cellular authentication, Plang compiler, PVM-32 anastomosis VM, 4 compiled living .hbin species, WebGL2 3D temporal-quantum engine, 16-suite falsification harness, Ed25519 attestation, frozen 7-page AMS-LaTeX white paper PDF + standalone arXiv bundle, and 38 pure Lean 4 (v4.35.0) machine-checked proofs.
- **Verification Boundary:** All 38 Lean 4 theorems (covering GF(256) arithmetic, Byzantine quorum thresholds, mitosis bounds, stratum anastomosis, xenograft ABI, and quantum-temporal norm/rewind/combinatorial invariants) compile cleanly in pure Lean 4.35.0 with zero Mathlib, zero native_decide, and zero sorry, strictly within [propext, Classical.choice, Quot.sound]. Runtime JS implementation, Monte Carlo survival curves, and WebGL2 3D engine are separately tested by the 16-suite falsification harness (npm test) and Ubuntu CI.
- **Dossier:** [`EVIDENCE.md`](../builds/0TH-BUILD-002_planaria/EVIDENCE.md) · [`METADATA.json`](../builds/0TH-BUILD-002_planaria/METADATA.json)

## 0TH-BUILD-003 — ULTRAMETRICA: Exact Non-Archimedean Holography, Recursive Adelic Valuation-Residue Symmetries, Tate-Curve BTZ Ollivier-Ricci Curvature, and Lean 4 Formal Verification

- **Repository:** https://github.com/0thernes/ultrametrica (`v1.1.0`, pinned `3fe39163a838` at `repos/ultrametrica`)
- **Lean 4 Audit:** Build completed successfully (7 jobs); 0 sorry; all 36 #print axioms in VerifyAxioms.lean strictly within [propext, Classical.choice, Quot.sound] (14 zero-axiom)
- **Summary:** Zero-dependency computational laboratory, zero-warning AMS-LaTeX white paper PDF, standalone arXiv bundle, and formal framework coupling discrete p-adic QFT on Z_p/p^n Z_p to Bruhat-Tits tree and rotating Tate-curve BTZ holography, verified by 36 pure Lean 4 (v4.35.0) machine-checked proofs and an independent exact-rational (fractions.Fraction & Q(i)) Python falsifier.
- **Verification Boundary:** All 36 audited Lean 4 declarations compile cleanly in pure Lean 4.35.0 with zero Mathlib and zero sorry, strictly within [propext, Classical.choice, Quot.sound] (14 zero-axiom). Independent exact-rational Python checks verify 7,033 conjugate Adelic pairs, 45 BTZ optimal-transport horizons, and exact Q(i) Rank-1 Sherman-Morrison solves with zero rounding error; floating-point FFT/PDE simulations complement the exact discrete algebraic theorems. No empirical discovery of new physical laws of nature is claimed.
- **Dossier:** [`EVIDENCE.md`](../builds/0TH-BUILD-003_ultrametrica/EVIDENCE.md) · [`METADATA.json`](../builds/0TH-BUILD-003_ultrametrica/METADATA.json)

## 0TH-BUILD-004 — Adversarial Verification in AI-Assisted Collatz Research: An Eight-Hour Repository Case Study

- **Repository:** https://github.com/0thernes/unsolved-mathematics (`2026-07-02-qa`, pinned `f32ae6515006` at `repos/unsolved-mathematics`)
- **Lean 4 Audit:** N/A (methodology & adversarial verification study)
- **Summary:** Eight-hour multi-model empirical case study on adversarial QA and artifact grounding in AI-assisted mathematics research, accompanied by an independent QA audit and editorial review inside the Unsolved Mathematics Atlas.
- **Verification Boundary:** Explicitly proves and claims no part of the Collatz Conjecture (status: OPEN). Serves as a reproducible methodological case study grounded in committed git artifacts.
- **Dossier:** [`EVIDENCE.md`](../builds/0TH-BUILD-004_unsolved-mathematics/EVIDENCE.md) · [`METADATA.json`](../builds/0TH-BUILD-004_unsolved-mathematics/METADATA.json)

## 0TH-BUILD-005 — Cosmogonic Quantum Mechalogodrom (CQM): Artificial Life Verification Audit & NHSI Research Papers Ledger

- **Repository:** https://github.com/0thernes/cosmogonic-quantum-mechalogodrom (`v0.14.3`, pinned `b0dcf153b93a` at `repos/cosmogonic-quantum-mechalogodrom`)
- **Lean 4 Audit:** N/A (A-Life verification audit PDF)
- **Summary:** Formal verification audit PDF and NHSI applied-research papers ledger documenting operational functional markers and simulation validation in the Cosmogonic Quantum Mechalogodrom artificial life platform.
- **Verification Boundary:** Explicitly disclaims sentience or consciousness; documents operational simulation markers and code-to-literature provenance.
- **Dossier:** [`EVIDENCE.md`](../builds/0TH-BUILD-005_cosmogonic-quantum-mechalogodrom/EVIDENCE.md) · [`METADATA.json`](../builds/0TH-BUILD-005_cosmogonic-quantum-mechalogodrom/METADATA.json)

## 0TH-BUILD-006 — Black Hole Simulation Lab: Exact Schwarzschild Lean 4 Certificates (ClassicalGR.lean) & Kerr Shadow Asymmetry Analytic Anchors

- **Repository:** https://github.com/0thernes/black-hole-simulation-lab (`main+research-branch`, pinned `050455db866d` at `repos/black-hole-simulation-lab`)
- **Lean 4 Audit:** Live lean 4.35.0 EXIT 0; all 8 rfl theorems depend on ZERO axioms (does not depend on any axioms)
- **Summary:** GR-exact Schwarzschild/Kerr geodesic simulation lab with an 8-theorem zero-axiom Lean 4 certificate (proofs/ClassicalGR.lean on branch cursor/research-archive-and-starfield-b952) verifying photon-sphere u=1/3, critical potential 1/27, b_crit^2=27, ISCO E^2=8/9 & L^2=12, and BPT a=0 -> r=6, paired with exact Bardeen Kerr shadow asymmetry anchors (M5_SHADOW_ASYMMETRY.md) and 20+ GR source cards.
- **Verification Boundary:** ClassicalGR.lean certifies exact rational Schwarzschild algebraic limits by pure kernel definitional reduction (rfl, zero axioms); it explicitly disclaims proving the full Einstein field equations. Kerr shadow asymmetry anchors are closed-form analytic_classical checks.
- **Dossier:** [`EVIDENCE.md`](../builds/0TH-BUILD-006_black-hole-simulation-lab/EVIDENCE.md) · [`METADATA.json`](../builds/0TH-BUILD-006_black-hole-simulation-lab/METADATA.json)

## 0TH-BUILD-007 — Unsolved Problems Mega-Atlas (V2.2.0): A Unified Cross-Disciplinary Taxonomy, 1,855-Node Knowledge Connectome, November 2026 AI Proof-Claim Verification Audit, Offline Hybrid RAG & MCP Server, Karpathy-Style AutoResearch Harness, and Pure Lean 4.35.0 Formal Invariant Suite

- **Repository:** https://github.com/0thernes/unsolved-problems-mega-atlas (`v2.2.0`, pinned `5983f455844c` at `repos/unsolved-problems-mega-atlas`)
- **Lean 4 Audit:** Build completed successfully (9 jobs); 0 warnings; 0 sorry; all 58 #print axioms within [propext, Quot.sound] or empty
- **Summary:** Reproducible cross-disciplinary research infrastructure cataloging 1,855 strictly deduplicated unsolved, open, and hard problems across 8 Macro-Pillars x 28 Superdomains wired into 1 connected 5,597-edge knowledge graph, scored under unified 0thernes CSS (0-100) and Composite Titan Index, paired with a live Nov 20, 2026 AI proof-claim audit (12 unretired claims), Hybrid BM25+Graph-Authority RAG CLI (96.0% MRR@5), zero-dependency 7-tool MCP stdio server, Karpathy-style AutoResearch harness (program.md, immutable evaluate.py, results.tsv), FAIR Croissant 1.0 / RO-Crate 1.1 / Zenodo metadata, 19-test pytest suite, 12 PNG/SVG charts, 163-page vector PDF, GitHub Pages live explorer, and 58 Pure Lean 4.35.0 formal invariants.
- **Verification Boundary:** All 58 Pure Lean 4.35.0 theorems (covering CSS bounds/monotonicity/300-year saturation, Titan Index, Near-Term Leverage, 4-Quadrant and 6-Era partitions, 8x28 taxonomy surjection, finite Handshaking Lemma, cross-partition edge hierarchy, deduplication cardinality bounds, Karpathy AutoResearch anti-reward-hacking keep/discard ratchet, and pairwise delta antisymmetry) compile cleanly with zero Mathlib, zero sorry, and strictly constructive axioms ([propext, Quot.sound] or empty). Explicitly makes ZERO claim to prove or retire any of the 1,855 open problems; quantitative rubric inputs are disclosed solo-human + AI-assisted falsifiable editorial estimates, not peer-reviewed measurements.
- **Dossier:** [`EVIDENCE.md`](../builds/0TH-BUILD-007_unsolved-problems-mega-atlas/EVIDENCE.md) · [`METADATA.json`](../builds/0TH-BUILD-007_unsolved-problems-mega-atlas/METADATA.json)

## 0TH-BUILD-008 — CELLULAR ENGINE OMEGA v4.2: Deep Strata Biophysics, Bio-Frostbite Interaction Nets & Virtual-Cell Singularity with 61 Pure Lean 4.35.0 Theorems

- **Repository:** https://github.com/0thernes/cellular-engine-omega (`v4.2.0`, pinned `9f0802789219` at `repos/cellular-engine-omega`)
- **Lean 4 Audit:** Ubuntu CI GREEN (run 44887931871) & local lake build EXIT 0; 61/61 theorems (O01-O59 + O01b + O41b), 0 sorryAx, strictly [propext, Quot.sound] or empty
- **Summary:** Clean-room native C11+AVX2 16-testbed cellular biophysics and Bio-Frostbite interaction-net engine accompanied by 61 universally quantified pure Lean 4.35.0 theorems (Purcell gauge geometry, Hopfield-Ninio/Eigen proofreading, Turing/Feinberg CRNT, TUR speed limits, C11-to-Lean4 differential trace conservation O59) and 5 frontier cellular treatises.
- **Verification Boundary:** All 61 Lean 4.35.0 theorems compile cleanly in pure Lean 4 with zero Mathlib, zero sorry, and strictly constructive axioms ([propext, Quot.sound] or empty). Theorems certify mathematical invariants and rewrite confluence of the discrete models; runtime C11 execution is verified via 43 falsification gates and 10 planted negative mutants.
- **Dossier:** [`EVIDENCE.md`](../builds/0TH-BUILD-008_cellular-engine-omega/EVIDENCE.md) · [`METADATA.json`](../builds/0TH-BUILD-008_cellular-engine-omega/METADATA.json)

## 0TH-BUILD-009 — AUTOPHAGE v1.0: Bare-Metal Polymorphic x86-64 Galois-Field Genetic Engine with 31 Lean 4.35.0 Formal Theorems

- **Repository:** https://github.com/0thernes/autophage (`v1.0.0`, pinned `185bd16c9c2d` at `repos/autophage`)
- **Lean 4 Audit:** Ubuntu CI GREEN (run 44887958546) & local lean EXIT 0; 31/31 theorems (T01-T30 + T05a), 0 sorry (uses built-in bv_decide reflection on BitVec identities)
- **Summary:** Bare-metal polymorphic x86-64 Galois-field genetic engine with 31 Lean 4.35.0 theorems covering GFNI affine involutions, Weismann roundtrip, GF(256)/Cauchy ECC recovery, 64-bit Toffoli/Fredkin symplectic reversibility and Landauer erasure, 2-adic Strong Triangle Inequality, JIT bounds, and thermodynamic monotonicity.
- **Verification Boundary:** Compiles cleanly in Lean 4.35.0 on Ubuntu CI with 0 sorry and 0 custom user axioms; transparently discloses reliance on Lean 4's built-in bv_decide native bitvector reflection axioms for finite BitVec theorems. Runtime verified by 18 silicon falsification gates and 6 planted negative mutants on Win64 and Linux.
- **Dossier:** [`EVIDENCE.md`](../builds/0TH-BUILD-009_autophage/EVIDENCE.md) · [`METADATA.json`](../builds/0TH-BUILD-009_autophage/METADATA.json)
