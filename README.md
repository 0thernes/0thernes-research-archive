# 0thernes Research Archive

[![Archive Cryptographic & Structural Audit](https://github.com/0thernes/0thernes-research-archive/actions/workflows/archive-audit.yml/badge.svg)](https://github.com/0thernes/0thernes-research-archive/actions/workflows/archive-audit.yml)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0006--8168--9648-A6CE39.svg)](https://orcid.org/0009-0006-8168-9648)
[![Lean 4 Verified](https://img.shields.io/badge/Formal_Proofs-Lean_4_%7C_Standard_Axioms-2ea44f.svg)](registry/PAPERS.md)
[![Checksums Verified](https://img.shields.io/badge/Integrity-SHA--256_Manifest-blue.svg)](CHECKSUMS.sha256)

**Permanent, cryptographically audited master vault of all public Lean 4–verified research preprints, embedded build white papers, pure Lean 4 proof suites, frozen PDFs, falsification dossiers, and pinned source repositories authored by Alexander Stephen Donahue (`0thernes LLC`).**

- **Author:** Alexander Stephen Donahue (`Alexander S. Donahue`) · **0thernes LLC**, Spokane, WA, USA
- **ORCID:** [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648)
- **Contact:** `0_0@0thernes.art` · [0thernes.art](https://0thernes.art) · [github.com/0thernes](https://github.com/0thernes)
- **Total Public Repositories Pinned:** **11** (6 standalone research preprints + 5 engineering/build white papers & embedded Lean 4 proof suites)

---

## I. Standalone Research Preprints (`registry/PAPERS.json`)

| ID | Date | Domain | Paper & Frozen PDF | Version | Lean 4 Verification | Evidence & Source Repo |
|---|---|---|---|---|---|---|
| `0TH-2026-006` | 2026-11-20 | Mathematical Statistics | [Resolution and Lean 4 Formal Verification of Conjecture 7.7 on the Second-Order Variance of Multinomial Discrete Total Variation](papers/0TH-2026-006_multinomial-tv-conjecture/Donahue_2026_Conjecture_7_7_Multinomial_TV.pdf) | `v1.0.0` | Lean 4.35.0 / Mathlib (4,960 lines, 19 audited theorems, standard axioms) | [Repo](https://github.com/0thernes/multinomial-tv-conjecture) · [Evidence](papers/0TH-2026-006_multinomial-tv-conjecture/EVIDENCE.md) · [CI](https://github.com/0thernes/multinomial-tv-conjecture/actions/runs/44862576204) |
| `0TH-2026-005` | 2026-11-10 | Quantum Foundations / Statistics | [Contextuality Evidence Lab: Exact Sequential Certificates and a Constructive Setting-Bias Attack](papers/0TH-2026-005_contextuality-evidence-lab/whitepaper.pdf) | `v1.0.0` | Lean 4 finite adaptive-tree & bias-cap proofs (standard axioms) | [Repo](https://github.com/0thernes/contextuality-evidence-lab) · [Evidence](papers/0TH-2026-005_contextuality-evidence-lab/EVIDENCE.md) · [Lab](https://0thernes.github.io/contextuality-evidence-lab/) |
| `0TH-2026-004` | 2026-11-10 | Quantum Foundations / Combinatorics | [Certified exact minima of Kochen-Specker sets inside coordinate pools (31, 33, 18, 29)](papers/0TH-2026-004_kochen-specker-extremal-lab/ks-minimum.pdf) | `v1.0.0` | Pure Lean 4 (no Mathlib) + checked DRUP UNSAT proofs | [Repo](https://github.com/0thernes/kochen-specker-extremal-lab) · [Evidence](papers/0TH-2026-004_kochen-specker-extremal-lab/EVIDENCE.md) · [Site](https://0thernes.github.io/kochen-specker-extremal-lab/) |
| `0TH-2026-003` | 2026-11-10 | Quantum Foundations | [Exact contextuality degrees for disjoint Mermin configurations](papers/0TH-2026-003_contextuality-tensor-lab/contextuality-tensor.pdf) | `v0.1.0` | Lean 4 (153-declaration axiom audit, standard axioms) | [Repo](https://github.com/0thernes/contextuality-tensor-lab) · [Evidence](papers/0TH-2026-003_contextuality-tensor-lab/EVIDENCE.md) · [Lab](https://0thernes.github.io/contextuality-tensor-lab/) |
| `0TH-2026-002` | 2026-11-10 | Quantum Foundations | [Spectral bounds and their limits in Pauli contextuality: exact configurations and a proof of Jonah's Conjecture E](papers/0TH-2026-002_hoggar-bound-lab/unified-contextuality.pdf) | `v1.4.0` | Lean 4.35.0 spectral floor, saturated degrees & all-qubit C3 family | [Repo](https://github.com/0thernes/hoggar-bound-lab) · [Evidence](papers/0TH-2026-002_hoggar-bound-lab/EVIDENCE.md) · [Site](https://0thernes.github.io/hoggar-bound-lab/) |
| `0TH-2026-001` | 2026-11-09 | Quantum Foundations | [A third-moment bound on the contextuality degree of multiqubit Pauli configurations](papers/0TH-2026-001_hoggar-bound/main.pdf) | `v1.0.0` | Lean 4 / Mathlib third-moment & Kramers bounds | [Repo](https://github.com/0thernes/hoggar-bound) · [Evidence](papers/0TH-2026-001_hoggar-bound/EVIDENCE.md) |

Full standalone registry: [`registry/PAPERS.md`](registry/PAPERS.md) · Machine-readable schema: [`registry/PAPERS.json`](registry/PAPERS.json)

---

## II. Build White Papers & Embedded Lean 4 Proof Suites (`registry/BUILD_PAPERS.json`)

Engineering and laboratory builds containing embedded technical white papers, verification audits, and **120 additional live-compiled pure Lean 4 (`v4.35.0`, zero Mathlib, zero `sorry`) machine-checked invariants** (`[propext, Quot.sound]` or zero axioms):

| ID | Date | Build Repo & Version | Embedded Pure Lean 4.35.0 Suite | Archived White Paper / Audit | Dossier |
|---|---|---|---|---|---|
| `0TH-BUILD-001` | 2026-11-19 | [`cellulogonic-mecha`](https://github.com/0thernes/cellulogonic-mecha) `v1.2.0` | **58 audited theorems** (8 files, 1,405 lines, 0 `sorry`) | [WHITE_PAPER.md](builds/0TH-BUILD-001_cellulogonic-mecha/WHITE_PAPER.md) | [Evidence](builds/0TH-BUILD-001_cellulogonic-mecha/EVIDENCE.md) |
| `0TH-BUILD-002` | 2026-11-18 | [`planaria`](https://github.com/0thernes/planaria) `v2.0.0` | **38 audited theorems** (7 files, 976 lines, 0 `sorry`) | [WHITE_PAPER.md](builds/0TH-BUILD-002_planaria/WHITE_PAPER.md) | [Evidence](builds/0TH-BUILD-002_planaria/EVIDENCE.md) |
| `0TH-BUILD-003` | 2026-11-18 | [`ultrametrica`](https://github.com/0thernes/ultrametrica) `v1.0.0` | **24 audited theorems** (5 files, 614 lines, 0 `sorry`) | [WHITE_PAPER.md](builds/0TH-BUILD-003_ultrametrica/WHITE_PAPER.md) | [Evidence](builds/0TH-BUILD-003_ultrametrica/EVIDENCE.md) |
| `0TH-BUILD-004` | 2026-07-01 | [`unsolved-mathematics`](https://github.com/0thernes/unsolved-mathematics) `2026-07-02-qa` | Adversarial QA & Methodology Study (non-Lean) | [Collatz Case Study](builds/0TH-BUILD-004_unsolved-mathematics/WHITEPAPER-COLLATZ-MULTI-MODEL-CASE-STUDY-2026-07-01.md) · [QA Audit](builds/0TH-BUILD-004_unsolved-mathematics/WHITEPAPER-COLLATZ-MULTI-MODEL-CASE-STUDY-2026-07-01-QA-AUDIT-2026-07-02.md) | [Evidence](builds/0TH-BUILD-004_unsolved-mathematics/EVIDENCE.md) |
| `0TH-BUILD-005` | 2026-06-27 | [`cosmogonic-quantum-mechalogodrom`](https://github.com/0thernes/cosmogonic-quantum-mechalogodrom) `v0.14.3` | A-Life Verification Audit PDF (non-Lean) | [cqm-alife-audit.pdf](builds/0TH-BUILD-005_cosmogonic-quantum-mechalogodrom/cqm-alife-audit.pdf) | [Evidence](builds/0TH-BUILD-005_cosmogonic-quantum-mechalogodrom/EVIDENCE.md) |

Full build registry: [`registry/BUILD_PAPERS.md`](registry/BUILD_PAPERS.md) · Machine-readable schema: [`registry/BUILD_PAPERS.json`](registry/BUILD_PAPERS.json)

---

## Non-Negotiable Verification & Epistemic Standards

Every paper and embedded proof suite archived in this vault obeys four strict rules:
1. **Kernel-Checked Proofs:** Formalized claims compile in Lean 4 with zero `sorry`, zero `admit`, zero custom axioms, and explicit `#print axioms` audits strictly within `[propext, Classical.choice, Quot.sound]`.
2. **Independent Falsifiability:** Every entry ships an explicit reproduction and falsification command so any third party can independently test every claim.
3. **Cryptographic Immutability:** Every frozen release PDF and white paper is archived under `papers/` or `builds/`, hashed in [`CHECKSUMS.sha256`](CHECKSUMS.sha256), and matched against the exact pinned Git submodule commit under `repos/`.
4. **Honest Boundaries:** Every dossier explicitly distinguishes kernel-checked theorems, paper proofs, executable counts, AI-assisted authorship under human direction, and remaining open questions. Private repositories remain strictly excluded from this public archive.

---

## Cloning the Full 11-Repository Stack & Running the Cryptographic Audit

```bash
# Clone the archive + all 11 pinned Lean 4 & white-paper repositories
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive

# Verify every SHA-256 digest, ORCID, axiom allowlist, and all 11 submodule pins
python scripts/verify_archive.py
sha256sum -c CHECKSUMS.sha256
```

### Registering Future Standalone Papers

```bash
python scripts/register_paper.py \
  --id 0TH-2026-007 \
  --slug <repo-slug> \
  --title "<Paper Title>" \
  --domain "<Field>" \
  --version v1.0.0 \
  --date YYYY-MM-DD \
  --repo https://github.com/0thernes/<repo-slug> \
  --pdf /path/to/frozen.pdf \
  --ci-url https://github.com/0thernes/<repo-slug>/actions/runs/<id> \
  --core-result "<Concise proved result>" \
  --boundary "<Exact verification boundary>" \
  --falsify "<Reproduction command>"
```
