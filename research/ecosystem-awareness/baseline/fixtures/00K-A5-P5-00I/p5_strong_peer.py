"""Strong peer for 00K A5 that binds the full declared material basis.

The original simple generation compare is intentionally retained in
ablation_A5.py because it is useful as a partial repair. This peer is the
stronger reconstruction used by the extended material-change grid.
"""
from ablation_A5 import (
    Disposition, QueuedAction, CurrentState, p1_basis_is_well_formed,
)


def full_basis_compare_before_act(action: QueuedAction, current: CurrentState) -> Disposition:
    if not action.grant.current or not p1_basis_is_well_formed(action):
        return Disposition.DBC_DENY
    if not current.source_available:
        return Disposition.DBC_HOLD

    b = action.basis
    material_match = (
        current.generation == b.qualified_generation
        and current.incident_open == b.incident_open
        and current.freeze_active == b.freeze_active
        and current.source_version == b.source_version
    )
    return Disposition.DBC_EXECUTE if material_match else Disposition.DBC_REQUALIFY
