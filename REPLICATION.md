# Replication Protocol (`REPLICATION.md`)

Any third party can verify the entire canonical master archive, live ecosystem mirror, and Mega-Atlas bridge from a clean clone:

```bash
# 1. Clone the archive (add --recursive to fetch all 23 pinned public submodules)
git clone https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
python3 -m pip install -r requirements.txt

# 2. Verify every SHA-256 digest, ORCID, axiom policy, zero broken links, README sync, and submodule pin
python3 scripts/verify_archive.py
sha256sum -c CHECKSUMS.sha256

# 3. Run automated integrity, privacy-firewall, failure-injection, property, negative, mutation & idempotence tests
python3 -m pytest -v tests/
python3 scripts/build_site.py
bash scripts/audit-repo.sh .
```

To refresh the live upstream status mirror against GitHub right now, run `python3 scripts/live_sync.py`. To verify a specific paper's Lean 4 formal proof from scratch, run `git submodule update --init repos/<slug>` and execute the exact `falsification_command` printed in `papers/<id>/EVIDENCE.md`.

## Replication Log

| Date | Replicator | Environment | Version | Archive Audit & Pytest | Notes |
|---|---|---|---|---|---|
| 2026-11-25 | Alexander S. Donahue (author) | Windows 11, Python 3.13.12 | `2026.11.25` | PASS | Full `verify_archive.py --sync`, pytest ladder, `Audit-Repo.ps1` 100.0%. |
| 2026-11-25 | GitHub Actions CI (`ubuntu-latest`, `windows-latest`, `macos-latest`) | Hosted runners, Python 3.12 | `2026.11.25` | PASS (3 OSes) | Cross-platform verification, static Pages portal, and `SHA256SUMS` + SLSA release. |
| 2026-11-26 | Alexander S. Donahue + 3-Cycle Hardening Audit | Windows 11 + Ubuntu/macOS/Windows CI | `2026.11.26` | PASS | Consolidated 36 entries / 23 submodules, `0TH-2026-013`, `0TH-BUILD-004 v0.5.0`, `0TH-BUILD-010/011`, `0TH-DISC-011/012`, live sync mirror (`live-sync.yml`), Mega-Atlas bridge, WCAG 2.2 AA 3-tier portal, zero broken links, zero unformed LLC strings. |
