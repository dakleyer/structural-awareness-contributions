"""Bounded, deterministic queue/guard/executor simulation; not an AWS adapter.

Runtime receives scenario inputs only. The evaluator imports this module, never
the reverse. Authority, source completeness and a common revision protocol are
fixture contracts; they are not discovered facts about a real organisation.
"""
from copy import deepcopy
from dataclasses import asdict, dataclass, replace


@dataclass(frozen=True)
class Intent:
    id: str = "PATCH-A"
    target: str = "db-7/shard-9"
    desired_generation: int = 216
    grant_expires: int = 5400


@dataclass(frozen=True)
class Permit:
    id: str
    intent: Intent
    revision: int
    expires: int


class World:
    def __init__(self, omit_reference_freeze=False):
        self.now = 120
        self.revision = 1
        self.values = dict(generation=217, incident=True, freeze=False,
                           diagnosis="config_regression", superseded=False,
                           freeze_b=True, metric=10)
        self.manifest_version = "v17"
        self.freshness_budget = 60
        self.omit_reference_freeze = omit_reference_freeze
        self.faults = {}
        self.events = []
        self.completed = {}
        self.permits = {}
        self.next_permit = 1
        self.reads = 0
        self.writes = 0

    def log(self, event, **details):
        self.events.append(dict(at=self.now, event=event, **deepcopy(details)))

    def advance(self, now):
        if now < self.now:
            raise ValueError("logical clock cannot go backwards")
        self.now = now

    def manifest(self):
        fields = dict(generation=(217, "config-owner"), incident=(True, "incident-owner"),
                      freeze=(False, "freeze-owner"), diagnosis=("config_regression", "diagnosis-owner"),
                      superseded=(False, "config-owner"))
        if self.omit_reference_freeze:
            fields.pop("freeze")
        if self.manifest_version == "v18":
            fields["freeze_b"] = (False, "finance-owner")
        return {k: dict(allowed=v, owner=owner, max_age=self.freshness_budget) for k, (v, owner) in fields.items()}

    def change(self, event):
        self.advance(event["at"])
        field, value = event["field"], event["value"]
        if field == "observation":
            self.faults[value] = event["fault"]
        elif field == "patch_b":
            self.values.update(generation=value, incident=False, superseded=True)
        elif field == "manifest":
            self.manifest_version = value
        elif field == "freshness_budget":
            self.freshness_budget = value
            self.manifest_version = "v19-freshness"
        else:
            self.values[field] = value
        material = field not in ("observation", "metric")
        if material and not event.get("bypass", False):
            self.revision += 1
        self.log("environment_change", change=event, revision=self.revision,
                 protocol_bypassed=bool(event.get("bypass")))


class Sources:
    """In-memory source adapter. Faults model metadata failures, not real APIs."""
    def __init__(self, world):
        self.world = world

    def read(self, source):
        w = self.world
        w.reads += 1
        is_manifest = source == "manifest"
        owner = "governance-owner" if is_manifest else {
            "generation": "config-owner", "incident": "incident-owner",
            "freeze": "freeze-owner", "diagnosis": "diagnosis-owner",
            "superseded": "config-owner", "freeze_b": "finance-owner",
        }.get(source)
        value = w.manifest() if is_manifest else w.values.get(source)
        result = dict(source=source, owner=owner, value=deepcopy(value),
                      sampled_at=w.now, revision=w.revision,
                      version=w.manifest_version if is_manifest else str(w.revision),
                      available=value is not None)
        fault = w.faults.get(source)
        if fault == "unavailable":
            result["available"] = False
        elif fault == "missing":
            result["value"] = None
        elif fault == "stale":
            result["sampled_at"] = w.now - 61
        elif fault == "near_expiry":
            result["sampled_at"] = w.now - 59
        elif fault == "six_seconds_old":
            result["sampled_at"] = w.now - 6
        elif fault == "boundary":
            result["sampled_at"] = w.now - 60
        elif fault == "future":
            result["sampled_at"] = w.now + 1
        elif fault == "wrong_owner":
            result["owner"] = "untrusted-owner"
        elif fault == "wrong_type":
            result["value"] = "false"
        w.log("source_read", observation=result)
        return result


