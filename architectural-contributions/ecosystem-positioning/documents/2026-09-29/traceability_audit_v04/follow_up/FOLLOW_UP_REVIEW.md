## Appendix E Publication verification and assumption review

29 September 2026. Audit update 0.4.1. This supplement preserves all preceding text and qualifies the interpretation of the P6 source-dependence test. It also adds input-admission and cost-ledger checks without altering the original published runs.

### E1 Publication and reproduction

All twenty document and evidence blobs under the dated publication directory at commit 3744ef953265727612da979878f7e97a0b7fe989 were compared with local bytes and matched their Git hashes. Both published result files, results.json and review_results.json, reproduced exactly in a separate directory. This verifies publication completeness and reproducibility for that snapshot. It does not independently validate the scientific interpretation.

### E2 Evaluator weaknesses found and addressed

The original generators produce inputs inside declared domains, but several evaluators did not reject malformed inputs if called separately. Invalid evidence could leave no compatible world and produce a vacuous support result. A truncated execution record or an execution reported at a nonaction event could escape the temporal evaluator. The time evaluator accepted charges supplied in the candidate's output, so a false zero charge could appear timely.

The added checked_evaluators.py rejects the tested malformed records. Its time score uses observation and response charges supplied separately by the test environment and checks the candidate's record against that ledger. The original generator already supplied the correct charges, so the earlier counts do not change. Trusted measurement remains an explicit assumption; an independently supplied ledger is not a real measurement merely because it is stored separately.

Eleven malformed-record controls were rejected. Rechecking 189 P1 inputs, 28,644 P2 combinations and all 335,922 P5 extended-domain words preserved the previous scores for the candidates examined. Explicit continuity assertions confirm that Q,A and Q,C,Q,A execute, while Q,C,R,A does not. These checks strengthen the evaluators' admission boundary; they do not certify arbitrary malformed inputs or hostile runtime code.

### E3 Structural ancestry is not statistical independence

The P6 DAG test establishes whether two reports share a represented root. Its variable names use “independent”, but root separation alone does not establish statistical independence, factual truth or absence of unrepresented common causes. That interpretation requires additional assumptions about the source process and completeness of the represented dependencies.

A counterexample makes this explicit. Two reports have separate represented roots, but their values are jointly (0,0) or (1,1), each with probability one half. The graph check reports root separation. Yet the joint probability of both values being one is 0.5, whereas the product of their marginal probabilities is 0.25. The source values are dependent. This counterexample is retained in follow_up_results.json. Read the earlier P6 results as structural provenance checks; a statistical or epistemic independence claim requires further evidence.

### E4 Assumptions that must accompany the results

P1 assumes accurate evidence labels and a fixed three-proposition truth model. It does not evaluate calibrated degrees of certainty, mistaken observations or an open-world ontology. P2 models known deterministic observation and response charges; queues, communication, human delays and other costs count only if explicitly charged. It establishes timing, not successful business recovery.

P3 uses eight author-specified dispositions. P4 trusts the issuer records and their action/cap meanings; authenticity and real mandate interpretation are external obligations. P5 treats each C/X as invalidating the relevant basis and each Q as successful renewed qualification. It assumes serialized events and does not test whether Q acquired adequate evidence. P6 assumes a known forward DAG and reports ancestry overlap as clarified above. The H4 impossibility witness assumes the stated incompatible required actions and absence of another timely distinguishing observation.

Separate code does not create independent semantic validation. The foundation-to-principle links still require source-led interpretation and explicit design objectives, including external authority. The earlier P1/P2/P4 implications remain consistency results. The six causal family witnesses, empirical H1–H6 comparisons and the complete HS mechanism remain separate, uncompleted validation obligations.

### E5 Reproduction of this supplement

From the evidence-package root run `python3 follow_up/run_follow_up.py`. The command writes follow_up/follow_up_results.json and fails if a declared check does not hold. The original audit commands and files remain unchanged. The strongest justified conclusion is bounded reproducible support with named assumptions, adverse results and open obligations. No claim of complete freedom from modelling error or circularity is made.
