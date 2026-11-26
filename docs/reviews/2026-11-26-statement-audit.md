# Statement audit of the archive's results (2026-11-26)

This log records the audit behind [`RESULTS.md`](../../RESULTS.md) and the corrections it caused. It is updated as each entry's audit finishes. The audit is an internal, AI-assisted review run under the author's direction. It is not peer review.

## Method

For every Tier I and Tier II entry, at the commit the archive pins:

1. **Rebuild.** `lake build` in a fresh clone checked out at the pinned commit, one project at a time, on Windows 11 with Lean 4.35.0. Fourteen Tier I projects without Mathlib were built from scratch (2 to 128 seconds each). Twelve Tier II projects had been built in the same fresh clones by the first, interrupted audit run; Lake confirmed them up to date. The two active Mathlib projects were built on top of the downloaded Mathlib cache. The six-kernel `lake comparator --paranoid` replays need Linux `bubblewrap` and were not re-run; for those the audit checked the cited CI run and its commit instead.
2. **Trust base.** A scan of every Lean file for `sorry`, `admit`, `native_decide`, `axiom` declarations, `unsafe`, `@[extern]`, `@[implemented_by]` and `opaque`, and `#print axioms` on the headline theorems after the rebuild.
3. **Statement fidelity.** A formal auditor read each headline Lean statement down to its definitions and compared it with the claim in the README, the paper and the archive's registry.
4. **Literature.** A second auditor opened the cited source at the cited place, checked whether it poses the question as open, and searched for earlier and parallel work (arXiv, Semantic Scholar citations, Crossref, web search; queries are recorded in each report).
5. **Blind referee.** For each entry that claimed to answer a published question, a third auditor who did not see the other reports worked only from the source paper and the Lean files.
6. **Skeptic.** A final auditor tried to refute every critical and major finding from primary evidence, kept only what it reproduced, resolved disagreements, and proposed the ledger records.
7. **Review.** The author's session applied the corrections, rejected wording that added new claims, recorded its own decisions in the ledger overrides with reasons, and checked by script that every Lean declaration cited in the ledger is at the cited file and line in the audited commit.

Findings use the ten classes of Build Standard v1.2.0 (bug, error, issue, problem, concern, dilemma, conflict, gap, hole, blindspot).

## Rebuild results

28 of the archive's 32 Lean projects were built at their pinned commits, all with `Build completed successfully` (26 without Mathlib, 2 with Mathlib). The four superseded Mathlib snapshots (`0TH-2026-001`, `-002`, `-003`, `-005`) were reviewed statically and not rebuilt. In the audits completed so far, every printed axiom set was within `propext`, `Classical.choice` and `Quot.sound`, and no `sorry` was found in a built target (statement-only comparator files contain `sorry` by design and are not built).

## Entries audited so far

