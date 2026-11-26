# Claim-Language Blind-Spot Scan — 2026-11-26

## Scope

The author's local working copies of the repositories (three folders of clones on one
workstation, kept by three different AI coding tools) were scanned. This is a local,
non-reproducible observation: the clones include private and work-in-progress repositories
that are not part of this archive.

Git itself identified **71 local repositories**. Research-facing `README*`, `CLAIMS*`,
paper, and Markdown audit/limitation files were searched for claim-language
patterns including `solved`, `proved`, `conjecture`, `proof of`, `breakthrough`,
and `open problem`.

The search returned research-language hits in **66 repositories**. This is a
lexical discovery count, not a count of mathematical claims: ordinary words such
as “resolved,” “proof,” and “solved” also occur in compiler, UI, issue, backlog,
and operational text.

## Findings

The high-signal results fell into three groups:

1. **Explicit non-retirement boundaries.** Many research builds explicitly state
   `0 / 1,900` Mega-Atlas grand problems retired and separate bounded formal
   results from the open parent problems.
2. **Already-registered bounded results.** The strongest theorem-level claims —
   multinomial TV, coded-PIR/MLWE, Strassen–Winograd rank, finite
   Kochen–Specker minima, catalytic-register theorems, finite Ramsey/Lonely
   Runner results, Pauli contextuality, and zero-error capacity records — already
   have archive entries and bridge classifications.
3. **Non-mathematical lexical matches.** Software behavior, compiler linking,
   issue resolution, calculator operations, and project-management notes were
   excluded from epistemic promotion.

## Result

No clearly unregistered high-confidence claim that a grand Mega-Atlas conjecture
was solved was found by this scan. The strongest unresolved candidate remains the
unreleased catalytic-register public head, which is already marked `AHEAD_OF_PIN`
by the live mirror and has an explicit Tier-4 open-frontier boundary.

This scan is a discovery aid, not a proof of absence. Promotion still requires a
scoped theorem/claim dossier, reproducible artifacts, a release or commit pin,
and an explicit statement of what remains open.

