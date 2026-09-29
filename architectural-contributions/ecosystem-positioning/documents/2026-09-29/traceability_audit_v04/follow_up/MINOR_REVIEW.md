# Minor input validation review

29 September 2026. Reviewed publication base 4af45abb310c62f687421b98040c1b9e0549221e. The traceability document remains version 0.4.1; no hypothesis, principle, interpretation or previously reported result is revised by this maintenance change.

The additional review found that Python accepts Boolean and floating-point values as equal to integer graph identifiers. The checked graph evaluator therefore admitted identifiers outside its intended typed domain. Some malformed event, evidence or edge records also raised an incidental TypeError or IndexError instead of the declared ValueError rejection.

The corrected admission checks validate container, record shape and exact scalar types before indexing, unpacking or constructing sets. Graph edges supplied as JSON-style lists or Python tuples receive the same interpretation. This affects malformed inputs only; the documented admitted-domain candidates and numerical results remain unchanged.

Twelve targeted negative controls now reject Boolean or floating-point report identifiers, a non-string event, an empty charge row, an unhashable claim element, missing evidence/output/cost/edge collections, a short edge, duplicate list-form edges and a Boolean graph node. A positive control verifies that valid list and tuple graph records agree.

The existing follow-up suite was rerun: its complete result file is byte-for-byte unchanged. That suite rechecks 189 P1 inputs, 28,644 P2 combinations and 335,922 P5 event words as well as the earlier eleven malformed-record controls. The extra twelve controls are input checks, not twelve empirical tests of the research hypotheses.

Run `python3 follow_up/run_minor_review.py` from the evidence-package root. The runner checks the new boundaries and replays the prior follow-up suite, requiring its result bytes to remain unchanged. It rejects execution with Python optimization enabled because that mode disables assertions. The child replay ignores inherited Python environment options. A deliberate optimized invocation was checked to exit with the stated error. The original research runners should likewise be used with their documented ordinary Python commands, without optimization.

The result is stored in minor_review_results.json with hashes of the corrected evaluator and preserved prior result. Earlier versions remain available in Git history. All Word documents and historical result files remain unchanged.
