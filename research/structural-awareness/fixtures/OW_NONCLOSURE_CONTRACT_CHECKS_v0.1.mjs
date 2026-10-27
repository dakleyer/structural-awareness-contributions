#!/usr/bin/env node

/**

 * OW non-closure: bounded executable contract sanity checks (research fixture).

 * No external dependencies. Run: node OW_NONCLOSURE_CONTRACT_CHECKS_v0.1.mjs

 * Tests scoped output semantics, NOT the undecidability theorem or a real city.

 * The trustedInventory argument is a PREVERIFIED contract supplied by an

 * external qualified verifier. This fixture does NOT authenticate it or

 * construct a global closed population from observed peers.

 */

function assert(condition, message) { if (!condition) throw new Error(message); }

function contractReport(query, trustedInventory = null) {
  // "trustedInventory" is a pre-verified external certificate, NOT verified here.
  const allowed = new Set(["YES", "NO", "UNKNOWN"]);
  const seen = new Set();
  const positive = [];
  const negative = [];
  const unresolved = [];
  const diagnostics = [];
  for (const rec of query.records) {
    if (!rec.id || seen.has(rec.id) || !allowed.has(rec.verdict)) throw new Error("INVALID_RECORD");
    seen.add(rec.id);
    if (rec.verdict === "YES") positive.push(rec.id);
    if (rec.verdict === "NO") negative.push(rec.id);
    if (rec.verdict === "UNKNOWN") unresolved.push(rec.id);
    if ((rec.diagnostic === "BAD_FRAME" || rec.diagnostic === "TIMEOUT") &&
        rec.verdict !== "UNKNOWN" && !rec.independentEvidence) throw new Error("UNQUALIFIED_SEMANTIC_PROMOTION");
    if (rec.diagnostic) diagnostics.push({id: rec.id, diagnostic: rec.diagnostic});
  }
  let populationCoverage = "OPEN";
  if (trustedInventory !== null) {
    if (trustedInventory.scope !== query.scope || trustedInventory.snapshot !== query.snapshot) throw new Error("CERTIFICATE_SCOPE_MISMATCH");
    const ids = new Set(trustedInventory.peerIds);
    if (ids.size !== trustedInventory.peerIds.length || ids.size !== seen.size ||
        [...ids].some(x => !seen.has(x))) throw new Error("CERTIFICATE_COVERAGE_MISMATCH");
    populationCoverage = "CERTIFIED_CLOSED";
  }
  const semanticCompleteness = unresolved.length === 0 ? "COMPLETE_ON_OBSERVED" : "INCOMPLETE_ON_OBSERVED";
  const globalSetCoverage = populationCoverage === "CERTIFIED_CLOSED" && unresolved.length === 0 ? "CERTIFIED_CLOSED" : "OPEN";
  return {scope: query.scope, snapshot: query.snapshot, positive, negative, unresolved, diagnostics, populationCoverage, semanticCompleteness, globalSetCoverage};
}

function nearestObserved(query) {
  const candidates = query.records.filter(r => r.verdict === "YES");
  for (const x of candidates) if (!(Number.isFinite(x.distance) && x.distance >= 0)) throw new Error("NO_QUALIFIED_DISTANCE");
  if (candidates.length === 0) return {status:"NO_MATCH_OBSERVED"};
  candidates.sort((a,b) => a.distance-b.distance || a.id.localeCompare(b.id));
  return {status:"NEAREST_OBSERVED_ONLY",id:candidates[0].id,distance:candidates[0].distance};
}

function nearestGlobal(query, trustedInventory = null) {
  const report = contractReport(query,trustedInventory);
  const local = nearestObserved(query);
  if (report.globalSetCoverage !== "CERTIFIED_CLOSED") return {status:"INDETERMINATE_GLOBAL",local,coverage:report.globalSetCoverage};
  if (local.status === "NO_MATCH_OBSERVED") return {status:"CERTIFIED_NO_MATCH",coverage:"CERTIFIED_CLOSED"};
  return {status:"CERTIFIED_GLOBAL_NEAREST",id:local.id,distance:local.distance,coverage:"CERTIFIED_CLOSED"};
}

