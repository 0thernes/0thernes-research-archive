# External Scholarly Portal Submission Pack & Readiness Audit

> **Generated:** `2026-11-28T04:08:35Z` · **Author:** Alexander Stephen Donahue (ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648), Independent Researcher, Spokane, WA, USA)
> **Epistemic Integrity Rule:** Zero fabricated submissions, zero bypassed logins/CLAs/depositor attestations, and zero false open-problem claims.

## 1. Portal Readiness Summary

| Portal | Status | Automated Work Completed | Required Human Action (Auth / Legal Attestation) |
|---|---|---|---|
| **Software Heritage** (`archive.softwareheritage.org`) | **LIVE ARCHIVED** | **28/29** Tier-I papers & **14/17** Tier-II builds now carry live verified ISO/IEC 18670 SWHIDs in `registry/PAPERS.json` & `registry/BUILD_PAPERS.json` | Optional: re-run Save Code Now after future releases (`0TH-2026-029`, `0TH-BUILD-005/006/015` when SWH burst limit resets) |
| **ORCID** (`0009-0006-8168-9648`) | **1-CLICK READY** | Generated verified **58-work** BibTeX file [`registry/orcid_works_import.bib`](../registry/orcid_works_import.bib) with exact titles, versions, DOIs, release URLs & SWHIDs | Sign in at <https://orcid.org/my-orcid> → **Add works** → **Add BibTeX** → upload `registry/orcid_works_import.bib` |
| **Zenodo** (`zenodo.org`) | **READY FOR TOGGLE** | Verified `.zenodo.json` metadata across active repos; **3** paper entries already carry verified DOIs (`10.5281/zenodo.24548051`, `10.5281/zenodo.24517198`) | Sign in at <https://zenodo.org/account/settings/github/>, flip target repos ON (or supply `ZENODO_TOKEN`), and attest human review per Zenodo's April 2026 depositor policy |
| **Palomar Registry** (`submit.palomar-registry.org`) | **CRITICAL SCHEMA FIX PREPARED** | Audited against official `PalomarRegistry/PalomarTemplate`; vendored official [`schema/palomar-v0.4.schema.json`](../schema/palomar-v0.4.schema.json) and built [`scripts/validate_palomar_v04.py`](../scripts/validate_palomar_v04.py). **Caught systemic Gate-3 blocker:** existing custom `formalization.yaml` files must be migrated to official `v0.4` (`version: 'v0.4'`, `project.license: 'Apache-2.0'`, `sources[]`, `automation.methods[]`, `review.status`) before submission | Migrate target repo's `formalization.yaml` until `validate_palomar_v04.py` exits `0`, push commit, then sign in with GitHub at <https://submit.palomar-registry.org> and paste the 40-char commit SHA below |
| **Google DeepMind `formal-conjectures`** | **HUMAN CLA REQUIRED** | Audited all 62,790 mirrored targets (`google-deepmind/formal-conjectures`): zero of our proved preprint sub-conjectures currently sit as open targets in `formal-conjectures`; zero unauthorized PR spam sent | Sign Google CLA at <https://cla.developers.google.com/>, open a coordination issue first, and contribute new Mathlib statements under `FormalConjectures/` |
| **Erdős Problems** (`teorth/erdosproblems`) | **NOT ELIGIBLE (0 SOLVED)** | Audited all Erdős entries (`#28`, `#30`, `#142`, Happy Ending, Erdős–Straus): **0 open Erdős problems solved by `0thernes`** (Mordell mod-840 is classical 1967) | Do **not** submit resolution claims until an open Erdős problem is genuinely settled |

## 2. Active Tier-I Paper Submission Roster (Exact 40-Char Commit SHAs & SWHIDs)