def usable(observation, owner, now, max_age):
    return (type(observation) is dict and observation.get("available") is True
            and observation.get("value") is not None
            and observation.get("owner") == owner
            and type(observation.get("sampled_at")) is int
            and type(now) is int and type(max_age) is int and max_age > 0
            and 0 <= now - observation["sampled_at"] < max_age)


def qualified_observation(observation, source, owner, now, max_age):
    return (usable(observation, owner, now, max_age)
            and observation.get("source") == source
            and type(observation.get("revision")) is int and observation["revision"] > 0
            and type(observation.get("version")) is str and bool(observation["version"].strip()))


def valid_manifest(manifest):
    # Structural validity is not semantic completeness. A nonempty but incomplete
    # manifest still fails the shared-omission scenario, deliberately retained.
    return (type(manifest) is dict and bool(manifest) and all(
        type(name) is str and bool(name.strip())
        and type(rule) is dict and set(rule) == {"allowed", "owner", "max_age"}
        and type(rule["allowed"]) in (str, bool, int)
        and type(rule["owner"]) is str and bool(rule["owner"].strip())
        and type(rule["max_age"]) is int and rule["max_age"] > 0
        for name, rule in manifest.items()))


class Guard:
    def __init__(self, world, sources, mode):
        self.world, self.sources, self.mode = world, sources, mode

    def decide(self, intent, queued_basis, queued_manifest, omit_checked=False):
        w = self.world
        if w.now >= intent.grant_expires:
            return "DENY", "grant_expired", None
        if self.mode == "deny_all":
            return "DENY", "deny_all_control", None
        manifest_obs = self.sources.read("manifest")
        if not qualified_observation(manifest_obs, "manifest", "governance-owner", w.now, 60):
            return "HOLD", "manifest_unknown", None
        manifest = queued_manifest if self.mode == "static_manifest" else manifest_obs["value"]
        if not valid_manifest(manifest):
            return "HOLD", "manifest_invalid", None
        evidence_expiry = manifest_obs["sampled_at"] + 60
        w.log("basis_selected", version=manifest_obs["version"], used_fields=list(manifest),
              uses_queued_manifest=self.mode == "static_manifest")
        if self.mode == "coverage_only":
            checked = set(queued_basis)
            if omit_checked:
                checked.discard("freeze")
            missing = sorted(set(manifest) - checked)
            w.log("coverage_check", missing=missing)
            if missing:
                return "DENY", "missing_coverage", None
        else:
            observations = {name: self.sources.read(name) for name in manifest}
            for name, rule in manifest.items():
                obs = observations[name]
                if (not qualified_observation(obs, name, rule["owner"], w.now, rule["max_age"])
                        or type(obs["value"]) is not type(rule["allowed"])):
                    return "HOLD", "evidence_unknown:" + name, None
                # A source revision mismatch makes the multi-read snapshot unusable.
                if obs["revision"] != manifest_obs["revision"]:
                    return "HOLD", "inconsistent_snapshot", None
                evidence_expiry = min(evidence_expiry, obs["sampled_at"] + rule["max_age"])
            changed = [name for name, obs in observations.items()
                       if name not in queued_basis or obs["value"] != queued_basis[name]]
            if changed:
                w.log("reassessment", changed_fields=changed)
            prohibited = [name for name, rule in manifest.items()
                          if observations[name]["value"] != rule["allowed"]]
            if prohibited:
                return "DENY", "current_basis_prohibits:" + ",".join(prohibited), None
        permit = Permit("permit-" + str(w.next_permit), intent, manifest_obs["revision"], min(w.now + 10, evidence_expiry))
        w.next_permit += 1
        w.permits[permit.id] = permit
        w.log("permit_issued", permit=asdict(permit))
        return "EXECUTE", "current_basis_permits", permit


