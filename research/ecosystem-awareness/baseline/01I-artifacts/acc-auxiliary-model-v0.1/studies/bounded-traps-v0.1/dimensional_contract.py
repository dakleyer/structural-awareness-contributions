"""Open non-fungible dimensional comparison for ACC source-owned experiments.

A dimension is a separately identified, measured decision criterion, NOT every
coefficient of a utility equation. No fixed list of dimensions, no universal
score, no automatic conversion between R, C, E, V, or any later d_(n+1).

Uses only exact rational, within-dimension measurements and componentwise
partial ordering. Unknown relevant dimensions remain unknown. Nothing here
assigns rights, consent, utility across people, or empirical measurements.
"""
from __future__ import annotations

from fractions import Fraction
from typing import Any, Mapping


def _fraction(x:Any)->Fraction:
    if isinstance(x,bool) or x is None or isinstance(x,float):
        raise ValueError("finite explicit rational measurement required")
    try:
        a=Fraction(x)
    except (ValueError,TypeError,ZeroDivisionError) as exc:
        raise ValueError("invalid dimensional measure") from exc
    if abs(a)>10**12 or a.denominator>10**9:
        raise ValueError("unbounded dimensional measurement")
    return a


def compare_dimensions(
    before:Mapping[str,Any],after:Mapping[str,Any],
    *, declared_directions:Mapping[str,str],
    explicitly_unknown:tuple[str,...]=(),
)->dict:
    """Finite partial order in an OPEN set K; never compensate one axis.

    Each dimension has its own nested named components and unit. For actor
    payoff dimension R, components can be participants, without aggregating
    them. For C, components may separately represent actor coordination
    burdens. Extensible dimensions require explicit comparable measurements.
    """
    if not isinstance(before,dict) or not before or set(before)!=set(after):
        raise ValueError("both states must have exactly the same known dimensions")
    if set(before)!=set(declared_directions):
        raise ValueError("every measured dimension requires a declared direction")
    if not isinstance(explicitly_unknown,tuple) or set(explicitly_unknown)&set(before):
        raise ValueError("unknown dimension cannot be silently treated as zero")
    detail={};better=[];worse=[];unchanged=[]
    for dim in before:
        direction=declared_directions[dim]
        if direction not in ("INCREASE","DECREASE"):
            raise ValueError("comparison direction must be explicit")
        old=before[dim];new=after[dim]
        if (not isinstance(old,dict) or not isinstance(new,dict) or
            set(old)!={"unit","components"} or set(new)!={"unit","components"}):
            raise ValueError("dimension requires unit and actor/measure components")
        if (old["unit"]!=new["unit"] or not isinstance(old["unit"],str) or not old["unit"]):
            raise ValueError("within-dimension unit mismatch")
        a=old["components"];z=new["components"]
        if not isinstance(a,dict) or not a or not isinstance(z,dict) or set(a)!=set(z):
            raise ValueError("dimension comparison requires same referenced components")
        changes={k:_fraction(z[k])-_fraction(a[k]) for k in a}
        good=any((v>0 if direction=="INCREASE" else v<0) for v in changes.values())
        bad=any((v<0 if direction=="INCREASE" else v>0) for v in changes.values())
        if good and bad:
            status="INTERNALLY_NONCOMPARABLE"
        elif good:
            status="IMPROVES"
        elif bad:
            status="WORSENS"
        else:
            status="UNCHANGED"
        detail[dim]={
            "declared_unit":old["unit"],"direction":direction,
            "component_changes":{k:str(v) for k,v in changes.items()},
            "status":status,"no_cross_dimension_netting":True
        }
        if good:better.append(dim)
        if bad:worse.append(dim)
        if not good and not bad:unchanged.append(dim)
    if better and worse:
        relation="INCOMPARABLE_K_TRADEOFF"
    elif worse:
        relation="NO_MONOTONE_IMPROVEMENT_IN_K"
    elif better:
        relation="MONOTONE_IMPROVEMENT_IN_K"
    else:
        relation="EQUIVALENT_IN_K"
    # Even the best result is *only* relative to the dimensions actually
    # characterized. We cannot infer absent E/V or any future dimensions.
    return {
        "known_dimension_ids":list(before),
        "other_dimensions_uncharacterized":list(explicitly_unknown),
        "per_dimension":detail,
        "known_K_partial_order":relation,
        "full_open_model_dominance":"NOT_ESTABLISHED",
        "accepted_tradeoff_or_compensation":"NOT_INFERRED",
        "authority_or_consent":"OUTSIDE_DIMENSIONAL_COMPARISON",
        "no_global_scalarization":True,
    }
