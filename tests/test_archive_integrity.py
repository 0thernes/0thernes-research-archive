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
import privacy  # noqa: E402
import verify_archive as va  # noqa: E402

# A synthetic name used to exercise the firewall; it is not one of the owner's repositories.
SYNTHETIC_PRIVATE = "example-nonpublic-repo"


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
    """No non-public repository name appears in the archive's registries, code, tests or docs."""
    assert va.check_privacy_firewall(ROOT) == []
    assert len(privacy.PRIVATE_SHA256) > 0
    assert all(re.fullmatch(r"[0-9a-f]{64}", h) for h in privacy.PRIVATE_SHA256)


def test_privacy_firewall_detects_a_leak_without_naming_it(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Mutation test: a planted non-public name is caught, and the report does not repeat it."""
    planted = frozenset({privacy.digest(SYNTHETIC_PRIVATE)})
    monkeypatch.setattr(privacy, "PRIVATE_SHA256", planted)
    text = f"see https://github.com/0thernes/{SYNTHETIC_PRIVATE.upper()}/blob/main/x.md and repos/other"
    assert privacy.private_names_in(text) == [SYNTHETIC_PRIVATE.upper()]
    assert privacy.private_names_in("nothing private here") == []
    # Hyphenated neighbours are different names: a prefix or suffix must not match.
    assert privacy.private_names_in(f"{SYNTHETIC_PRIVATE}-fork x{SYNTHETIC_PRIVATE}") == []
    (tmp_path / "registry").mkdir()
    (tmp_path / "README.md").write_text(f"links: {SYNTHETIC_PRIVATE}\n", encoding="utf-8")
    issues = va.check_privacy_firewall(tmp_path)
    assert issues and all(SYNTHETIC_PRIVATE not in i for i in issues), issues


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
    assert len(papers) == 26
    assert papers["0TH-2026-006"]["version"] == "v2.6.0"
    assert papers["0TH-2026-006"]["lean_verification"]["audited_theorems"] == 894
    assert papers["0TH-2026-009"]["version"] == "v3.2.0"
    assert papers["0TH-2026-009"]["lean_verification"]["audited_theorems"] == 2306
    assert papers["0TH-2026-009"]["lean_verification"]["comparator_targets"] == 18
    assert papers["0TH-2026-009"]["lean_verification"]["explicit_print_axioms"] == 198
    assert papers["0TH-2026-004"]["version"] == "v2.2.0"
    assert papers["0TH-2026-011"]["version"] == "v2.5.0"
    assert papers["0TH-2026-012"]["version"] == "v5.1.0"
    assert papers["0TH-2026-012"]["lean_verification"]["audited_theorems"] == 34
    assert papers["0TH-2026-013"]["slug"] == "p-vs-np-frontier-lab"
    assert papers["0TH-2026-013"]["version"] == "v1.2.0"
    assert papers["0TH-2026-013"]["lean_verification"]["audited_theorems"] == 25
    assert papers["0TH-2026-014"]["slug"] == "monodromia"
    assert papers["0TH-2026-015"]["slug"] == "promislow-fracton-amoeba"
    assert papers["0TH-2026-016"]["slug"] == "zero-error-torus-frontier"
    assert papers["0TH-2026-017"]["slug"] == "octonionica"
    assert papers["0TH-2026-017"]["version"] == "v1.2.0"
    assert papers["0TH-2026-017"]["lean_verification"]["audited_theorems"] == 128
    assert papers["0TH-2026-018"]["slug"] == "apollonian-sandpile-markov"
    assert papers["0TH-2026-018"]["version"] == "v2.1.0"
    assert papers["0TH-2026-018"]["lean_verification"]["audited_theorems"] == 19
    assert papers["0TH-2026-019"]["slug"] == "cayley-dickson-terrace-frontier"
    assert papers["0TH-2026-019"]["version"] == "v2.0.0"
    assert papers["0TH-2026-019"]["lean_verification"]["audited_theorems"] == 35
    assert papers["0TH-2026-020"]["slug"] == "quantum-phasespace-rigidity"
    assert papers["0TH-2026-020"]["version"] == "v1.0.0"
    assert papers["0TH-2026-020"]["lean_verification"]["audited_theorems"] == 23
    assert papers["0TH-2026-021"]["slug"] == "weyl-magic-stabilizer-frontier"
    assert papers["0TH-2026-021"]["version"] == "v1.0.0"
    assert papers["0TH-2026-021"]["lean_verification"]["audited_theorems"] == 31
    assert papers["0TH-2026-022"]["slug"] == "weyl-magic-obstruction-frontier"
    assert papers["0TH-2026-022"]["version"] == "v1.0.2"
    assert papers["0TH-2026-022"]["lean_verification"]["audited_theorems"] == 36
    assert papers["0TH-2026-023"]["slug"] == "quantum-latin-spectrum-frontier"
    assert papers["0TH-2026-023"]["version"] == "v1.0.0"
    assert papers["0TH-2026-023"]["lean_verification"]["audited_theorems"] == 32
    assert papers["0TH-2026-024"]["slug"] == "spectral-eclipse-frontier"
    assert papers["0TH-2026-024"]["version"] == "v1.0.0"
    assert papers["0TH-2026-024"]["lean_verification"]["audited_theorems"] == 568
    assert papers["0TH-2026-025"]["slug"] == "clifford-radon-stabilizers"
    assert papers["0TH-2026-025"]["version"] == "v1.0.0"
    assert papers["0TH-2026-025"]["lean_verification"]["audited_theorems"] == 33
    assert papers["0TH-2026-026"]["slug"] == "schur-clifford-frontier"
    assert papers["0TH-2026-026"]["version"] == "v1.0.0"
    assert papers["0TH-2026-026"]["lean_verification"]["audited_theorems"] == 30

    builds = {
        b["id"]: b
        for b in json.loads((ROOT / "registry" / "BUILD_PAPERS.json").read_text(encoding="utf-8"))["builds"]
    }
    assert len(builds) == 17
    assert builds["0TH-BUILD-004"]["version"] == "v0.5.0"
    assert builds["0TH-BUILD-004"]["lean_verification"]["audited_theorems"] == 69
    assert builds["0TH-BUILD-007"]["version"] == "v2.10.0"
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
    """The bridge's solved count is derived from its own classes and agrees with the Results Ledger.

    (Until 2026-11-26 this test pinned the literal 5; the statement audit of that day found that
    three of the five did not answer a question posed in their cited source.)
    """
    bridge = json.loads((ROOT / "registry" / "SOLVED_AND_ATLAS_BRIDGE.json").read_text(encoding="utf-8"))
    assert bridge["mega_atlas_total_problems"] == 2000
    assert bridge["grand_problems_retired"] == 0
    assert bridge["author"]["orcid"] == va.EXPECTED_ORCID
    solved = {e["archive_id"] for e in bridge["entries"] if e["resolution_class"] == "SOLVED_SUB_CONJECTURE"}
    assert bridge["epistemic_summary"]["published_open_subconjectures_proved_in_lean"] == len(solved)
    for entry in bridge["entries"]:
        assert entry["grand_atlas_problem_retired"] is False
        assert entry["honesty_boundary"]
    assert (ROOT / "registry" / "SOLVED_AND_ATLAS_BRIDGE.md").exists()

    ledger = json.loads((ROOT / "registry" / "RESULTS_LEDGER.json").read_text(encoding="utf-8"))
    in_ledger = {r["archive_id"] for r in ledger["results"]}
    answers = {r["archive_id"] for r in ledger["results"]
               if r["kind"] == "ANSWERS_PUBLISHED_QUESTION" and r["status"] == "ACTIVE"}
    # an entry in section A of the ledger must be a solved entry in the bridge ...
    assert answers <= solved, f"ledger answers a question the bridge does not class as solved: {answers - solved}"
    # ... and a solved bridge entry that the ledger has audited must have a section-A result
    assert (solved & in_ledger) <= answers, f"bridge says solved but the audited ledger does not: {(solved & in_ledger) - answers}"


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
    planted = frozenset({privacy.digest(SYNTHETIC_PRIVATE)})
    original = privacy.PRIVATE_SHA256
    privacy.PRIVATE_SHA256 = planted
    try:
        with pytest.raises(ValueError, match="Privacy firewall") as excinfo:
            ls.parse_repo_slug(f"https://github.com/0thernes/{SYNTHETIC_PRIVATE}")
        assert SYNTHETIC_PRIVATE not in str(excinfo.value)
    finally:
        privacy.PRIVATE_SHA256 = original
    assert ls.parse_repo_slug("https://github.com/0thernes/p-vs-np-frontier-lab") == "p-vs-np-frontier-lab"

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


def test_offline_sync_keeps_last_known_live_state(tmp_path: Path) -> None:
    """Regression (2026-11-26): an offline run must not replace committed live records with placeholders."""
    reg = tmp_path / "registry"
    reg.mkdir()
    live = {
        "slug": "demo-repo", "archive_ids": ["0TH-2026-999"], "pinned_commit": "a" * 40,
        "sync_status": "EXACT_PIN_MATCH", "live_head_commit": "a" * 40, "ci_conclusion": "success",
    }
    stale = dict(live, slug="moved-repo", pinned_commit="b" * 40)
    (reg / "LIVE_ECOSYSTEM_MIRROR.json").write_text(
        json.dumps({"sync_mode": "live-github-api", "repositories": [live, stale]}), encoding="utf-8"
    )
    offline = [
        {"slug": "demo-repo", "archive_ids": ["0TH-2026-999"], "pinned_commit": "a" * 40, "sync_status": "OFFLINE_PIN_ONLY"},
        {"slug": "moved-repo", "archive_ids": ["0TH-2026-999"], "pinned_commit": "c" * 40, "sync_status": "OFFLINE_PIN_ONLY"},
        {"slug": "new-repo", "archive_ids": ["0TH-2026-998"], "pinned_commit": "d" * 40, "sync_status": "OFFLINE_PIN_ONLY"},
    ]
    kept = ls.preserve_last_known_live_state(tmp_path, offline)
    assert kept[0]["sync_status"] == "EXACT_PIN_MATCH" and kept[0]["ci_conclusion"] == "success"
    assert kept[1]["sync_status"] == "OFFLINE_PIN_ONLY", "a moved pin must not inherit stale live data"
    assert kept[2]["sync_status"] == "OFFLINE_PIN_ONLY"


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


def test_prose_counts_guards_hardening_index_and_colon_format(tmp_path: Path) -> None:
    """Regression guard: check_prose_counts catches drift in HARDENING_INDEX.md and colon-format Tier counts."""
    assert "HARDENING_INDEX.md" in va.COUNT_GUARDED_FILES
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "architecture.md").write_text(
        "Tier I: 18 Standalone Preprints\n`34` submodules\n",
        encoding="utf-8",
    )
    (tmp_path / "HARDENING_INDEX.md").write_text(
        "**45 public research entries** and **34 submodules**\n",
        encoding="utf-8",
    )
    issues = va.check_prose_counts(tmp_path, total=48, pcount=19, bcount=17, dcount=12, subcount=35)
    joined = "\n".join(issues)
    assert "docs/architecture.md:1" in joined and "Tier I" in joined
    assert "HARDENING_INDEX.md:1" in joined and "public research entries" in joined
    assert "HARDENING_INDEX.md:1" in joined and "pinned submodules" in joined