| ID | Version | Repository | Pinned 40-Char Commit SHA | SWHID | Zenodo DOI |
|---|---|---|---|---|---|
| `0TH-2026-001` | `v1.0.0` | [hoggar-bound](https://github.com/0thernes/hoggar-bound) | `c74135c429a0ef827c757df5fc76139aed62a819` | `swh:1:snp:3b6cddfca8423d21206d194e585c241f5fa14464` | Pending Zenodo toggle |
| `0TH-2026-002` | `v1.8.0` | [hoggar-bound-lab](https://github.com/0thernes/hoggar-bound-lab) | `eb2d83ef72f882b33a89d81bead66def2ab5283d` | `swh:1:snp:f8afa748054409dffbad57b721d07eb57a545757` | Pending Zenodo toggle |
| `0TH-2026-003` | `v0.1.0` | [contextuality-tensor-lab](https://github.com/0thernes/contextuality-tensor-lab) | `f7a1e6e74f8590d9cee0aa4c01f9ea3800f7fe87` | `swh:1:rev:de48ed9002e930825f1cf5f140c8dc8cbfdc1ea0` | Pending Zenodo toggle |
| `0TH-2026-004` | `v2.3.0` | [kochen-specker-extremal-lab](https://github.com/0thernes/kochen-specker-extremal-lab) | `d2ebab5ec0161504eccac1fbacca9e561ae0bc66` | `swh:1:snp:4c421f5d8b6cf9d06c224ed7bfafe88bc3392f4f` | Pending Zenodo toggle |
| `0TH-2026-005` | `v1.0.0` | [contextuality-evidence-lab](https://github.com/0thernes/contextuality-evidence-lab) | `ef0682cd24ca248c5e502731c462272a4ac93432` | `swh:1:snp:605cb0348709a4542f6992fe770a8b58a92dd476` | Pending Zenodo toggle |
| `0TH-2026-006` | `v2.7.0` | [multinomial-tv-conjecture](https://github.com/0thernes/multinomial-tv-conjecture) | `5b3d51071ddcdb8cdf3133ff0535762a9ad43989` | `swh:1:snp:7374ae324967c1eb8c5a11f16bdf58763e6db39a` | Pending Zenodo toggle |
| `0TH-2026-007` | `v1.3.0` | [human-synaptic-bouton-verification](https://github.com/0thernes/human-synapse-bouton-lab) | `06e0dcdd5fc4cb406e9fe21d260ff94b68a414d4` | `swh:1:snp:8ef70f745fae4f91f040720b28e21560c73deffc` | `10.5281/zenodo.24548051` |
| `0TH-2026-008` | `v1.3.0` | [open-hard-problems-consciousness-frontier](https://github.com/0thernes/human-synapse-bouton-lab) | `06e0dcdd5fc4cb406e9fe21d260ff94b68a414d4` | `swh:1:snp:8ef70f745fae4f91f040720b28e21560c73deffc` | `10.5281/zenodo.24548051` |
| `0TH-2026-009` | `v3.4.0` | [pauli-contextuality-lab](https://github.com/0thernes/pauli-contextuality-lab) | `05c1e4a4a7999f3d8bac5f1e756cce94e5b9e110` | `swh:1:snp:cf9ae7bd108e9556e79d4c0c81c8de92632b91c1` | Pending Zenodo toggle |
| `0TH-2026-010` | `v1.0.1` | [catalytic-register-frontiers](https://github.com/0thernes/catalytic-register-frontiers) | `4bfeabb05a960450114f975f477259ccf189cdf1` | `swh:1:snp:f960eeda6f145e54c0ac52538ace866a16e24085` | `10.5281/zenodo.24517198` |
| `0TH-2026-011` | `v2.5.0` | [secmesh-pqsi](https://github.com/0thernes/secmesh-pqsi) | `6c7f6421465c0018f2cfa385ede6f1041a62e543` | `swh:1:snp:eea7aacfbc56dfb0cc50f1602a3e4cbb54fe76f5` | Pending Zenodo toggle |
| `0TH-2026-012` | `v5.4.0` | [coded-pir-mlwe-complexity-lab](https://github.com/0thernes/coded-pir-mlwe-complexity-lab) | `84d2f721653d201a2573d4d0c43324f23c0d42da` | `swh:1:snp:badfe4328be66ecd30b2e745b31e7dd232fe3aa9` | Pending Zenodo toggle |
| `0TH-2026-013` | `v1.2.0` | [p-vs-np-frontier-lab](https://github.com/0thernes/p-vs-np-frontier-lab) | `a70733fc388c24e3789eef9fb7afc8464f1669fe` | `swh:1:snp:bd0c8799846460f2c8d552e8a2f1317d37cd43e5` | Pending Zenodo toggle |
| `0TH-2026-014` | `v1.0.0` | [monodromia](https://github.com/0thernes/monodromia) | `153792bdaee2b01f9a56afbcb60af7d2957d5669` | `swh:1:snp:c2071e6233ff31c36dab1392682036763a15c851` | Pending Zenodo toggle |
| `0TH-2026-015` | `v1.0.0` | [promislow-fracton-amoeba](https://github.com/0thernes/promislow-fracton-amoeba) | `c829ab811568a13e2283db2175f684e35b17c816` | `swh:1:snp:3de955e528951f543794d11b7c4ec43d5869e611` | Pending Zenodo toggle |
| `0TH-2026-016` | `v1.0.0` | [zero-error-torus-frontier](https://github.com/0thernes/zero-error-torus-frontier) | `af343aaa1701637e23733ac0abd7a8f9b2e22b60` | `swh:1:snp:6794c5e91c92e22925244c886095bc5d12d9fb63` | Pending Zenodo toggle |
| `0TH-2026-017` | `v1.3.0` | [octonionica](https://github.com/0thernes/octonionica) | `b485fd9f67451ce8e7abfd95be85199782684955` | `swh:1:snp:9ff0d3d02f71abe1108d23cc5ea17caf43a517af` | Pending Zenodo toggle |
| `0TH-2026-018` | `v3.0.0` | [apollonian-sandpile-markov](https://github.com/0thernes/apollonian-sandpile-markov) | `bc6464b19737aed6255993a966fbeb0110aa099e` | `swh:1:snp:392d116f12dbe6820df783848373d27bbf138c55` | Pending Zenodo toggle |
| `0TH-2026-019` | `v2.1.0` | [cayley-dickson-terrace-frontier](https://github.com/0thernes/cayley-dickson-terrace-frontier) | `0ea58439e9f98b4f44f13fa484c5ee4b50badb10` | `swh:1:snp:a8698046c6b39a1531cfb5a74c6fa17c36a5d981` | Pending Zenodo toggle |
| `0TH-2026-020` | `v2.0.0` | [quantum-phasespace-rigidity](https://github.com/0thernes/quantum-phasespace-rigidity) | `a99f327698a46ecc249f5cc1a98a387969d80d24` | `swh:1:snp:91466bc3ff5dad44fef051db37afc2dcb91aa57b` | Pending Zenodo toggle |
| `0TH-2026-021` | `v2.0.0` | [weyl-magic-stabilizer-frontier](https://github.com/0thernes/weyl-magic-stabilizer-frontier) | `ab70ad2e7c5c4c037e794b1e6944c12c98ff237d` | `swh:1:snp:f5d459ee8888a15fc0310532d3c6ba402835c939` | Pending Zenodo toggle |
| `0TH-2026-022` | `v1.1.1` | [weyl-magic-obstruction-frontier](https://github.com/0thernes/weyl-magic-obstruction-frontier) | `fbfd12365dfa963421a69f530cf0c97bc866663b` | `swh:1:snp:8c1d97bd8c7f23b45d70d4a5750690b9f74e7b97` | Pending Zenodo toggle |
| `0TH-2026-023` | `v2.0.0` | [quantum-latin-spectrum-frontier](https://github.com/0thernes/quantum-latin-spectrum-frontier) | `728c1536f96c1f4a8404b71abd89a6778602f297` | `swh:1:snp:a13ad420f794605f15f7eb1f1c81cb82a38ca0c2` | Pending Zenodo toggle |
| `0TH-2026-024` | `v1.1.0` | [spectral-eclipse-frontier](https://github.com/0thernes/spectral-eclipse-frontier) | `780519d24c05d8e0c4170fa45508d9e7cb62367f` | `swh:1:snp:37fd5b55ad30a2e1cedc2949415bfacf4d5d1efc` | Pending Zenodo toggle |
| `0TH-2026-025` | `v1.1.0` | [clifford-radon-stabilizers](https://github.com/0thernes/clifford-radon-stabilizers) | `6fde4054f2445da9c3f81c9d82930c9834470b5c` | `swh:1:snp:d8ed231796b86384a1b8ff11c1fcf1d38cd93db2` | Pending Zenodo toggle |
| `0TH-2026-026` | `v1.1.0` | [schur-clifford-frontier](https://github.com/0thernes/schur-clifford-frontier) | `09ea389f20d95d2424524715d9d856517435fd26` | `swh:1:snp:4d16f7077d1ecbc298e024cc6304c83b72d9d422` | Pending Zenodo toggle |
| `0TH-2026-027` | `v1.1.0` | [nonlocal-magic-spectral-frontier](https://github.com/0thernes/nonlocal-magic-spectral-frontier) | `9bf524a31abc4f42c27b96198c3618157ffc3bfc` | `swh:1:snp:de43e715a87ea52ef52400c827cab59313d5a1f9` | Pending Zenodo toggle |
| `0TH-2026-028` | `v1.0.0` | [quantum-latin-design-frontier](https://github.com/0thernes/quantum-latin-design-frontier) | `c0ba7735c09a2d45aaa3c2dd295a6d294e43159d` | `swh:1:snp:f247003902278120c8ab10cfdf96b63a541478f5` | Pending Zenodo toggle |
| `0TH-2026-029` | `v1.0.0` | [barker-hadamard-frontier](https://github.com/0thernes/barker-hadamard-frontier) | `4d527bdf40574f9a823d0c34d941b2728aa22dc3` | Queued / pending | Pending Zenodo toggle |

## 3. Tier-II Formal Build Roster (SWHID & Zenodo Status)

| ID | Version | Repository | Pinned 40-Char Commit SHA | SWHID |
|---|---|---|---|---|
| `0TH-BUILD-001` | `v1.6.0` | [cellulogonic-mecha](https://github.com/0thernes/cellulogonic-mecha) | `d033ab025ede1118b8b1d3c9a9f9d876d97f3542` | `swh:1:snp:e4817d1409a55e725424476b0f6abc43df1730ee` |
| `0TH-BUILD-002` | `v2.4.0` | [planaria](https://github.com/0thernes/planaria) | `6979cc1be4eaaf8d6af30387fe1ace3ec7586d00` | `swh:1:snp:eee13b691a8f094598ce42304e7f16fc0bd5ae07` |
| `0TH-BUILD-003` | `v1.8.1` | [ultrametrica](https://github.com/0thernes/ultrametrica) | `d538a4e32e6c99ca55ba1c1838b49cbdf1b810a4` | `swh:1:snp:6a9e09a321d145ae3fd35d429efc869bcbff493f` |
| `0TH-BUILD-004` | `v0.5.0` | [unsolved-mathematics](https://github.com/0thernes/unsolved-mathematics) | `0604df5c70c850df44f3fdd20519e46c82925224` | `swh:1:snp:c11ec8263dd64b986c52bb400b8c3a85a3e6a254` |
| `0TH-BUILD-005` | `v0.23.0+63` | [cosmogonic-quantum-mechalogodrom](https://github.com/0thernes/cosmogonic-quantum-mechalogodrom) | `b0dcf153b93af839a8f7406795dd2e0e45777df4` | Pending SWH queue |
| `0TH-BUILD-006` | `main+research-branch` | [black-hole-simulation-lab](https://github.com/0thernes/black-hole-simulation-lab) | `050455db866d32eb115d0cd1a39f9b90a76fdd6f` | Pending SWH queue |
| `0TH-BUILD-007` | `v2.11.0` | [unsolved-problems-mega-atlas](https://github.com/0thernes/unsolved-problems-mega-atlas) | `e488704150ad2b11afecc0bc2657d86678571072` | `swh:1:snp:3cfb2f088ea1553b388f7fab01b7bf2859668903` |
| `0TH-BUILD-008` | `v5.3.0` | [cellular-engine-omega](https://github.com/0thernes/cellular-engine-omega) | `4b257af5f2659ab29a29dc026a17d1c92d011ace` | `swh:1:snp:b1734acc036650d5a32194f3437e93ca83a891b8` |
| `0TH-BUILD-009` | `v1.4.0` | [autophage](https://github.com/0thernes/autophage) | `1956c2cc54845ebadc54b2a5276cbc66bf031a8b` | `swh:1:snp:6ea23803655df1f9679deb98d44efbf53321a393` |
| `0TH-BUILD-010` | `v2.1.0` | [noetic-organism-omega](https://github.com/0thernes/noetic-organism-omega) | `c4301d926fa12334f8f8f54b2994dfc12ff649b8` | `swh:1:snp:b6ab6984080956100c967e802c6fb44e0da7ff52` |
| `0TH-BUILD-011` | `v1.1.0` | [asmodensius-native](https://github.com/0thernes/asmodensius-native) | `67bedd4abb9d03c7b94e70c8bf46f5b5f6893e6d` | `swh:1:snp:08a957772115194b51a4eadb77331b8bab261773` |
| `0TH-BUILD-012` | `v3.1.0` | [xiaomi-17t-pro-lab](https://github.com/0thernes/xiaomi-17t-pro-lab) | `f1da68b78e749a194b993bc8ad20f54016f610a0` | `swh:1:snp:06ad26ff598cf7d592768bdef08d9de7616cd4e0` |
| `0TH-BUILD-013` | `v3.4.0` | [alife-singularity-omega-package](https://github.com/0thernes/alife-singularity-omega-package) | `a08294c97f0e0e40cb1eff0dfee1b27dfe9ca5f2` | `swh:1:snp:e275a272a8b937aaecde04e2984abeaa609b2a82` |
| `0TH-BUILD-014` | `v6.7.0` | [omega-triscale-observatory](https://github.com/0thernes/omega-triscale-observatory) | `bbe4da96c5d2c6d24078bf6f88e77126de324b1d` | `swh:1:snp:045edd61e0805b3778e40f5230062e8cc245bb60` |
| `0TH-BUILD-015` | `v2.3.0` | [glitchling-jam](https://github.com/0thernes/glitchling-jam) | `92799daae8682a2df30702077bdee4ac0e17c5cf` | Pending SWH queue |
| `0TH-BUILD-016` | `v3.0.0` | [ALife-Framework](https://github.com/0thernes/ALife-Framework) | `48a2a0aa2baeea1e430c2134a7b963a7cf67727b` | `swh:1:snp:b641740a773cbd94992f7a25a150680e741c1e8f` |
| `0TH-BUILD-017` | `v1.0.0` | [beast-civilization](https://github.com/0thernes/beast-civilization) | `ccb67a8f606457db79dddafe43953227ceff2c6c` | `swh:1:snp:ebc7145f621be051e808c8adc34f17c20c830faf` |
