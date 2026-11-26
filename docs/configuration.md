# Configuration & Environments (`docs/configuration.md`)

This repository requires **no runtime secrets, API keys, or external services**.

| File | Purpose |
|---|---|
| `VERSION` | Single semantic version source (`2026.11.26`), matched with `CHANGELOG.md` and `CITATION.cff`. |
| `registry/PAPERS.json`, `BUILD_PAPERS.json`, `LAWS_AND_DISCOVERIES.json` | Canonical machine-readable three-tier registries. |
| `CHECKSUMS.sha256` & `data/MANIFEST.sha256` | Synchronized SHA-256 digests for all archived PDFs, metadata, white papers, and discovery snapshots. |
| `.gitmodules` | Exact URLs and paths of all 35 pinned public repositories under `repos/`. |
| `requirements.txt` | Pinned Python dependencies for pytest, Hypothesis, schema checks, `ruff`, and `mypy`. |
| `repo.yaml` & `repo-standard.schema.json` | Build Standard v1.2.0 manifest and JSON Schema Draft 2020-12 validator. |
