# Node cards: explanatory documentation

This guide extends the Atlas phase-2 item and node procedure. It provides a versioned vocabulary for explaining a thought clearly while retaining its sources, identity and neighbouring facets.

## Start with the thought

An item identifies something referable: a document, dialogue, page, software artefact or located fragment. A node explains a conceptual position that can be supported by one or several such items. One item can support several nodes; several items can support one node.

Write the explanation before assigning tags. A reader should be able to identify what the thought concerns, the distinction or operation it introduces, and the conditions under which it is being described. Definitions, mechanisms, questions, hypotheses, examples and observations serve different purposes. Their source roles remain explicit.

## A clear node card

The description develops the thought in connected prose. Technical terms receive local meanings where needed. A formal expression retains its notation, reference conventions and a located source. A worked example makes the idea concrete and identifies whether it is reported by a source or constructed for explanation. Where a result requires reasoning, the premises and steps are made visible.

Not every thought needs an equation, an example or a failure analysis. Those additions are selected for what they explain. A person, a cultural practice and a mathematical definition should not be forced into the same analytical form.

| Existing vocabulary | Explanatory function |
| --- | --- |
| `node:role` | The thought's function in the argument |
| `node:mechanism` | How a described process operates |
| `node:scope` | The domain or setting of the formulation |
| `node:distinction` | A difference from neighbouring ideas |
| `node:observable` | What can be observed or measured |
| `node:condition` | A relevant assumption or prerequisite |

## Six additional entries

[The extended dictionary](TAG_DICTIONARY_v0.2.json) retains the original 28 keys and adds six explicitly proposed entries for the working vocabulary.

| Key | Type and location | What it adds |
| --- | --- | --- |
| `proposed:node-question` | String in `etiquetas` | The question this thought helps a reader answer |
| `proposed:node-formulations` | Array at `/formulations` | Expressions, notation and source locations, stored once |
| `proposed:node-example` | Object in `etiquetas` | A concrete situation, reasoning and result, with its example kind |
| `proposed:node-derivation` | Array in `etiquetas` | Ordered steps from premises to a stated result |
| `proposed:node-terminology` | Array in `etiquetas` | The local meaning of necessary terms and symbols |
| `proposed:node-failure-mode` | String in `etiquetas` | A specific breakdown of the model, application or interpretation |

These entries distinguish explanation from classification. A derivation differs from an operating mechanism. A constructed example differs from an observed result. A local term definition does not establish a theme. A failure mode is used for a particular breakdown, rather than as a generic qualification appended to every card.

The `proposed:` prefix records their extension state under the existing phase-2 procedure. Existing shared keys retain their identities and applicability. Controlled research definitions, A/B/C/D and Jumps & Falls remain unchanged.

## Example: a reference capacity

Consider a model with eight equiprobable states. Its selected information capacity is `C = log₂ 8 = 3 bits`. A clear explanation identifies the state space, the equiprobability convention, the base of the logarithm and what the result measures.

This is a constructed illustration of a definition. It does not by itself demonstrate a physical work output or an empirical result. If a second card discusses the complexity of an individual state, the overlap is the common capacity reference; the two cards answer different questions about it.

## Source correspondence and overlap

Each material claim points to its supporting item and a useful locator: a page, line range, paragraph or section, together with the observed revision or content hash. The record distinguishes a source statement, an editorial interpretation and a constructed example.

Overlapping cards retain their different questions, assumptions, units or observational positions. Sharing a term or a source does not create a relation automatically. A retained relation states what is shared and what each neighbouring thought contributes.

## Review gates

1. Read the relevant source argument, including the conditions and notation needed for the thought.
2. Check that the description is intelligible without an earlier paragraph or an unexplained table row.
3. Define the technical vocabulary that the intended reader needs.
4. Verify each formal expression and the arithmetic of any constructed example.
5. Explain the role of each supporting source and each retained overlap.
6. Apply only relevant dictionary entries with their declared types.
7. Record the source revision and the explanation review separately from structural validation.

An extracted paragraph remains an extraction record until this explanatory review is performed. Table fragments, damaged characters, instructions and context-dependent sentences are returned to their source for reconstruction. Word counts and JSON validity help locate work; they do not establish conceptual understanding.

## Incremental operation

Retain item and node identities. Enrich existing cards under their existing IDs and record the revision. Keep source passages, dates and voice attribution available. A change to a source triggers review of the explanations that depend on it. Versions of the dictionary remain resolvable so that older extraction records and newer developed cards can be read together.

This documentation layer can be presented in HTML while its JSON remains the machine-readable representation. It complements the corpus and its source navigation; it does not replace the source documents.
