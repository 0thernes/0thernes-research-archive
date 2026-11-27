"""Integrity, negative, mutation and property tests for the numbered Results Ledger."""
from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_ledger as bl  # noqa: E402

SHA_A = "a" * 40
SHA_B = "b" * 40


def _index() -> dict[str, dict[str, Any]]:
    return {
        "0TH-TEST-001": {
            "tier": "I", "title": "Test entry", "repository": "https://github.com/0thernes/test-repo",
            "slug": "test-repo", "version": "v1.0.0", "pinned_commit": SHA_A,
            "pdf": "papers/x/x.pdf", "ci_run_url": None, "peer_review_status": "",
        },
        "0TH-TEST-002": {
            "tier": "II", "title": "Other entry", "repository": "https://github.com/0thernes/other-repo",
            "slug": "other-repo", "version": "v0.1.0", "pinned_commit": SHA_B,
            "pdf": None, "ci_run_url": None, "peer_review_status": "",
        },
    }


def _result(n: int = 1, **over: Any) -> dict[str, Any]:
    base: dict[str, Any] = {
        "n": n, "archive_id": "0TH-TEST-001", "key": f"T{n}", "status": "ACTIVE",
        "title": "A closed form for a lattice constant",
        "statement": "The constant equals 1/32 - 4*sqrt(3)/243.",
        "kind": "ANSWERS_PUBLISHED_QUESTION", "evidence": "kernel-checked",
        "asked_in": {"citation": "Author, Paper (2026)", "url": "https://arxiv.org/abs/0000.00000", "locator": "Conjecture 1"},
        "lean": [{"decl": "Ns.main_theorem", "file": "lean/Main.lean", "line": 3}],
        "axioms": "propext, Classical.choice, Quot.sound",
        "audited_commit": SHA_A,
        "audit": {"date": "2026-11-26", "rebuild": "PASS", "fidelity": "AUDITED_MATCH", "prior_work": "NONE_FOUND"},
        "limits": [], "check": "cd lean && lake build",
    }
    base.update(over)
    return base


def _ledger(*results: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "author": {"full_name": "A. Author", "affiliation": "Independent Researcher", "orcid": "0000-0000-0000-0000"},
        "read_first": ["Nothing here is peer reviewed."],
        "not_claimed": ["No grand problem is solved."],
        "admission_rules": ["Audit first."],
        "challenge": ["Open an issue."],
        "entries_without_results": {},
        "results": list(results) if results else [_result()],
    }


# ---------------------------------------------------------------- real ledger

def test_real_ledger_validates_and_outputs_are_current() -> None:
    res = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_ledger.py"), "--check"],
        cwd=ROOT, capture_output=True, text=True, encoding="utf-8",
    )
    assert res.returncode == 0, res.stdout + res.stderr
    assert "PASS: Results Ledger verified" in res.stdout


def test_every_registered_entry_is_accounted_for_in_results_md() -> None:
    ledger = bl.load_json(ROOT / "registry" / "RESULTS_LEDGER.json")
    index = bl.registry_index(ROOT)
    text = (ROOT / "RESULTS.md").read_text(encoding="utf-8")
    for aid in index:
        assert f"`{aid}`" in text, f"{aid} is registered but absent from RESULTS.md"
    covered = {r["archive_id"] for r in ledger["results"]}
    explained = set(ledger.get("entries_without_results", {}))
    assert covered | explained | set(bl.pending_entries(ledger, index)) == set(index)


def test_real_ledger_numbers_are_permanent_and_contiguous() -> None:
    ledger = bl.load_json(ROOT / "registry" / "RESULTS_LEDGER.json")
    assert [r["n"] for r in ledger["results"]] == list(range(1, len(ledger["results"]) + 1))


def test_real_ledger_claims_no_grand_problem() -> None:
    text = (ROOT / "RESULTS.md").read_text(encoding="utf-8")
    bridge = json.loads((ROOT / "registry" / "SOLVED_AND_ATLAS_BRIDGE.json").read_text(encoding="utf-8"))
    assert bridge["grand_problems_retired"] == 0
    assert f"0 of {bridge['mega_atlas_total_problems']:,} catalogued open problems" in text
    assert "peer reviewed" in text


def test_portal_lists_the_ledger() -> None:
    import build_site as bs

    assert bs.main() == 0
    site = ROOT / "build" / "site"
    html_txt = (site / "index.html").read_text(encoding="utf-8")
    assert 'id="h-ledger"' in html_txt and 'data-section="ledger"' in html_txt
    assert "None of these results is peer reviewed" in html_txt
    assert (site / "registry" / "RESULTS_LEDGER.json").is_file()
    ledger = bl.load_json(ROOT / "registry" / "RESULTS_LEDGER.json")
    for r in ledger["results"]:
        if r["status"] == "ACTIVE":
            assert f'RESULTS.md#r{r["n"]}"' in html_txt


# ---------------------------------------------------------------- unit checks

def test_minimal_valid_ledger_passes() -> None:
    assert bl.validate(_ledger(), _index()) == []


