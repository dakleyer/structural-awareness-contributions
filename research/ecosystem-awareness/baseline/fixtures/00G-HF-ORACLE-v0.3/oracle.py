"""C2: unchanged C1 outcome predicates plus separate, optional observations."""
import argparse
import json
from pathlib import Path
from core import evaluate as evaluate_core
from assessments import assess

if not __debug__:
    raise RuntimeError('Use Python without -O: the preserved C1 validator uses assertions.')


def evaluate(world, trace, assessment=None):
    result = evaluate_core(world, trace)
    result['scope'] = 'SINGLE_RECIPIENT_BOUNDED_EPISODE'
    result['population_result'] = 'NOT_ASSESSED'
    if assessment is None:
        result['assessment'] = {'status': 'NOT_ASSESSED'}
    elif result['record_status'] == 'INVALID':
        result['assessment'] = {'status': 'NOT_ASSESSED', 'reason': 'invalid core record'}
    else:
        result['assessment'] = assess(world, trace, assessment)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('world', type=Path)
    parser.add_argument('trace', type=Path)
    parser.add_argument('--assessment', type=Path)
    args = parser.parse_args()
    supplementary = json.loads(args.assessment.read_text()) if args.assessment else None
    print(json.dumps(evaluate(json.loads(args.world.read_text()),
                              json.loads(args.trace.read_text()), supplementary), indent=2))
