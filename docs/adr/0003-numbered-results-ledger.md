# ADR 0003: One Numbered Results Ledger

- **Status:** Accepted (`2026-11-26`)
- **Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA; ORCID `0009-0006-8168-9648`)
- **Builds on:** [ADR 0002](0002-canonical-hub-and-live-sync.md) (single canonical hub and live sync)

## Context

The hub answers "which repositories exist and are they intact". It did not answer, in one readable place, "what exactly has been proven". That information was spread across long table cells in `README.md`, the Mega-Atlas bridge and each paper, written per repository rather than per result, and mixed with build and provenance detail. A reader could not see a plain list of results, and a claim's wording was never tied to an audit of the statement itself.

## Decision

1. **One list.** `RESULTS.md` is the single numbered list of results. It is generated; nobody edits it by hand.
2. **One source.** `registry/RESULTS_LEDGER.json` holds one record per audited result: a plain statement, its kind, its evidence, the question it answers (if any), the Lean declarations with file and line, the commit that was audited, the audit outcome, its limits and a check command.
3. **Joined, not copied.** Version, repository, pin and paper path are not stored in the ledger. `scripts/build_ledger.py` joins them from `registry/PAPERS.json` and `registry/BUILD_PAPERS.json`, and reads the live mirror for upstream state. The ledger therefore follows every registry update and every live sync without anyone retyping a number.
4. **An audit is tied to a commit.** Evidence links are permalinks at the audited commit. If the archive pin moves past it, the result is shown as "re-audit pending". If the source repository moves past the pin, the result says so.
5. **Nothing is silently missing.** Every Tier I and Tier II entry appears: through its results, through a stated reason, or under "registered but not yet audited into this ledger".
6. **Numbers are permanent.** A result that is narrowed keeps its number. A result that fails is marked withdrawn and keeps its number.
7. **Wording is checked.** The generator rejects promotional wording, a "published open question answered" without a cited source and a recorded statement audit and prior-work search, a "new theorem" that is known mathematics, and a kernel-checked result without a cited declaration.

## Consequences

- **Positive:** one page a reader can check line by line; counts in `README.md` come from the ledger; the list cannot drift from the registries; a release or a pin move cannot inherit an audit it did not have.
- **Cost:** a result enters the list only after a statement audit, so the ledger can lag behind a new paper. The lag is visible, by design.
- **Limit:** the audit is an internal, AI-assisted check directed by the author. It is not peer review, and the ledger says so at the top.

## How to use

```bash
python scripts/build_ledger.py            # regenerate RESULTS.md and the README block
python scripts/build_ledger.py --check    # fail if the ledger is invalid or the outputs are stale
python scripts/build_ledger.py --check --checkouts <dir>   # also confirm each Lean declaration is at the cited line
```

`python scripts/verify_archive.py --sync` runs the first form; `python scripts/verify_archive.py` runs the second.
