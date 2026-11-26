# Replication Protocol (`REPLICATION.md`)

Any third party can verify the entire canonical master archive, live ecosystem mirror, Mega-Atlas bridge, and DigiCert RFC 3161 TSA release seal from a clean clone:

```bash
# 1. Clone the archive (add --recursive to fetch every pinned public submodule).
#    Needs Python 3.10 or newer: the pinned test tools do not install on 3.9. CI uses 3.12.
git clone https://github.com/0thernes/0thernes-research-archive.git
cd 0thernes-research-archive
python3 -m pip install -r requirements.txt

# 2. Verify every SHA-256 digest, RFC 3161 TSA seal, ORCID, axiom policy, bridge parity, table continuity,
#    zero broken links, every submodule pin, and the numbered Results Ledger (RESULTS.md)
python3 scripts/verify_archive.py
sha256sum -c CHECKSUMS.sha256
python3 scripts/build_ledger.py --check

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
| 2026-11-26 | Alexander S. Donahue + Round 1 3-Cycle Hardening | Windows 11 + Ubuntu/macOS/Windows CI | `2026.11.26` | PASS | Consolidated canonical hub (`live-sync.yml`), Mega-Atlas bridge, `0TH-2026-013 v1.1.0`, WCAG 2.2 AA 3-tier portal, zero broken links, zero unformed LLC strings. |
| 2026-11-26 | Alexander S. Donahue + Round 2 Overnight Hardening | Windows 11 + Ubuntu/macOS/Windows CI | `2026.11.26` | PASS | Synced **45 entries (`16+17+12`) / 32 submodules / 1,058 Tier-II Lean decls**, upgraded `0TH-2026-013` → `v1.2.0` (25 decls + live negative kernel rejection + 27 bibliography entries (25 DOIs, 3 resolving to unrelated papers) + DigiCert TSA), expanded `SOLVED_AND_ATLAS_BRIDGE.json` to 26 version-checked rows (later 29; 3 answered preprint questions per RESULTS.md section A; `0TH-2026-016` answers none), fixed split `README.md` Tier II table, added table/count/bridge/mirror/TSA verification guards & live DigiCert RFC 3161 `.tsr` over `data/RELEASE_FREEZE.sha256`. |
