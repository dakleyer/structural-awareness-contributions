"""Selected primitive accounting. Parameters/tokens/keys are never logged."""
import collections, contextlib, contextvars, hashlib, json, sqlite3, time

ACTIVE = contextvars.ContextVar('dds_cost_ledger', default=None)
ROLE = contextvars.ContextVar('dds_cost_role', default='fixture')
REAL_CONNECT = sqlite3.connect

class Ledger:
    def __init__(self):
        self.events = []
        self.started = time.perf_counter_ns()
        self.candidate_seal = None
        self.role_wall_ns = collections.Counter()
    def add(self, operation, units=1):
        assert units >= 0
        assert self.candidate_seal is None or ROLE.get() != 'candidate', 'Candidate trace already sealed'
        self.events.append({'seq': len(self.events)+1, 'role': ROLE.get(),
                            'operation': operation, 'units': units})
    @contextlib.contextmanager
    def role(self, role):
        if role == 'evaluator' and self.candidate_seal is None:
            self.candidate_seal = hashlib.sha256(json.dumps([e for e in self.events if e['role']=='candidate'],
                sort_keys=True,separators=(',',':')).encode()).hexdigest()
        began = time.perf_counter_ns()
        a, b = ACTIVE.set(self), ROLE.set(role)
        try:
            yield
        finally:
            self.role_wall_ns[role] += time.perf_counter_ns()-began
            ROLE.reset(b); ACTIVE.reset(a)
    def result(self):
        roles = collections.defaultdict(collections.Counter)
        for event in self.events:
            roles[event['role']][event['operation']] += event['units']
        actor = dict(roles['candidate'])
        return {'C_selected_api_units': sum(actor.values()), 'candidate_components': actor,
                'other_roles': {k: dict(v) for k,v in roles.items() if k != 'candidate'},
                'elapsed_instrumented_wall_ns': time.perf_counter_ns()-self.started,
                'events': self.events, 'money_cost': None,
                'candidate_trace_sha256_before_adjudication': self.candidate_seal,
                'role_inclusive_wall_ns': dict(self.role_wall_ns),
                'nested_role_durations_are_not_additive': True,
                'unscored': ['tokens', 'real human service', 'network', 'lifecycle', 'money pricing'],
                'duration_is_not_in_the_unit_sum': True}

def charge(operation, units=1):
    meter = ACTIVE.get()
    if meter is not None:
        meter.add(operation, units)

class Connection(sqlite3.Connection):
    def execute(self, sql, parameters=()):
        verb = sql.strip().split()[0].upper()
        charge('sqlite.'+verb)
        return super().execute(sql, parameters)
    def executemany(self, sql, parameters):
        rows = list(parameters)
        charge('sqlite.executemany_rows', len(rows))
        return super().executemany(sql, rows)
    def executescript(self, sql):
        # One native API invocation, not a guessed count of internal engine statements.
        charge('sqlite.executescript')
        return super().executescript(sql)
    def commit(self):
        charge('sqlite.commit')
        return super().commit()
    def rollback(self):
        charge('sqlite.rollback')
        return super().rollback()
    def close(self):
        charge('sqlite.close')
        return super().close()

def connect(*args, **kwargs):
    charge('sqlite.connect')
    kwargs['factory'] = Connection
    return REAL_CONNECT(*args, **kwargs)

class Counter(dict):
    """Source counters increment immediately before actual selected native attempts."""
    def __setitem__(self, key, value):
        previous = self.get(key, 0)
        if value > previous and key == 'file_hash_reads':
            charge('file.hash_read', value-previous)
        super().__setitem__(key, value)

class PublicKey:
    """Count an actual native verify invocation, after argument decoding succeeds."""
    def __init__(self, key):
        self.key = key
    def verify(self, *args, **kwargs):
        charge('crypto.verify')
        return self.key.verify(*args, **kwargs)

def instrument_crypto(module):
    original = module.parse
    def parse(value):
        charge('json.parse')
        return original(value)
    module.parse = parse

