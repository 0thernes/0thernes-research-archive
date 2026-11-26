# Statement audit of the archive's results (2026-11-26)

This log records the audit behind [`RESULTS.md`](../../RESULTS.md) and the corrections it caused. The audit is an internal, AI-assisted review run under the author's direction. It is not peer review.

It ran in three cycles: (1) an audit of every Tier I and Tier II entry, described below; (2) corrections pushed to the source repositories' own claim documents; (3) a hostile re-audit of every ledger record against its Lean source, of the hub's text against the ledger, and of the cycle-2 corrections.

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

28 of the archive's 32 Lean projects were built at their pinned commits, all with `Build completed successfully` (26 without Mathlib, 2 with Mathlib). The four superseded Mathlib snapshots (`0TH-2026-001`, `-002`, `-003`, `-005`) were reviewed statically and not rebuilt. In every audit, every printed axiom set was within `propext`, `Classical.choice` and `Quot.sound`, and no `sorry` was found in a built target (statement-only comparator files contain `sorry` by design and are not built).

## Entries audited

All 36 Tier I and Tier II entries were audited. After cycle 3 the ledger holds 94 results from 28 of them (3 answered questions from the literature, 11 new theorems, 11 bounded or partial cases, 55 known results formalized, 14 engineering invariant suites); the other eight are listed in `RESULTS.md` with the reason they have no separate result.

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
| `0TH-2026-009` | Lean answers the Muller–Saniga stacking-limit question for disjoint squares and pentagrams, and proves Jonah's Conjecture E with one representative per case (Theorem B4 is cited from outside Lean). | Both answers are narrower than first claimed; nine modules (degrees 75, 480 and 729,344) are not compiled; the W(7,2) and Q⁺(9,2) lower bounds are filed as known results, because an earlier unreviewed note (Jonah, Zenodo, 20 October 2026) states exact values that imply them. |
| `0TH-2026-015` | Known facts, elementary identities and finite computations about the Hantzsche–Wendt group ring, Gardam's unit, Haah's CC1 curve and S₄. | The hub said the unit conjecture is open over ℂ; Gardam (arXiv:2312.05240) refuted it for this group. T1c's first conjunct is a tautology, T1e contains no Hensel tower, and T1f shows only that a necessary determinant test fails (the non-unit conclusion follows from Tabei, arXiv:2608.00103). Passman (arXiv:2108.06570) is now credited. Reclassified. |
| `0TH-2026-017` | Integer formalizations of classical identities: octonions, S⁶, the Albert algebra, E8 and the Golay code, Ramanujan τ, Fibonacci anyons and Markov triples. No new theorem. | The E8 "240 roots", Leech 196,560 and Moonshine 196,884 items are closed-form counts or plain arithmetic, the "Hurwitz barrier" is the inequality 0 < 9m² − 4 < 9m², and six kernels checked only the 8 comparator targets and their dependency closure. Added to the bridge. |
| `0TH-2026-018` | Known results formalized (the Haag–Kertzer–Rickards–Stange obstruction for three packings, Zhang's mod-32 theorem, Hurwitz's equation for n = 4, abelian sandpile laws), small computations and one elementary lattice-parity lemma. | "Our Exact Mod-32 Theorem" is Ying Zhang's (Acta Arith. 2007), now credited; T1d is a mod-8 congruence; T2b never states det = 100352; T2d's "universal" claim omitted a hypothesis. Reclassified. |
| `0TH-2026-019` | Counting identities for 2-blade nullities, coordinate right-multiplier families and finite certificates in Cayley–Dickson algebras. | Lean proves facts about the sign table and block counts; that these counts are annihilator dimensions is a paper lemma. 4 ∣ ν is Moreno's theorem and the n = 4 midpoint count is de Marrais's 42 assessors; both are credited in the ledger. Reclassified as a new-theorem suite. |
| `0TH-2026-008` | Companion survey to `0TH-2026-007`; no formal result of its own. | The hub record re-claimed the shared Lean suite, and its crosswalk counted generic 2×2 determinant identities as progress on Atlas problems; both corrected. |
| `0TH-2026-001`, `-002`, `-003`, `-005` | Superseded snapshots of `0TH-2026-009`, reviewed statically; no separate results. | The 97.24% figure (`-005`) is a Python calculation, not Lean. Two snapshots name a "0thernes LLC" that was never formed; their repositories are archived and read-only, so the text stays in those frozen copies. |
| `0TH-BUILD-001` to `-017`, except `-005`, `-006` and `-014` | Kernel-checked invariants of each repository's own software model; no open problem is retired. | Theorem counts include literal arithmetic and definitional identities; several physics- or biology-named theorems are elementary arithmetic; hub rows overstated what Lean covers (for example GF(2⁸) MDS recovery, the Vladimirov operator, a Toffoli popcount law). Ledger statements now say only what the cited declarations state. |
| `0TH-BUILD-004` | Classical lemmas and finite checks in eight open-problem areas. | The hub cited a dependency-graph run instead of the CI run; the n = 3 Lonely Runner item covers 27 of 64 residue classes, not 7/8; the conjecture is proved for up to 13 runners (arXiv:2604.23906), not 7. |
| `0TH-BUILD-005`, `-014` | No proof at the pinned commit: a source-review catalogue and a test-only telemetry hub. | `-005` was described as a "formal verification audit", and its version is v0.23.0+63 (git describe at the pin), not v0.14.3. `-014`'s invariants are tests, so it has no ledger result. |
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
- **error:** "Ubuntu 24.04 CI". GitHub's `ubuntu-latest` jobs in November 2026 ran on the `ubuntu-26.04` image (read from two run logs); the version number was removed in 11 places.
- **error:** six-kernel coverage for `0TH-2026-017` is the 8 comparator targets and their dependency closure, not all 93 declarations. Corrected; the other comparator-only repositories are checked in cycle 3.
- **error:** citation counts. Crossref title checks of 18 bibliographies at their pins found one wrong DOI each in `0TH-BUILD-008` (Nüchter et al. 2006; the correct DOI is 10.1016/j.cub.2006.03.089) and `0TH-BUILD-014` (Bedau, Snyder and Packard 1998). All other DOIs matched; arXiv, Zenodo and LIPIcs DOIs resolve through DataCite.
- **error:** `0TH-BUILD-005` version and date (v0.23.0+63 by `git describe` at the pin; PDF edition 2026-10-21).
- **gap:** `0TH-2026-017` had no bridge row. Added.
- **error:** the audit's own suggestions were checked before use: one proposed version label (v0.23.0+154) and one statement of the state of the art (Lonely Runner "known through 7 runners") were wrong and were not applied.
- **error (audit):** the `0TH-BUILD-007` audit called the Mega-Atlas's report of a Lean-certified proof of the Riemann Hypothesis "unverified", and the cycle-2 erratum repeated it. Both were wrong: the Lean FRO and the Mathlib Initiative certified Levent Alpöge's proof on 21 November 2026 ([joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)). The erratum was withdrawn upstream, and the hub's statements about the Atlas now say "solved by this work".

