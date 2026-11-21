# 0thernes Research Archive

[![Archive Cryptographic & Structural Audit](https://github.com/0thernes/0thernes-research-archive/actions/workflows/archive-audit.yml/badge.svg)](https://github.com/0thernes/0thernes-research-archive/actions/workflows/archive-audit.yml)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0006--8168--9648-A6CE39.svg)](https://orcid.org/0009-0006-8168-9648)
[![Lean 4 Verified](https://img.shields.io/badge/Formal_Proofs-Lean_4_%7C_Standard_Axioms-2ea44f.svg)](registry/PAPERS.md)
[![Checksums Verified](https://img.shields.io/badge/Integrity-SHA--256_Manifest-blue.svg)](CHECKSUMS.sha256)

**Permanent, cryptographically audited master vault of all PUBLIC Lean 4–verified research preprints, embedded build white papers, pure Lean 4 proof suites, architectural laws, pre-registered empirical claims, controlled discoveries, frozen PDFs, falsification dossiers, and pinned source repositories authored by Alexander Stephen Donahue (`0thernes LLC`).**

- **Author:** Alexander Stephen Donahue (`Alexander S. Donahue`) · **0thernes LLC**, Spokane, WA, USA
- **ORCID:** [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648)
- **Contact:** `0_0@0thernes.art` · [0thernes.art](https://0thernes.art) · [github.com/0thernes](https://github.com/0thernes)
- **Scope:** **25 public research entries** across **3 explicitly separated epistemic tiers** + **15 pinned public Git submodules** (strictly excluding private/proprietary repositories and third-party forks).

---

## Tier I — Standalone Formalized Research Preprints (`registry/PAPERS.json`)

| ID | Date | Domain | Paper & Frozen PDF | Version | Lean 4 Verification | Evidence & Source Repo |
|---|---|---|---|---|---|---|
| `0TH-2026-006` | 2026-11-20 | Mathematical Statistics | [Resolution and Lean 4 Formal Verification of Conjecture 7.7 on the Second-Order Variance of Multinomial Discrete Total Variation](papers/0TH-2026-006_multinomial-tv-conjecture/Donahue_2026_Conjecture_7_7_Multinomial_TV.pdf) | `v1.0.0` | Lean 4.35.0 / Mathlib (4,960 lines, 19 audited theorems, standard axioms) | [Repo](https://github.com/0thernes/multinomial-tv-conjecture) · [Evidence](papers/0TH-2026-006_multinomial-tv-conjecture/EVIDENCE.md) · [CI](https://github.com/0thernes/multinomial-tv-conjecture/actions/runs/44862576204) |
| `0TH-2026-005` | 2026-11-10 | Quantum Foundations / Statistics | [Contextuality Evidence Lab: Exact Sequential Certificates and a Constructive Setting-Bias Attack](papers/0TH-2026-005_contextuality-evidence-lab/whitepaper.pdf) | `v1.0.0` | Lean 4 finite adaptive-tree & bias-cap proofs (standard axioms) | [Repo](https://github.com/0thernes/contextuality-evidence-lab) · [Evidence](papers/0TH-2026-005_contextuality-evidence-lab/EVIDENCE.md) · [Lab](https://0thernes.github.io/contextuality-evidence-lab/) |
| `0TH-2026-004` | 2026-11-10 | Quantum Foundations / Combinatorics | [Certified exact minima of Kochen-Specker sets inside coordinate pools (31, 33, 18, 29)](papers/0TH-2026-004_kochen-specker-extremal-lab/ks-minimum.pdf) | `v1.0.0` | Pure Lean 4 (no Mathlib) + checked DRUP UNSAT proofs | [Repo](https://github.com/0thernes/kochen-specker-extremal-lab) · [Evidence](papers/0TH-2026-004_kochen-specker-extremal-lab/EVIDENCE.md) · [Site](https://0thernes.github.io/kochen-specker-extremal-lab/) |
| `0TH-2026-003` | 2026-11-10 | Quantum Foundations | [Exact contextuality degrees for disjoint Mermin configurations](papers/0TH-2026-003_contextuality-tensor-lab/contextuality-tensor.pdf) | `v0.1.0` | Lean 4 (153-declaration axiom audit, standard axioms) | [Repo](https://github.com/0thernes/contextuality-tensor-lab) · [Evidence](papers/0TH-2026-003_contextuality-tensor-lab/EVIDENCE.md) · [Lab](https://0thernes.github.io/contextuality-tensor-lab/) |
| `0TH-2026-002` | 2026-11-21 | Quantum Foundations | [Spectral bounds and their limits in Pauli contextuality: exact configurations and a proof of Jonah's Conjecture E](papers/0TH-2026-002_hoggar-bound-lab/unified-contextuality.pdf) | `v1.6.0` | **Complete Lean 4.35.0** (+7,686 new lines: Kramers, Saturation, Lemmas 20–21, Thm 22, **all 9 vertex cases of Conjecture E for all $N \ge 4$**, Cor 16 & 18; 49 new audited decls, standard axioms) | [Repo](https://github.com/0thernes/hoggar-bound-lab) · [Evidence](papers/0TH-2026-002_hoggar-bound-lab/EVIDENCE.md) · [Site](https://0thernes.github.io/hoggar-bound-lab/) |
| `0TH-2026-001` | 2026-11-09 | Quantum Foundations | [A third-moment bound on the contextuality degree of multiqubit Pauli configurations](papers/0TH-2026-001_hoggar-bound/main.pdf) | `v1.0.0` | Lean 4 / Mathlib third-moment & Kramers bounds | [Repo](https://github.com/0thernes/hoggar-bound) · [Evidence](papers/0TH-2026-001_hoggar-bound/EVIDENCE.md) |

Full Tier I registry: [`registry/PAPERS.md`](registry/PAPERS.md) · Machine-readable schema: [`registry/PAPERS.json`](registry/PAPERS.json)

---

## Tier II — Public Build White Papers & Embedded Pure Lean 4 Suites (`registry/BUILD_PAPERS.json`)

Public engineering and laboratory repositories containing embedded technical white papers, verification audits, and **325 additional live-compiled Lean 4 (`v4.35.0`, zero Mathlib, zero `sorry`) machine-checked invariants** (294 strictly within `[propext, Classical.choice, Quot.sound]` or zero axioms, plus 31 `bv_decide`-reflected bitvector theorems in `autophage`):

| ID | Date | Build Repo & Version | Embedded Pure Lean 4.35.0 Suite | Archived White Paper / Artifact | Dossier |
|---|---|---|---|---|---|
| `0TH-BUILD-001` | 2026-11-21 | [`cellulogonic-mecha`](https://github.com/0thernes/cellulogonic-mecha) `v1.2.1` | **58 audited theorems** (8 files, 1,438 lines, 0 `sorry`) | [Donahue_2026_cellulogonic_mecha.pdf](builds/0TH-BUILD-001_cellulogonic-mecha/Donahue_2026_cellulogonic_mecha.pdf) · [WHITE_PAPER.md](builds/0TH-BUILD-001_cellulogonic-mecha/WHITE_PAPER.md) · [VERIFICATION.md](builds/0TH-BUILD-001_cellulogonic-mecha/VERIFICATION.md) | [Evidence](builds/0TH-BUILD-001_cellulogonic-mecha/EVIDENCE.md) · [CI](https://github.com/0thernes/cellulogonic-mecha/actions/runs/44903924086) |
| `0TH-BUILD-002` | 2026-11-21 | [`planaria`](https://github.com/0thernes/planaria) `v2.1.0` | **38 audited theorems** (7 files, 976 lines, 0 `sorry`) | [Donahue_2026_planaria.pdf](builds/0TH-BUILD-002_planaria/Donahue_2026_planaria.pdf) · [WHITE_PAPER.md](builds/0TH-BUILD-002_planaria/WHITE_PAPER.md) | [Evidence](builds/0TH-BUILD-002_planaria/EVIDENCE.md) |
| `0TH-BUILD-003` | 2026-11-21 | [`ultrametrica`](https://github.com/0thernes/ultrametrica) `v1.2.0` | **71 audited theorems** (6 files, 1,706 lines, 0 `sorry`) | [Donahue_2026_Ultrametrica.pdf](builds/0TH-BUILD-003_ultrametrica/Donahue_2026_Ultrametrica.pdf) · [WHITE_PAPER.md](builds/0TH-BUILD-003_ultrametrica/WHITE_PAPER.md) · [CLAIMS.md](builds/0TH-BUILD-003_ultrametrica/CLAIMS.md) | [Evidence](builds/0TH-BUILD-003_ultrametrica/EVIDENCE.md) · [Lab](https://0thernes.github.io/ultrametrica/) · [CI](https://github.com/0thernes/ultrametrica/actions/runs/44897905339) |
| `0TH-BUILD-004` | 2026-07-01 | [`unsolved-mathematics`](https://github.com/0thernes/unsolved-mathematics) `2026-07-02-qa` | Adversarial QA & Editorial Review (non-Lean) | [Collatz Case Study](builds/0TH-BUILD-004_unsolved-mathematics/WHITEPAPER-COLLATZ-MULTI-MODEL-CASE-STUDY-2026-07-01.md) · [QA Audit](builds/0TH-BUILD-004_unsolved-mathematics/WHITEPAPER-COLLATZ-MULTI-MODEL-CASE-STUDY-2026-07-01-QA-AUDIT-2026-07-02.md) · [Editorial Review](builds/0TH-BUILD-004_unsolved-mathematics/EDITORIAL-REVIEW-WHITEPAPER-2026-07-01.md) | [Evidence](builds/0TH-BUILD-004_unsolved-mathematics/EVIDENCE.md) |
| `0TH-BUILD-005` | 2026-06-27 | [`cosmogonic-quantum-mechalogodrom`](https://github.com/0thernes/cosmogonic-quantum-mechalogodrom) `v0.14.3` | A-Life Verification Audit PDF (non-Lean) | [cqm-alife-audit.pdf](builds/0TH-BUILD-005_cosmogonic-quantum-mechalogodrom/cqm-alife-audit.pdf) | [Evidence](builds/0TH-BUILD-005_cosmogonic-quantum-mechalogodrom/EVIDENCE.md) |
| `0TH-BUILD-006` | 2026-11-10 | [`black-hole-simulation-lab`](https://github.com/0thernes/black-hole-simulation-lab) `main+research` | **8 zero-axiom `rfl` theorems** (`ClassicalGR.lean`, 0 axioms) | [ClassicalGR.lean](builds/0TH-BUILD-006_black-hole-simulation-lab/ClassicalGR.lean) · [M5_SHADOW_ASYMMETRY.md](builds/0TH-BUILD-006_black-hole-simulation-lab/M5_SHADOW_ASYMMETRY.md) | [Evidence](builds/0TH-BUILD-006_black-hole-simulation-lab/EVIDENCE.md) |
| `0TH-BUILD-007` | 2026-11-21 | [`unsolved-problems-mega-atlas`](https://github.com/0thernes/unsolved-problems-mega-atlas) `v2.2.0` | **58 audited theorems** (7 files, 817 lines, 0 `sorry`) | [WHITE_PAPER.md](builds/0TH-BUILD-007_unsolved-problems-mega-atlas/WHITE_PAPER.md) · [RANKING.md](builds/0TH-BUILD-007_unsolved-problems-mega-atlas/RANKING.md) · [VERIFICATION.md](builds/0TH-BUILD-007_unsolved-problems-mega-atlas/VERIFICATION.md) · [DATASHEET.md](builds/0TH-BUILD-007_unsolved-problems-mega-atlas/DATASHEET.md) | [Evidence](builds/0TH-BUILD-007_unsolved-problems-mega-atlas/EVIDENCE.md) · [Web Atlas](https://0thernes.github.io/unsolved-problems-mega-atlas/) |
| `0TH-BUILD-008` | 2026-11-21 | [`cellular-engine-omega`](https://github.com/0thernes/cellular-engine-omega) `v4.2.0` | **61 audited theorems** (12 files, 1,197 lines, 0 `sorry`) | [Frontier Theorems & Conjectures](builds/0TH-BUILD-008_cellular-engine-omega/CELLULAR_BLEEDING_EDGE_THEOREMS_CONJECTURES_AND_HARD_PROBLEMS.md) · [VERIFICATION.md](builds/0TH-BUILD-008_cellular-engine-omega/VERIFICATION.md) | [Evidence](builds/0TH-BUILD-008_cellular-engine-omega/EVIDENCE.md) · [CI](https://github.com/0thernes/cellular-engine-omega/actions/runs/44887931871) |
| `0TH-BUILD-009` | 2026-11-21 | [`autophage`](https://github.com/0thernes/autophage) `v1.0.0` | **31 audited theorems** (1 file, 394 lines, 0 `sorry`, `bv_decide`) | [VERIFICATION.md](builds/0TH-BUILD-009_autophage/VERIFICATION.md) · [ARCHITECTURE.md](builds/0TH-BUILD-009_autophage/ARCHITECTURE.md) | [Evidence](builds/0TH-BUILD-009_autophage/EVIDENCE.md) · [CI](https://github.com/0thernes/autophage/actions/runs/44887958546) |

Full Tier II registry: [`registry/BUILD_PAPERS.md`](registry/BUILD_PAPERS.md) · Machine-readable schema: [`registry/BUILD_PAPERS.json`](registry/BUILD_PAPERS.json)

---

## Tier III — Public Laws, Pre-Registered Empirical Claims, Discoveries & Open-Problem Atlases (`registry/LAWS_AND_DISCOVERIES.json`)

Strictly separated from Lean-proved theorems, Tier III preserves SHA-256-verified snapshots of binding architectural laws, pre-registered empirical falsification tables (including null/falsified results), finite computational certificates, and open-problem catalogues across public repositories:

| ID | Epistemic Tier | Source Repo | Highlights | Dossier |
|---|---|---|---|---|
| `0TH-DISC-001` | `binding_architectural_law_and_meta_analysis` | [`cosmogonic-quantum-mechalogodrom`](https://github.com/0thernes/cosmogonic-quantum-mechalogodrom) | Social Contact Density Law (ADR 0016), CQM-25 Capability Law (ADR 0018), 500-Checkpoint Peer-Review Meta-Analysis | [Evidence](discoveries/0TH-DISC-001_cosmogonic-laws-and-meta-analysis/EVIDENCE.md) |
| `0TH-DISC-002` | `empirical_discovery_ledger` | [`Asmodensius`](https://github.com/0thernes/Asmodensius) | Creature #1 Empirical Discovery Ledger (`DISCOVERIES.md`, 408 lines) & honest null results (`STATUS-R20.md`) | [Evidence](discoveries/0TH-DISC-002_asmodensius-discoveries/EVIDENCE.md) |
| `0TH-DISC-003` | `preregistered_empirical_claims` | [`neuralese`](https://github.com/0thernes/neuralese) | SHA-256-locked pre-registrations & interpretability falsification tables (`v11`–`v14x`) | [Evidence](discoveries/0TH-DISC-003_neuralese-preregistered-claims/EVIDENCE.md) |
| `0TH-DISC-004` | `preregistered_empirical_claims` | [`neuralese-diffusion`](https://github.com/0thernes/neuralese-diffusion) | Cross-modality diffusion interpretability pre-registered claims & negative results (`v1`–`v2`) | [Evidence](discoveries/0TH-DISC-004_neuralese-diffusion-claims/EVIDENCE.md) |
| `0TH-DISC-005` | `finite_computational_certificate_and_open_problem_atlas` | [`unsolved-mathematics`](https://github.com/0thernes/unsolved-mathematics) | 900+ open-problem atlas, finite Odd-Unit Lock Bridge Certificate (proves no part of Collatz) & Failed-Attempts Atlas | [Evidence](discoveries/0TH-DISC-005_unsolved-math-certificates-and-atlas/EVIDENCE.md) |
| `0TH-DISC-006` | `open_problem_catalogue` | [`unsolved-black-hole-problems`](https://github.com/0thernes/unsolved-black-hole-problems) | 16 ranked unsolved black-hole problems with CI citation integrity & 6 truth tiers | [Evidence](discoveries/0TH-DISC-006_unsolved-black-hole-problems/EVIDENCE.md) |
| `0TH-DISC-007` | `technical_synthesis_compendium` | [`glitchling-jam`](https://github.com/0thernes/glitchling-jam) | 29-PDF Master Technical Compendium (1,932 pages distilled) under Principle P1 honesty rules | [Evidence](discoveries/0TH-DISC-007_glitchling-master-compendium/EVIDENCE.md) |
| `0TH-DISC-008` | `architectural_synthesis_report` | [`dimension-omega-singularity`](https://github.com/0thernes/dimension-omega-singularity) | 3×1,000 mechanism architectural synthesis reports (Substrates, High-Weirdness, A-Life) | [Evidence](discoveries/0TH-DISC-008_dimension-omega-3000-catalogs/EVIDENCE.md) |
| `0TH-DISC-009` | `computational_reference_atlas` | [`grimoire-algorithms-of-the-arcane`](https://github.com/0thernes/grimoire-algorithms-of-the-arcane) / [`professional-calculator`](https://github.com/0thernes/professional-calculator) | Closed-form `MATH_STUDY_ATLAS.md` (1,123 tests) & 1,000-algorithm source/verification ledger | [Evidence](discoveries/0TH-DISC-009_math-and-algorithm-atlases/EVIDENCE.md) |
| `0TH-DISC-010` | `formal_addenda_and_provenance_map` | [`hoggar-bound-lab`](https://github.com/0thernes/hoggar-bound-lab) | Provenance map of 3 historical component papers, `CLAIMS.md`, `ADDENDUM-conjecture-e.md`, and v1.6.0 49-declaration axiom log | [Evidence](discoveries/0TH-DISC-010_hoggar-component-map-and-addenda/EVIDENCE.md) |

Full Tier III registry: [`registry/LAWS_AND_DISCOVERIES.md`](registry/LAWS_AND_DISCOVERIES.md) · Machine-readable schema: [`registry/LAWS_AND_DISCOVERIES.json`](registry/LAWS_AND_DISCOVERIES.json)

---

## Non-Negotiable Verification & Epistemic Standards

1. **Kernel-Checked Proofs:** Formalized claims compile in Lean 4 with zero `sorry`, zero `admit`, zero custom axioms, and explicit `#print axioms` audits strictly within `[propext, Classical.choice, Quot.sound]`.
2. **Independent Falsifiability:** Every Tier I & Tier II entry ships an explicit reproduction and falsification command so any third party can independently test every claim.
3. **Cryptographic Immutability:** Every frozen release PDF, Lean certificate, white paper, and discovery snapshot is hashed in [`CHECKSUMS.sha256`](CHECKSUMS.sha256), matched against pinned public Git submodules under `repos/`, and audited by GitHub Actions CI on every push.
4. **Honest Boundaries & Privacy Discipline:** Every dossier explicitly separates kernel-checked theorems, paper proofs, pre-registered empirical claims, finite computational certificates, exploratory syntheses, and open questions. Private repositories and third-party forks remain strictly excluded from this public archive.

---

## Cloning the Full Public Stack & Running the Cryptographic Audit

```bash
# Clone the archive + all 15 pinned PUBLIC Lean 4 & white-paper repositories
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive

# Verify every SHA-256 digest, ORCID, axiom allowlist, and all 15 public submodule pins
python scripts/verify_archive.py
sha256sum -c CHECKSUMS.sha256
```
