# Limitations, Verification Boundaries & Real-vs-Metaphor Table

This document defines the exact epistemic and engineering boundaries of **ALife-Framework v3.0.0** (Build Standard v1.2.0 `B41` and Playbook v1.3).

## 1. Zero Overarching Mega-Atlas Open Problems Retired (`0 / 1,900`)

As audited line-by-line in [docs/MEGA_ATLAS_AUDIT.md](docs/MEGA_ATLAS_AUDIT.md), `ALife-Framework` solves **zero (`0 / 1,900`)** overarching open problems in `0thernes/unsolved-problems-mega-atlas`. Formal Lean proofs verify closed finite algebraic invariants of *this kernel*; finite witnesses (`Hoggar 315 > 189`, `CEGA-18`, `KCBS`, `srg(16,6,2,2)`) reproduce known finite-dimensional separations without resolving their parent mathematical or physical conjectures.

## 2. Explicit Scope of Lean 4.35.0 Proofs vs. Runtime Code

- **Inside Lean 4.35.0 (`82` theorems, `lean/`):** Exact integer micro-joule 11-pool conservation, exact integer 4:1 C/N stoichiometry, basis-point HEPTARCH simplex anti-dictatorship, WCAG `<= 3000 mHz` clamp, CEGA-18 parity impossibility, Hoggar/Tsirelson/KCBS/cospectral integer bounds, `RS[15,11]` MDS/burst & `GF(2^4)` XOR involutivity, Monarch parameter inequality (`p >= 3`), combinatorial Hodge Pythagorean identity, and structural/custody counts.
- **Outside Lean 4.35.0 (verified via differential, property-based, and empirical tests):** IEEE-754 float64 rounding errors in `expDet`/`logDet`/`sinDet`/`cosDet`/`tanhDet`, XPBD soft-body collision PDEs, WebGL2 GLSL shader rendering, and Chromium DOM interactions. See [docs/statement-fidelity.md](docs/statement-fidelity.md).

## 3. Disclosed Scientific & Physical Simplifications

- **FMO ENAQT Honest Förster Caveat:** The 4-chromophore Lindblad-like flora model (`FmoVibronicEnaqtFloraOrgan`) reproduces a non-monotonic dephasing curve $\eta(\gamma)$ with exact density-matrix trace conservation (`< 1e-12`), **and explicitly verifies that classical Förster hopping is NOT beaten at intermediate dephasing** (`tests/frontier-2026-and-100passes.test.ts`). No biological quantum advantage is claimed.
- **Cry4 Radical-Pair Compass:** Reduced 8-state axial Zeeman + hyperfine Haberkorn model demonstrating exact $\Phi_S(\pi - \theta) = \Phi_S(\theta)$ symmetry and lesion collapse; proves nothing about in vivo avian retinal magnetoreception at $313\text{ K}$ / $50\,\mu\text{T}$ (`CHEM-061`).
- **Consciousness & Sentience Indicators (`Butlin-14`, `Frameworks-10`, `CQM-25`):** Executable architectural/functional indicator tests ONLY (`indicatorOnly: true`). Simulated creatures possess **zero** demonstrated phenomenal consciousness, subjective qualia, or moral patienthood (`NEURO-001`, `PHIL-005`).
- **Finite Arena vs. Unbounded Open-Ended Evolution:** Fixed `TypedArray` memory guarantees deterministic zero-GC execution, which mathematically caps maximum state complexity (`AI-045` remains open).

## 4. Untested Platforms, Sample-Size Caveats & Peer-Review Status

- **Tested locally:** Windows 11 x64 (`Node v25.8.2`, `Lean v4.35.0`, `Rust 1.94.1`, `Tectonic 0.17.0`, Playwright Chromium).
- **Untested locally (covered by informational GitHub Actions matrix):** `ubuntu-latest` CI workflow is configured and ready; `macos-latest` and ARM64 (Apple Silicon / Linux `aarch64`) have not yet been executed locally and are explicitly declared untested.
- **Sample sizes:** Paired qualification families use `N = 64` seeds (`L1–L9`) and stress sweeps use `N = 100` seeds (`100..199`); results outside these seed ranges or over million-tick horizons are not exhaustively guaranteed beyond conserved algebraic invariants.
- **Peer review:** Independent solo research release (`Alexander Stephen Donahue`). Not externally peer-reviewed; no unminted DOI or arXiv ID is claimed.

## 5. Literal vs. Metaphor Table (`B41`)

| Term Used in Codebase / UI | Literal Engineering Reality | What It Is NOT (Metaphor Boundary) |
| --- | --- | --- |
| **Creature / Organism / Species (25 clades)** | Deterministic SoA state-vector structs executing closed-loop physics, metabolic ledgers, and control policies. | NOT living biological organisms, sentient beings, or carbon-based cells. |
| **Consciousness Scorecard (`Butlin-14`, `CQM-25`, `PCI*`)** | Automated software ablation tests measuring architectural routing, workspace broadcast, and LZ compression complexity of perturbation traces. | NOT a detector of subjective qualia, suffering, pleasure, or moral patienthood. |
| **Affective State / PAD Jet / Pain / Satiety** | Bounded scalar homeostatic error signals (`indicatorOnly: true`) modulating policy gain and foraging priority. | NOT felt human or animal emotional experience. |
| **HEPTARCH Council (`Surge..Jester`)** | 7-logit capped-simplex convex arbiter (`π_i <= 0.48`, `∑π_i = 1`) preventing single-objective takeover. | NOT conscious sub-personalities or deliberating minds. |
| **Quantum Organ / Bell Twins / Contextuality Witness** | Deterministic linear-algebraic density matrices, exact finite Pauli/KS combinatorial checks, and reduced ODEs on CPU float64. | NOT physical quantum hardware, faster-than-light signaling, or proof of in vivo biological entanglement. |
| **Omni-Dome AAA Observatory** | Clean-room WebGL2 GLSL ES 3.00 signed-distance-field raymarcher (plus Canvas2D fallback) driven directly by live simulation state. | NOT a commercial AAA game engine or photorealistic physical fluid/optics renderer. |
| **100-Pass Crucible / 3×1,000 Hardening** | Automated deterministic regression, defect-reduction, and 1,000-check repository/kernel verification harnesses. | NOT a substitute for external human peer review or independent laboratory replication. |