| Entry | Outcome | Main correction |
|---|---|---|
| `0TH-2026-006` | Conjecture 7.7 of Banić–Elezović (arXiv:2610.17046v1) is proved as stated. | The γ closed forms are algebra on the preprint's formulas, not "100% kernel-checked unconditional" variance results; the source is an unrefereed preprint, not "peer literature"; Part 5 locators were wrong (Theorem 5.2 is 3.10). |
| `0TH-2026-010` | New kernel-checked theorems extending Vinciguerra (arXiv:2609.18692). | Section 6 of the source poses neither question the archive said it resolved; "optimal" and "unique global minimiser" are not proved. Reclassified from solved sub-conjecture to new-theorem suite. |
| `0TH-2026-012` | Elementary identities, finite certificates and known results formalized; numerical experiments outside Lean. | "Resolves the Sun–Tao–Xu–Zhang problem" and "refutes Luo" are unsupported (the cited Luo paper contains no such argument); the Lean model of FIPS 203 Compress_1 differs from the standard at x = 832. Reclassified. |
| `0TH-2026-016` | Θ(C₂₅) ≥ 12.3442 and Θ(C₂₉) ≥ 14.3199 exceed the best published values found; the C₂₇ and C₃₁ bounds are below values published in 2003. | "Resolves Tandon Open Problem #2" is unsupported (the source lists a future-work direction, and the Lean theorem assumes the condition it was asked to find); "world records" withdrawn for C₂₇ and C₃₁; Codenotti–Gerace–Resta (2003) now cited. Reclassified. |
| `0TH-2026-004` | Lean proves the minima 31 and 18 for two finite ray pools; SAT certificates support 31, 33 and 29 in further pools. | The Lean and six-kernel credentials applied only to two of the four numbers; Kernaghan (arXiv:2603.16988v10) has independent proofs of 31 and 33. |
| `0TH-2026-007` | Elementary inequalities and conservation identities about the repository's own synapse-model formulas. | "23/23 live Crossref citations verified" was false (one DOI wrong); the biological "refutation" rests on simulator constants. Reclassified. |
| `0TH-2026-011` | Integer, Boolean and polynomial facts behind known cryptographic and quantum-information results. | The "Toner monogamy" proof assumes the quantum reduction; the "Chern–Concurrence–Entropy Conservation Law" is the double-angle identity (Jakob–Bergou 2003); the Compress_1 model deviates from FIPS 203. Reclassified. |
| `0TH-2026-013` | The Baker–Gill–Solovay theorem, the counting step of natural proofs and twelve classical lemmas. | Two listed results (slice monotonicity, Schaefer dichotomy) do not exist in the code; "27/27 live verified citations" was false (three DOIs resolve to unrelated papers). |
| `0TH-2026-014` | Integer and Laurent-polynomial identities for six known non-Hermitian and knot models. | Physics-named theorems are arithmetic in Lean; one conjunct is vacuous (ρ³ = ρ + 1 has no integer solution); several "new" results are published (Bode et al. 2017, Hartley 1979, Wiersig 2023). Reclassified. |
| `0TH-BUILD-006` | No Lean result at the pinned commit. | The eight theorems are literal arithmetic on an unmerged branch; one passes with wrong constants because of truncated natural-number subtraction. |

## Hub findings fixed in this round

- **error (critical):** `0TH-DISC-005` was titled a "900+ open-problem atlas"; the source repository holds 106 problems. Fixed.
- **conflict:** the hub's own privacy firewall spelled three non-public repository names in public scripts and tests. Replaced by SHA-256 digests (`scripts/privacy.py`); the check now also covers code, tests and docs, and never prints a name.
- **issue:** "real-time" sync. The history showed 0 dispatch-triggered runs and no upstream token. The schedule is now hourly and the wording says what runs ([ADR 0002 update](../adr/0002-canonical-hub-and-live-sync.md)).
- **hole:** `live_sync.py --offline` (used by `just sync`) erased the committed live state. Fixed, with a regression test.
- **hole:** archive totals were guarded on one README line only. `check_prose_counts` now fails on any stale total in current-state prose.
- **hole:** a test pinned the literal "5 solved sub-conjectures". It now derives the count and checks that the bridge and the Results Ledger agree.
- **gap:** no one-command re-seal of the RFC 3161 release freeze. Added `scripts/stamp_freeze.py` (`just seal`).
- **concern:** workstation paths in a public registry file; CITATION.cff licence did not match LICENSE. Fixed.

## Open items for the owner (not changed by this audit)

- **dilemma:** frozen Tier III snapshots under `discoveries/` (copied byte for byte from public upstream repositories and covered by the sealed freeze) name four non-public repositories and quote prompts. Editing them breaks the frozen copies; leaving them keeps the names public. The upstream public files carry the same text.
- **problem:** push-triggered sync needs a token secret in each upstream repository. Only the owner can create it.
- **concern:** the release tag `v2026.11.26` was moved twice, so one version string names several archive states. Future releases should use a new version instead of moving a tag.
- Upstream repositories still carry the corrected wording in their own READMEs and papers; those fixes are tracked per repository.
