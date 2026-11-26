#!/usr/bin/env python3
"""Build a static, WCAG 2.2 AA, searchable GitHub Pages portal for 0thernes-research-archive at build/site/."""
from __future__ import annotations

import html
import json
import shutil
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "build" / "site"
ARCHIVED_SUPERSEDED_IDS = frozenset({"0TH-2026-001", "0TH-2026-002", "0TH-2026-003", "0TH-2026-005"})


def load_json(rel: str) -> dict[str, Any]:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def badge(text: str, cls: str = "tag") -> str:
    return f'<span class="{cls}">{html.escape(text)}</span>'


def main() -> int:
    papers = load_json("registry/PAPERS.json")["papers"]
    builds = load_json("registry/BUILD_PAPERS.json")["builds"]
    discs = load_json("registry/LAWS_AND_DISCOVERIES.json")["discoveries"]
    bridge = load_json("registry/SOLVED_AND_ATLAS_BRIDGE.json")
    mirror_path = ROOT / "registry" / "LIVE_ECOSYSTEM_MIRROR.json"
    mirror = json.loads(mirror_path.read_text(encoding="utf-8")) if mirror_path.exists() else None
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()

    total_entries = len(papers) + len(builds) + len(discs)
    total_build_lean = sum(int(b["lean_verification"]["audited_theorems"]) for b in builds)
    synced_utc = mirror["synced_utc"] if mirror else "offline"
    unique_repos = mirror["counts"]["unique_public_repositories"] if mirror else 0
    pinned_subs = mirror["counts"]["pinned_submodules"] if mirror else 0

    bridge_rows = []
    for e in bridge["entries"]:
        ids = ", ".join(f"<code>{html.escape(m)}</code>" for m in e["related_mega_atlas_ids"]) or "<em>Infrastructure / A-Life</em>"
        cls = "tag-ok" if e["resolution_class"] == "SOLVED_SUB_CONJECTURE" else "tag-info"
        search_txt = html.escape(
            f"{e['archive_id']} {e['slug']} {e['resolution_class']} {' '.join(e['related_mega_atlas_ids'])} {e['target_statement']}".lower()
        )
        bridge_rows.append(
            f'<tr data-search="{search_txt}">'
            f'<td><code>{html.escape(e["archive_id"])}</code></td>'
            f'<td><a href="{html.escape(e["repository"])}">{html.escape(e["slug"])}</a> <code>{html.escape(e["version"])}</code></td>'
            f'<td>{badge(e["resolution_class"], cls)}</td>'
            f'<td>{ids}</td>'
            f'<td>{html.escape(e["target_statement"])}<div class="muted">{html.escape(e["honesty_boundary"])}</div></td>'
            f'</tr>'
        )

    mirror_rows = []
    if mirror:
        for r in mirror["repositories"]:
            status = str(r["sync_status"])
            scls = (
                "tag-ok"
                if status == "EXACT_PIN_MATCH"
                else ("tag-warn" if status == "AHEAD_OF_PIN" else "tag-muted")
            )
            ci_cell = (
                f'<a href="{html.escape(r["ci_html_url"])}"><code>{html.escape(str(r["ci_conclusion"]))}</code></a>'
                if r.get("ci_html_url") and r.get("ci_conclusion")
                else "—"
            )
            live_sha = html.escape(r["live_head_commit"][:10]) if r.get("live_head_commit") else "—"
            rel_tag = html.escape(r["latest_release_tag"] or r["archived_version"])
            ids_html = " ".join(f"<code>{html.escape(i)}</code>" for i in r["archive_ids"])
            search_txt = html.escape(f"{r['slug']} {' '.join(r['archive_ids'])} {status} {rel_tag}".lower())
            mirror_rows.append(
                f'<tr data-search="{search_txt}">'
                f'<td><a href="{html.escape(r["repository"])}">{html.escape(r["slug"])}</a></td>'
                f'<td>{ids_html}</td>'
                f'<td><code>{html.escape(r["pinned_commit"][:10])}</code></td>'
                f'<td><code>{live_sha}</code></td>'
                f'<td><code>{rel_tag}</code></td>'
                f'<td>{ci_cell}</td>'
                f'<td>{badge(status, scls)}</td>'
                f'</tr>'
            )

    paper_rows = []
    for p in reversed(papers):
        repo = html.escape(p["repository"])
        title = html.escape(p["title"])
        hist_tag = (
            " " + badge("HISTORICAL -> 0TH-2026-009", "tag-muted")
            if p["id"] in ARCHIVED_SUPERSEDED_IDS
            else ""
        )
        search_txt = html.escape(f"{p['id']} {p['slug']} {p['domain']} {p['title']} {p['version']}".lower())
        paper_rows.append(
            f'<tr data-search="{search_txt}">'
            f'<td><code>{html.escape(p["id"])}</code></td>'
            f'<td>{html.escape(p["date_released"])}</td>'
            f'<td><code>{html.escape(p["version"])}</code></td>'
            f'<td><a href="{repo}">{title}</a>{hist_tag}<div class="muted">{html.escape(p["domain"])}</div></td>'
            f'<td><code>{html.escape(p["pdf_sha256"][:12])}…</code></td>'
            f'</tr>'
        )

    build_rows = []
    for b in builds:
        repo = html.escape(b["repository"])
        lv = b["lean_verification"]
        lean_txt = (
            f"{lv['audited_theorems']} decls ({lv['lines']:,} lines)"
            if lv["has_lean"]
            else "Audit / Non-Lean"
        )
        search_txt = html.escape(f"{b['id']} {b['slug']} {b['domain']} {b['title']} {b['version']}".lower())
        build_rows.append(
            f'<tr data-search="{search_txt}">'
            f'<td><code>{html.escape(b["id"])}</code></td>'
            f'<td><code>{html.escape(b["version"])}</code></td>'
            f'<td><a href="{repo}">{html.escape(b["title"])}</a><div class="muted">{html.escape(b["domain"])}</div></td>'
            f'<td>{html.escape(lean_txt)}</td>'
            f'</tr>'
        )

    disc_rows = []
    for d in discs:
        repo = html.escape(d["repository"])
        search_txt = html.escape(f"{d['id']} {d['slug']} {d['epistemic_tier']} {d['title']}".lower())
        disc_rows.append(
            f'<tr data-search="{search_txt}">'
            f'<td><code>{html.escape(d["id"])}</code></td>'
            f'<td>{badge(d["epistemic_tier"], "tag-info")}</td>'
            f'<td><a href="{repo}">{html.escape(d["title"])}</a></td>'
            f'<td>{len(d["archived_artifacts"])} files</td>'
            f'</tr>'
        )

    page = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>0thernes Research Archive · Canonical Hub ({html.escape(version)})</title>
  <style>
    :root {{ color-scheme: dark; --bg:#090e1c; --card:#111a2e; --border:#233252; --fg:#f1f5f9; --muted:#94a3b8; --accent:#38bdf8; --ok:#4ade80; --warn:#fbbf24; }}
    * {{ box-sizing: border-box; }}
    body {{ font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif; background: var(--bg); color: var(--fg); margin: 0; line-height: 1.55; }}
    .skip-link {{ position: absolute; left: -9999px; top: 0; background: #38bdf8; color: #090e1c; padding: .6rem 1rem; font-weight: 700; z-index: 100; }}
    .skip-link:focus {{ left: .75rem; top: .75rem; border-radius: 6px; }}
    a:focus-visible, button:focus-visible, input:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 2px; }}
    header {{ background: linear-gradient(135deg, #0f172a, #172554); border-bottom: 1px solid #1e3a8a; padding: 2.5rem 1.5rem 2rem; }}
    .wrap {{ max-width: 1180px; margin: 0 auto; }}
    h1 {{ margin: .3rem 0 .5rem; font-size: 2.15rem; color: #f8fafc; }}
    h2 {{ margin-top: 2.2rem; color: #f8fafc; border-bottom: 1px solid var(--border); padding-bottom: .4rem; }}
    .eyebrow {{ color: var(--ok); font-size: .82rem; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; }}
    .lead {{ color: #cbd5e1; max-width: 900px; }}
    .kpis {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(175px, 1fr)); gap: .75rem; margin: 1.25rem 0; }}
    .kpi {{ background: rgba(15,23,42,.78); border: 1px solid var(--border); border-radius: 10px; padding: .85rem 1rem; }}
    .kpi-num {{ font-size: 1.45rem; font-weight: 800; color: #f8fafc; }}
    .kpi-lbl {{ font-size: .78rem; color: var(--muted); text-transform: uppercase; letter-spacing: .06em; }}
    .pills {{ display: flex; flex-wrap: wrap; gap: .5rem; margin-top: 1rem; }}
    .pill {{ padding: .4rem .8rem; border-radius: 999px; background: #1e293b; border: 1px solid #334155; color: #f8fafc; text-decoration: none; font-size: .84rem; font-weight: 600; }}
    .pill:hover {{ background: #26354d; }}
    .controls {{ display: flex; flex-wrap: wrap; gap: .6rem; align-items: center; margin: 1.5rem 0 .5rem; padding: .9rem 1rem; background: var(--card); border: 1px solid var(--border); border-radius: 10px; }}
    .controls input {{ flex: 1 1 260px; background: #0b1224; color: var(--fg); border: 1px solid #334155; border-radius: 6px; padding: .5rem .75rem; font-size: .92rem; }}
    .filter-btn {{ background: #1e293b; color: #e2e8f0; border: 1px solid #334155; border-radius: 6px; padding: .45rem .75rem; cursor: pointer; font-size: .84rem; font-weight: 600; }}
    .filter-btn[aria-pressed="true"] {{ background: #0369a1; border-color: #38bdf8; color: #fff; }}
    main {{ padding: 1rem 1.5rem 4rem; }}
    section {{ margin-bottom: 2rem; }}
    table {{ width: 100%; border-collapse: collapse; margin-top: .7rem; font-size: .88rem; }}
    th, td {{ border-bottom: 1px solid #1e293b; padding: .55rem .6rem; text-align: left; vertical-align: top; }}
    th {{ color: #cbd5e1; font-weight: 700; background: rgba(17,26,46,.7); }}
    a {{ color: var(--accent); text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    code {{ background: #0f172a; padding: .1rem .32rem; border-radius: 4px; color: #7dd3fc; font-size: .85em; }}
    .muted {{ color: var(--muted); font-size: .82rem; margin-top: .2rem; }}
    .tag, .tag-ok, .tag-warn, .tag-info, .tag-muted {{ display: inline-block; padding: .12rem .45rem; border-radius: 999px; font-size: .74rem; font-weight: 700; letter-spacing: .02em; }}
    .tag-ok {{ background: rgba(74,222,128,.16); color: #86efac; border: 1px solid rgba(74,222,128,.35); }}
    .tag-warn {{ background: rgba(251,191,36,.16); color: #fde68a; border: 1px solid rgba(251,191,36,.35); }}
    .tag-info {{ background: rgba(56,189,248,.14); color: #7dd3fc; border: 1px solid rgba(56,189,248,.35); }}
    .tag-muted {{ background: rgba(148,163,184,.14); color: #cbd5e1; border: 1px solid rgba(148,163,184,.3); }}
    .callout {{ background: #111a2e; border-left: 4px solid var(--ok); padding: .85rem 1rem; border-radius: 6px; margin-top: .8rem; font-size: .9rem; }}
    footer {{ border-top: 1px solid #1e293b; padding: 1.5rem; text-align: center; color: var(--muted); font-size: .85rem; }}
    @media (prefers-reduced-motion: reduce) {{ * {{ transition: none !important; animation: none !important; }} }}
  </style>
</head>
<body>
  <a class="skip-link" href="#main-content">Skip to main content</a>
  <header>
    <div class="wrap">
      <div class="eyebrow">Single Canonical Public Research Vault &amp; Live Ecosystem Mirror &middot; {html.escape(version)}</div>
      <h1>0thernes Research Archive</h1>
      <p class="lead">Master SHA-256 audited consolidation hub authored by Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA; ORCID <code>0009-0006-8168-9648</code>). Strictly public non-fork repositories only; synced live with upstream builds and specialist atlases (<code>{html.escape(synced_utc)}</code>).</p>
      <div class="kpis" aria-label="Archive summary metrics">
        <div class="kpi"><div class="kpi-num">{total_entries}</div><div class="kpi-lbl">Public Entries (3 Tiers)</div></div>
        <div class="kpi"><div class="kpi-num">{unique_repos} / {pinned_subs}</div><div class="kpi-lbl">Tracked Repos / Submodules</div></div>
        <div class="kpi"><div class="kpi-num">{bridge['grand_problems_retired']} / {bridge['mega_atlas_total_problems']}</div><div class="kpi-lbl">Grand Mega-Atlas Retired</div></div>
        <div class="kpi"><div class="kpi-num">{bridge['epistemic_summary']['published_open_subconjectures_proved_in_lean']}</div><div class="kpi-lbl">Peer Sub-Conjectures Proved</div></div>
        <div class="kpi"><div class="kpi-num">{total_build_lean:,}</div><div class="kpi-lbl">Tier II Lean 4 Decls</div></div>
      </div>
      <nav class="pills" aria-label="Machine-readable endpoints">
        <a class="pill" href="https://github.com/0thernes/0thernes-research-archive">GitHub Vault</a>
        <a class="pill" href="registry/PAPERS.json">PAPERS.json</a>
        <a class="pill" href="registry/BUILD_PAPERS.json">BUILD_PAPERS.json</a>
        <a class="pill" href="registry/LAWS_AND_DISCOVERIES.json">LAWS_AND_DISCOVERIES.json</a>
        <a class="pill" href="registry/SOLVED_AND_ATLAS_BRIDGE.json">SOLVED_AND_ATLAS_BRIDGE.json</a>
        <a class="pill" href="registry/LIVE_ECOSYSTEM_MIRROR.json">LIVE_ECOSYSTEM_MIRROR.json</a>
        <a class="pill" href="CHECKSUMS.sha256">CHECKSUMS.sha256</a>
        <a class="pill" href="llms.txt">llms.txt</a>
      </nav>
    </div>
  </header>
  <main id="main-content" class="wrap">
    <div class="controls" role="search" aria-label="Filter archive entries">
      <label for="search-box" class="muted" style="margin:0;">Search:</label>
      <input id="search-box" type="search" placeholder="Filter by ID (0TH-2026-013, CS-053, QM-011), repo, or keyword…"/>
      <button type="button" class="filter-btn" data-section="all" aria-pressed="true">All</button>
      <button type="button" class="filter-btn" data-section="bridge" aria-pressed="false">Mega-Atlas Bridge</button>
      <button type="button" class="filter-btn" data-section="mirror" aria-pressed="false">Live Mirror</button>
      <button type="button" class="filter-btn" data-section="tier1" aria-pressed="false">Tier I ({len(papers)})</button>
      <button type="button" class="filter-btn" data-section="tier2" aria-pressed="false">Tier II ({len(builds)})</button>
      <button type="button" class="filter-btn" data-section="tier3" aria-pressed="false">Tier III ({len(discs)})</button>
    </div>

    <section data-group="bridge" aria-labelledby="h-bridge">
      <h2 id="h-bridge">Solved Sub-Conjectures &amp; Mega-Atlas V2 Cross-Reference Bridge</h2>
      <div class="callout">{html.escape(bridge['epistemic_summary']['statement'])}</div>
      <table>
        <thead><tr><th>Archive ID</th><th>Repository</th><th>Epistemic Class</th><th>Mega-Atlas IDs</th><th>Verified Scope &amp; Honesty Boundary</th></tr></thead>
        <tbody>{"".join(bridge_rows)}</tbody>
      </table>
    </section>

    <section data-group="mirror" aria-labelledby="h-mirror">
      <h2 id="h-mirror">Live Upstream Ecosystem Mirror ({unique_repos} Public Repositories · Synced <code>{html.escape(synced_utc)}</code>)</h2>
      <table>
        <thead><tr><th>Repository</th><th>Archive IDs</th><th>Pinned</th><th>Live HEAD</th><th>Release</th><th>Latest CI</th><th>Status</th></tr></thead>
        <tbody>{"".join(mirror_rows)}</tbody>
      </table>
    </section>

    <section data-group="tier1" aria-labelledby="h-tier1">
      <h2 id="h-tier1">Tier I — Standalone Formalized Research Preprints ({len(papers)})</h2>
      <table>
        <thead><tr><th>ID</th><th>Date</th><th>Version</th><th>Title &amp; Domain</th><th>PDF SHA-256</th></tr></thead>
        <tbody>{"".join(paper_rows)}</tbody>
      </table>
    </section>

    <section data-group="tier2" aria-labelledby="h-tier2">
      <h2 id="h-tier2">Tier II — Public Build White Papers &amp; Embedded Pure Lean 4 Suites ({len(builds)})</h2>
      <table>
        <thead><tr><th>ID</th><th>Version</th><th>Title &amp; Domain</th><th>Lean 4 Audit</th></tr></thead>
        <tbody>{"".join(build_rows)}</tbody>
      </table>
    </section>

    <section data-group="tier3" aria-labelledby="h-tier3">
      <h2 id="h-tier3">Tier III — Public Laws, Pre-Registered Empirical Claims, Discoveries &amp; Open-Problem Atlases ({len(discs)})</h2>
      <table>
        <thead><tr><th>ID</th><th>Epistemic Tier</th><th>Title</th><th>Frozen Snapshots</th></tr></thead>
        <tbody>{"".join(disc_rows)}</tbody>
      </table>
    </section>
  </main>
  <footer>
    ORCID <a href="https://orcid.org/0009-0006-8168-9648">0009-0006-8168-9648</a> &middot;
    <a href="https://github.com/0thernes/0thernes-research-archive">0thernes-research-archive</a> &middot;
    Public-only cryptographic vault (zero private repositories).
  </footer>
  <script>
    (function() {{
      const input = document.getElementById('search-box');
      const btns = Array.from(document.querySelectorAll('.filter-btn'));
      const sections = Array.from(document.querySelectorAll('section[data-group]'));
      let active = 'all';
      function apply() {{
        const q = (input.value || '').trim().toLowerCase();
        sections.forEach(sec => {{
          const showSec = active === 'all' || sec.dataset.group === active;
          sec.style.display = showSec ? '' : 'none';
          if (!showSec) return;
          sec.querySelectorAll('tbody tr').forEach(tr => {{
            const hay = tr.dataset.search || '';
            tr.style.display = (!q || hay.includes(q)) ? '' : 'none';
          }});
        }});
      }}
      btns.forEach(b => b.addEventListener('click', () => {{
        active = b.dataset.section;
        btns.forEach(x => x.setAttribute('aria-pressed', String(x === b)));
        apply();
      }}));
      input.addEventListener('input', apply);
    }})();
  </script>
</body>
</html>
"""
    SITE.mkdir(parents=True, exist_ok=True)
    (SITE / ".nojekyll").write_text("", encoding="utf-8")
    (SITE / "index.html").write_text(page, encoding="utf-8", newline="\n")
    (SITE / "registry").mkdir(parents=True, exist_ok=True)
    for fname in (
        "PAPERS.json",
        "BUILD_PAPERS.json",
        "LAWS_AND_DISCOVERIES.json",
        "SOLVED_AND_ATLAS_BRIDGE.json",
        "LIVE_ECOSYSTEM_MIRROR.json",
    ):
        src = ROOT / "registry" / fname
        if src.exists():
            shutil.copy2(src, SITE / "registry" / fname)
    shutil.copy2(ROOT / "CHECKSUMS.sha256", SITE / "CHECKSUMS.sha256")
    if (ROOT / "llms.txt").exists():
        shutil.copy2(ROOT / "llms.txt", SITE / "llms.txt")
    print(f"PASS: Built WCAG 2.2 AA 3-tier + live mirror archive portal at {SITE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