@pytest.mark.parametrize(
    "mutation, needle",
    [
        (lambda r: r.update(title="A world-record closed form"), "promotional wording"),
        (lambda r: r.update(statement="This breakthrough equals 1."), "promotional wording"),
        (lambda r: r.update(limits=["It completely resolves the area."]), "promotional wording"),
        (lambda r: r.update(asked_in=None), "kind A needs asked_in.citation"),
        (lambda r: r["audit"].update(fidelity="NOT_AUDITED"), "requires an audited statement"),
        (lambda r: r["audit"].update(prior_work="NOT_SEARCHED"), "requires a recorded prior-work search"),
        (lambda r: r["audit"].update(fidelity="AUDITED_NARROWER"), "must say how"),
        (lambda r: r["audit"].update(prior_work="OVERLAP_FOUND"), "must be described under 'limits'"),
        (lambda r: r.update(lean=[]), "must cite at least one Lean declaration"),
        (lambda r: r.update(axioms=""), "must state the axioms used"),
        (lambda r: r.update(audited_commit="abc123"), "40-character commit SHA"),
        (lambda r: r.update(archive_id="0TH-NOPE-999"), "is not in registry"),
        (lambda r: r.update(kind="MIRACLE"), "unknown kind"),
        (lambda r: r.update(evidence="vibes"), "unknown evidence"),
        (lambda r: r.update(n=2), "result numbers must be 1..N"),
        (lambda r: r.update(statement=" ".join(["word"] * 80)), "statement has 80 words"),
        (lambda r: r.update(status="WITHDRAWN"), "needs 'withdrawn_reason'"),
        (lambda r: r["audit"].update(date="yesterday"), "audit.date must be YYYY-MM-DD"),
        (lambda r: r["lean"][0].update(line=0), "positive line"),
    ],
)
def test_mutations_are_rejected(mutation: Any, needle: str) -> None:
    r = _result()
    mutation(r)
    errors = bl.validate(_ledger(r), _index())
    assert any(needle in e for e in errors), errors


def test_known_result_cannot_be_listed_as_new_theorem() -> None:
    r = _result(kind="NEW_THEOREM", asked_in=None)
    r["audit"]["prior_work"] = "KNOWN"
    assert any("cannot be listed as a new theorem" in e for e in bl.validate(_ledger(r), _index()))


def test_duplicate_key_is_rejected() -> None:
    errors = bl.validate(_ledger(_result(1), _result(2, key="T1")), _index())
    assert any("duplicate (archive_id, key)" in e for e in errors)


def test_pin_move_is_rendered_as_reaudit_pending(tmp_path: Path) -> None:
    index = _index()
    ledger = _ledger(_result())
    assert "Re-audit pending" not in "\n".join(bl.render_result(ledger["results"][0], index["0TH-TEST-001"]))
    index["0TH-TEST-001"]["pinned_commit"] = SHA_B
    text = "\n".join(bl.render_result(ledger["results"][0], index["0TH-TEST-001"]))
    assert "Re-audit pending" in text and SHA_A[:7] in text and SHA_B[:7] in text


def test_upstream_ahead_of_pin_is_disclosed() -> None:
    ent = _index()["0TH-TEST-001"]
    live: dict[str, Any] = {
        "synced_utc": "2026-11-26T00:00:00Z",
        "repos": {"test-repo": {"sync_status": "AHEAD_OF_PIN", "latest_release_tag": "v1.1.0"}},
    }
    text = "\n".join(bl.render_result(_result(), ent, live))
    assert "**Upstream.**" in text and "`v1.1.0`" in text and "not covered by this audit" in text
    live["repos"]["test-repo"]["sync_status"] = "EXACT_PIN_MATCH"
    assert "**Upstream.**" not in "\n".join(bl.render_result(_result(), ent, live))
    assert "**Upstream.**" not in "\n".join(bl.render_result(_result(), ent, None))


def test_only_section_a_says_asked_in() -> None:
    ent = _index()["0TH-TEST-001"]
    assert "**Asked in.**" in "\n".join(bl.render_result(_result(), ent))
    other = _result(kind="BOUNDED_CASE")
    text = "\n".join(bl.render_result(other, ent))
    assert "**Asked in.**" not in text and "**Related source.**" in text


def test_count_phrase_singular_and_plural() -> None:
    assert bl.count_phrase("NEW_THEOREM", 1) == "1 new theorem"
    assert bl.count_phrase("NEW_THEOREM", 3) == "3 new theorems"
    assert bl.count_phrase("ANSWERS_PUBLISHED_QUESTION", 2) == "2 open questions from the literature answered"


def test_evidence_links_are_commit_permalinks() -> None:
    line = bl.evidence_line(_result(), _index()["0TH-TEST-001"])
    assert f"https://github.com/0thernes/test-repo/blob/{SHA_A}/lean/Main.lean#L3" in line


