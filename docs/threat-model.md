# Threat Model (`docs/threat-model.md`)

| Threat ID | Threat | Impact | Mitigations |
|---|---|---|---|
| **T1** | **Artifact tampering / silent PDF substitution** | Frozen paper differs from verified release | Byte-exact SHA-256 verification on every push in `scripts/verify_archive.py`, `sha256sum -c CHECKSUMS.sha256`, and `data/MANIFEST.sha256`; SLSA attestations on releases. |
| **T2** | **Submodule drift** (registry claims commit X while `repos/` points to commit Y) | Reproduction tests wrong source tree | `get_git_submodule_commits` cross-checks `git ls-files --stage repos` against every `pinned_commit` in CI. |
| **T3** | **Privacy-firewall leakage** (accidental inclusion of a private repository in public vault) | Exposure of private/proprietary paths or slugs | Automated visibility enforcement (`visibility == "PUBLIC"`) and private-slug guard in `tests/test_archive_integrity.py`. |
| **T4** | **Epistemic tier conflation** (presenting empirical/exploratory Tier III items as Lean-proved Tier I theorems) | Misleading scientific claims | Three physically separated JSON/MD registries with mandatory `verification_boundary` fields checked in CI. |
| **T5** | **Secret leakage or CI compromise** | Credential exposure | `gitleaks` report-only scan in `.github/workflows/archive-audit.yml`; minimal `contents: read` permissions on CI jobs. |
