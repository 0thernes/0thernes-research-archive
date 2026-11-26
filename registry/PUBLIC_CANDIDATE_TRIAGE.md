# Public Candidate Triage

**Purpose:** explain why public owner repositories discovered by the live mirror are
not automatically promoted into the epistemic research registries.

This file is a bounded triage snapshot (last manually audited 2026-11-26 UTC). The live source of truth for repository
presence, timestamps, and registration status is
[`PUBLIC_REPO_INVENTORY.json`](./PUBLIC_REPO_INVENTORY.json), which is refreshed by
the scheduled live-sync workflow. Promotion still requires an explicit registry
entry, a stable public artifact, a reproducible verification route, and claims
whose scope is stated narrowly enough to audit.

## Current high-signal candidates

| Repository | Current evidence | Classification | Required next evidence |
|---|---|---|---|
| [`glidiebirdie`](https://github.com/0thernes/glidiebirdie) | README advertises 55 Lean declarations and an AMS-LaTeX build paper; the formalization is currently on open [PR #37](https://github.com/0thernes/glidiebirdie/pull/37), branch `feat/v3.2.0-build-standard-lean-whitepaper`; the latest released main-line tag remains `v3.1.0`. | Discovery candidate; not a released theorem record and not evidence that an open conjecture was solved | Merge or release the formal package, then audit the exact theorem scope, axioms, artifact digests, and CI evidence before registration. |
| [`yarvpilled`](https://github.com/0thernes/yarvpilled) | Public README reports 31 Lean theorems and supporting C/CBMC/Kani/statistical material, but explicitly limits the Lean layer to integer bookkeeping/invariants and not the floating-point geometry. | Engineering/formal-invariant candidate; no new conjecture solved by current evidence | A bounded paper or claim dossier identifying a mathematical target, formal theorem statements, reproducible artifacts, and release-pinned verification. |
| [`xenophora`](https://github.com/0thernes/xenophora) | Mathematical and scientific literature is cited for the rendering/PDE design; the repository presents an implementation and literature lineage, not a new theorem or solved open problem. | Literature-backed build; discovery-only | A novel, independently stated result with a reproducible proof or falsifiable experiment if it is to enter the research registry. |
| [`professional-calculator`](https://github.com/0thernes/professional-calculator) | Large test-backed scientific calculator and knowledge atlas; current README emphasizes implementation correctness and type safety. | Software/tooling candidate | A separately scoped mathematical result, not merely calculator coverage, before promotion as research. |
| [`computer-evolution-lab`](https://github.com/0thernes/computer-evolution-lab) | Interactive museum and executable historical/modern computer models with tests and citations. | Educational/simulation build | A research claim and reproducible experimental dossier if a result beyond the museum is asserted. |

## Remaining discovery candidates

The other currently unregistered public repositories — `art-provenance-vault`,
`CQM2`, `forge-compiler`, `global-map-app`, `oppen-agent`, `prompt-architect`,
`thingmaker`, and `tsotchke-chaos` — remain discovery-only because their current
top-level artifacts describe products, architecture, demos, or operational tools,
not a released mathematical theorem, conjecture resolution, or bounded empirical
research record. This is not a quality judgment and is not a claim that their
software is untested; it is an epistemic registry boundary.

## Anti-overclaim rule

Lean declarations, passing CI, a large test count, citations to peer-reviewed
literature, or a repository description are not by themselves evidence that an
open conjecture was solved. The archive registers the exact statement and its
scope only after inspecting the released artifact and its verification route.

## Promotion gate for unreleased formal work

An open pull request, feature branch, untagged commit, or passing branch CI is
not eligible for a solved-result entry. Before promotion, a candidate must have
a public released commit or tag, a narrowly stated theorem or experiment, an
inspectable proof or reproduction route, recorded dependencies and axioms, and
an archive-side digest. If the result concerns an open problem, the exact
parent conjecture must be named and the evidence must distinguish a full proof
from a bounded case, reduction, obstruction, or engineering invariant.