@pytest.mark.parametrize("note", ["the converse is a paper argument", "The converse is a paper argument."])
def test_evidence_note_is_one_clean_sentence(note: str) -> None:
    line = bl.evidence_line(_result(evidence_note=note), _index()["0TH-TEST-001"])
    assert line.endswith("Quot.sound. The converse is a paper argument.")
    assert ".." not in line


def test_withdrawn_result_keeps_its_number() -> None:
    r = _result(status="WITHDRAWN", withdrawn_reason="A gap was found in step 2.")
    ledger = _ledger(r)
    assert bl.validate(ledger, _index()) == []
    text = "\n".join(bl.render_result(r, _index()["0TH-TEST-001"]))
    assert "### R1." in text and "**Withdrawn.** A gap was found in step 2." in text
    assert bl.counts_by_kind(ledger)["ANSWERS_PUBLISHED_QUESTION"] == 0


def test_unregistered_entries_surface_as_pending() -> None:
    ledger = _ledger(_result())
    assert bl.pending_entries(ledger, _index()) == ["0TH-TEST-002"]
    ledger["entries_without_results"] = {"0TH-TEST-002": "Superseded."}
    assert bl.pending_entries(ledger, _index()) == []


def test_readme_block_replacement_is_idempotent() -> None:
    block = f"{bl.BLOCK_START}\nnew\n{bl.BLOCK_END}"
    readme = f"top\n{bl.BLOCK_START}\nold\n{bl.BLOCK_END}\nbottom\n"
    once = bl.apply_readme_block(readme, block)
    assert once == f"top\n{block}\nbottom\n"
    assert bl.apply_readme_block(once, block) == once
    assert bl.apply_readme_block("no markers here", block) is None


def test_declaration_check_accepts_right_line_and_rejects_wrong_line(tmp_path: Path) -> None:
    repo = tmp_path / "test-repo"
    (repo / "lean").mkdir(parents=True)
    (repo / "lean" / "Main.lean").write_text(
        "namespace Ns\n\ntheorem main_theorem : True := trivial\n\n\n\n\n\ntheorem other : True := trivial\n",
        encoding="utf-8",
    )
    env = ["-c", "user.name=t", "-c", "user.email=t@example.invalid", "-c", "commit.gpgsign=false"]
    subprocess.run(["git", "init", "-q", str(repo)], check=True)
    subprocess.run(["git", "-C", str(repo), "add", "."], check=True)
    subprocess.run(["git", "-C", str(repo), *env, "commit", "-q", "-m", "init"], check=True)
    sha = subprocess.run(["git", "-C", str(repo), "rev-parse", "HEAD"], check=True, capture_output=True, text=True).stdout.strip()
    index = _index()
    good = _ledger(_result(audited_commit=sha))
    assert bl.check_declarations(good, index, tmp_path) == []
    bad = copy.deepcopy(good)
    bad["results"][0]["lean"][0]["line"] = 9
    assert any("is not at lean/Main.lean:9" in e for e in bl.check_declarations(bad, index, tmp_path))
    missing = copy.deepcopy(good)
    missing["results"][0]["lean"][0]["file"] = "lean/Nope.lean"
    assert any("not found at" in e for e in bl.check_declarations(missing, index, tmp_path))


@given(text=st.text(max_size=200))
@settings(max_examples=120, derandomize=True)
def test_property_table_cells_never_break_the_table(text: str) -> None:
    out = bl.cell(text)
    assert "\n" not in out and "\r" not in out
    backslashes = 0
    for ch in out:
        if ch == "|":
            assert backslashes % 2 == 1, f"unescaped pipe in {out!r}"
        backslashes = backslashes + 1 if ch == "\\" else 0


def test_bridge_class_follows_strongest_active_kind() -> None:
    ledger = {"results": [
        {"archive_id": "X", "kind": "KNOWN_RESULT_FORMALIZED", "status": "ACTIVE"},
        {"archive_id": "X", "kind": "NEW_THEOREM", "status": "ACTIVE"},
        {"archive_id": "Y", "kind": "ENGINEERING_INVARIANTS", "status": "ACTIVE"},
        {"archive_id": "Z", "kind": "ANSWERS_PUBLISHED_QUESTION", "status": "WITHDRAWN"},
    ]}
    expected = bl.expected_bridge_classes(ledger)
    assert expected["X"] == ("NEW_THEOREM_SUITE",)
    assert expected["Y"] == ("FORMAL_INVARIANT_SUITE",)
    assert "Z" not in expected


def test_every_bridge_row_matches_its_ledger_kind() -> None:
    ledger = json.loads((ROOT / "registry" / "RESULTS_LEDGER.json").read_text(encoding="utf-8"))
    bridge = json.loads((ROOT / "registry" / "SOLVED_AND_ATLAS_BRIDGE.json").read_text(encoding="utf-8"))
    expected = bl.expected_bridge_classes(ledger)
    for row in bridge["entries"]:
        assert row["archive_id"] in expected, f"{row['archive_id']} has a bridge row but no active result"
        assert row["resolution_class"] in expected[row["archive_id"]], row["archive_id"]