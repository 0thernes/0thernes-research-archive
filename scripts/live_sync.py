#!/usr/bin/env python3
"""
Real-time live cross-repository sync, mirror, and Mega-Atlas bridge generator
for the canonical 0thernes Research Archive hub.

Responsibilities:
  1. Collect every unique public 0thernes repository referenced across Tier I
     (registry/PAPERS.json), Tier II (registry/BUILD_PAPERS.json), and Tier III
     (registry/LAWS_AND_DISCOVERIES.json).
  2. Enforce the strict PUBLIC-ONLY privacy firewall (never emit private repos,
     third-party forks, or non-0thernes repositories).
  3. Query the GitHub REST API (or run deterministically in --offline mode) for
     each tracked repo's live default-branch HEAD SHA, latest release tag, push
     timestamp, archived flag, GitHub Pages URL, and latest main-branch CI run.
  4. Write registry/LIVE_ECOSYSTEM_MIRROR.json and registry/LIVE_ECOSYSTEM_MIRROR.md.
  4b. Write a public-only inventory of every owner repository so new research
      candidates are discoverable without silently entering the archive.
  5. Render registry/SOLVED_AND_ATLAS_BRIDGE.md from registry/SOLVED_AND_ATLAS_BRIDGE.json.
  6. Refresh the bounded <!-- LIVE_ECOSYSTEM_STATUS:START --> block inside README.md.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import privacy  # sibling module: hashed denylist of non-public repository names

OWNER = "0thernes"
ARCHIVE_SLUG = "0thernes-research-archive"
BLOCK_START = "<!-- LIVE_ECOSYSTEM_STATUS:START -->"
BLOCK_END = "<!-- LIVE_ECOSYSTEM_STATUS:END -->"


def parse_repo_slug(repo_url: str) -> str:
    cleaned = repo_url.rstrip("/")
    if cleaned.endswith(".git"):
        cleaned = cleaned[:-4]
    parts = cleaned.split("/")
    if len(parts) < 2 or parts[-2].lower() != OWNER.lower():
        raise ValueError(f"Non-0thernes repository URL rejected: {repo_url}")
    slug = parts[-1]
    if privacy.is_private_name(slug):
        # Do not echo the name: it is exactly what the firewall keeps out of public logs.
        raise ValueError("Privacy firewall violation: a non-public repository was referenced")
    return slug


def assert_public_repo_metadata(meta: dict[str, Any], slug: str) -> None:
    if meta.get("private") is True:
        raise ValueError(f"Privacy firewall violation: {slug} is private")
    if meta.get("fork") is True:
        raise ValueError(f"Privacy firewall violation: {slug} is a third-party fork")
    owner_login = str((meta.get("owner") or {}).get("login", "")).lower()
    if owner_login and owner_login != OWNER.lower():
        raise ValueError(f"Privacy firewall violation: owner {owner_login!r} != {OWNER!r}")


def gh_api_json(endpoint: str, token: str | None = None, timeout: float = 15.0) -> Any:
    url = f"https://api.github.com/{endpoint.lstrip('/')}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "0thernes-research-archive-live-sync/1.0",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout) as resp:  # noqa: S310
        return json.loads(resp.read().decode("utf-8"))


def collect_public_inventory(
    tracked: dict[str, dict[str, Any]],
    *,
    offline: bool,
    token: str | None,
    fetcher: Any = gh_api_json,
) -> dict[str, Any]:
    """Discover public owner repos without promoting them into the archive.

    The inventory is deliberately separate from the epistemic registries: a
    public repository can be visible here while still being an app, tool,
    creative experiment, private-to-the-owner candidate, or an unreleased
    research branch.  Only a human-reviewed registry entry can make a claim.
    """
    if offline:
        return {"repositories": [], "sync_status": "OFFLINE_NOT_QUERIED", "error": None}

    repos: list[dict[str, Any]] = []
    for page in range(1, 11):
        batch = fetcher(
            f"users/{OWNER}/repos?type=owner&per_page=100&page={page}&sort=updated",
            token=token,
        )
        if not isinstance(batch, list):
            raise ValueError("GitHub owner repository response was not a list")
        if not batch:
            break
        for meta in batch:
            slug = str(meta.get("name") or "")
            if not slug:
                continue
            # Owner listings may include the owner's own forks.  They are
            # intentionally invisible to this inventory, not an error.
            if meta.get("fork") is True:
                continue
            assert_public_repo_metadata(meta, slug)
            if slug == ARCHIVE_SLUG:
                continue
            repos.append(
                {
                    "slug": slug,
                    "repository": f"https://github.com/{OWNER}/{slug}",
                    "description": meta.get("description"),
                    "default_branch": meta.get("default_branch") or "main",
                    "archived": bool(meta.get("archived", False)),
                    "pushed_at": meta.get("pushed_at"),
                    "homepage": meta.get("homepage") or None,
                    "latest_release": None,
                    "archive_registered": slug in tracked,
                    "inventory_status": "REGISTERED" if slug in tracked else "UNREGISTERED_PUBLIC_REPO",
                }
            )
        if len(batch) < 100:
            break
    repos.sort(key=lambda item: item["slug"].lower())
    return {"repositories": repos, "sync_status": "LIVE_GITHUB_API", "error": None}


def render_public_inventory_md(inventory: dict[str, Any], synced_utc: str) -> str:
    repos = inventory["repositories"]
    registered = sum(1 for r in repos if r["archive_registered"])
    candidates = len(repos) - registered
    lines = [
        "# Public 0thernes Repository Inventory",
        "",
        f"**Synced (UTC):** `{synced_utc}` · **Public non-fork repositories:** `{len(repos)}` · **Registered:** `{registered}` · **Unregistered candidates:** `{candidates}`",
        "",
        "> This is a discovery inventory, not an epistemic registry. An unregistered repository is not asserted to contain a paper, proof, solved conjecture, or research result. Private repositories and third-party forks are excluded by the privacy firewall.",
        "",
        "| Repository | Status | Default branch | Last push | Description |",
        "|---|---|---|---|---|",
    ]
    for r in repos:
        desc = str(r.get("description") or "").replace("|", "\\|").replace("\n", " ")
        lines.append(f"| [`{r['slug']}`]({r['repository']}) | `{r['inventory_status']}` | `{r['default_branch']}` | `{r.get('pushed_at') or '—'}` | {desc or '—'} |")
    lines.extend(["", "**Promotion rule:** only a reviewed entry in `PAPERS.json`, `BUILD_PAPERS.json`, or `LAWS_AND_DISCOVERIES.json` can enter the canonical archive.", ""])
    return "\n".join(lines)


def collect_tracked_repos(
    papers_data: dict[str, Any],
    builds_data: dict[str, Any],
    discs_data: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    tracked: dict[str, dict[str, Any]] = {}

    def register(
        repo_url: str,
        entry_id: str,
        tier: str,
        pinned_commit: str,
        version: str,
        submodule_path: str | None = None,
        pages_url: str | None = None,
    ) -> None:
        slug = parse_repo_slug(repo_url)
        rec = tracked.setdefault(
            slug,
            {
                "slug": slug,
                "repository": f"https://github.com/{OWNER}/{slug}",
                "archive_ids": [],
                "tiers": [],
                "pinned_commit": pinned_commit,
                "archived_version": version,
                "submodule_path": submodule_path,
                "registered_pages_url": pages_url,
            },
        )
        if entry_id not in rec["archive_ids"]:
            rec["archive_ids"].append(entry_id)
        if tier not in rec["tiers"]:
            rec["tiers"].append(tier)
        if submodule_path and not rec["submodule_path"]:
            rec["submodule_path"] = submodule_path
        if pages_url and not rec["registered_pages_url"]:
            rec["registered_pages_url"] = pages_url
        # Prefer Tier I or Tier II pin over older Tier III pin if repo appears in multiple tiers
        if tier in ("Tier I", "Tier II"):
            rec["pinned_commit"] = pinned_commit
            rec["archived_version"] = version

    for p in papers_data.get("papers", []):
        register(
            p["repository"],
            p["id"],
            "Tier I",
            p["pinned_commit"],
            p["version"],
            p.get("submodule_path"),
            p.get("pages_url"),
        )
    for b in builds_data.get("builds", []):
        register(
            b["repository"],
            b["id"],
            "Tier II",
            b["pinned_commit"],
            b["version"],
            b.get("submodule_path"),
            b.get("pages_url"),
        )
    for d in discs_data.get("discoveries", []):
        if d.get("visibility") != "PUBLIC":
            raise ValueError(f"Non-PUBLIC discovery entry rejected: {d.get('id')}")
        register(
            d["repository"],
            d["id"],
            "Tier III",
            d["pinned_commit"],
            d.get("branch", "main"),
        )

    return dict(sorted(tracked.items(), key=lambda kv: kv[0].lower()))


def fetch_repo_live_state(
    rec: dict[str, Any],
    *,
    offline: bool,
    token: str | None,
    fetcher: Any = gh_api_json,
) -> dict[str, Any]:
    slug = rec["slug"]
    out: dict[str, Any] = {
        **rec,
        "default_branch": "main",
        "archived": False,
        "live_head_commit": None,
        "latest_release_tag": None,
        "pushed_at": None,
        "ci_run_id": None,
        "ci_conclusion": None,
        "ci_html_url": None,
        "ci_status_reason": "NO_SUBSTANTIVE_CI_RUN",
        "pages_url": rec.get("registered_pages_url"),
        "sync_status": "OFFLINE_PIN_ONLY",
        "error": None,
    }
    if offline:
        return out

    try:
        meta = fetcher(f"repos/{OWNER}/{slug}", token=token)
        assert_public_repo_metadata(meta, slug)
        branch = str(meta.get("default_branch") or "main")
        out["default_branch"] = branch
        out["archived"] = bool(meta.get("archived", False))
        out["pushed_at"] = meta.get("pushed_at")
        if meta.get("has_pages") and not out["pages_url"]:
            out["pages_url"] = f"https://{OWNER}.github.io/{slug}/"

        commit_obj = fetcher(f"repos/{OWNER}/{slug}/commits/{branch}", token=token)
        live_sha = str(commit_obj.get("sha") or "")
        out["live_head_commit"] = live_sha or None

        try:
            rel_obj = fetcher(f"repos/{OWNER}/{slug}/releases/latest", token=token)
            out["latest_release_tag"] = rel_obj.get("tag_name")
        except urllib.error.HTTPError as exc:
            if exc.code != 404:
                raise

        try:
            runs_obj = fetcher(
                f"repos/{OWNER}/{slug}/actions/runs?per_page=20&branch={branch}",
                token=token,
            )
            wruns = runs_obj.get("workflow_runs") or []
            # Pages/deploy/dependency-management workflows are operational
            # side effects, not the repository's substantive verification
            # result.  Prefer the newest actual build/test/audit workflow so
            # a failed deployment cannot mask a green proof or test run.
            excluded_markers = ("pages", "deploy", "dependabot", "dependency graph")
            substantive = [
                run
                for run in wruns
                if str(run.get("event") or "").lower() != "dynamic"
                and not any(
                    marker in str(run.get("name") or run.get("workflow_name") or "").lower()
                    for marker in excluded_markers
                )
            ]
            if substantive:
                latest = substantive[0]
                out["ci_run_id"] = latest.get("id")
                out["ci_conclusion"] = latest.get("conclusion") or latest.get("status")
                out["ci_html_url"] = latest.get("html_url")
                out["ci_status_reason"] = None
        except urllib.error.HTTPError as exc:
            if exc.code not in (403, 404):
                raise

        if out["archived"]:
            out["sync_status"] = "HISTORICAL_ARCHIVED"
        elif live_sha and live_sha == rec["pinned_commit"]:
            out["sync_status"] = "EXACT_PIN_MATCH"
        elif live_sha:
            out["sync_status"] = "AHEAD_OF_PIN"
        else:
            out["sync_status"] = "UNKNOWN"
    except ValueError:
        raise
    except Exception as exc:  # noqa: BLE001
        out["sync_status"] = "API_ERROR"
        out["error"] = f"{type(exc).__name__}: {exc}"

    return out


def render_live_mirror_md(mirror: dict[str, Any]) -> str:
    repos = mirror["repositories"]
    exact = sum(1 for r in repos if r["sync_status"] == "EXACT_PIN_MATCH")
    ahead = sum(1 for r in repos if r["sync_status"] == "AHEAD_OF_PIN")
    archived = sum(1 for r in repos if r["sync_status"] == "HISTORICAL_ARCHIVED")
    errors = sum(1 for r in repos if r["sync_status"] == "API_ERROR")
    lines = [
        "# Live Upstream Ecosystem Mirror (`registry/LIVE_ECOSYSTEM_MIRROR.md`)",
        "",
        f"**Canonical Hub:** [{OWNER}/{ARCHIVE_SLUG}](https://github.com/{OWNER}/{ARCHIVE_SLUG})  ",
        f"**Synced (UTC):** `{mirror['synced_utc']}` · **Mode:** `{mirror['sync_mode']}`  ",
        f"**Tracked Public Repositories:** {len(repos)} (`{exact}` exact pin match, `{ahead}` active upstream ahead of release pin, `{archived}` historical archived snapshots, `{errors}` API errors)",
        "",
        "> **Privacy Firewall:** Strictly tracks **PUBLIC, non-fork `0thernes/*` repositories** registered in `PAPERS.json`, `BUILD_PAPERS.json`, and `LAWS_AND_DISCOVERIES.json`. Private repositories are never queried, mirrored, or referenced here.",
        "",
        "| Repository | Archive IDs | Tiers | Archived Pin | Live `main` HEAD | Release | Latest CI | Sync Status |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in repos:
        ids = ", ".join(f"`{i}`" for i in r["archive_ids"])
        tiers = " / ".join(r["tiers"])
        pin = f"`{r['pinned_commit'][:10]}`"
        live = f"`{r['live_head_commit'][:10]}`" if r["live_head_commit"] else "—"
        rel = f"`{r['latest_release_tag']}`" if r["latest_release_tag"] else f"`{r['archived_version']}`"
        if r["ci_html_url"] and r["ci_conclusion"]:
            ci = f"[`{r['ci_conclusion']}`]({r['ci_html_url']})"
        else:
            ci = "—"
        lines.append(
            f"| [`{r['slug']}`]({r['repository']}) | {ids} | {tiers} | {pin} | {live} | {rel} | {ci} | `{r['sync_status']}` |"
        )
    lines.extend(
        [
            "",
            "---",
            "",
            "## Automatic Real-Time Sync Protocol",
            "",
            "- **Push-based dispatch:** Upstream repositories carrying `.github/workflows/notify-archive.yml` dispatch `upstream-repo-updated` to this hub on every `main` push (see [`docs/upstream-notify-workflow.yml`](../docs/upstream-notify-workflow.yml)).",
            "- **Scheduled pull mirror:** [`.github/workflows/live-sync.yml`](../.github/workflows/live-sync.yml) refreshes this mirror every 2 hours (`0 */2 * * *`), re-verifies SHA-256 integrity and `pytest`, and republishes the live GitHub Pages portal automatically whenever upstream status changes.",
            "- **Discovery inventory:** [`PUBLIC_REPO_INVENTORY.md`](PUBLIC_REPO_INVENTORY.md) lists every public, non-fork owner repository and marks unregistered repositories as candidates without promoting them into the epistemic archive.",
            "- **Immutability rule:** Release-pinned frozen PDFs and Rekor-attested submodules are only advanced when matching frozen artifacts are archived; post-release upstream commits appear immediately as `AHEAD_OF_PIN` with live CI links.",
            "",
        ]
    )
    return "\n".join(lines)


def render_bridge_md(bridge: dict[str, Any]) -> str:
    es = bridge["epistemic_summary"]
    lines = [
        "# Solved Sub-Conjectures & Mega-Atlas V2 Cross-Reference Bridge",
        "",
        f"**Audit Date:** `{bridge['audit_date']}` · **Author:** {bridge['author']['full_name']} ({bridge['author']['affiliation']}, ORCID [`{bridge['author']['orcid']}`](https://orcid.org/{bridge['author']['orcid']}))  ",
        f"**Mega-Atlas Grand Problems Retired:** **`{bridge['grand_problems_retired']} / {bridge['mega_atlas_total_problems']}`**  ",
        f"**Peer-Literature Open Sub-Conjectures / Open Questions Proved in Lean 4.35.0:** **{es['published_open_subconjectures_proved_in_lean']}** (+ {es['preprint_conjectures_proved_with_external_citation_caveat']} preprint conjecture with explicit external-citation caveat)",
        "",
        f"> **Epistemic Boundary:** {es['statement']}",
        "",
        "| Archive ID | Repository | Version | Epistemic Class | Mega-Atlas IDs | Grand Problem Retired? | Verified Result & Boundary |",
        "|---|---|---|---|---|---|---|",
    ]
    for e in bridge["entries"]:
        ids = ", ".join(f"`{m}`" for m in e["related_mega_atlas_ids"]) if e["related_mega_atlas_ids"] else "*(infrastructure / A-Life)*"
        retired = "**YES**" if e["grand_atlas_problem_retired"] else "No"
        lines.append(
            f"| `{e['archive_id']}` | [`{e['slug']}`]({e['repository']}) | `{e['version']}` | `{e['resolution_class']}` | {ids} | {retired} | {e['target_statement']} *(Boundary: {e['honesty_boundary']})* |"
        )
    lines.append("")
    return "\n".join(lines)


def update_readme_live_block(
    readme_path: Path,
    mirror: dict[str, Any],
    bridge: dict[str, Any],
    papers_count: int,
    builds_count: int,
    discs_count: int,
    submodules_count: int,
) -> bool:
    if not readme_path.exists():
        return False
    txt = readme_path.read_text(encoding="utf-8")
    if BLOCK_START not in txt or BLOCK_END not in txt:
        return False
    repos = mirror["repositories"]
    exact = sum(1 for r in repos if r["sync_status"] == "EXACT_PIN_MATCH")
    ahead = sum(1 for r in repos if r["sync_status"] == "AHEAD_OF_PIN")
    archived = sum(1 for r in repos if r["sync_status"] == "HISTORICAL_ARCHIVED")
    total_entries = papers_count + builds_count + discs_count
    block = "\n".join(
        [
            BLOCK_START,
            f"> **Live Canonical Hub Mirror (`{mirror['synced_utc']}`):** Tracking **{total_entries} public research entries** ({papers_count} Tier I preprints · {builds_count} Tier II builds · {discs_count} Tier III laws/discoveries/atlases) across **{len(repos)} unique public repositories** and **{submodules_count} pinned Git submodules** (`{exact}` exact pin matches · `{ahead}` active upstream ahead of release pin · `{archived}` archived historical snapshots).  ",
            f"> **Mega-Atlas V2 Cross-Check:** **`{bridge['grand_problems_retired']} / {bridge['mega_atlas_total_problems']}` grand open problems retired** · **{bridge['epistemic_summary']['published_open_subconjectures_proved_in_lean']} peer-literature open sub-conjectures/questions formally proved in Lean 4.35.0** across 6 independent kernels. Full tables: [`registry/LIVE_ECOSYSTEM_MIRROR.md`](registry/LIVE_ECOSYSTEM_MIRROR.md) · [`registry/SOLVED_AND_ATLAS_BRIDGE.md`](registry/SOLVED_AND_ATLAS_BRIDGE.md) · [Live Portal](https://0thernes.github.io/0thernes-research-archive/).",
            BLOCK_END,
        ]
    )
    pattern = re.compile(re.escape(BLOCK_START) + r".*?" + re.escape(BLOCK_END), re.S)
    new_txt = pattern.sub(block, txt, count=1)
    if new_txt != txt:
        readme_path.write_bytes(new_txt.encode("utf-8"))
        return True
    return False


def count_git_submodules(root: Path) -> int:
    res = subprocess.run(
        ["git", "ls-files", "--stage", "repos"],
        cwd=root,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    if res.returncode != 0:
        return 0
    return sum(1 for ln in res.stdout.splitlines() if ln.startswith("160000 "))


def resolve_local_github_token() -> str | None:
    """Use an explicit token first, then the user's authenticated gh session.

    CI supplies ``GITHUB_TOKEN``/``GH_TOKEN``.  On a developer workstation the
    GitHub CLI often already has an authenticated token, while leaving both
    environment variables unset would silently fall back to GitHub's very
    small anonymous rate limit and make a full-fleet sync fail spuriously.
    """
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        return token
    try:
        result = subprocess.run(
            ["gh", "auth", "token"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=10,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    if result.returncode == 0 and result.stdout.strip():
        return result.stdout.strip()
    return None


def run_sync(root: Path, *, offline: bool, token: str | None) -> dict[str, Any]:
    papers_data = json.loads((root / "registry" / "PAPERS.json").read_text(encoding="utf-8"))
    builds_data = json.loads((root / "registry" / "BUILD_PAPERS.json").read_text(encoding="utf-8"))
    discs_data = json.loads((root / "registry" / "LAWS_AND_DISCOVERIES.json").read_text(encoding="utf-8"))
    bridge_path = root / "registry" / "SOLVED_AND_ATLAS_BRIDGE.json"
    bridge_data = json.loads(bridge_path.read_text(encoding="utf-8"))

    tracked = collect_tracked_repos(papers_data, builds_data, discs_data)
    mirror_repos = [
        fetch_repo_live_state(rec, offline=offline, token=token)
        for rec in tracked.values()
    ]

    counts = {
        "tier1_papers": len(papers_data["papers"]),
        "tier2_builds": len(builds_data["builds"]),
        "tier3_discoveries": len(discs_data["discoveries"]),
        "total_entries": (
            len(papers_data["papers"])
            + len(builds_data["builds"])
            + len(discs_data["discoveries"])
        ),
        "unique_public_repositories": len(mirror_repos),
        "pinned_submodules": count_git_submodules(root),
        "exact_pin_match": sum(1 for r in mirror_repos if r["sync_status"] == "EXACT_PIN_MATCH"),
        "ahead_of_pin": sum(1 for r in mirror_repos if r["sync_status"] == "AHEAD_OF_PIN"),
        "historical_archived": sum(1 for r in mirror_repos if r["sync_status"] == "HISTORICAL_ARCHIVED"),
        "api_errors": sum(1 for r in mirror_repos if r["sync_status"] == "API_ERROR"),
    }

    # Never publish a partial live snapshot.  A transient GitHub outage,
    # token/rate-limit failure, or malformed upstream response must leave the
    # last known-good mirror intact; otherwise the generated registry would
    # silently replace every live field with nulls and become misleading while
    # still looking structurally valid.  Offline mode is intentionally exempt:
    # it is the deterministic pinned-manifest renderer used for local builds.
    if not offline and counts["api_errors"]:
        error_samples = [
            f"{r['slug']}: {r['error']}"
            for r in mirror_repos
            if r["sync_status"] == "API_ERROR" and r.get("error")
        ][:5]
        detail = " | ".join(error_samples)
        raise RuntimeError(
            f"live GitHub sync aborted with {counts['api_errors']} API errors; "
            "preserving the previous mirror (use --offline for a pinned snapshot). "
            f"Sample failures: {detail or 'no error details captured'}"
        )

    inventory = collect_public_inventory(
        tracked, offline=offline, token=token
    )
    if offline:
        inventory_path = root / "registry" / "PUBLIC_REPO_INVENTORY.json"
        if inventory_path.exists():
            previous_inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
            inventory = {
                "repositories": previous_inventory.get("repositories", []),
                "sync_status": "OFFLINE_PRESERVED_LAST_KNOWN_GOOD",
                "error": None,
            }

    # Zero-noise idempotence: preserve synced_utc whenever upstream state & counts are unchanged
    mirror_json_path = root / "registry" / "LIVE_ECOSYSTEM_MIRROR.json"
    synced_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if mirror_json_path.exists():
        prev = json.loads(mirror_json_path.read_text(encoding="utf-8"))
        if offline or (prev.get("repositories") == mirror_repos and prev.get("counts") == counts):
            synced_utc = prev.get("synced_utc", synced_utc)

    mirror: dict[str, Any] = {
        "schema_version": "1.0.0",
        "canonical_hub": f"https://github.com/{OWNER}/{ARCHIVE_SLUG}",
        "synced_utc": synced_utc,
        "sync_mode": "offline" if offline else "live-github-api",
        "privacy_firewall": "PUBLIC_NON_FORK_0THERNES_ONLY",
        "counts": counts,
        "repositories": mirror_repos,
    }

    mirror_json_path.write_bytes((json.dumps(mirror, indent=2) + "\n").encode("utf-8"))
    (root / "registry" / "LIVE_ECOSYSTEM_MIRROR.md").write_bytes(
        render_live_mirror_md(mirror).encode("utf-8")
    )
    inventory_path = root / "registry" / "PUBLIC_REPO_INVENTORY.json"
    inventory_text = (
        json.dumps(
            {
                "schema_version": "1.0.0",
                "canonical_hub": f"https://github.com/{OWNER}/{ARCHIVE_SLUG}",
                "synced_utc": synced_utc,
                "privacy_firewall": "PUBLIC_NON_FORK_0THERNES_ONLY",
                **inventory,
            },
            indent=2,
        )
        + "\n"
    )
    inventory_path.write_bytes(inventory_text.encode("utf-8"))
    (root / "registry" / "PUBLIC_REPO_INVENTORY.md").write_bytes(
        render_public_inventory_md(inventory, synced_utc).encode("utf-8")
    )
    (root / "registry" / "SOLVED_AND_ATLAS_BRIDGE.md").write_bytes(
        render_bridge_md(bridge_data).encode("utf-8")
    )
    update_readme_live_block(
        root / "README.md",
        mirror,
        bridge_data,
        len(papers_data["papers"]),
        len(builds_data["builds"]),
        len(discs_data["discoveries"]),
        counts["pinned_submodules"],
    )
    return mirror


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync live upstream GitHub ecosystem mirror and Mega-Atlas bridge.")
    parser.add_argument("--offline", action="store_true", help="Skip live GitHub API calls and render from pinned manifests")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    token = resolve_local_github_token()
    mirror = run_sync(root, offline=args.offline, token=token)
    c = mirror["counts"]
    print(
        f"SYNCED ({mirror['sync_mode']}): {c['unique_public_repositories']} unique public repos | "
        f"{c['exact_pin_match']} exact pin | {c['ahead_of_pin']} ahead | "
        f"{c['historical_archived']} historical archived | {c['api_errors']} API errors."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
