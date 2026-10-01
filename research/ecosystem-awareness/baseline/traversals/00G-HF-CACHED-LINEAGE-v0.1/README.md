# 00G-HF — cached-lineage software witness v0.1

**Executed software witness:** cached reference fails all three primary F branches; existing EA integration repairs them and preserves all three legitimate G branches. Conventional fresh revalidation also repairs them and costs less. These are author-programmed decisions, not model decisions or a product failure. See [results and limits](./RESULTS.md), [protocol](./PROTOCOL.md), [cases](./CASES.json), [predictions](./EXPECTED.json) and [design freeze](./FREEZE.json).

This is a new application profile: source-to-root bindings are cached at enrollment while source dependencies can change. All arms have equal access to current receipt provenance. The comparison includes cached reference, matched placebo, cached reference plus existing EA component, conventional fresh revalidation and deliberately ignored EA signal.

Native-first lot: 10 episodes, 21/21 verification checks. Matched lot: 50 episodes, 120/120 verification checks. Across ten cases: cached 6/10 tasks, EA 8/10, fresh revalidation 9/10. EA loses a legitimate transition under missing provenance and a short-deadline task. Predicted failures remain failures. Native replay is not independent evidence.

Full raw journals are published as lossless `EPISODES.json.gz` archives, with original and archive hashes in [EVIDENCE_MANIFEST.json](./EVIDENCE_MANIFEST.json). Decompress to inspect the original JSON. Follow the protocol commands with fresh output directories to reproduce; preserve the published verification records. [CASE_SUMMARY.json](./CASE_SUMMARY.json) provides a directly readable view.

Earlier effect-guarded native results and EA components remain unchanged. External model execution remains blocked by missing configured access; this package is not substituted for empirical E1/E3.
