# Task runner for 0thernes-research-archive (Build Standard v1.2.0, A31 & B01)
set shell := ["bash", "-euo", "pipefail", "-c"]

default:
    @just --list

setup:
    python3 -m pip install -r requirements.txt

live-sync:
    python3 scripts/live_sync.py
    python3 scripts/verify_archive.py --sync
    python3 scripts/generate_llms_full.py
    python3 scripts/build_site.py

sync:
    python3 scripts/live_sync.py --offline
    python3 scripts/verify_archive.py --sync
    python3 scripts/generate_llms_full.py

ledger:
    python3 scripts/build_ledger.py

# Re-seal data/RELEASE_FREEZE.sha256 (RFC 3161) after changing any frozen registry file
seal:
    python3 scripts/stamp_freeze.py
    python3 scripts/verify_archive.py

ledger-check:
    python3 scripts/build_ledger.py --check

test:
    python3 -m pytest -v tests/

lint:
    python3 -m ruff check scripts/ tests/ || true
    python3 -m mypy --ignore-missing-imports scripts/ || true

site:
    python3 scripts/build_site.py

reproduce:
    python3 scripts/verify_archive.py
    python3 -m pytest -v tests/
    python3 scripts/build_site.py
    bash scripts/audit-repo.sh .

audit:
    bash scripts/audit-repo.sh .
