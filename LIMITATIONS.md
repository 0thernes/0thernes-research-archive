# Limitations, Epistemic Boundaries & Real-vs-Metaphor (`LIMITATIONS.md`)

## 1. What This Master Archive Does and Does Not Guarantee

- **Cryptographic provenance, NOT external peer review:** `0thernes-research-archive` cryptographically locks frozen PDFs, exact Git submodule commits, Lean 4 axiom policies, and CI run links. None of the archived research preprints have undergone external journal peer review unless explicitly recorded with a publisher DOI.
- **No Mega-Atlas grand-problem retirement claimed:** As documented in [`RESULTS.md`](RESULTS.md) and [`registry/SOLVED_AND_ATLAS_BRIDGE.md`](registry/SOLVED_AND_ATLAS_BRIDGE.md) (the archived upstream audit `builds/0TH-BUILD-007_unsolved-problems-mega-atlas/0THERNES_SOLVED_AUDIT_2026-11-25.md` predates the 2026-11-26 statement audit and still says two Vinciguerra questions are resolved), **0 of 2,000** grand open problems in `unsolved-problems-mega-atlas` (`v2.10.0`; `0 of 1,900` in the earlier `v2.5.0` snapshot) are retired by entries in this archive; specialized theorems (such as Conjecture 7.7 of Banić & Elezović in `0TH-2026-006`) are proved within their exact cited scopes.
- **Historical snapshots vs. live repos:** Superseded repositories (`0TH-2026-001`, `002`, `003`, `005`) remain pinned as immutable historical snapshots for provenance while active unified research continues in `0TH-2026-009` (`pauli-contextuality-lab`). Historical `METADATA.json` records may retain earlier version metadata as frozen snapshots.
- **AI-assisted provenance:** Individual papers and builds were produced by solo researcher Alexander Stephen Donahue (`Independent Researcher, Spokane, WA, USA`, ORCID `0009-0006-8168-9648`) with disclosed AI assistance; epistemic trust rests on reproducible kernel verification and falsification commands in each entry's `EVIDENCE.md`.

## 2. Real vs. Metaphor

- **"Vault" / "Frozen":** Literally means committed Git blobs hashed with SHA-256 inside `CHECKSUMS.sha256` and verified on every push by GitHub Actions CI.
- **"Tier I / Tier II / Tier III":** Strict epistemic separation: Tier I holds standalone research preprints; Tier II holds engineering build white papers and embedded Pure Lean invariant suites; Tier III holds architectural laws, pre-registered empirical claims (including null results), finite computational certificates, and open-problem atlases—never conflated with Lean-proved general mathematical theorems.
