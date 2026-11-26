"""Automated integrity, property-based, negative, mutation, failure-injection, link, and privacy-firewall tests for 0thernes-research-archive."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import urllib.error
from pathlib import Path
from typing import Any

import jsonschema
import pytest
import yaml
from hypothesis import given, settings
from hypothesis import strategies as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_site as bs  # noqa: E402
import live_sync as ls  # noqa: E402
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
    """Ensure private repository slugs never leak into public archive manifests or docs."""
    private_slugs = ("0thernes-private-research-vault", "gigachad-browser", "grade-a-standard")
    for rel in (
        "README.md",
        ".gitmodules",
        "llms.txt",
        "registry/PAPERS.json",
        "registry/BUILD_PAPERS.json",
        "registry/LAWS_AND_DISCOVERIES.json",
        "registry/SOLVED_AND_ATLAS_BRIDGE.json",
        "registry/LIVE_ECOSYSTEM_MIRROR.json",
    ):
        txt = (ROOT / rel).read_text(encoding="utf-8")
        for slug in private_slugs:
            assert slug not in txt, f"Private slug '{slug}' leaked in {rel}"


def test_active_archive_headers_and_registries_no_unformed_llc() -> None:
    for rel in va.ACTIVE_IDENTITY_FILES:
        txt = (ROOT / rel).read_text(encoding="utf-8")
        assert "0thernes LLC" not in txt, f"Unformed entity '0thernes LLC' found in {rel}"

    for reg_rel, key in (
        ("registry/PAPERS.json", "papers"),
        ("registry/BUILD_PAPERS.json", "builds"),
        ("registry/LAWS_AND_DISCOVERIES.json", "discoveries"),
    ):
        entries = json.loads((ROOT / reg_rel).read_text(encoding="utf-8"))[key]
        for entry in entries:
            assert "0thernes LLC" not in str(entry.get("affiliation", "")), (
                f"Unformed LLC in {reg_rel} entry {entry['id']}"
            )


def test_zero_broken_relative_markdown_links() -> None:
    broken = va.check_markdown_links(ROOT)
    assert broken == [], "\n".join(broken)


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


def test_consolidated_latest_entries_registered() -> None:
    papers = {
        p["id"]: p
        for p in json.loads((ROOT / "registry" / "PAPERS.json").read_text(encoding="utf-8"))["papers"]
    }
    assert len(papers) == 19
    assert papers["0TH-2026-006"]["version"] == "v2.3.0"
    assert papers["0TH-2026-006"]["lean_verification"]["audited_theorems"] == 730
    assert papers["0TH-2026-009"]["version"] == "v3.0.0"
    assert papers["0TH-2026-004"]["version"] == "v2.0.0"
    assert papers["0TH-2026-011"]["version"] == "v2.5.0"
    assert papers["0TH-2026-012"]["version"] == "v5.0.0"
    assert papers["0TH-2026-012"]["lean_verification"]["audited_theorems"] == 34
    assert papers["0TH-2026-013"]["slug"] == "p-vs-np-frontier-lab"
    assert papers["0TH-2026-013"]["version"] == "v1.2.0"
    assert papers["0TH-2026-013"]["lean_verification"]["audited_theorems"] == 25
    assert papers["0TH-2026-014"]["slug"] == "monodromia"
    assert papers["0TH-2026-015"]["slug"] == "promislow-fracton-amoeba"
    assert papers["0TH-2026-016"]["slug"] == "zero-error-torus-frontier"
    assert papers["0TH-2026-017"]["slug"] == "octonionica"
    assert papers["0TH-2026-017"]["version"] == "v1.0.0"
    assert papers["0TH-2026-017"]["lean_verification"]["audited_theorems"] == 93
    assert papers["0TH-2026-018"]["slug"] == "apollonian-sandpile-markov"
    assert papers["0TH-2026-018"]["version"] == "v1.0.0"
    assert papers["0TH-2026-018"]["lean_verification"]["audited_theorems"] == 18
    assert papers["0TH-2026-019"]["slug"] == "cayley-dickson-terrace-frontier"
    assert papers["0TH-2026-019"]["version"] == "v1.0.0"
    assert papers["0TH-2026-019"]["lean_verification"]["audited_theorems"] == 30

    builds = {
        b["id"]: b
        for b in json.loads((ROOT / "registry" / "BUILD_PAPERS.json").read_text(encoding="utf-8"))["builds"]
    }
    assert len(builds) == 17
    assert builds["0TH-BUILD-004"]["version"] == "v0.5.0"
    assert builds["0TH-BUILD-004"]["lean_verification"]["audited_theorems"] == 69
    assert builds["0TH-BUILD-007"]["version"] == "v2.8.0"
    assert builds["0TH-BUILD-007"]["lean_verification"]["audited_theorems"] == 103
    assert builds["0TH-BUILD-010"]["slug"] == "noetic-organism-omega"
    assert builds["0TH-BUILD-011"]["slug"] == "asmodensius-native"
    assert builds["0TH-BUILD-012"]["slug"] == "xiaomi-17t-pro-lab"
    assert builds["0TH-BUILD-015"]["slug"] == "glitchling-jam"
    assert builds["0TH-BUILD-016"]["slug"] == "ALife-Framework"
    assert builds["0TH-BUILD-017"]["slug"] == "beast-civilization"
    assert builds["0TH-BUILD-017"]["version"] == "v0.7.0"

    discs = {
        d["id"]: d
        for d in json.loads((ROOT / "registry" / "LAWS_AND_DISCOVERIES.json").read_text(encoding="utf-8"))["discoveries"]
    }
    assert len(discs) == 12
    assert "0TH-DISC-011" in discs and discs["0TH-DISC-011"]["slug"] == "alife-singularity-omega-package"
    assert "0TH-DISC-012" in discs and discs["0TH-DISC-012"]["slug"] == "omega-triscale-observatory"


def test_solved_and_atlas_bridge_epistemic_honesty() -> None:
    bridge = json.loads((ROOT / "registry" / "SOLVED_AND_ATLAS_BRIDGE.json").read_text(encoding="utf-8"))
    assert bridge["mega_atlas_total_problems"] == 1900
    assert bridge["grand_problems_retired"] == 0
    assert bridge["epistemic_summary"]["published_open_subconjectures_proved_in_lean"] == 5
    assert bridge["author"]["orcid"] == va.EXPECTED_ORCID
    assert len(bridge["entries"]) == 28
    for entry in bridge["entries"]:
        assert entry["grand_atlas_problem_retired"] is False
        assert entry["honesty_boundary"]
    assert (ROOT / "registry" / "SOLVED_AND_ATLAS_BRIDGE.md").exists()


def test_readme_table_continuity_and_split_table_mutant_killed() -> None:
    """Regression & negative mutant test (H-19): README tables stay contiguous; blank-line split is rejected."""
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert va.check_readme_table_integrity(readme) == []

    mutated = readme.replace("\n| `0TH-BUILD-015` |", "\n\n| `0TH-BUILD-015` |", 1)
    issues = va.check_readme_table_integrity(mutated)
    assert len(issues) == 1
    assert "splits consecutive registry table rows" in issues[0]


def test_rfc3161_release_freeze_tsa_and_tamper_rejection(tmp_path: Path) -> None:
    """Verify DigiCert RFC 3161 TSA token binds data/RELEASE_FREEZE.sha256 and rejects tampered freeze manifests."""
    freeze = ROOT / "data" / "RELEASE_FREEZE.sha256"
    tsr = ROOT / "data" / "RELEASE_FREEZE.sha256.tsr"
    assert freeze.is_file()
    assert tsr.is_file()
    assert va.check_rfc3161_tsa(freeze, tsr) == []

    tampered = tmp_path / "RELEASE_FREEZE.sha256"
    tampered.write_bytes(freeze.read_bytes() + b"\n# tampered\n")
    issues = va.check_rfc3161_tsa(tampered, tsr)
    assert len(issues) == 1
    assert "does not match" in issues[0]


def test_live_sync_privacy_firewall_and_failure_injection() -> None:
    """Negative & failure-injection tests (B06, B21) for live_sync.py."""
    with pytest.raises(ValueError, match="Privacy firewall"):
        ls.parse_repo_slug("https://github.com/0thernes/0thernes-private-research-vault")

    with pytest.raises(ValueError, match="Non-0thernes"):
        ls.parse_repo_slug("https://github.com/someone-else/some-repo")

    with pytest.raises(ValueError, match="is private"):
        ls.assert_public_repo_metadata({"private": True, "fork": False, "owner": {"login": "0thernes"}}, "secret")

    with pytest.raises(ValueError, match="third-party fork"):
        ls.assert_public_repo_metadata({"private": False, "fork": True, "owner": {"login": "0thernes"}}, "forked")

    rec = {
        "slug": "p-vs-np-frontier-lab",
        "repository": "https://github.com/0thernes/p-vs-np-frontier-lab",
        "archive_ids": ["0TH-2026-013"],
        "tiers": ["Tier I"],
        "pinned_commit": "01e56da105db4ec7cabb8aa19b8c7f6dfd48ac67",
        "archived_version": "v1.1.0",
        "submodule_path": "repos/p-vs-np-frontier-lab",
        "registered_pages_url": "https://0thernes.github.io/p-vs-np-frontier-lab/",
    }

    def fail_http_500(endpoint: str, token: str | None = None) -> Any:
        raise urllib.error.HTTPError(endpoint, 500, "Internal Server Error", hdrs=None, fp=None)  # type: ignore[arg-type]

    err_state = ls.fetch_repo_live_state(rec, offline=False, token=None, fetcher=fail_http_500)
    assert err_state["sync_status"] == "API_ERROR"
    assert "500" in str(err_state["error"])

    offline_state = ls.fetch_repo_live_state(rec, offline=True, token=None)
    assert offline_state["sync_status"] == "OFFLINE_PIN_ONLY"


def test_live_sync_api_errors_preserve_last_known_good_mirror(monkeypatch: pytest.MonkeyPatch) -> None:
    """A failed live refresh must not overwrite the canonical mirror with null metadata."""
    mirror_paths = (
        ROOT / "registry" / "LIVE_ECOSYSTEM_MIRROR.json",
        ROOT / "registry" / "LIVE_ECOSYSTEM_MIRROR.md",
        ROOT / "registry" / "SOLVED_AND_ATLAS_BRIDGE.md",
        ROOT / "README.md",
    )
    before = {path: path.read_bytes() for path in mirror_paths}

    monkeypatch.setattr(
        ls,
        "fetch_repo_live_state",
        lambda rec, *, offline, token: {
            "slug": rec["slug"],
            "repository": rec["repository"],
            "sync_status": "API_ERROR",
            "error": "HTTPError: 500",
        },
    )

    with pytest.raises(RuntimeError, match="preserving the previous mirror"):
        ls.run_sync(ROOT, offline=False, token=None)

    assert {path: path.read_bytes() for path in mirror_paths} == before


def test_build_site_wcag_and_all_tiers_and_endpoints() -> None:
    rc = bs.main()
    assert rc == 0
    html_txt = (ROOT / "build" / "site" / "index.html").read_text(encoding="utf-8")
    assert 'class="skip-link"' in html_txt
    assert "0TH-2026-013" in html_txt
    assert "0TH-BUILD-010" in html_txt
    assert "0TH-DISC-012" in html_txt
    assert "Solved Sub-Conjectures" in html_txt
    assert "Live Upstream Ecosystem Mirror" in html_txt
    for fname in (
        "PAPERS.json",
        "BUILD_PAPERS.json",
        "LAWS_AND_DISCOVERIES.json",
        "SOLVED_AND_ATLAS_BRIDGE.json",
        "LIVE_ECOSYSTEM_MIRROR.json",
    ):
        assert (ROOT / "build" / "site" / "registry" / fname).is_file()


def test_metamorphic_sync_idempotence() -> None:
    """Metamorphic idempotence check (B14): verify_archive.py --sync leaves tracked outputs byte-identical."""
    before = (ROOT / "CHECKSUMS.sha256").read_bytes()
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "verify_archive.py"), "--sync"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    after = (ROOT / "CHECKSUMS.sha256").read_bytes()
    assert before == after


@given(payload=st.binary(min_size=1, max_size=4096))
@settings(max_examples=80, derandomize=True, deadline=None)
def test_property_sha256_file_matches_hashlib(tmp_path_factory: pytest.TempPathFactory, payload: bytes) -> None:
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
