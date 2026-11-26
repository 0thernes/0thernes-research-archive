# Legacy Index and Results-Ledger Migration

**Status:** Canonical policy note  
**Audited:** 2026-11-26 UTC

## Purpose

Several local worktrees contain older archive-like indexes, including the Claude
hub at `Math Conjectures on Retard Breinraut Mode - Claude\hub`. Those indexes
are useful working records, but they are not independent evidence and are not
authoritative when they disagree with this repository.

## Canonical source

The authoritative public index is:

- [GitHub archive](https://github.com/0thernes/0thernes-research-archive)
- [Live archive portal](https://0thernes.github.io/0thernes-research-archive/)
- [`PAPERS.json`](PAPERS.json), [`BUILD_PAPERS.json`](BUILD_PAPERS.json), and [`LAWS_AND_DISCOVERIES.json`](LAWS_AND_DISCOVERIES.json)
- [`SOLVED_AND_ATLAS_BRIDGE.json`](SOLVED_AND_ATLAS_BRIDGE.json)
- [`LIVE_ECOSYSTEM_MIRROR.json`](LIVE_ECOSYSTEM_MIRROR.json)

The canonical archive currently records five bounded peer-literature
open-sub-conjecture/open-question results, while retaining the strict boundary
of `0 / 1,900` grand Mega-Atlas problems retired. A legacy ledger reporting zero
entries is therefore a stale or incomplete view, not contradictory evidence.

## Migration rule

Legacy ledgers and duplicate lists may contribute candidate metadata, missing
provenance, or a proposed schema. They must not replace the canonical bridge or
promote a claim automatically. To migrate an entry, an operator must:

1. identify the public repository, release or commit, and exact statement;
2. classify it as a published open question, new theorem, bounded case,
   refutation, known result formalization, or engineering invariant;
3. record the evidence artifact, verification route, dependencies, and axiom
   boundary;
4. preserve the parent-problem boundary and state whether the result retires a
   grand Mega-Atlas problem; and
5. run `python scripts/verify_archive.py --sync` and the archive test suite.

Until those gates pass, a legacy entry remains discovery-only. No local legacy
worktree is reset, cleaned, or overwritten by this policy.