class Executor:
    def __init__(self, world, enforce_binding=True):
        self.world = world
        self.enforce_binding = enforce_binding

    def attempt(self, intent, permit):
        w = self.world
        w.log("execution_attempt", intent=asdict(intent))
        if intent.id in w.completed:
            if w.completed[intent.id] != intent:
                w.log("execution_rejected", reason="idempotency_payload_conflict")
                return "REJECTED"
            w.log("execution_rejected", reason="already_applied")
            return "ALREADY_APPLIED"
        reason = None
        if permit is None or w.permits.get(permit.id) != permit:
            reason = "no_registered_permit"
        elif permit.intent != intent:
            reason = "intent_binding_lost"
        elif w.now >= intent.grant_expires:
            reason = "grant_expired"
        elif w.now >= permit.expires:
            reason = "permit_expired"
        elif self.enforce_binding and permit.revision != w.revision:
            reason = "revision_binding_lost"
        if reason:
            w.log("execution_rejected", reason=reason)
            return "REJECTED"
        # Atomic only in this single-threaded model: no event between compare/apply.
        before = w.values["generation"]
        w.values["generation"] = intent.desired_generation
        w.revision += 1
        w.writes += 1
        w.completed[intent.id] = intent
        w.log("action_effect", before_generation=before,
              after_generation=w.values["generation"], simulated_reboot=True)
        return "APPLIED"


def run_case(case):
    """Returns observations/effects; has no oracle argument or expected outcomes."""
    w = World(case.get("omit_reference_freeze", False))
    sources = Sources(w)
    intent = Intent()
    mode = case["mode"]
    initial_manifest = sources.read("manifest")["value"]
    basis = {name: sources.read(name)["value"] for name in initial_manifest}
    if any(type(basis[k]) is not type(rule["allowed"]) or basis[k] != rule["allowed"]
           for k, rule in initial_manifest.items()):
        raise ValueError("fixture does not begin with a legitimate queued action")
    queue = [intent]
    w.log("queued", intent=asdict(intent), decision_basis=basis,
          manifest=initial_manifest, scheduled_at=2520)
    pending = sorted(deepcopy(case.get("events", [])), key=lambda e: e["at"])

    def advance_to(at):
        while pending and pending[0]["at"] <= at:
            w.change(pending.pop(0))
        w.advance(at)

    advance_to(2520)
    disposition, reason, permit = Guard(w, sources, mode).decide(
        intent, basis, initial_manifest, case.get("omit_checked_freeze", False))
    w.log("guard_decision", disposition=disposition, reason=reason)
    if disposition == "HOLD":
        advance_to(w.now + 5)
        disposition = "ESCALATE"
        w.log("bounded_escalation", owner="change-operations", deadline=w.now,
              external_acknowledgement=False)
    advance_to(max(w.now, case.get("act_at", 2522)))
    queued_intent = queue.pop(0)
    if case.get("substitute_intent"):
        queued_intent = replace(queued_intent, desired_generation=215)
    executor = Executor(w, enforce_binding=mode != "unbound")
    result = executor.attempt(queued_intent, permit)
    if result == "REJECTED" and disposition == "EXECUTE":
        disposition = "DENY"
    if case.get("duplicate"):
        executor.attempt(queued_intent, permit)
    w.log("queue_closed", status="APPLIED" if result == "APPLIED" else disposition)
    return dict(id=case["id"], mode=mode, disposition=disposition,
                applied=w.writes > 0, final_generation=w.values["generation"],
                effects=w.writes, final_state=deepcopy(w.values),
                control_burden=dict(source_reads=w.reads, elapsed_seconds=w.now - 2520),
                trace=w.events)
