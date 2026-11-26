# Build White Paper & Proof Evidence Dossier — `0TH-BUILD-011`

**Title:** Asmodensius-Native v1.1.0: A Freestanding C23, AVX-VNNI, and Pure-Integer CUDA PTX Artificial-Life Engine with 30 Pure Six-Kernel Lean 4.35.0 Formal Invariants  
**Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA, ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648))  
**Domain:** Artificial Life / Systems Engineering / GPU Kernel Verification / Formal Methods  
**Version / Date:** `v1.1.0` (2026-11-26)

## Cryptographic Identity & Provenance

| Field | Value |
|---|---|
| Source Repository | https://github.com/0thernes/asmodensius-native |
| Pinned Git Submodule | `repos/asmodensius-native` @ `67bedd4abb9d03c7b94e70c8bf46f5b5f6893e6d` |
| Archived Artifact | `builds/0TH-BUILD-011_asmodensius-native/Donahue_2026_asmodensius_native.pdf` (from `dist/Donahue_2026_asmodensius_native.pdf`) |
| Artifact SHA-256 | `6e87e375176c00ed0f3ed3cbe56fb1f76eb2129ac45b2bff6ee530c306936eb7` |
| Archived Artifact | `builds/0TH-BUILD-011_asmodensius-native/arxiv_submission.tar.gz` (from `dist/arxiv_submission.tar.gz`) |
| Artifact SHA-256 | `1780ccb2b6b5d9050beba5dda010c7fff36c5af0453393a787829a71d70c9eab` |
| Archived Artifact | `builds/0TH-BUILD-011_asmodensius-native/AsmodensiusProofs.lean` (from `lean/AsmodensiusProofs.lean`) |
| Artifact SHA-256 | `33aac74ff22b6b6240d8068f4d186bad1fe29b2cdfac5e515e00952db23fe62a` |
| Archived Artifact | `builds/0TH-BUILD-011_asmodensius-native/AGENTS.md` (from `AGENTS.md`) |
| Artifact SHA-256 | `6ce72bfe1eeea640bed2bd5fd9d2073b82141a882d9927c55dbdca30db1594e8` |
| Archived Artifact | `builds/0TH-BUILD-011_asmodensius-native/CLAIMS.md` (from `CLAIMS.md`) |
| Artifact SHA-256 | `e7ac06988c57e044abd02fb7d9d7d36e64bb8576082a868ec08df9da091359f6` |
| Archived Artifact | `builds/0TH-BUILD-011_asmodensius-native/HARDENING_LOG.md` (from `HARDENING_LOG.md`) |
| Artifact SHA-256 | `9ba14290194f3f143a33703a805ea86364bcf22353302a82eecc4a7099bfd513` |
| Archived Artifact | `builds/0TH-BUILD-011_asmodensius-native/MEGA_ATLAS_CROSSCHECK.md` (from `docs/MEGA_ATLAS_CROSSCHECK.md`) |
| Artifact SHA-256 | `fda66dabe724f1c48daebc28e9b9abcb5a367fdb2fac2fba7beaee89c3d9e739` |
| Archived Artifact | `builds/0TH-BUILD-011_asmodensius-native/lean4-asmodensius-audit.txt` (from `results/lean4-asmodensius-audit.txt`) |
| Artifact SHA-256 | `ecf8ca73327437ae478afe61a58167174c9c39349820b8479edba624cc7f252c` |
| Archived Artifact | `builds/0TH-BUILD-011_asmodensius-native/lean4-multi-kernel.txt` (from `results/lean4-multi-kernel.txt`) |
| Artifact SHA-256 | `25eb27e9eba9b838a5dd43b401e33107e7f30510a43c005d28aeb82844bb0652` |

## Summary

Hardened through 3 full audit cycles under dual Apache-2.0 / CC-BY-4.0 licenses and 100.0% (74/74, 31/31 Core) Build Standard v1.2.0 compliance: Windows-native freestanding ISO C23 artificial-life engine (22 core modules, zero libc/heap/FP ops in core/, 4 NASM AVX2/AVX-VNNI twins, Clang 21 nvptx64 pure-integer CUDA PTX module) scaling 1 to 1,004,019 page-locked organisms with bit-exact lab replay across scalar C, 24-core AVX-VNNI, and RTX 5070 Ti GPU. Verified by 77/77 CTest targets, 164/164 test_gpu differential checks, 30 pure Lean 4.35.0 Palomar theorems (A01-A30) across all 6 independent kernels, 9-page zero-overflow AMS-LaTeX PDF (17/17 live refs), SLSA #72476291, and honest 0/1,900 Mega-Atlas cross-check.

## Embedded Lean 4 Proof Suite Audit

- **Framework:** Pure Lean 4.35.0 (Palomar module headers, zero Mathlib, autoImplicit = false, zero native_decide, 6-kernel bubblewrap lake check --paranoid & 30-theorem lake comparator --paranoid)
- **Lean Modules / Lines:** 7 files / 534 lines
- **Audited Theorems (`#print axioms`):** 30
- **Entry Point:** `lean/VerifyAxioms.lean`
- **Permitted Axioms:** `propext, Classical.choice, Quot.sound`
- **Live Audit Status:** GitHub Actions CI GREEN (run #45748401683, 4/4 jobs: Windows README-axiom and offline-citation check + Lean build + Build Standard v1.2.0 100.0% 74/74 + 9-page 0-overfull Tectonic AMS-LaTeX PDF & clean-room arXiv tarball with 17/17 live citations + SLSA provenance #72476291 / Rekor 4117160172 + 6-kernel bubblewrap lake check --paranoid & lake comparator --paranoid across lean4, leanchecker-paranoid, lean4lean, nanoda_bin, con-leche, con-ron); local Win64 77/77 CTest + 164/164 test_gpu (0 differing bits over 1M brains & 1M kinematics lanes) + live 24C == RTX 5070 Ti GPU hash parity; Release v1.1.0 & SWH snapshot swh:1:snp:08a957772115194b51a4eadb77331b8bab261773 archived; 30/30 audited theorems (A01-A30 incl. NonVacuity & sharp guard-boundary refutations) strictly within [propext, Classical.choice, Quot.sound], 0 sorryAx outside isolated Challenge.lean, 0 warnings

## Verification Boundary

All 30 Lean 4.35.0 theorems (A01-A30 across 7 files / 534 lines) prove discrete conservation, guard-boundary, ABI-constant, Philox-key and VRAM-offset properties of abstract Nat models (about 14 of the 30 are constant identities, literal arithmetic such as 1 + 1 = 2, or conclusions that restate their hypotheses) with zero Mathlib, zero native_decide, zero sorry outside isolated Challenge.lean, and strictly [propext, Classical.choice, Quot.sound], verified across all 6 independent kernels on Ubuntu CI (#45748401683, SLSA #72476291 / Rekor 4117160172). Native C23/NASM/CUDA PTX execution, 77/77 CTest, 164/164 test_gpu, and bare-metal benchmarks (honestly disclosing PCIe/compaction overhead where 24C CPU beats GPU at 1M founders) lie outside the Lean kernel. Explicitly disclaims sentience, biological life, peer review, and retires 0/1,900 overarching Mega-Atlas open problems.

## Independent Reproduction & Falsification Protocol

```bash
git clone --recursive https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
cd repos/asmodensius-native && python3 scripts/check_readme_axioms.py && (cd lean && lake build && lake build Challenge && lake env lean VerifyAxioms.lean && lake check --paranoid && lake comparator --config comparator.json --paranoid)
```
