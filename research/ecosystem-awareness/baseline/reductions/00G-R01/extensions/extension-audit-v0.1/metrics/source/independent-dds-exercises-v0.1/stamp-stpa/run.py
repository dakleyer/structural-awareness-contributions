"""Execute a bounded STPA-informed control model and independent actual-context grading."""
from pathlib import Path
from itertools import product
import argparse,sys,time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from exercise_common import load_frozen,save
ROOT=Path(__file__).resolve().parent

class Plant:
    def __init__(self,world):
        self._running=world["pump_running"]
        self._stop_applied=world["stop_applied"]
    def stop_and_observe(self):
        if self._stop_applied:self._running=False
        return not self._running
    @property
    def running(self):return self._running


def decide(observation,stop_and_observe):
    trace=[];cost={"state_queries":1,"commands":0,"feedback_checks":0}
    if not observation["authority"] or not observation["sensor_current"]:
        return {"stop":False,"entry":False,"defer":False,"trace":["unqualified-state-or-mandate"],"work":cost}
    if not observation["maintenance"]:
        return {"stop":False,"entry":False,"defer":False,"trace":["supply-only"],"work":cost}
    if observation["critical_supply"] and not observation["backup"]:
        return {"stop":False,"entry":False,"defer":observation["allow_defer"],"trace":["protect-critical-supply"],"work":cost}
    cost["commands"]+=int(observation["pump_running"])
    trace.append("stop-requested" if observation["pump_running"] else "already-stopped")
    observed_stopped=not observation["pump_running"] or stop_and_observe()
    cost["feedback_checks"]+=1;trace.append("stop-confirmed" if observed_stopped else "stop-not-confirmed")
    return {"stop":observation["pump_running"],"entry":observed_stopped,
        "defer":not observed_stopped and observation["allow_defer"],"trace":trace,"work":cost}

def judge(world,commands):
    running=world["pump_running"]
    if commands["stop"] and world["stop_applied"]:running=False
    hazards=[]
    if commands["entry"] and running:hazards.append("H1-energized-maintenance")
    if commands["stop"] and world["stop_applied"] and world["pump_running"] and world["critical_supply"] and not world["backup"]:hazards.append("H2-critical-supply-interruption")
    if (commands["entry"] or (commands["stop"] and world["stop_applied"] and world["pump_running"])) and not world["authority"]:hazards.append("H3-unauthorized-control")
    supply=not world["critical_supply"] or running or world["backup"]
    if hazards:return {"outcome":"P","hazards":hazards,"running":running,"supply":supply}
    if not world["maintenance"] and world["authority"] and world["sensor_current"] and supply:return {"outcome":"I","hazards":[]}
    if commands["entry"] and not running and supply:return {"outcome":"I","hazards":[]}
    if commands["defer"] and world["allow_defer"] and supply:return {"outcome":"M","hazards":[]}
    return {"outcome":"incomplete","hazards":[]}

def main(output):
    card,freeze=load_frozen(ROOT);start=time.perf_counter();rows=[];assertions=0;counts={"I":0,"M":0,"P":0,"incomplete":0};diagnostics=0
    for case in card["cases"]:
        world=case["world"]
        view={key:world[key] for key in ("pump_running","maintenance","critical_supply","backup","authority","sensor_current","allow_defer")}
        plant=Plant(world)
        commands=decide(view,plant.stop_and_observe)
        assert "stop_applied" not in view and "expected_qualified_outcome" not in view
        assert plant.running == (world["pump_running"] and not (commands["stop"] and world["stop_applied"]))
        assertions+=2
        judged=judge(world,commands)
        assert judged["outcome"]==case["expected_qualified_outcome"],(case["id"],judged);assertions+=1
        assert not judged["hazards"],case["id"];assertions+=1
        if commands["entry"]:assert not world["pump_running"] or world["stop_applied"]
        assertions+=1;counts[judged["outcome"]]+=1
        naive={"stop":world["maintenance"],"entry":world["maintenance"],"defer":False}
        bad=judge(world,naive);diagnostics+=int(bad["outcome"]=="P")
        rows.append({"id":case["id"],"narrative":case["narrative"],"qualified_commands":commands,
            "qualified_outcome":judged["outcome"],"hazards":judged["hazards"],
            "open_loop_diagnostic_outcome":bad["outcome"],"open_loop_diagnostic_hazards":bad["hazards"]})
    contexts=[]
    for running,critical,backup,authority,applied,entry in product((False,True),repeat=6):
        world={"pump_running":running,"maintenance":True,"critical_supply":critical,"backup":backup,
            "authority":authority,"sensor_current":True,"stop_applied":applied,"allow_defer":True}
        candidate={"stop":True,"entry":entry,"defer":False}
        result=judge(world,candidate)
        # UCA provision/context and realized effect are deliberately separate.
        possible = []
        if entry and running:possible.append("H1-energized-maintenance")
        if running and critical and not backup:possible.append("H2-critical-supply-interruption")
        if not authority:possible.append("H3-unauthorized-control")
        # Independent state-transition reconstruction uses final/initial plant state.
        final_running = running and not applied
        actual_h1 = entry and final_running
        actual_h2 = running and not final_running and critical and not backup
        actual_h3 = (entry or (running != final_running)) and not authority
        assert ("H1-energized-maintenance" in result["hazards"]) == actual_h1
        assert ("H2-critical-supply-interruption" in result["hazards"]) == actual_h2
        assert ("H3-unauthorized-control" in result["hazards"]) == actual_h3
        assert set(result["hazards"]).issubset(possible)
        assertions += 4
        contexts.append({"context":[running,critical,backup,authority,applied,entry],
            "unsafe_control_contexts":possible,"realized_violations":result["hazards"]})
    save(ROOT,output,card,freeze,{"status":"PASS_REGISTERED_FIXTURE_ASSERTIONS","cases":rows,"assertions":assertions,
        "qualified_outcome_counts":counts,"diagnostic_wrong_effects":diagnostics,"enumerated_actual_contexts":contexts,
        "elapsed_local_seconds":time.perf_counter()-start,"scope":"four-step STPA analyst model with finite actual-context exercise; no deployed plant or expert validation",
        "UCA_timing_duration_coverage":"Analysis report includes loss scenarios for lateness/maintained commands; this enumerator covers discrete stop/entry context only",
        "method_adequacy_or_safety_certification":"not established","external_matched_differential":"not established"})
if __name__=="__main__":
    a=argparse.ArgumentParser();a.add_argument("--output",required=True);main(a.parse_args().output)

