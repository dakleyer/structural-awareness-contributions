"""Receipt projection to the existing frozen EA v0.1/v0.2 components."""
from copy import deepcopy
import importlib.util
from pathlib import Path
from environment import SCOPE

TEMPORAL_PATH = Path(__file__).resolve().parents[2] / 'fixtures' / '00G-HF-EA-COMPONENT-v0.2' / 'temporal.py'
spec = importlib.util.spec_from_file_location('existing_temporal', TEMPORAL_PATH)
temporal = importlib.util.module_from_spec(spec)
spec.loader.exec_module(temporal)


def snapshot(records, checks, now, deadline, transport=0):
    # Roots refer to immutable report receipts, not a promise that a live
    # service will retain the same upstream. Expiries come from the service.
    reports = [{k: deepcopy(r[k]) for k in ('id', 'kind', 'decision', 'claim', 'value',
                'qualified', 'lineage_source', 'roots', 'observed_at', 'valid_until')} for r in records]
    return dict(view=dict(decision=deepcopy(SCOPE), now=now,
                          timing=dict(transport_ticks=transport, response_ticks=3, last_useful_at=deadline),
                          checks=deepcopy(checks), reports=reports), point_observations=[])


def make_signal(enrollment, resolved, now):
    previous = snapshot(enrollment['initial_reports'], enrollment['checks'],
                        enrollment['now'], enrollment['deadline'])
    current = snapshot(resolved.get('reports', []), resolved.get('checks', enrollment['checks']),
                       now, enrollment['deadline'], transport=1)
    return dict(previous_input=previous, current_input=current,
                signal=temporal.compare(previous, current))
