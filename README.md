# 0thernes Research Archive

[![Archive Cryptographic & Structural Audit](https://github.com/0thernes/0thernes-research-archive/actions/workflows/archive-audit.yml/badge.svg)](https://github.com/0thernes/0thernes-research-archive/actions/workflows/archive-audit.yml)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0006--8168--9648-A6CE39.svg)](https://orcid.org/0009-0006-8168-9648)
[![Lean 4 Verified](https://img.shields.io/badge/Formal_Proofs-Lean_4_%7C_Standard_Axioms-2ea44f.svg)](registry/PAPERS.md)
[![Checksums Verified](https://img.shields.io/badge/Integrity-SHA--256_Manifest-blue.svg)](CHECKSUMS.sha256)

**Permanent, cryptographically audited master vault of all Lean 4–verified papers, frozen release PDFs, falsification protocols, and pinned proof repositories authored by Alexander Stephen Donahue (`0thernes LLC`).**

- **Author:** Alexander Stephen Donahue (`Alexander S. Donahue`) · **0thernes LLC**, Spokane, WA, USA
- **ORCID:** [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648)
- **Contact:** `0_0@0thernes.art` · [0thernes.art](https://0thernes.art) · [github.com/0thernes](https://github.com/0thernes)

---

## Master Catalog of Machine-Checked Papers (`registry/PAPERS.json`)

| ID | Date | Domain | Paper & Frozen PDF | Version | Lean 4 Verification | Evidence & Source Repo |
|---|---|---|---|---|---|---|
| `0TH-2026-006` | 2026-11-20 | Mathematical Statistics | [Resolution and Lean 4 Formal Verification of Conjecture 7.7 on the Second-Order Variance of Multinomial Discrete Total Variation](papers/0TH-2026-006_multinomial-tv-conjecture/Donahue_2026_Conjecture_7_7_Multinomial_TV.pdf) | `v1.0.0` | Lean 4.35.0 / Mathlib (4,960 lines, 19 audited theorems, standard axioms) | [Repo](https://github.com/0thernes/multinomial-tv-conjecture) · [Evidence](papers/0TH-2026-006_multinomial-tv-conjecture/EVIDENCE.md) · [CI](https://github.com/0thernes/multinomial-tv-conjecture/actions/runs/44862576204) |
| `0TH-2026-005` | 2026-11-10 | Quantum Foundations / Statistics | [Contextuality Evidence Lab: Exact Sequential Certificates and a Constructive Setting-Bias Attack](papers/0TH-2026-005_contextuality-evidence-lab/whitepaper.pdf) | `v1.0.0` | Lean 4 finite adaptive-tree & bias-cap proofs (standard axioms) | [Repo](https://github.com/0thernes/contextuality-evidence-lab) · [Evidence](papers/0TH-2026-005_contextuality-evidence-lab/EVIDENCE.md) · [Lab](https://0thernes.github.io/contextuality-evidence-lab/) |
| `0TH-2026-004` | 2026-11-10 | Quantum Foundations / Combinatorics | [Certified exact minima of Kochen-Specker sets inside coordinate pools (31, 33, 18, 29)](papers/0TH-2026-004_kochen-specker-extremal-lab/ks-minimum.pdf) | `v1.0.0` | Pure Lean 4 (no Mathlib) + checked DRUP UNSAT proofs | [Repo](https://github.com/0thernes/kochen-specker-extremal-lab) · [Evidence](papers/0TH-2026-004_kochen-specker-extremal-lab/EVIDENCE.md) · [Site](https://0thernes.github.io/kochen-specker-extremal-lab/) |
| `0TH-2026-003` | 2026-11-10 | Quantum Foundations | [Exact contextuality degrees for disjoint Mermin configurations](papers/0TH-2026-003_contextuality-tensor-lab/contextuality-tensor.pdf) | `v0.1.0` | Lean 4 (153-declaration axiom audit, standard axioms) | [Repo](https://github.com/0thernes/contextuality-tensor-lab) · [Evidence](papers/0TH-2026-003_contextuality-tensor-lab/EVIDENCE.md) · [Lab](https://0thernes.github.io/contextuality-tensor-lab/) |
| `0TH-2026-002` | 2026-11-10 | Quantum Foundations | [Spectral bounds and their limits in Pauli contextuality: exact configurations and a proof of Jonah's Conjecture E](papers/0TH-2026-002_hoggar-bound-lab/unified-contextuality.pdf) | `v1.4.0` | Lean 4.35.0 spectral floor, saturated degrees & all-qubit C3 family | [Repo](https://github.com/0thernes/hoggar-bound-lab) · [Evidence](papers/0TH-2026-002_hoggar-bound-lab/EVIDENCE.md) · [Site](https://0thernes.github.io/hoggar-bound-lab/) |
| `0TH-2026-001` | 2026-11-09 | Quantum Foundations | [A third-moment bound on the contextuality degree of multiqubit Pauli configurations](papers/0TH-2026-001_hoggar-bound/main.pdf) | `v1.0.0` | Lean 4 / Mathlib third-moment & Kramers bounds | [Repo](https://github.com/0thernes/hoggar-bound) · [Evidence](papers/0TH-2026-001_hoggar-bound/EVIDENCE.md) |

Full structured registry: [`registry/PAPERS.md`](registry/PAPERS.md) · Machine-readable schema: [`registry/PAPERS.json`](registry/PAPERS.json)

---

## Companion Lean-Backed Systems & Problem Atlases (Not Standalone Preprints)

- [`0thernes/cellulogonic-mecha`](https://github.com/0thernes/cellulogonic-mecha) — 3D off-lattice developmental embryogenesis & 58 pure Lean 4 proofs.
- [`0thernes/planaria`](https://github.com/0thernes/planaria) — 3D temporal-quantum WebGL2 engine & 38 pure Lean 4 proofs.
- [`0thernes/ultrametrica`](https://github.com/0thernes/ultrametrica) — p-adic AdS/CFT & 24 pure Lean 4 (`v4.35.0`) proofs.
- [`0thernes/unsolved-mathematics`](https://github.com/0thernes/unsolved-mathematics) & [`0thernes/unsolved-black-hole-problems`](https://github.com/0thernes/unsolved-black-hole-problems) — structured open-problem dossiers.

---

## Non-Negotiable Verification & Epistemic Standards

Every paper archived in this vault obeys four strict rules:
1. **Kernel-Checked Proofs:** Formalized claims compile in Lean 4 with zero `sorry`, zero `admit`, zero custom axioms, and explicit `#print axioms` audits strictly within `[propext, Classical.choice, Quot.sound]`.
2. **Independent Falsifiability:** Every entry ships an explicit reproduction and falsification command (exact arithmetic, arbitrary-precision verification, or external DRUP/certificate checkers) so any third party can independently test every claim.
3. **Cryptographic Immutability:** Every frozen release PDF is archived under `papers/<id>_<slug>/`, hashed in [`CHECKSUMS.sha256`](CHECKSUMS.sha256), and matched against the exact pinned Git submodule commit under `repos/<slug>/`.
4. **Honest Boundaries:** Every dossier explicitly distinguishes kernel-checked theorems, paper proofs, executable counts, AI-assisted authorship under human direction, and remaining open questions. Peer review or external DOIs are never claimed unless independently completed.

---

## Cloning the Full Stack & Running the Cryptographic Audit

```bash
# Clone the archive + every pinned Lean 4 & LaTeX paper repository
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive

# Verify every PDF SHA-256, ORCID, axiom allowlist, and submodule commit pin
python scripts/verify_archive.py
sha256sum -c CHECKSUMS.sha256
```

### Registering Future Papers

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
