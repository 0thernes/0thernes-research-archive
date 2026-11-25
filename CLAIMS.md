# Claims Ledger (`CLAIMS.md`)

| ID | Claim | Verification Tier | Evidence | What Would Prove Us Wrong |
|---|---|---|---|---|
| **C1** | Every archived PDF, white paper, Lean certificate, metadata file, and discovery snapshot across all 31 entries (12 Tier I + 9 Tier II + 10 Tier III) matches its byte-exact SHA-256 digest in `CHECKSUMS.sha256`, `data/MANIFEST.sha256`, and `registry/*.json`. | **Cryptographic SHA-256 check** | `scripts/verify_archive.py`, `sha256sum -c CHECKSUMS.sha256`, `tests/test_archive_integrity.py` | Any SHA-256 mismatch, missing file, or unregistered PDF in `papers/`. |
| **C2** | Every pinned public Git submodule under `repos/` (`20` public repositories) matches the exact commit SHA recorded in `registry/PAPERS.json` and `registry/BUILD_PAPERS.json`. | **Exact Git index check** | `get_git_submodule_commits` in `scripts/verify_archive.py` | Any submodule drift between `git ls-files --stage repos` and `pinned_commit`. |
| **C3** | Every entry across all three tiers carries canonical ORCID `0009-0006-8168-9648`, an explicit `verification_boundary`, and Lean axiom allowlists strictly within `[propext, Classical.choice, Quot.sound]`. | **Automated schema & policy check** | `scripts/verify_archive.py`, `tests/test_archive_integrity.py` | Any missing ORCID, missing verification boundary, or non-standard axiom in any allowlist. |
| **C4** | Zero private repositories or third-party forks are exposed anywhere in `registry/`, `repos/`, or `.gitmodules`. | **Automated visibility & privacy check** | `test_privacy_firewall_no_private_repos` in `tests/test_archive_integrity.py` | Any `visibility != "PUBLIC"` entry or any private repository slug appearing in public manifests. |

## What Would Prove Us Wrong (Falsification Protocol)

Any failing run of `python3 scripts/verify_archive.py`, `sha256sum -c CHECKSUMS.sha256`, or `python3 -m pytest -v tests/` immediately falsifies the corresponding integrity claim above. External critics can also independently clone any pinned submodule at its exact commit SHA and run the entry's `falsification_command` from `EVIDENCE.md`.
