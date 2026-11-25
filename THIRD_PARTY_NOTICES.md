# Third-Party Notices

This master archive contains only public works authored by Alexander Stephen Donahue (ORCID `0009-0006-8168-9648`) and depends only on standard Python verification tooling:

| Component | License | Role |
|---|---|---|
| Python 3 | PSF-2.0 | `scripts/verify_archive.py` and test suite |
| pytest (`requirements.txt`) | MIT | Automated archive integrity test runner |
| Hypothesis (`requirements.txt`) | MPL-2.0 | Property-based schema/hash verification |
| PyYAML (`requirements.txt`) | MIT | `repo.yaml` and `CITATION.cff` parsing |
| jsonschema (`requirements.txt`) | MIT | JSON Schema Draft 2020-12 validation |
| Ruff (`requirements.txt`) | MIT | Report-only Python static linter |
| mypy (`requirements.txt`) | MIT | Report-only static type checker |

Pinned Git submodules under `repos/` carry their own `LICENSE`, `NOTICE`, and `THIRD_PARTY_NOTICES.md` files.