function expectError(fn, code) {
  try { fn(); } catch (e) { assert(e.message === code,"Expected "+code+" got "+e.message); return; }
  throw new Error("Expected error: "+code);
}

function runChecks() {
  let checks = 0;
  const check = (ok, desc) => {assert(ok,desc);checks++};
  const q={scope:"city-zone-A",snapshot:"t0",records:[{id:"a",verdict:"YES",distance:7},{id:"b",verdict:"NO"}]};
  const open=contractReport(q);
  check(open.globalSetCoverage==="OPEN"&&open.unresolved.length===0,"all observed classified does not close the world");
  check(nearestGlobal(q).status==="INDETERMINATE_GLOBAL","nearest globally cannot be certified from open coverage");
  check(nearestObserved(q).id==="a"&&nearestObserved(q).status==="NEAREST_OBSERVED_ONLY","nearest observed is permissible local result");
  const timeout={scope:q.scope,snapshot:q.snapshot,records:[{id:"a",verdict:"UNKNOWN",diagnostic:"TIMEOUT"}]};
  check(contractReport(timeout).unresolved[0]==="a","timeout leaves eventual outcome unknown");
  expectError(()=>contractReport({scope:q.scope,snapshot:q.snapshot,records:[{id:"a",verdict:"NO",diagnostic:"TIMEOUT"}]}),"UNQUALIFIED_SEMANTIC_PROMOTION");checks++;
  const damaged={scope:q.scope,snapshot:q.snapshot,records:[{id:"a",verdict:"UNKNOWN",diagnostic:"BAD_FRAME"}]};
  check(contractReport(damaged).diagnostics[0].diagnostic==="BAD_FRAME"&&contractReport(damaged).unresolved.length===1,"corrupt frame leaves source semantics unknown");
  expectError(()=>contractReport({scope:q.scope,snapshot:q.snapshot,records:[{id:"a",verdict:"NO",diagnostic:"BAD_FRAME"}]}),"UNQUALIFIED_SEMANTIC_PROMOTION");checks++;
  const trusted={scope:q.scope,snapshot:q.snapshot,peerIds:["a","b"]}; // PRE-VERIFIED by an external authority
  const closed=contractReport(q,trusted);
  check(closed.globalSetCoverage==="CERTIFIED_CLOSED"&&nearestGlobal(q,trusted).id==="a","certified finite inventory permits scoped global min");
  expectError(()=>contractReport(q,{scope:q.scope,snapshot:q.snapshot,peerIds:["a","b","c"]}),"CERTIFICATE_COVERAGE_MISMATCH");checks++;
  expectError(()=>contractReport(q,{scope:q.scope,snapshot:"other-time",peerIds:["a","b"]}),"CERTIFICATE_SCOPE_MISMATCH");checks++;
  const unresolved={scope:q.scope,snapshot:q.snapshot,records:[{id:"a",verdict:"YES",distance:7},{id:"b",verdict:"UNKNOWN"}]};
  const semi=contractReport(unresolved,trusted);
  check(semi.populationCoverage==="CERTIFIED_CLOSED"&&semi.globalSetCoverage==="OPEN","complete population does not imply complete semantic classification");
  check(nearestGlobal(unresolved,trusted).status==="INDETERMINATE_GLOBAL","known matching candidate is not proven nearest when another peer is unknown");
  check(nearestObserved({scope:q.scope,snapshot:q.snapshot,records:[]}).status==="NO_MATCH_OBSERVED","empty observation is not global absence");
  expectError(()=>contractReport({scope:q.scope,snapshot:q.snapshot,records:[{id:"a",verdict:"YES"},{id:"a",verdict:"NO"}]}),"INVALID_RECORD");checks++;
  const repaired={scope:q.scope,snapshot:q.snapshot,records:[{id:"a",verdict:"YES",independentEvidence:true,diagnostic:"BAD_FRAME",distance:1},{id:"b",verdict:"NO"}]};
  check(contractReport(repaired,trusted).globalSetCoverage==="CERTIFIED_CLOSED","independently verified evidence may repair corrupted payload");
  return checks;
}

const checks = runChecks();

console.log("OW-NC research fixture: "+checks+" bounded assertions passed");

