# 00M and 00N publication and preservation record

Publication package prepared against public main commit `9f22a4455e8a2806a35efcdb20770b5c81afca23`. This is a documentation publication and fidelity check, not a new scientific or runtime validation.

## Scope

Current reading route: **00M v0.8**, then **00N v0.7**, with three visual reading aids. The optional research-neighbour addendum is also published. Its original companion versions, 00M v0.6 and 00N v0.5, are retained solely to preserve its historical links. No local intermediate revision replaces the current reading route.

The original note and figure bytes are unchanged. Research-note status remains a proposal for review. Publishing the proposed common semantics does not silently amend the frozen requirements or older controlled corpus. The current linked requirements remain authoritative for their own freeze.

## Preservation method

- Start from the full existing remote tree, not the older local branch.
- Add the selected notes and graphics as new paths.
- Insert one navigation section into each of the three existing READMEs; removing that exact insertion reproduces the prior README byte for byte.
- Do not delete, rename or rewrite any other existing path.
- Resolve relative links in the added package against the existing tree plus the new paths.
- Parse the SVGs and inspect all three PNGs; retain full text as their interpretation authority.
- Before publishing, compare the proposed Git tree against the base: only the three named READMEs may change; all other existing blob identifiers must remain identical. Use a non-forced, fast-forward main update so concurrent public changes cannot be overwritten.
- After publication, read the published tree and verify the payload blob identifiers and README content again.

## Existing READMEs preserved

- `README.md` — previous blob `55776ebde0be5ddeed09e1ef8f94573641a533e8`.
- `research/ecosystem-awareness/README.md` — previous blob `ebb217cf2d245fd0dbe372391b2fd2c7d4d8de93`.
- `research/ecosystem-awareness/baseline/README.md` — previous blob `bccd29910ebf6c257eff01d9fa21a564edf29f3a`.

## Unchanged authored payloads

| Path relative to baseline | SHA-256 of local source and published payload |
|---|---|
| `00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md` | `37ac24628214a711caf083d7dc7bf0714ced8e7109259f00c5bd5e0bdd772377` |
| `00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md` | `f1e20b38d6dcf656d47024a0e8d9e5e51dc5a566f962818ef49ef83a11a414b9` |
| `00N_RESEARCH_NEIGHBOURS_AND_EXPERIMENTAL_PRECEDENTS_v0.1_ADDENDUM.md` | `344fdc9df4a92e9a20c57eeedd0900fbe775dbc2400ed0e4be734456e1d0c26b` |
| `00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.6_RESEARCH_NOTE.md` | `4dc4967b7f8fbd98f10d0250a46172611c78a9390a8bd72a547ee744dba8a10c` |
| `00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.5_RESEARCH_NOTE.md` | `bc4ebdba01bc1cd2a52d2844b698574e0c584dc2a6561dc33982bcdc4f29a439` |
| `visuals/EA_ABCD_v0.1.svg` | `3bd92827df8034b35f8695a4b7790fc082124604eb8ed208b79b65b4a1186c63` |
| `visuals/EA_MECHANISMS_v0.1.svg` | `8aa9e40d2afcb6a4db43de03b13ccb708ca64c49a2b757d92833a18d9b38a230` |
| `visuals/EA_REQUIREMENTS_v0.1.svg` | `a9f9475a9297781c8570e17ccc8a542fd3f454f015e1d203acf60253f902a365` |
| `visuals/EA_VISUAL_READING_AIDS_v0.1.html` | `17925ed8459b71f24e0b7332903d8bb0ab4be659348fd003c026ea715e9dab99` |
| `visuals/EA_ABCD_v0.1.png` | `af0959ef5d994a0b6fc6a459382f75eac193a9f6360eabd5e74627b9a8518242` |
| `visuals/EA_MECHANISMS_v0.1.png` | `ed8801f2b76cc0d810597b27fa82bc30bd2d6ef07b4bf298cce6001caabecf67` |
| `visuals/EA_REQUIREMENTS_v0.1.png` | `f6bbfb091076f781dc79db872238502c78eb280590111b5a9ea9e267b76670c3` |

The Tegrity entry article and its annexes are a separate update-planning task; this publication does not edit the website or reclassify its evidence claims. Any later edits should preserve the original published snapshots and explicitly identify successor semantics.
