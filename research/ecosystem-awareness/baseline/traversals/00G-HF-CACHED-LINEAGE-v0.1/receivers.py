"""Declared deterministic comparator policies. No case labels or hidden world."""


def admissible_references(packet, now):
    return [r for r in packet['references'] if r['authenticated'] and r['claim'] == 'Q'
            and r['value'] is True and now < r['valid_until']]


class CachedReceiver:
    """Onboarding-qualified roots cached by stable source ID, with fixed TTL.

    This is the examined application defect: TTL is used as a proxy for current
    source/receipt binding. It is NOT the earlier effect-guarded native receiver.
    """
    def __init__(self, enrollment):
        self.catalog = enrollment['catalog']
        self.expires = enrollment['now'] + enrollment['cache_ttl']
        self.minimum = enrollment['conditional_transition']['minimum_independent_roots']

    def propose(self, packet, now):
        refs = admissible_references(packet, now)
        roots = {root for r in refs for root in self.catalog.get(r['source'], [])} if now < self.expires else set()
        frame = 'FRAME_B' if packet['proposed'] == 'FRAME_B' and len(roots) >= self.minimum else 'FRAME_A'
        return dict(frame=frame, reason='cached_source_roots', roots=sorted(roots),
                    cache_expires=self.expires, basis=[r['id'] for r in refs])


def fresh_proposal(packet, resolved, minimum, now):
    """Conventional per-decision receipt binding, no EA imports or vocabulary."""
    refs = {r['id'] for r in admissible_references(packet, now)}
    roots = {root for r in resolved.get('reports', [])
             if r['id'] in refs and r['qualified'] and r['value'] and now < r['valid_until']
             for root in r['roots']}
    return dict(frame='FRAME_B' if packet['proposed'] == 'FRAME_B' and len(roots) >= minimum else 'FRAME_A',
                reason='current_receipt_roots', roots=sorted(roots), basis=sorted(refs))


def consume(proposal, packet, signal):
    current = signal['current']
    if not current['timely']:
        return dict(frame=None, reason='signal_has_no_response_margin')
    if packet['proposed'] == 'FRAME_B' and current['basis_sufficiency'] != 'SUFFICIENT_WITHIN_VIEW':
        return dict(frame='FRAME_A', reason='transition_basis_not_sufficient',
                    evidence_status=current['evidence']['status'])
    return dict(proposal, reason='signal_preserves_proposal')
