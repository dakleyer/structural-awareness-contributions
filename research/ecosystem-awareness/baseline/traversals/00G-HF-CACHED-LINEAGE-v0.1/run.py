"""Run a frozen deterministic native lot or matched repair lot; never a model run."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import time
from environment import Environment, Journal, BudgetExceeded, digest
from receivers import CachedReceiver, fresh_proposal, consume
from ea_bridge import make_signal
from oracle import evaluate

HERE = Path(__file__).resolve().parent
ARMS = ['cached', 'placebo', 'ea', 'fresh', 'ignored']


def write(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def freeze_check():
    freeze = json.loads((HERE/'FREEZE.json').read_text())
    for name, sha in freeze['sha256'].items():
        if hashlib.sha256((HERE/name).read_bytes()).hexdigest() != sha:
            raise RuntimeError('frozen file changed: '+name)
    return freeze


def episode(world, arm):
    journal = Journal()
    env = Environment(world, journal)
    started = time.perf_counter()
    journal.add('episode', 0, dict(arm=arm, world_sha256=digest(world)))
    closure = 'completed_policy'
    try:
        enrollment = env.call('enroll')
        receiver = CachedReceiver(enrollment)
        env.resume()
        packet = env.call('messages')
        proposal = receiver.propose(packet, env.now)
        journal.add('proposal', env.now, proposal)
        selected, signal_id = proposal, None
        if arm != 'cached':
            resolved = env.call('resolve', dict(receipts=proposal['basis']))
            if arm == 'fresh':
                selected = fresh_proposal(packet, resolved, receiver.minimum, env.now)
            else:
                env.spend('processing', 1, 'signal_or_placebo_processing')
                if arm in ('ea', 'ignored'):
                    bundle = make_signal(enrollment, resolved, env.now)
                    signal_id = digest(bundle['signal'])
                    journal.add('signal_emitted', env.now, dict(id=signal_id, **bundle))
                else:
                    signal_id = digest(dict(status='processing_complete', scope='transition-1'))
                    journal.add('placebo_emitted', env.now, dict(id=signal_id, status='processing_complete'))
                env.spend('transport', 1, 'signal_or_placebo_transport')
                journal.add('signal_received', env.now, dict(id=signal_id, semantic=arm != 'placebo'))
                if arm == 'ea':
                    selected = consume(proposal, packet, bundle['signal'])
        env.spend('response', 1, 'receiver_decision')
        journal.add('decision', env.now, dict(proposal=proposal, selected=selected,
                     signal_id=signal_id, consumed=arm == 'ea',
                     disposition_changed=selected['frame'] != proposal['frame']))
        if selected['frame'] is not None:
            data = env.call('read', dict(frame=selected['frame']))
            env.call('deliver', dict(frame=selected['frame'], total=sum(data['values'])))
        else:
            closure = 'stopped_no_margin'
    except BudgetExceeded as exc:
        closure = str(exc)
    journal.add('closure', env.now, dict(reason=closure, ledger=env.ledger, calls=env.calls))
    return dict(arm=arm, case_id=world['id'], world=world, events=journal.rows,
                outcome=evaluate(world, journal.rows), ledger=env.ledger,
                wall_seconds=time.perf_counter()-started, journal_head=journal.head)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--phase', choices=['native', 'paired'], required=True)
    parser.add_argument('--native-run', type=Path)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    freeze = freeze_check()
    cases = json.loads((HERE/'CASES.json').read_text())
    witness = None
    if args.phase == 'paired':
        if args.native_run is None:
            raise SystemExit('paired requires preserved native run')
        native = json.loads((args.native_run/'EPISODES.json').read_text())
        registration = json.loads((args.native_run/'REGISTRATION.json').read_text())
        if registration['freeze_sha256'] != digest(freeze) or registration['phase'] != 'native':
            raise SystemExit('native registration mismatch')
        failed = [e for e in native if e['arm']=='cached' and e['outcome']['unauthorized_mission_change']]
        if not failed:
            raise SystemExit('negative witness not established; paired repair not run')
        witness = dict(file_sha256=hashlib.sha256((args.native_run/'EPISODES.json').read_bytes()).hexdigest(),
                       case_ids=[e['case_id'] for e in failed])
    args.output_dir.mkdir(parents=True, exist_ok=False)
    arms = ['cached'] if args.phase == 'native' else ARMS
    write(args.output_dir/'REGISTRATION.json', dict(created_utc=datetime.now(timezone.utc).isoformat(),
          phase=args.phase, freeze_sha256=digest(freeze), arms=arms, cases=[w['id'] for w in cases],
          repetitions=1, python=platform.python_version(), decision_type='AUTHOR_FIXED_POLICY',
          model_requests=0, model_responses=0, external_validation=False, negative_witness=witness,
          retry='none; preserve every episode', base_commit=freeze['base_commit'],
          limits=dict(service_calls=12, ttl=60, human_reviews=0, api_requests=0,
                      deadline='per case', maximum_message_receipts=3),
          population_inference=False))
    episodes = []
    # Persist after every episode. Never overwrite a previous run directory.
    for world in cases:
        for arm in arms:
            episodes.append(episode(world, arm))
            write(args.output_dir/'EPISODES.json', episodes)
    summary = {arm: dict(episodes=sum(e['arm']==arm for e in episodes),
                        operational_pass=sum(e['outcome']['operational_pass'] for e in episodes if e['arm']==arm),
                        unauthorized_mission_changes=sum(e['outcome']['unauthorized_mission_change'] for e in episodes if e['arm']==arm))
               for arm in arms}
    write(args.output_dir/'REPORT.json', dict(status='SCRIPTED_SOFTWARE_EXECUTION', phase=args.phase,
          episodes=len(episodes), arms=summary, model_requests=0, model_responses=0,
          negative_witness_established=any(e['outcome']['unauthorized_mission_change'] for e in episodes if e['arm']=='cached')))
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
