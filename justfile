# Task runner for 0thernes-research-archive (Build Standard v1.2.0, A31 & B01)
set shell := ["bash", "-euo", "pipefail", "-c"]

default:
    @just --list

setup:
    python3 -m pip install -r requirements.txt

sync:
    python3 scripts/verify_archive.py --sync
    cp CHECKSUMS.sha256 data/MANIFEST.sha256

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
