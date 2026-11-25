# AGENTS.md — Canonical Agent Instructions (`0thernes-research-archive`)

This file is the canonical instruction file for all AI agents (`CLAUDE.md`, `GEMINI.md`, and `.cursor/rules/build-standard.mdc` point here).

## Mission & Identity

- **Repository:** `https://github.com/0thernes/0thernes-research-archive`
- **Author:** Alexander Stephen Donahue (`Independent Researcher, Spokane, WA, USA`, ORCID `0009-0006-8168-9648`, `0_0@0thernes.art`). Do NOT assert an unformed LLC entity in new headers or metadata.
- **Privacy Firewall (MANDATORY):** NEVER register, mention, or submodule private repositories or third-party forks. Every entry MUST be `PUBLIC`.

## Hard Rules (`R1`–`R8`)

1. Commit and push straight to `main` (`R1`/`R2`); CI is informational (`R3`); zero banned files such as `PULL_REQUEST_TEMPLATE.md` or `dependabot.yml` (`R4`).
2. Never fabricate SHA-256 digests, CI run URLs, DOIs, or peer-review status (`R6`).
3. Always run `python3 scripts/verify_archive.py --sync` after updating any PDF, artifact, or submodule pin, and copy `CHECKSUMS.sha256` to `data/MANIFEST.sha256`.
4. Classify every defect into one of the 10 Build Standard classes (`R7`; `docs/glossary.md`).

## Core Commands

```bash
just reproduce   # Verify archive, checksums, pytest suite, static site, and Build Standard audit
just sync        # Regenerate METADATA.json, EVIDENCE.md, registry/*.md, CHECKSUMS.sha256, data/MANIFEST.sha256
just test        # Run pytest integrity/property/negative/mutation suite
just audit       # Score repo against Build Standard v1.2.0
```
