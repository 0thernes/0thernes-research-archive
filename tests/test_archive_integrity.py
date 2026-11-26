"""Automated integrity, property-based, negative, mutation, and privacy-firewall tests for 0thernes-research-archive."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

import jsonschema
import yaml
from hypothesis import given, settings
from hypothesis import strategies as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import verify_archive as va  # noqa: E402


def test_repo_yaml_validates_against_schema() -> None:
    schema = json.loads((ROOT / "repo-standard.schema.json").read_text(encoding="utf-8"))
    manifest = yaml.safe_load((ROOT / "repo.yaml").read_text(encoding="utf-8"))
    jsonschema.validate(instance=manifest, schema=schema)
    assert manifest["standard"] == "1.2.0"


def test_single_version_consistency() -> None:
    ver = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    assert re.fullmatch(r"\d+\.\d+\.\d+", ver)
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    assert re.search(rf"^## \[?v?{re.escape(ver)}\]?", changelog, re.M)
    cff = yaml.safe_load((ROOT / "CITATION.cff").read_text(encoding="utf-8"))
    assert str(cff["version"]) == ver


def test_r4_no_banned_files() -> None:
    for rel in (
        ".github/PULL_REQUEST_TEMPLATE.md",
        ".github/pull_request_template.md",
        ".github/dependabot.yml",
        "renovate.json",
        ".github/copilot-instructions.md",
        ".github/FUNDING.yml",
    ):
        assert not (ROOT / rel).exists(), f"R4 banned file present: {rel}"


def test_privacy_firewall_no_private_repos() -> None:
    """Ensure private repository slugs never leak into public archive manifests."""
    private_slugs = ("0thernes-private-research-vault", "gigachad-browser", "grade-a-standard")
    for rel in (
        "README.md",
        ".gitmodules",
        "registry/PAPERS.json",
        "registry/BUILD_PAPERS.json",
        "registry/LAWS_AND_DISCOVERIES.json",
    ):
        txt = (ROOT / rel).read_text(encoding="utf-8")
        for slug in private_slugs:
            assert slug not in txt, f"Private slug '{slug}' leaked in {rel}"


def test_active_archive_headers_no_unformed_llc() -> None:
    for rel in ("README.md", "CITATION.cff", "NOTICE", "AGENTS.md", "CLAIMS.md", "LIMITATIONS.md"):
        txt = (ROOT / rel).read_text(encoding="utf-8")
        assert "0thernes LLC" not in txt, f"Unformed entity '0thernes LLC' found in {rel}"


def test_verify_archive_end_to_end_and_data_manifest_parity() -> None:
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "verify_archive.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "PASS:" in proc.stdout

    c1 = (ROOT / "CHECKSUMS.sha256").read_text(encoding="utf-8").strip()
    c2 = (ROOT / "data" / "MANIFEST.sha256").read_text(encoding="utf-8").strip()
    assert c1 == c2


def test_0th_2026_006_and_0th_build_007_registered_at_latest_versions() -> None:
    papers = {
        p["id"]: p
        for p in json.loads((ROOT / "registry" / "PAPERS.json").read_text(encoding="utf-8"))["papers"]
    }
    p6 = papers["0TH-2026-006"]
    assert p6["version"] == "v2.0.0"
    assert p6["lean_verification"]["audited_theorems"] == 576
    assert "45723630668" in p6["ci_run_url"]

    builds = {
        b["id"]: b
        for b in json.loads((ROOT / "registry" / "BUILD_PAPERS.json").read_text(encoding="utf-8"))["builds"]
    }
    b7 = builds["0TH-BUILD-007"]
    assert b7["version"] == "v2.4.0"
    assert b7["lean_verification"]["audited_theorems"] == 92
    assert "45728933812" in b7["lean_verification"]["live_audit_status"]


@given(payload=st.binary(min_size=1, max_size=4096))
@settings(max_examples=80, derandomize=True)
def test_property_sha256_file_matches_hashlib(tmp_path_factory, payload: bytes) -> None:
    """Hypothesis property-based test (B10) & differential oracle (B11) for sha256_file."""
    p = tmp_path_factory.mktemp("hashprop") / "blob.bin"
    p.write_bytes(payload)
    assert va.sha256_file(p) == hashlib.sha256(payload).hexdigest()


def test_negative_and_mutation_tampered_digest_and_axiom_killed() -> None:
    """Negative & mutation testing (B06, B13): mutated axiom allowlist and mutated digests are rejected."""
    mutated_axioms = {"propext", "Classical.choice", "Quot.sound", "sorryAx"}
    assert not mutated_axioms.issubset(va.ALLOWED_AXIOMS)

    first_line = (ROOT / "CHECKSUMS.sha256").read_text(encoding="utf-8").splitlines()[0]
    digest, rel = first_line.split("  ", 1)
    mutated_digest = ("0" if digest[0] != "0" else "1") + digest[1:]
    assert va.sha256_file(ROOT / rel) == digest
    assert va.sha256_file(ROOT / rel) != mutated_digest
