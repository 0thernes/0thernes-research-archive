# ADR 0001: Three-Tier Epistemic Separation and Pinned Submodule Vault Architecture

- **Status:** Accepted
- **Date:** 2026-11-21 (formalized in ADR format 2026-11-25)

## Context
A single researcher producing both standalone machine-checked mathematical preprints, engineering systems with embedded formal invariant proofs, and empirical/exploratory open-problem atlases risks conflating distinct levels of proof rigor if all artifacts sit in one flat bibliography.

## Decision
Separate the public master archive into three machine-readable registries (`registry/PAPERS.json`, `registry/BUILD_PAPERS.json`, `registry/LAWS_AND_DISCOVERIES.json`), require an explicit `verification_boundary` on every entry, pin every public source repository as an exact Git submodule under `repos/`, and lock every frozen artifact with byte-exact SHA-256 digests (`CHECKSUMS.sha256` & `data/MANIFEST.sha256`) verified on every push.

## Consequences
- Readers and auditors can immediately distinguish Lean 4 research proofs (Tier I; six-kernel checks cover each repository's comparator targets, or all default targets where CI runs `lake check --paranoid`) from engineering invariant suites (Tier II) and empirical/atlas registries (Tier III).
- Any upstream tampering or accidental submodule drift immediately fails `scripts/verify_archive.py`.
