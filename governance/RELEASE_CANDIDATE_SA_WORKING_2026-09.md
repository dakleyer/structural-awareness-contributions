# Release Candidate — Structural Awareness Programme — September 2026

> **Preparation only — no GitHub Release or Zenodo DOI is claimed by this file.**

**Proposed tag:** `sa-working-2026-09`  
**Proposed title:** *Structural Awareness Programme — public working corpus, September 2026*  
**Publication approval:** explicitly approved by Iván Abril Palma on 23 September 2026 as part of Priority C execution.  
**Current execution boundary:** the available GitHub connector can update repository content but does not expose a GitHub Release creation action, and no Zenodo/DOI connector is available. Therefore no release, DOI or DOI metadata has been fabricated.

## Release boundary

This is a **public working corpus**, not:

- a completed comparative validation;
- proof of superiority over strong peer architectures;
- an adopted standard or ITU-T deliverable;
- institutional endorsement by a standards body, university or funding authority;
- a completed joint pilot.

The current canonical EA benchmark defines the B0–B3 comparison and EA-H1–EA-H4 falsification route. Comparative execution and independent validation remain pending.

## Proposed release notes

**Structural Awareness Programme — public working corpus, September 2026**

This release candidate freezes a citable working snapshot of the public Structural Awareness corpus, including the current Ecosystem Positioning architecture, Ecosystem Awareness, Regime Awareness and Minimum Sufficient Control routes, together with their current provenance, claim boundaries, benchmark design and preserved historical sources.

Key boundaries:

- working proposal / pre-standardization material;
- comparative execution pending;
- independent validation pending;
- no standards-body adoption or endorsement claimed;
- field cases establish engineering provenance only within their stated contexts;
- current and historical/frozen materials retain distinct citation and ownership rules.

The repository-level licence is CC BY-SA 4.0 subject to the scope limits in `LICENSE.md`.

## Required execution sequence when release tooling is available

1. Re-check `main`, `CLAIM_BOUNDARIES.md`, `LICENSE.md`, `CITATION.cff` and the current benchmark status immediately before release.
2. Create GitHub tag/release `sa-working-2026-09` from the approved commit.
3. Ensure the repository is connected to Zenodo **before publishing the release** if automatic archival/DOI minting is desired.
4. Publish the GitHub Release with the boundary text above.
5. Record the actual GitHub release URL and immutable release commit.
6. Record the Zenodo **version DOI** and **concept DOI** returned by Zenodo.
7. Only then update `CITATION.cff`, for example:

```yaml
version: "sa-working-2026-09"
date-released: <actual release date>
doi: <actual Zenodo concept DOI>
identifiers:
  - type: doi
    value: <actual Zenodo version DOI>
    description: Archived snapshot of this release
```

8. Add the DOI badge to the root README only after the DOI resolves.
9. Commit the citation/DOI update separately so the pre-release corpus and publication metadata remain distinguishable.

## Current files intentionally unchanged

- `CITATION.cff` remains `version: "0.1-working"` with its existing date until a real release is created.
- The root README has licence, status, validation and citation badges, but **no DOI badge**.
- No Zenodo identifier is reserved, guessed or represented as existing.

## Conservation rule

Creating the release must not remove, compact or rewrite the working corpus. The tagged release is a snapshot of the approved Git state. Historical public formulations preserved under `governance/preserved-public-snapshots/` remain part of the repository record but are not promoted back into current semantics.
