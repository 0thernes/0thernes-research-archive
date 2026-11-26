# ADR 0002: Single Canonical Public Hub, Atlas Consolidation, and Real-Time Live Sync

- **Status:** Accepted (`2026-11-25`)
- **Author:** Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA; ORCID `0009-0006-8168-9648`)
- **Supersedes:** Scattered ad-hoc manual synchronization across specialist catalogues

## Context

Across the `0thernes` GitHub ecosystem, five repositories previously appeared to act as overlapping "lists or archives":

1. `0thernes/0thernes-research-archive` — Public cryptographic master vault of all Tier I preprints, Tier II build white papers & Lean 4 suites, and Tier III laws/discoveries/atlases.
2. `0thernes/unsolved-problems-mega-atlas` — Cross-disciplinary 1,900-problem open-problems connectome (`0TH-BUILD-007`).
3. `0thernes/unsolved-mathematics` — Mathematics-focused open-problem atlas and 8-domain Lean 4 structural core (`0TH-BUILD-004`, `0TH-DISC-005`).
4. `0thernes/unsolved-black-hole-problems` — 16-problem ranked black-hole physics catalogue (`0TH-DISC-006`).
5. Private research staging repositories (strictly non-public; never referenced or indexed in public vaults).

Without a unified live-sync layer and cross-atlas bridge, readers and agents had to inspect multiple repositories to answer basic questions: *"Which repository is the authoritative master list?"*, *"Which upstream repos have moved ahead of their frozen release pin?"*, and *"Have any of the 1,900 Mega-Atlas problems or smaller peer-literature conjectures been formally proved?"*

## Decision

1. **Single Canonical Public Hub:** Establish `0thernes/0thernes-research-archive` (and its GitHub Pages portal `https://0thernes.github.io/0thernes-research-archive/`) as the **one authoritative public master hub**. Specialist open-problem catalogues remain focused domain spokes indexed inside Tier II / Tier III and link back to the hub.
2. **Authoritative Solved-Subconjecture & Mega-Atlas Bridge:** Maintain `registry/SOLVED_AND_ATLAS_BRIDGE.json` (and derived `.md`) inside this hub, explicitly enforcing `grand_problems_retired = 0 / 1900` while indexing every machine-checked peer-literature sub-conjecture, bounded partial result, barrier formalization, and discrete invariant suite.
3. **Hybrid Pull + Push Real-Time Live Sync (Preserving Release Immutability):**
   - **Pull-based scheduled mirror (zero secrets required):** `.github/workflows/live-sync.yml` runs `scripts/live_sync.py` every 2 hours (`0 */2 * * *`) using the standard `GITHUB_TOKEN` to refresh `registry/LIVE_ECOSYSTEM_MIRROR.json/.md`, update `README.md`'s bounded live status block, re-run `verify_archive.py --sync` + `pytest`, and commit straight to `main` (which immediately redeploys GitHub Pages).
   - **Push-based instant dispatch (opt-in):** Upstream repos carrying `.github/workflows/notify-archive.yml` (template in `docs/upstream-notify-workflow.yml`) fire `repository_dispatch` (`upstream-repo-updated`) on every `main` push once `ARCHIVE_SYNC_TOKEN` is configured.
   - **Why we do NOT inject commits into already-attested Tier I release repos:** Pushing cosmetic workflow files onto completed, Sigstore/Rekor-attested releases would break `HEAD == release_tag` parity and trigger redundant 20-minute 6-kernel CI runs. The 2-hour scheduled pull mirror already tracks every public repo automatically without disturbing immutable release tags.
4. **Strict Public-Only Privacy Firewall:** `scripts/live_sync.py` rejects any repository where `private == true`, `fork == true`, or `owner != 0thernes`, enforced both at runtime and in `tests/test_archive_integrity.py`.

## Consequences

- **Positive:** One single canonical source of truth, automatically refreshed live mirror and GitHub Pages portal, zero broken cross-atlas links, and strict separation between immutable frozen release pins and live upstream `main` HEADs.
- **Trade-off:** Instant sub-minute push updates require setting one optional `ARCHIVE_SYNC_TOKEN` secret on upstream repos; without it, sync latency is bounded by the 2-hour schedule (or instant via manual `workflow_dispatch`).

## Update (2026-11-26): what is actually running

An audit of the workflow history and the upstream repositories on 2026-11-26 found that the push path had never fired: 0 of the hub's sync runs were started by `repository_dispatch`, 2 of the 41 tracked repositories carried a notify workflow, and none had the `ARCHIVE_SYNC_TOKEN` secret. The mirror is therefore a scheduled pull, and calling it "real-time" overstated it. Changes made:

- The schedule moved from every 2 hours to hourly (`17 * * * *`; minute 17 avoids the top-of-hour queue, where GitHub delays scheduled runs most).
- Generated and hand-written text now says "refreshed hourly" and states that push dispatch is optional and not configured.
- The mirror's `synced_utc` stamp is the time of the last change in upstream state, not of the last check; the generated page says so.

Push-triggered refresh remains available as an owner action: create one fine-grained token that may send `repository_dispatch` to this repository, and store it as `ARCHIVE_SYNC_TOKEN` in each upstream repository that carries the notify workflow. Tokens are never created or stored by automation in this repository. The numbered results list ([ADR 0003](0003-numbered-results-ledger.md)) does not depend on this path: it joins versions and pins from the registries on every sync and marks results whose source has moved past the audited commit.
