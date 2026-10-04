"""Technology-neutral bounded tool broker for R01.

The broker exposes only manifest-declared participant responses. Private effect
and adjudication data are retained for the later oracle/evaluator.
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
        entry = self._catalog_entry(operation, target_id)
        response = deepcopy(entry.get("response", spec.get("response", {})))
        private = deepcopy(entry.get("private", {}))

        before_cost, before_clock = self.cost, self.clock
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
            "events": deepcopy(self.public_trace),
        }

    def private_environment_trace(self) -> list[dict[str, Any]]:
        """Oracle-side evidence. Never pass this value to a candidate adapter."""
        return deepcopy(self._private_trace)
