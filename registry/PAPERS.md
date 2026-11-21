# Master Paper Registry — Tier I: Standalone Research Preprints

**Author:** Alexander Stephen Donahue (0thernes LLC, Spokane, WA, USA)  
**ORCID:** [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648) · **GitHub:** https://github.com/0thernes · **Updated:** `2026-11-21T09:06:23Z`

| ID | Date | Version | Domain | Title | Frozen PDF SHA-256 (prefix) | Repo / Evidence |
|---|---|---|---|---|---|---|
| `0TH-2026-001` | 2026-11-09 | `v1.0.0` | Quantum Foundations / Quantum Contextuality | [A third-moment bound on the contextuality degree of multiqubit Pauli configurations](../papers/0TH-2026-001_hoggar-bound/main.pdf) | `df01bbbd97f9…` | [Repo](https://github.com/0thernes/hoggar-bound) · [Evidence](../papers/0TH-2026-001_hoggar-bound/EVIDENCE.md) |
| `0TH-2026-002` | 2026-11-21 | `v1.5.0` | Quantum Foundations / Quantum Contextuality | [Spectral bounds and their limits in Pauli contextuality: exact configurations and a proof of Jonah's Conjecture E](../papers/0TH-2026-002_hoggar-bound-lab/unified-contextuality.pdf) | `89532166e850…` | [Repo](https://github.com/0thernes/hoggar-bound-lab) · [Evidence](../papers/0TH-2026-002_hoggar-bound-lab/EVIDENCE.md) |
| `0TH-2026-003` | 2026-11-10 | `v0.1.0` | Quantum Foundations / Quantum Contextuality | [Exact contextuality degrees for disjoint Mermin configurations](../papers/0TH-2026-003_contextuality-tensor-lab/contextuality-tensor.pdf) | `2d0f0d2af417…` | [Repo](https://github.com/0thernes/contextuality-tensor-lab) · [Evidence](../papers/0TH-2026-003_contextuality-tensor-lab/EVIDENCE.md) |
| `0TH-2026-004` | 2026-11-10 | `v1.0.0` | Quantum Foundations / Combinatorial Optimization | [Certified exact minima of Kochen-Specker sets inside coordinate pools: 31 and 33 rays in dimension three, 18 in dimension four, 29 in dimension five](../papers/0TH-2026-004_kochen-specker-extremal-lab/ks-minimum.pdf) | `8063949e478c…` | [Repo](https://github.com/0thernes/kochen-specker-extremal-lab) · [Evidence](../papers/0TH-2026-004_kochen-specker-extremal-lab/EVIDENCE.md) |
| `0TH-2026-005` | 2026-11-10 | `v1.0.0` | Quantum Foundations / Statistical Hypothesis Testing | [Contextuality Evidence Lab: Exact Sequential Certificates and a Constructive Setting-Bias Attack](../papers/0TH-2026-005_contextuality-evidence-lab/whitepaper.pdf) | `8e34d2911a7c…` | [Repo](https://github.com/0thernes/contextuality-evidence-lab) · [Evidence](../papers/0TH-2026-005_contextuality-evidence-lab/EVIDENCE.md) |
| `0TH-2026-006` | 2026-11-20 | `v1.0.0` | Mathematical Statistics / Probability Theory | [Resolution and Lean 4 Formal Verification of Conjecture 7.7 on the Second-Order Variance of Multinomial Discrete Total Variation](../papers/0TH-2026-006_multinomial-tv-conjecture/Donahue_2026_Conjecture_7_7_Multinomial_TV.pdf) | `1a2f98651fd5…` | [Repo](https://github.com/0thernes/multinomial-tv-conjecture) · [Evidence](../papers/0TH-2026-006_multinomial-tv-conjecture/EVIDENCE.md) |

---

## 0TH-2026-001 — A third-moment bound on the contextuality degree of multiqubit Pauli configurations

- **Domain:** Quantum Foundations / Quantum Contextuality · **Release:** [`v1.0.0`](https://github.com/0thernes/hoggar-bound/releases/tag/v1.0.0) (2026-11-09)
- **Pinned Commit:** `c74135c429a0ef827c757df5fc76139aed62a819` (`repos/hoggar-bound`)
- **Frozen PDF:** [`papers/0TH-2026-001_hoggar-bound/main.pdf`](../papers/0TH-2026-001_hoggar-bound/main.pdf) (SHA-256: `df01bbbd97f9d1d1a270d9e90b7cbbb848c8b449fe6107a54fd5b77bf764a1c3`)
- **Lean 4 Audit:** Lean 4 / Mathlib · Allowlist: `propext, Classical.choice, Quot.sound`
- **Summary:** Proves a third-moment spectral lower bound on the contextuality degree of N-qubit Pauli configurations with a Kramers refinement for elliptic quadrics, attained on W(5,2) by the Hoggar SIC fiducial, with Lean 4 proofs, independent Python/C verification, and a Moonlab WASM demo.
- **Verification Boundary:** Core spectral bound and numerical corollaries are machine-checked in Lean 4; independent Python/C suites verify finite configurations; superseded/extended into the unified manuscript in 0TH-2026-002 (hoggar-bound-lab).
- **Dossier:** [`EVIDENCE.md`](../papers/0TH-2026-001_hoggar-bound/EVIDENCE.md) · [`METADATA.json`](../papers/0TH-2026-001_hoggar-bound/METADATA.json)

## 0TH-2026-002 — Spectral bounds and their limits in Pauli contextuality: exact configurations and a proof of Jonah's Conjecture E

- **Domain:** Quantum Foundations / Quantum Contextuality · **Release:** [`v1.5.0`](https://github.com/0thernes/hoggar-bound-lab/releases/tag/v1.5.0) (2026-11-21)
- **Pinned Commit:** `5d4f48901812b0265d292ba5db7b76eba657e5a7` (`repos/hoggar-bound-lab`)
- **Frozen PDF:** [`papers/0TH-2026-002_hoggar-bound-lab/unified-contextuality.pdf`](../papers/0TH-2026-002_hoggar-bound-lab/unified-contextuality.pdf) (SHA-256: `89532166e85088b98b157d5521785955c501f1b75e33f53e4d199a4ce58ea203`)
- **Lean 4 Audit:** Lean 4.35.0 / Mathlib v4.35.0 · Allowlist: `propext, Classical.choice, Quot.sound`
- **Summary:** Unified study with complete Lean 4.35.0 formalizations of the spectral floor, Theorem 2 (Kramers / quaternionic floor and elliptic quadrics Q-(2N-1,2)), Theorems 3-4 (5-way saturation equivalences and (2^N-1)|S| = square), exact contextuality degrees (75, 480, 729344) for 4-, 5-, and 7-qubit configurations, a four-qubit cospectral C3 pair with distinct completion spectra, Lemmas 20-21 (Jordan restriction and universal cubic-trace identity), and Theorem 19: a full machine-checked Lean 4 proof of Jonah's Conjecture E across all nine vertex cases (C1, C3, C5, C6, C8, C11, C12, C14, C15) for every N >= 4.
- **Verification Boundary:** As of v1.5.0, the spectral floor, Kramers quaternionic floor, 5-way saturation equivalences, saturated configurations, four-qubit C3 certificate, all-qubit C3 family, Lemmas 20-21, and Theorem 19 (Jonah's Conjecture E in all 9 vertex cases for every N >= 4) are all kernel-checked in Lean 4.35.0 with zero sorry, zero native_decide, and strictly standard axioms [propext, Classical.choice, Quot.sound]. Historical source manuscripts remain preserved inside the repository as component records of this single combined study (see publication/PAPER-MAP.md).
- **Dossier:** [`EVIDENCE.md`](../papers/0TH-2026-002_hoggar-bound-lab/EVIDENCE.md) · [`METADATA.json`](../papers/0TH-2026-002_hoggar-bound-lab/METADATA.json)

## 0TH-2026-003 — Exact contextuality degrees for disjoint Mermin configurations

- **Domain:** Quantum Foundations / Quantum Contextuality · **Release:** [`v0.1.0`](https://github.com/0thernes/contextuality-tensor-lab/releases/tag/v0.1.0) (2026-11-10)
- **Pinned Commit:** `f7a1e6e74f8590d9cee0aa4c01f9ea3800f7fe87` (`repos/contextuality-tensor-lab`)
- **Frozen PDF:** [`papers/0TH-2026-003_contextuality-tensor-lab/contextuality-tensor.pdf`](../papers/0TH-2026-003_contextuality-tensor-lab/contextuality-tensor.pdf) (SHA-256: `2d0f0d2af4177a48d5691286b470b7b14d709646e1d1c4874ce04795408e8b6f`)
- **Lean 4 Audit:** Lean 4 · Allowlist: `propext, Classical.choice, Quot.sound`
- **Summary:** Proves exact arbitrary-copy contextuality degree formulas d_k = (7^k - 5^k)/2 for k disjoint Peres-Mermin squares and (6^k - 4^k)/2 for k Mermin pentagrams under full nonempty-union context families, answering Section 6 of Muller & Saniga (arXiv:2609.19862v1).
- **Verification Boundary:** Exact multiplicative identity and attaining assignments are machine-checked in Lean 4 (153-declaration axiom audit strictly within standard axioms), paired with independent Python and JavaScript exact enumeration.
- **Dossier:** [`EVIDENCE.md`](../papers/0TH-2026-003_contextuality-tensor-lab/EVIDENCE.md) · [`METADATA.json`](../papers/0TH-2026-003_contextuality-tensor-lab/METADATA.json)

## 0TH-2026-004 — Certified exact minima of Kochen-Specker sets inside coordinate pools: 31 and 33 rays in dimension three, 18 in dimension four, 29 in dimension five

- **Domain:** Quantum Foundations / Combinatorial Optimization · **Release:** [`v1.0.0`](https://github.com/0thernes/kochen-specker-extremal-lab/releases/tag/v1.0.0) (2026-11-10)
- **Pinned Commit:** `38108d26776a3356e56fe54b6338902602bf31e1` (`repos/kochen-specker-extremal-lab`)
- **Frozen PDF:** [`papers/0TH-2026-004_kochen-specker-extremal-lab/ks-minimum.pdf`](../papers/0TH-2026-004_kochen-specker-extremal-lab/ks-minimum.pdf) (SHA-256: `8063949e478c41b93913bfd9ff39b2d598c07ed7f0e539af300aa7375f5ae967`)
- **Lean 4 Audit:** Lean 4 (zero Mathlib) · Allowlist: `propext, Classical.choice, Quot.sound`
- **Summary:** Certifies exact minimum Kochen-Specker set sizes inside finite coordinate pools: 31 in 3D integer pools (|c|<=2,3,4), 33 in 3D N-th roots of unity (N=6,12,18,24), 18 in 4D {0,+1,-1}, and 29 in 5D {0,+1,-1}, using Lean 4 proofs and independently checked DRUP unsatisfiability certificates.
- **Verification Boundary:** Bound-2 3D minimum (31) and 4D minimum (18) are kernel-checked in pure Lean 4 without Mathlib; larger pools rest on independently checked DRUP certificates. Explicitly notes the general unrestricted minimal-KS problem remains open.
- **Dossier:** [`EVIDENCE.md`](../papers/0TH-2026-004_kochen-specker-extremal-lab/EVIDENCE.md) · [`METADATA.json`](../papers/0TH-2026-004_kochen-specker-extremal-lab/METADATA.json)

## 0TH-2026-005 — Contextuality Evidence Lab: Exact Sequential Certificates and a Constructive Setting-Bias Attack

- **Domain:** Quantum Foundations / Statistical Hypothesis Testing · **Release:** [`v1.0.0`](https://github.com/0thernes/contextuality-evidence-lab/releases/tag/v1.0.0) (2026-11-10)
- **Pinned Commit:** `ef0682cd24ca248c5e502731c462272a4ac93432` (`repos/contextuality-evidence-lab`)
- **Frozen PDF:** [`papers/0TH-2026-005_contextuality-evidence-lab/whitepaper.pdf`](../papers/0TH-2026-005_contextuality-evidence-lab/whitepaper.pdf) (SHA-256: `8e34d2911a7cc5dc5a02176515364729118fe07cca54d8d9be16e4a818e95743`)
- **Lean 4 Audit:** Lean 4 · Allowlist: `propext, Classical.choice, Quot.sound`
- **Summary:** Proves a finite adaptive-tree sequential contextuality evidence theorem and a sharp setting-bias bound for the Peres-Mermin square, constructing an explicit classical adversary causing a miscalibrated 1% test to reject 97.24% of the time while the bias-aware test stays below 1%.
- **Verification Boundary:** Adaptive-tree evidence bound, biased-setting classical cap (11/12), and counterexample are formally verified in Lean 4; paired with reproducible Moonlab/QGTL/QRNG/Eshkol simulation. Explicitly disclaims hardware contextuality or certified randomness.
- **Dossier:** [`EVIDENCE.md`](../papers/0TH-2026-005_contextuality-evidence-lab/EVIDENCE.md) · [`METADATA.json`](../papers/0TH-2026-005_contextuality-evidence-lab/METADATA.json)

## 0TH-2026-006 — Resolution and Lean 4 Formal Verification of Conjecture 7.7 on the Second-Order Variance of Multinomial Discrete Total Variation

- **Domain:** Mathematical Statistics / Probability Theory · **Release:** [`v1.0.0`](https://github.com/0thernes/multinomial-tv-conjecture/releases/tag/v1.0.0) (2026-11-20)
- **Pinned Commit:** `df6cab4b2b6cef7910f1990234741a328e52ea40` (`repos/multinomial-tv-conjecture`)
- **Frozen PDF:** [`papers/0TH-2026-006_multinomial-tv-conjecture/Donahue_2026_Conjecture_7_7_Multinomial_TV.pdf`](../papers/0TH-2026-006_multinomial-tv-conjecture/Donahue_2026_Conjecture_7_7_Multinomial_TV.pdf) (SHA-256: `1a2f98651fd5fbd5a88a64b8162612ab841ba368fe4fcb112897073f9f15bd16`)
- **Lean 4 Audit:** Lean 4.35.0 / Mathlib v4.35.0 · Allowlist: `propext, Classical.choice, Quot.sound`
- **Summary:** Proves Conjecture 7.7 (conj:atriangle) of Banic & Elezovic (arXiv:2610.17046v1, confirmed open in arXiv:2611.14735v1) via an exact 2D-to-1D combinatorial telescoping reduction, sharp non-asymptotic Stirling bounds, and cubic odd-Gaussian Euler-Maclaurin summation, establishing b_0 = 32*sqrt(3)/(81*pi), b_1 = b_2 = -22*sqrt(3)/(81*pi), d_0 = -4*sqrt(3)/(81*pi), a_triangle = 1/32 - 4*sqrt(3)/243, and gamma_2 = -1/(32*pi) - 8*sqrt(3)/(243*pi), rendering linear gamma(n) and cyclic gamma_c(n) unconditional for n >= 5.
- **Verification Boundary:** Entire proof of Conjecture 7.7, exact nested-sum fidelity check (hAdj_eq_nested_sum), and unconditional gamma(n) & gamma_c(n) closed forms are 100% kernel-checked in Lean 4 (4,960 lines, 0 sorry, standard axioms only), independently verified in exact rational arithmetic (L=3..45, 0/1 error) and 80-digit Richardson extrapolation (< 3e-55 error).
- **Dossier:** [`EVIDENCE.md`](../papers/0TH-2026-006_multinomial-tv-conjecture/EVIDENCE.md) · [`METADATA.json`](../papers/0TH-2026-006_multinomial-tv-conjecture/METADATA.json)
