"""Independent cross-scenario reimplementation of three 00K semantic kernels.

This module intentionally imports none of the six per-principle harnesses.
It tests whether the same small semantic invariant can be expressed in a
separate implementation and reused across materially different scenarios.
"""


def p4_non_amplifying_lineage(root_permissions: frozenset[str], requested_effect: str) -> bool:
    """A downstream/leaf effect is admissible only if it is within the
    authority/qualification carried from the root."""
    return requested_effect in root_permissions


def p5_material_basis_current(
    qualified: dict[str, object],
    current: dict[str, object],
    material_keys: tuple[str, ...],
) -> bool:
    """A prior determination remains usable only while every declared
    material basis field is current."""
    return bool(material_keys) and all(
        k in qualified and k in current
        and qualified[k] is not None and current[k] is not None
        and type(qualified[k]) is type(current[k])
        and qualified[k] == current[k] for k in material_keys)


def p6_independent_support(source_lineages: list[str], required: int) -> bool:
    """Participant/message count is not source independence."""
    return len(set(source_lineages)) >= required
