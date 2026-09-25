"""Independent P1/P2/P3 kernels for the 00K cross-scenario package.

These functions import none of A1–A6 and are deliberately smaller than the
scenario harnesses. They test whether the same semantic invariant can be
re-expressed independently and reused in a second scenario family.
"""


def p1_evidence_supports(required_proposition: str, supported_propositions: set[str]) -> bool:
    """Evidence for one proposition does not silently support a stronger one."""
    return required_proposition in supported_propositions


def p2_bounded_resolution(resolution_stream: tuple[bool, ...], budget: int) -> str:
    """Search/review may continue only inside a finite decision budget."""
    for resolved in resolution_stream[:budget]:
        if resolved:
            return "RESOLVED"
    return "BOUNDED_NO_CONCLUSION"


def p3_three_valued_closure(determined: bool, permitted_if_determined: bool) -> str:
    """Unresolved material state is neither permission nor denial."""
    if not determined:
        return "HOLD_REQUALIFY"
    return "EXECUTE" if permitted_if_determined else "DENY"