## Cycle 2: corrections in the source repositories

One reviewer per repository rewrote README, CLAIMS, LIMITATIONS, CITATION and docs text to match the audit, credited the prior work the audit named, and recorded errors in frozen papers and in Lean code in a dated `ERRATA.md` section instead of changing them. Where CI checks a checksum manifest that covers an edited file, the manifest was regenerated with the repository's own script, and RFC 3161 and OpenTimestamps tokens were re-minted where they bind it. Each repository's GitHub description was rewritten to match. Lean files, paper sources and PDFs were not edited, and archive pins were not moved: the ledger still describes the audited commits, and newer commits are reported by the live mirror.

| Entry | Repository | Commits |
|---|---|---|
| `0TH-2026-004` | [`kochen-specker-extremal-lab`](https://github.com/0thernes/kochen-specker-extremal-lab) | 9c8c016 |
| `0TH-2026-006` | [`multinomial-tv-conjecture`](https://github.com/0thernes/multinomial-tv-conjecture) | f807f8d |
| `0TH-2026-007` | [`human-synapse-bouton-lab`](https://github.com/0thernes/human-synapse-bouton-lab) | aeb47bf; 0174ff2 (manifest re-sealed after the 007 and 008 corrections) |
| `0TH-2026-008` | [`human-synapse-bouton-lab`](https://github.com/0thernes/human-synapse-bouton-lab) | 8c5a625 |
| `0TH-2026-009` | [`pauli-contextuality-lab`](https://github.com/0thernes/pauli-contextuality-lab) | 8cc02c3 |
| `0TH-2026-010` | [`catalytic-register-frontiers`](https://github.com/0thernes/catalytic-register-frontiers) | 2a159ce; 1d32df4 (manifest re-sealed) |
| `0TH-2026-011` | [`secmesh-pqsi`](https://github.com/0thernes/secmesh-pqsi) | e0892ed; c2bf7ca (manifest lines updated) |
| `0TH-2026-012` | [`coded-pir-mlwe-complexity-lab`](https://github.com/0thernes/coded-pir-mlwe-complexity-lab) | 400a8b3; 27e8f03 (manifest regenerated) |
| `0TH-2026-013` | [`p-vs-np-frontier-lab`](https://github.com/0thernes/p-vs-np-frontier-lab) | 296ec48 |
| `0TH-2026-014` | [`monodromia`](https://github.com/0thernes/monodromia) | 456968b |
| `0TH-2026-015` | [`promislow-fracton-amoeba`](https://github.com/0thernes/promislow-fracton-amoeba) | f0b9cac |
| `0TH-2026-016` | [`zero-error-torus-frontier`](https://github.com/0thernes/zero-error-torus-frontier) | ba30943; c9f54b1 (manifests regenerated) |
| `0TH-2026-017` | [`octonionica`](https://github.com/0thernes/octonionica) | dd28c46; 9e9279b (formalization.yaml corrected, CHECKSUMS re-sealed) |
| `0TH-2026-018` | [`apollonian-sandpile-markov`](https://github.com/0thernes/apollonian-sandpile-markov) | 0d11881 |
| `0TH-2026-019` | [`cayley-dickson-terrace-frontier`](https://github.com/0thernes/cayley-dickson-terrace-frontier) | 0ef44ab |
| `0TH-BUILD-001` | [`cellulogonic-mecha`](https://github.com/0thernes/cellulogonic-mecha) | 40ec5dd |
| `0TH-BUILD-002` | [`planaria`](https://github.com/0thernes/planaria) | 0597334 |
| `0TH-BUILD-003` | [`ultrametrica`](https://github.com/0thernes/ultrametrica) | 44e2dec |
| `0TH-BUILD-004` | [`unsolved-mathematics`](https://github.com/0thernes/unsolved-mathematics) | 22ace26; e56ac6e (data manifest timestamps re-minted) |
| `0TH-BUILD-005` | [`cosmogonic-quantum-mechalogodrom`](https://github.com/0thernes/cosmogonic-quantum-mechalogodrom) | a1c3886 |
| `0TH-BUILD-006` | [`black-hole-simulation-lab`](https://github.com/0thernes/black-hole-simulation-lab) | c2f9296 |
| `0TH-BUILD-007` | [`unsolved-problems-mega-atlas`](https://github.com/0thernes/unsolved-problems-mega-atlas) | 703e3db; ad3d5ed (wrong RH/GRH erratum withdrawn) |
| `0TH-BUILD-008` | [`cellular-engine-omega`](https://github.com/0thernes/cellular-engine-omega) | 342039e; 7626781 (CHECKSUMS regenerated and re-timestamped) |
| `0TH-BUILD-009` | [`autophage`](https://github.com/0thernes/autophage) | 005502a |
| `0TH-BUILD-010` | [`noetic-organism-omega`](https://github.com/0thernes/noetic-organism-omega) | 95c0ec6 |
| `0TH-BUILD-011` | [`asmodensius-native`](https://github.com/0thernes/asmodensius-native) | d658e1a |
| `0TH-BUILD-012` | [`xiaomi-17t-pro-lab`](https://github.com/0thernes/xiaomi-17t-pro-lab) | 42fbac5 |
| `0TH-BUILD-013` | [`alife-singularity-omega-package`](https://github.com/0thernes/alife-singularity-omega-package) | e78ef06 |
| `0TH-BUILD-014` | [`omega-triscale-observatory`](https://github.com/0thernes/omega-triscale-observatory) | d2fbe46 |
| `0TH-BUILD-015` | [`glitchling-jam`](https://github.com/0thernes/glitchling-jam) | e9efd97 |
| `0TH-BUILD-016` | [`ALife-Framework`](https://github.com/0thernes/ALife-Framework) | 8c79777 |
| `0TH-BUILD-017` | [`beast-civilization`](https://github.com/0thernes/beast-civilization) | ca347eb |
| `0TH-DISC-006` | [`unsolved-black-hole-problems`](https://github.com/0thernes/unsolved-black-hole-problems) | b6c7352 |

The four superseded snapshot repositories (`0TH-2026-001`, `-002`, `-003`, `-005`) are archived on GitHub and read-only; they already point to `pauli-contextuality-lab` and were not changed.

## Cycle 3: hostile re-audit

Five reviewers re-read every ledger record against its Lean source at the audited commit, its cited sources (arXiv, Crossref and DataCite APIs) and the kind definitions. Two independent reviewers re-read the hub's text against the ledger, and three re-read the cycle-2 commits.

- **Records:** 66 of the 94 stood as written, 28 were corrected, and none was withdrawn. Most corrections restore a hypothesis that the Lean statement needs (for example c > 0; a₀ > 0 and t > 0; a nonempty S; m ≥ 1, without which one stated identity is false at m = 0) or name a value or definition exactly. R13 stated the wrong sequence (the Lean definition has Z(4) = 14). R13 and R60 moved from bounded case to known result: R13's count is OEIS A164394, and R60's setting was classified by Levine, Pegden and Smart (Ann. of Math. 2017). Earlier reports of the same values were added to the limits of R7, R8 and R10.
- **Hub:** about 100 stale or overstated sentences were corrected, among them the counts in `llms.txt`, CLAIMS, the FAQ, ROADMAP, HARDENING_INDEX and the architecture page; six-kernel claims for repositories whose CI runs only `lake comparator`; and the citation count of `0TH-2026-013`. Bridge classes now follow the strongest ledger kind of each entry, and `verify_archive.py` and two tests check this. `0TH-BUILD-006`, which has no Lean at its pin, no longer has a bridge row, and its 8 declarations are no longer in the Tier II total (now 1,050).
- **Upstream:** 30 of the 33 repositories still had withdrawn claims outside the files cycle 2 edited: social-preview images, Pages sites, plan and ADR documents. A follow-up pass corrects them.

## Open items for the owner (not changed by this audit)

- **dilemma:** frozen Tier III snapshots under `discoveries/` (copied byte for byte from public upstream repositories and covered by the sealed freeze) name four non-public repositories and quote prompts. Editing them breaks the frozen copies; leaving them keeps the names public. The upstream public files carry the same text.
- **problem:** push-triggered sync needs a token secret in each upstream repository. Only the owner can create it.
- **concern:** the release tag `v2026.11.26` was moved twice, so one version string names several archive states. Future releases should use a new version instead of moving a tag.
- **issue:** frozen papers (PDF, LaTeX, arXiv bundles) and Lean names and docstrings in the source repositories still carry the errors listed in each repository's `ERRATA.md`. Fixing them in place needs a new release of each paper.
- **problem:** `LICENSE` files in some repositories (for example `glitchling-jam`, `beast-civilization`) and two archived snapshots name an "LLC" that was never formed. Only the owner can change the licence holder.
- **concern:** some release manifests that CI does not check were already out of date before this audit (for example `CHECKSUMS.sha256` in `noetic-organism-omega` and `autophage`). They are left for each repository's next release.
