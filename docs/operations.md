# Operations, Backups & Offsite Mirror (`docs/operations.md`)

## 1. Syncing & Verifying Cryptographic Digests

After updating any archived PDF, artifact, or pinned submodule commit:

```bash
python3 scripts/verify_archive.py --sync
cp CHECKSUMS.sha256 data/MANIFEST.sha256
sha256sum -c CHECKSUMS.sha256
python3 -m pytest -v tests/
```

## 2. Creating an Offline Git Bundle Backup

Create a self-contained single-file backup of all archive metadata, frozen PDFs, and submodule pin pointers:

```bash
git bundle create 0thernes-research-archive-$(cat VERSION).bundle --all
git bundle verify 0thernes-research-archive-$(cat VERSION).bundle
sha256sum 0thernes-research-archive-$(cat VERSION).bundle
```

## 3. Offsite Mirrors & Long-Term Preservation

- **GitHub Releases (`release.yml`):** Every `v*` tag publishes all three JSON registries, `CHECKSUMS.sha256`, `SHA256SUMS`, and Sigstore SLSA build-provenance attestations (`actions/attest-build-provenance@v2`).
- **Software Heritage & Zenodo:** Archive snapshots and individual paper repositories are preserved independently of GitHub via Software Heritage (`Save Code Now`) and Zenodo DOIs (e.g., `10.5281/zenodo.24517198` on `0TH-2026-010`).
- **Secondary Git remote mirror:** `git remote add mirror <url> && git push --mirror mirror`.
