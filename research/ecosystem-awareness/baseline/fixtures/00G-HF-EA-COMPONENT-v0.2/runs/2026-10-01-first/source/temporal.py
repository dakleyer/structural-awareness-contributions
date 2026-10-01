"""Bounded endpoint comparison, with no world, oracle or model access."""
from copy import deepcopy
import importlib.util
from pathlib import Path

PRIOR = Path(__file__).resolve().parent.parent / '00G-HF-EA-COMPONENT-v0.1' / 'component.py'
spec = importlib.util.spec_from_file_location('ea_qualifier_v01', PRIOR)
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)


def validate(snapshot):
    core.require(isinstance(snapshot, dict) and set(snapshot) == {'view', 'point_observations'}, 'snapshot keys')
    core.validate(snapshot['view'])
    points = snapshot['point_observations']
    core.require(isinstance(points, list) and len(points) <= 3, 'point bound')
    names = set()
    for r in points:
        core.require(isinstance(r, dict) and set(r) == {'name','source','decision','observed_at','value','version','valid_until'}, 'point shape')
        core.require(core.string(r['name']) and r['name'] in core.SOURCES and r['name'] not in names, 'point name')
        names.add(r['name'])
        core.require(core.string(r['source']) and core.scope_ok(r['decision']), 'point source/scope')
        core.require(type(r['observed_at']) is int and 0 <= r['observed_at'] <= snapshot['view']['now'], 'point observation time')
        core.require(type(r['value']) is bool and r['version'] is None and r['valid_until'] is None, 'point value/no fabricated metadata')


def points(snapshot):
    return {r['name']:r for r in snapshot['point_observations']
            if r['source'] == core.SOURCES[r['name']] and r['decision'] == snapshot['view']['decision']}


def compare(previous, current):
    validate(previous)
    validate(current)
    before, after = core.assess(previous['view']), core.assess(current['view'])
    identity = core.SCOPE - {'basis_version'}
    comparable = (all(previous['view']['decision'][k] == current['view']['decision'][k] for k in identity)
                  and previous['view']['now'] < current['view']['now'])
    qualifications, metadata, point_changes = [], [], []
    if comparable:
        for name in core.SOURCES:
            a, b = before['checks'][name], after['checks'][name]
            if a['status'] != b['status']:
                qualifications.append({'dimension':name, 'before':a['status'], 'after':b['status'],
                                       'meaning':'qualification changed; underlying world change not established'})
            if a['versions'] != b['versions']:
                metadata.append({'dimension':name, 'before':a['versions'], 'after':b['versions']})
        if before['evidence']['status'] != after['evidence']['status']:
            qualifications.append({'dimension':'evidence', 'before':before['evidence']['status'],
                                   'after':after['evidence']['status'], 'meaning':'qualified support changed'})
        if before['evidence']['qualified_positive_roots'] != after['evidence']['qualified_positive_roots']:
            metadata.append({'dimension':'evidence_roots', 'before':before['evidence']['qualified_positive_roots'],
                             'after':after['evidence']['qualified_positive_roots']})
        if before['decision']['basis_version'] != after['decision']['basis_version']:
            metadata.append({'dimension':'host_basis_label', 'before':before['decision']['basis_version'],
                             'after':after['decision']['basis_version']})
        left, right = points(previous), points(current)
        for name in sorted(left.keys() & right.keys()):
            a, b = left[name], right[name]
            if a['observed_at'] < b['observed_at'] and a['value'] != b['value']:
                point_changes.append({'dimension':name, 'before':deepcopy(a), 'after':deepcopy(b),
                                      'meaning':'different observed service responses; persistence and cause unknown'})
    changed = bool(qualifications or metadata or point_changes)
    if not comparable:
        classification = 'NOT_COMPARABLE'
    elif before['basis_sufficiency'] != 'SUFFICIENT_WITHIN_VIEW' and after['basis_sufficiency'] == 'SUFFICIENT_WITHIN_VIEW':
        classification = 'QUALIFIED_RECOVERY_WITHIN_VIEW'
    elif qualifications:
        classification = 'QUALIFICATION_CHANGE'
    elif point_changes:
        classification = 'OBSERVED_POINT_CHANGE'
    elif metadata:
        classification = 'METADATA_CHANGE'
    else:
        classification = 'NO_OBSERVED_CHANGE'
    return {'profile':'EA_TEMPORAL_VIEW_v2', 'comparable':comparable, 'classification':classification,
            'change_detected':changed, 'qualification_changes':qualifications, 'metadata_changes':metadata,
            'point_changes':point_changes, 'current_point_observations':deepcopy(current['point_observations']),
            'previous':before, 'current':after, 'authority_effect':'NONE',
            'global_stability_established':False, 'empirical_prevention_established':False,
            'residual':['Endpoint comparison can miss hidden changes and transient changes between samples.',
                        'Point responses have no source-native version or forward validity guarantee.',
                        'Metadata changes alone do not establish a material semantic change.']}
