"""Technology-neutral bounded tool broker for R01.

The broker exposes only manifest-declared participant responses. Private effect
and adjudication data are retained for the later oracle/evaluator.

A profile may enable the bounded R01 decision-state guard. When enabled, the
broker enforces the minimal causal order used by the current interactive
instrumentation profile: observation -> review -> commitment -> execution.
Profiles that deliberately disable this guard are behavioural/instrumentation
variants and must declare that fact explicitly.
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Mapping


class ToolBrokerError(ValueError):
    pass


class R01ToolBroker:
    def __init__(self, profile: Mapping[str, Any]):
        self.profile = deepcopy(dict(profile))
        self.budget = int(profile["physical_budget_R"])
        self.deadline = int(profile["deadline_T"])
        self.cost = 0
        self.clock = 0
        self.request_counter = 0
        self.terminated = False
        sm = profile.get("state_machine", {})
        self.state_machine_enabled = bool(sm.get("enabled", True))
        self.require_mandate_before_commit = bool(
            sm.get("require_mandate_before_commit", False)
        )
        self.target_state: dict[str, set[str]] = {}
        self.global_state: set[str] = set()
        self.public_trace: list[dict[str, Any]] = []
        self._private_trace: list[dict[str, Any]] = []

    def _catalog_entry(self, operation: str, target_id: str | None):
        catalog_name = self.profile["operations"][operation].get("catalog")
        if catalog_name is None:
            return {}
        if target_id is None:
            raise ToolBrokerError(f"{operation} requires target_id")
        catalog = self.profile.get("catalogs", {}).get(catalog_name, {})
        if target_id not in catalog:
            raise ToolBrokerError(f"unknown {catalog_name} target: {target_id}")
        return catalog[target_id]

    def _target_has(self, target_id: str | None, state: str) -> bool:
        return target_id is not None and state in self.target_state.get(target_id, set())

    def _set_target(self, target_id: str, state: str) -> None:
        self.target_state.setdefault(target_id, set()).add(state)

    def _charged_rejection(
        self,
        *,
        operation: str,
        request: Mapping[str, Any],
        status: str,
        reason: str,
        charge: int,
        duration: int,
        before_cost: int,
        before_clock: int,
    ) -> dict[str, Any]:
        self.cost += charge
        self.clock += duration
        event = {
            "request_index": self.request_counter,
            "operation": operation,
            "request": deepcopy(dict(request)),
            "status": status,
            "reason": reason,
            "charge": charge,
            "duration": duration,
            "cost_before": before_cost,
            "cost_after": self.cost,
            "clock_before": before_clock,
            "clock_after": self.clock,
        }
        self.public_trace.append(deepcopy(event))
        self._private_trace.append(deepcopy(event))
        return {
            "status": status,
            "operation": operation,
            "reason": reason,
            "remaining_budget": self.budget - self.cost,
            "remaining_time": self.deadline - self.clock,
        }

    def _state_rejection_reason(
        self,
        operation: str,
        request: Mapping[str, Any],
        response: Mapping[str, Any],
    ) -> str | None:
        if not self.state_machine_enabled:
            return None

        if operation == "inspect_relation":
            scope = response.get("scope")
            if not isinstance(scope, str) or not self._target_has(scope, "OBSERVED"):
                return "relation review requires an observed candidate"

        if operation == "decide":
            target_id = request.get("target_id")
            decision = request.get("decision")
            if decision == "COMMIT":
                if self._target_has(target_id, "EXECUTED"):
                    return "executed target requires an explicit new cycle before recommitment"
                if self._target_has(target_id, "COMMITTED"):
                    return "target already has an active commitment"
                if self._target_has(target_id, "REVIEW_REJECTED") or self._target_has(target_id, "REJECTED"):
                    return "commit cannot override a current rejection"
                if not self._target_has(target_id, "REVIEW_CLEAR"):
                    return "commit requires completed review without detected incompatibility"
                if self.require_mandate_before_commit and "MANDATE_SEEN" not in self.global_state:
                    return "commit requires the declared mandate check"
            elif decision == "REJECT":
                if not (
                    self._target_has(target_id, "REVIEW_REJECTED")
                    or self._target_has(target_id, "REVIEW_CLEAR")
                ):
                    return "rejection requires a completed review"
            else:
                return "unsupported decision value"

        if operation == "execute":
            target_id = request.get("target_id")
            if self._target_has(target_id, "EXECUTED"):
                return "target has already been executed in this decision cycle"
            if not self._target_has(target_id, "COMMITTED"):
                return "execution requires a matching commitment"

        return None

    def _apply_public_state(
        self,
        operation: str,
        request: Mapping[str, Any],
        response: Mapping[str, Any],
    ) -> None:
        if not self.state_machine_enabled:
            return

        if operation == "explore":
            target = response.get("candidate_id")
            if isinstance(target, str):
                self._set_target(target, "OBSERVED")

        elif operation == "inspect_relation":
            target = response.get("scope")
            if isinstance(target, str):
                states = self.target_state.setdefault(target, set())
                # A fresh review supersedes the prior review/commitment state for
                # this bounded decision cycle.
                states.discard("REVIEW_CLEAR")
                states.discard("REVIEW_REJECTED")
                states.discard("COMMITTED")
                if response.get("compatibility") == "INCOMPATIBILITY_DETECTED":
                    states.add("REVIEW_REJECTED")
                else:
                    states.add("REVIEW_CLEAR")
                    states.discard("REJECTED")

        elif operation == "query_mandate":
            self.global_state.add("MANDATE_SEEN")

        elif operation == "decide":
            target = request.get("target_id")
            if isinstance(target, str):
                if request.get("decision") == "COMMIT":
                    self._set_target(target, "COMMITTED")
                elif request.get("decision") == "REJECT":
                    states = self.target_state.setdefault(target, set())
                    states.discard("COMMITTED")
                    states.add("REJECTED")

        elif operation == "execute":
            target = request.get("target_id")
            if isinstance(target, str):
                states = self.target_state.setdefault(target, set())
                states.discard("COMMITTED")
                states.add("EXECUTED")

    def call(self, request: Mapping[str, Any]) -> dict[str, Any]:
        if self.terminated:
            raise ToolBrokerError("session already terminated")
        if not isinstance(request, Mapping):
            raise ToolBrokerError("request must be an object")

        operation = request.get("operation")
        if operation not in self.profile["operations"]:
            raise ToolBrokerError(f"operation not available in this profile: {operation!r}")

        spec = self.profile["operations"][operation]
        charge = int(spec["charge"])
        duration = int(spec["duration"])
        self.request_counter += 1

        # Hard resource barrier is checked before any semantic/catalog lookup:
        # it reveals no hidden datum and does not consume the operation charge.
        if self.cost + charge > self.budget or self.clock + duration > self.deadline:
            event = {
                "request_index": self.request_counter,
                "operation": operation,
                "request": deepcopy(dict(request)),
                "status": "RESOURCE_REJECTED",
                "cost_before": self.cost,
                "cost_after": self.cost,
                "clock_before": self.clock,
                "clock_after": self.clock,
            }
            self.public_trace.append(deepcopy(event))
            self._private_trace.append(deepcopy(event))
            return {
                "status": "RESOURCE_REJECTED",
                "operation": operation,
                "remaining_budget": self.budget - self.cost,
                "remaining_time": self.deadline - self.clock,
            }

        target_id = request.get("target_id")
        before_cost, before_clock = self.cost, self.clock
        try:
            entry = self._catalog_entry(operation, target_id)
        except ToolBrokerError as exc:
            return self._charged_rejection(
                operation=operation,
                request=request,
                status="REQUEST_REJECTED",
                reason=str(exc),
                charge=charge,
                duration=duration,
                before_cost=before_cost,
                before_clock=before_clock,
            )

        response = deepcopy(entry.get("response", spec.get("response", {})))
        private = deepcopy(entry.get("private", {}))

        state_reason = self._state_rejection_reason(operation, request, response)
        if state_reason is not None:
            return self._charged_rejection(
                operation=operation,
                request=request,
                status="STATE_REJECTED",
                reason=state_reason,
                charge=charge,
                duration=duration,
                before_cost=before_cost,
                before_clock=before_clock,
            )

        self.cost += charge
        self.clock += duration

        if operation == "communicate":
            response = {
                **response,
                "message_id": request.get("message_id"),
                "recipient": request.get("recipient"),
                "delivery": spec.get("delivery", "RECORDED"),
            }
        elif operation == "decide":
            response = {**response, "decision": request.get("decision"), "target_id": target_id}
        elif operation == "wait":
            response = {**response, "waited": duration}
        elif operation == "stop":
            self.terminated = True
            response = {**response, "terminated": True}

        self._apply_public_state(operation, request, response)

        public_event = {
            "request_index": self.request_counter,
            "operation": operation,
            "request": deepcopy(dict(request)),
            "response": deepcopy(response),
            "status": "OK",
            "charge": charge,
            "duration": duration,
            "cost_before": before_cost,
            "cost_after": self.cost,
            "clock_before": before_clock,
            "clock_after": self.clock,
        }
        private_event = deepcopy(public_event)
        if private:
            private_event["private_adjudication"] = private

        self.public_trace.append(public_event)
        self._private_trace.append(private_event)
        return deepcopy(response)

    def public_receipt(self) -> dict[str, Any]:
        return {
            "cost": self.cost,
            "clock": self.clock,
            "request_count": self.request_counter,
            "terminated": self.terminated,
            "state_machine_enabled": self.state_machine_enabled,
            "events": deepcopy(self.public_trace),
        }

    def private_environment_trace(self) -> list[dict[str, Any]]:
        """Oracle-side evidence. Never pass this value to a candidate adapter."""
        return deepcopy(self._private_trace)
