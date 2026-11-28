# External Scholarly Portal Submission Packet (`0thernes-research-archive`)

- **Generated (UTC):** `2026-11-28T05:10:27Z`
- **Author:** Alexander Stephen Donahue (`Independent Researcher, Spokane, WA, USA`)
- **ORCID:** [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648) · **Email:** `0_0@0thernes.art`
- **Policy Compliance:** No credentials, 2FA, CAPTCHAs, personal attestations, CLAs, or portal rate limits are bypassed.

---

## 1. ORCID (`0009-0006-8168-9648`) — Live Verified (`58/58` Works Already Synced)

- Public ORCID API audit confirms **102** live work groups already cover **29/29** Tier-I, **17/17** Tier-II, and **12/12** Tier-III entries.
- Updated BibTeX exports with all **26** API-verified Zenodo DOIs & `0TH-2026-023 v2.1.0`: [`registry/orcid_works.bib`](../registry/orcid_works.bib) and [`registry/orcid_works_import.bib`](../registry/orcid_works_import.bib).
- New `quantum-latin-spectrum-frontier v2.1.0` DOI [`10.5281/zenodo.24618988`](https://doi.org/10.5281/zenodo.24618988) syncs automatically via DataCite (or can be imported directly via **Works -> + Add -> Add DOI**).

---

## 2. Zenodo DOIs — Live Minted (`25/25` Active Tier-I Papers + `0TH-BUILD-004`)

- **All 25 active Tier-I entries** (plus `0TH-BUILD-004 unsolved-mathematics` [`10.5281/zenodo.24618624`](https://doi.org/10.5281/zenodo.24618624)) now hold live API-verified Zenodo DOIs recorded in [`registry/PAPERS.json`](../registry/PAPERS.json) and [`registry/BUILD_PAPERS.json`](../registry/BUILD_PAPERS.json).
- The 4 non-Zenodo Tier-I entries (`001, 002, 003, 005`) are superseded read-only archived GitHub repositories consolidated into `0TH-2026-009` (`pauli-contextuality-lab`, [`10.5281/zenodo.24618608`](https://doi.org/10.5281/zenodo.24618608)).

---

## 3. Palomar Registry (`submit.palomar-registry.org`) — 6 Verified `v0.4` Repos Ready Now

All **6** repositories below passed `scripts/validate_palomar_v04.py` (`0` errors against `schema/palomar-v0.4.schema.json`) and have **GREEN 6-kernel Lean 4.35.0 CI** at the exact 40-char commit SHA listed:

| Archive ID | Repository | Release | Verified 40-Char Commit SHA | `v0.4` Schema | 6-Kernel CI | Zenodo DOI |
|---|---|---|---|---|---|---|
| `0TH-2026-023` | [quantum-latin-spectrum-frontier](https://github.com/0thernes/quantum-latin-spectrum-frontier) | `v2.1.0` | `08128d316d8dc82ed840c65ceb394e7d65dc39e5` | **PASS (0 err)** | [10/10 GREEN](https://github.com/0thernes/quantum-latin-spectrum-frontier/actions/runs/46109609387) | [`10.5281/zenodo.24618988`](https://doi.org/10.5281/zenodo.24618988) |
| `0TH-2026-029` | [barker-hadamard-frontier](https://github.com/0thernes/barker-hadamard-frontier) | `v1.0.0` | `f4fef9aeaa7df2ef0d3cc442967144624e782066` | **PASS (0 err)** | [GREEN](https://github.com/0thernes/barker-hadamard-frontier/actions) | [`10.5281/zenodo.24618540`](https://doi.org/10.5281/zenodo.24618540) |
| `0TH-2026-026` | [schur-clifford-frontier](https://github.com/0thernes/schur-clifford-frontier) | `v1.1.0` | `bb2fdd0a4c779f118e688438ba32477e129dd78c` | **PASS (0 err)** | [GREEN](https://github.com/0thernes/schur-clifford-frontier/actions) | [`10.5281/zenodo.24618580`](https://doi.org/10.5281/zenodo.24618580) |
| `0TH-2026-014` | [monodromia](https://github.com/0thernes/monodromia) | `v1.0.0` | `4c8130e51fb3419b854c485a0497e6df23c734fb` | **PASS (0 err)** | [GREEN](https://github.com/0thernes/monodromia/actions) | [`10.5281/zenodo.24618620`](https://doi.org/10.5281/zenodo.24618620) |
| `0TH-2026-018` | [apollonian-sandpile-markov](https://github.com/0thernes/apollonian-sandpile-markov) | `v3.0.0` | `e58a8cc7344a24a1a9654193d0df9ef5dca9bbc9` | **PASS (0 err)** | [GREEN](https://github.com/0thernes/apollonian-sandpile-markov/actions/runs/46054181302) | [`10.5281/zenodo.24618594`](https://doi.org/10.5281/zenodo.24618594) |
| `0TH-2026-025` | [clifford-radon-stabilizers](https://github.com/0thernes/clifford-radon-stabilizers) | `v1.1.0` | `fbc25fe8d50af3914e58f9fa685bf0ce638b8300` | **PASS (0 err)** | [GREEN](https://github.com/0thernes/clifford-radon-stabilizers/actions/runs/46063758501) | [`10.5281/zenodo.24618578`](https://doi.org/10.5281/zenodo.24618578) |

*(The other 16 older active Tier-I repos have RFC 3161-sealed manifests covering their legacy `formalization.yaml`; migrate them to `v0.4` on each repo's next release bump.)*

---

## 4. Google DeepMind `formal-conjectures` & Erdős Problems (Honest Audit)

- **Google DeepMind `formal-conjectures`:** ONLY **`0TH-2026-029` [`barker-hadamard-frontier`](https://github.com/0thernes/barker-hadamard-frontier)** bridges an existing upstream file (`FormalConjectures/Arxiv/2104.00502/BarkerSequence.lean`, commit `9097e2f90e66d2f6244209cb1c07f7120d17ec53`) via `lean/BarkerFrontier/FormalConjecturesBridge.lean` (proving odd-length classification, $n \equiv 2 \pmod 4$ & $14 \le n \le 35$ exclusion, order-16 Circulant Hadamard impossibility, and `H_CirculantHadamard -> UpstreamBarkerConjecture`; even $n = 4u^2 \ge 36$ remains open/conditional). Do **not** submit off-topic PRs for the other 28 repos.
- **Erdős Problems (`erdosproblems.com` / `teorth/erdosproblems`):** **0 / 29** Tier-I repos solve an open Erdős problem. Zero false submissions made.

---

## 5. Software Heritage (`SWHID`) Queue — All Remaining 5 Repos Submitted (`2026-11-28T05:06Z`)

| Repository | Save Code Now Request ID | Status |
|---|---|---|
| `0thernes/barker-hadamard-frontier` | `#2703359` | Accepted |
| `0thernes/quantum-latin-spectrum-frontier` (`v2.1.0`) | `#2703360` | Accepted (prior baseline `swh:1:snp:a13ad420...`) |
| `0thernes/cosmogonic-quantum-mechalogodrom` | `#2703361` | Accepted |
| `0thernes/black-hole-simulation-lab` | `#2703362` | Accepted |
| `0thernes/glitchling-jam` | `#2703363` | Accepted |
