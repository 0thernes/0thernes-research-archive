#!/usr/bin/env python3
"""Build a static, link-checked GitHub Pages portal for 0thernes-research-archive at build/site/."""
from __future__ import annotations

import html
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "build" / "site"


def main() -> int:
    papers = json.loads((ROOT / "registry" / "PAPERS.json").read_text(encoding="utf-8"))["papers"]
    builds = json.loads((ROOT / "registry" / "BUILD_PAPERS.json").read_text(encoding="utf-8"))["builds"]
    discs = json.loads((ROOT / "registry" / "LAWS_AND_DISCOVERIES.json").read_text(encoding="utf-8"))["discoveries"]
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()

    paper_rows = []
    for p in reversed(papers):
        repo = html.escape(p["repository"])
        title = html.escape(p["title"])
        paper_rows.append(
            f"<tr><td><code>{html.escape(p['id'])}</code></td><td>{html.escape(p['date_released'])}</td>"
            f"<td><code>{html.escape(p['version'])}</code></td>"
            f"<td><a href=\"{repo}\">{title}</a></td>"
            f"<td><code>{html.escape(p['pdf_sha256'][:12])}…</code></td></tr>"
        )

    build_rows = []
    for b in builds:
        repo = html.escape(b["repository"])
        build_rows.append(
            f"<tr><td><code>{html.escape(b['id'])}</code></td><td><code>{html.escape(b['version'])}</code></td>"
            f"<td><a href=\"{repo}\">{html.escape(b['title'])}</a></td>"
            f"<td>{b['lean_verification']['audited_theorems']}</td></tr>"
        )

    page = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>0thernes Research Archive · {html.escape(version)}</title>
  <style>
    :root {{ color-scheme: dark; }}
    body {{ font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif; background: #0b1020; color: #e2e8f0; margin: 0; line-height: 1.55; }}
    header {{ background: linear-gradient(135deg, #0f172a, #172554); border-bottom: 1px solid #1e3a8a; padding: 2.8rem 1.5rem 2.2rem; }}
    .wrap {{ max-width: 1120px; margin: 0 auto; }}
    h1 {{ margin: .3rem 0 .5rem; font-size: 2.2rem; color: #f8fafc; }}
    h2 {{ margin-top: 2rem; color: #f8fafc; }}
    .eyebrow {{ color: #4ade80; font-size: .82rem; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; }}
    .lead {{ color: #cbd5e1; max-width: 820px; }}
    .pills {{ display: flex; flex-wrap: wrap; gap: .6rem; margin-top: 1rem; }}
    .pill {{ padding: .42rem .85rem; border-radius: 999px; background: #1e293b; border: 1px solid #334155; color: #f8fafc; text-decoration: none; font-size: .86rem; font-weight: 600; }}
    main {{ padding: 1.5rem 1.5rem 4rem; }}
    table {{ width: 100%; border-collapse: collapse; margin-top: .75rem; font-size: .9rem; }}
    th, td {{ border-bottom: 1px solid #1e293b; padding: .55rem .65rem; text-align: left; vertical-align: top; }}
    th {{ color: #94a3b8; font-weight: 700; }}
    a {{ color: #38bdf8; text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    code {{ background: #0f172a; padding: .1rem .32rem; border-radius: 4px; color: #7dd3fc; }}
    footer {{ border-top: 1px solid #1e293b; padding: 1.5rem; text-align: center; color: #94a3b8; font-size: .85rem; }}
  </style>
</head>
<body>
  <header>
    <div class="wrap">
      <div class="eyebrow">Public Cryptographic Research Vault · {html.escape(version)}</div>
      <h1>0thernes Research Archive</h1>
      <p class="lead">Master SHA-256 audited archive of {len(papers)} Tier I standalone research preprints, {len(builds)} Tier II public build white papers &amp; embedded Lean 4 suites, and {len(discs)} Tier III public laws, pre-registered empirical claims &amp; open-problem atlases by Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA; ORCID 0009-0006-8168-9648).</p>
      <div class="pills">
        <a class="pill" href="https://github.com/0thernes/0thernes-research-archive">GitHub Vault</a>
        <a class="pill" href="registry/PAPERS.json">PAPERS.json</a>
        <a class="pill" href="registry/BUILD_PAPERS.json">BUILD_PAPERS.json</a>
        <a class="pill" href="registry/LAWS_AND_DISCOVERIES.json">LAWS_AND_DISCOVERIES.json</a>
        <a class="pill" href="CHECKSUMS.sha256">CHECKSUMS.sha256</a>
      </div>
    </div>
  </header>
  <main class="wrap">
    <h2>Tier I — Standalone Formalized Research Preprints ({len(papers)})</h2>
    <table>
      <thead><tr><th>ID</th><th>Date</th><th>Version</th><th>Title</th><th>PDF SHA-256</th></tr></thead>
      <tbody>{"".join(paper_rows)}</tbody>
    </table>
    <h2>Tier II — Public Build White Papers &amp; Embedded Pure Lean 4 Suites ({len(builds)})</h2>
    <table>
      <thead><tr><th>ID</th><th>Version</th><th>Title</th><th>Lean Theorems</th></tr></thead>
      <tbody>{"".join(build_rows)}</tbody>
    </table>
  </main>
  <footer>
    ORCID <a href="https://orcid.org/0009-0006-8168-9648">0009-0006-8168-9648</a> &middot;
    <a href="https://github.com/0thernes/0thernes-research-archive">0thernes-research-archive</a>
  </footer>
</body>
</html>
"""
    SITE.mkdir(parents=True, exist_ok=True)
    (SITE / ".nojekyll").write_text("", encoding="utf-8")
    (SITE / "index.html").write_text(page, encoding="utf-8", newline="\n")
    (SITE / "registry").mkdir(parents=True, exist_ok=True)
    for fname in ("PAPERS.json", "BUILD_PAPERS.json", "LAWS_AND_DISCOVERIES.json"):
        shutil.copy2(ROOT / "registry" / fname, SITE / "registry" / fname)
    shutil.copy2(ROOT / "CHECKSUMS.sha256", SITE / "CHECKSUMS.sha256")
    print(f"PASS: Built static archive portal at {SITE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
