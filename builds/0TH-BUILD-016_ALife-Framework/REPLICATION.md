# Replication Protocol (`REPLICATION.md`)

This protocol specifies how any independent researcher or fresh clean-room environment can reproduce every headline claim in `CLAIMS.md`, `README.md`, and `paper/main.tex` (Build Standard v1.2.0 `B43`, `B44`).

## 1. Hardware & Toolchain Requirements

- **Hardware:** Any 64-bit x86_64 or ARM64 CPU, `>= 8 GB` RAM, `>= 2 GB` free disk space (GPU optional; WebGL2 tests fall back cleanly to Canvas2D / SwiftShader).
- **OS Tested:** Windows 11 x64 (`ubuntu-latest` configured in `.github/workflows/ci.yml`; macOS/ARM64 untested locally).
- **Required Toolchains (Pinned):**
  - `Node.js >= 24.12.0` (verified on `v25.8.2`, `npm 11.11.1`)
  - Optional for Lean formal proofs: `Lean v4.35.0` (`elan` reads `lean/lean-toolchain` automatically)
  - Optional for white paper PDF recompilation: `Tectonic 0.17.0` + `Python 3.13` (`matplotlib`, `numpy`)
  - Optional for external binary-export 0-ULP check: `uv` (`pyarrow`, `h5py`, `duckdb`, `numpy`, `openpyxl`)

## 2. Clean-Clone Setup & Reproduction Commands

```bash
git clone https://github.com/0thernes/ALife-Framework.git
cd ALife-Framework
npm ci

# 1. Core build, typecheck, 320+ tests, AST scan, headless run & 13/13 release gates (~30-60s)
npm run verify

# 2. Scope traceability, 100-pass forensic crucible & 12-invariant Laureate audit (~60-90s)
npm run audit:scope
npm run passes:100
npm run audit:science

# 3. Pure Lean 4.35.0 formal verification (82 theorems, ~5-15s)
cd lean
lake build
lake env lean ALifeProofs/VerifyAxioms.lean
lake env leanchecker --fresh ALifeProofs
lake env leanchecker --fresh PalomarSolution
cd ..
npm run audit:axioms

# 4. Indexed 1,000-check hardening audit (~35s) & Build Standard score (~3s)
npm run harden:3x1000
pwsh scripts/Audit-Repo.ps1 -Path .

# 5. Browser Observatory E2E tests (10/10 Playwright Chromium tests, ~25s)
npx playwright install chromium
npm run test:browser
```

## 3. Expected Outputs & Quantitative Tolerances

| Verification Step | Expected Result | Tolerance / Acceptance Criterion |
| --- | --- | --- |
| `npm run scan` | `0` findings across `45` files | Exact `0` findings |
| `npm test` | `100%` tests pass | `0` failures, `0` skipped |
| `npm run verify:release` | `825/825` checks, `100/100` milestones, `13/13` gates | Exact match (`0` gate failures) |
| `npm run passes:100` | `100/100` passes improved, `100/100` Omni-Dome seeds | `maxFirstLawResidual < 1e-12`, `C/N err < 1e-10` |
| `npm run audit:science` | `12/12` invariants passed (`allInvariantsPassed: true`) | `0-ULP` export parity; centered QR rank `= 63` |
| `lake build` + `leanchecker --fresh` | Exit code `0`, `82` theorems, axioms `⊆ [propext, Quot.sound]` | Zero `sorryAx`, zero `Classical.choice`, zero warnings |
| `npm run harden:3x1000` | `1,000 / 1,000 PASS` | `0` failed checks |
| `Audit-Repo.ps1` | Structure `100.0%`, Completion `100.0%`, Core `100.0%` | Exact `100.0%` across all 3 scores |
| `npm run test:browser` | `10/10` Chromium E2E tests | Exact live-vs-headless SHA-256 parity |

## 4. How to Report a Replication

Open an issue using `.github/ISSUE_TEMPLATE/question.yml` labeled `replication` with your OS, CPU, `node -v`, commit SHA, exact commands executed, and any discrepancies from Section 3.

## 5. Replication Log (`B44`)

| Date | Operator / Environment | Commit | Scope Executed | Outcome | Notes / Discrepancies |
| --- | --- | --- | --- | --- | --- |
| 2026-11-25 | Alexander Stephen Donahue — Clean scratch directory copy (Windows 11 x64, Node v25.8.2, Lean v4.35.0, Tectonic 0.17.0, Chromium) | `main` (`v3.0.0`) | Full `npm run verify`, `audit:science`, `passes:100`, `harden:3x1000`, `lake build` + `leanchecker --fresh`, arXiv clean-room tarball recompile, `Audit-Repo.ps1`, `test:browser` | **PASS (100% parity)** | Zero discrepancies; clean-room arXiv tarball compiled with `0` overfull hboxes and `0` undefined refs/citations; external third-party Linux/macOS replications welcome via Issues. |
