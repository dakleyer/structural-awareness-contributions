#!/usr/bin/env node

/**

 * Finite architectural-contract checks, not a halting-theorem proof.

 * Identical K/D/V execution, two allowed semantic export contracts:

 * closed-only (only facts within admitted A) and open-aware (A plus A-prime).

 * All worlds, reports and qualified evidence are synthetic; no global

 * completeness certificate or oracle is computed.

 * Run: node research/structural-awareness/fixtures/OPEN_ECOSYSTEM_COMPOSITION_AND_RESIDUAL_v0.1.mjs

 */

function test(ok,label){if(!ok)throw Error("FAIL: "+label)}

function sourceWorld(hasExternal,runUnknown){
return {relevantIds:hasExternal?["peer-known","peer-external"]:["peer-known"],
        seenIds:["peer-known"],
        inA:[{id:"peer-known",status:runUnknown?"UNKNOWN":"VERIFIED",evidence:"qualified"}],
        algorithmId:"K>D>V",
        task:"verify eligible peer response"};
}

function observedRun(w){
return {algorithm:w.algorithmId,task:w.task,admittedScope:[...w.seenIds],
        qualified:[...w.inA],
        observedUnresolved:w.inA.filter(x=>x.status==="UNKNOWN").map(x=>x.id)};
}

function closedOnly(w){
const r=observedRun(w);
return {algorithm:r.algorithm,task:r.task,admittedScope:r.admittedScope,qualified:r.qualified,observedUnresolved:r.observedUnresolved};
}

function openAware(w){
return {withinA:closedOnly(w),
        frontier:{kind:"OPEN",meaning:"not a certified global census of all task-relevant cases"},
        roleAssertions:[{aspect:"reserve",role:"B",evidence:"qualified"}],
        unqualifiedAspects:[{aspect:"not-characterized",role:"UNKNOWN"}]};
}

function forgetFrontier(msg){return msg.withinA;}

function exactGlobalClosureClaim(msg,w){return w.relevantIds.every(x=>msg.admittedScope.includes(x));}

function checks(){
let n=0;const c=(v,label)=>{test(v,label);n++};
const easy=sourceWorld(false,false),hidden=sourceWorld(true,false),unknown=sourceWorld(true,true);
c(JSON.stringify(observedRun(easy))===JSON.stringify(observedRun(hidden)),"indistinguishable run prefix");
c(JSON.stringify(closedOnly(easy))===JSON.stringify(closedOnly(hidden)),"same closed in-A message");
c(JSON.stringify(forgetFrontier(openAware(easy)))===JSON.stringify(closedOnly(easy)),"open recovers closed easy");
c(JSON.stringify(forgetFrontier(openAware(hidden)))===JSON.stringify(closedOnly(hidden)),"open recovers closed hidden");
c(openAware(easy).frontier.kind==="OPEN","OPEN stays present when no observed unknowns");
c(openAware(hidden).frontier.kind==="OPEN","OPEN persists despite same local successes");
c(openAware(hidden).withinA.observedUnresolved.length===0,"hidden unknowns not magically enumerated");
c(!exactGlobalClosureClaim(closedOnly(hidden),hidden),"closure claim falsified by invisible extra peer");
c(exactGlobalClosureClaim(closedOnly(easy),easy),"same finite scoped census might happen to be exhaustive");
c(openAware(unknown).withinA.observedUnresolved[0]==="peer-known","local unknown preserved by richer");
c(closedOnly(unknown).observedUnresolved[0]==="peer-known","closure-only may correctly preserve local unknown too");
c(openAware(unknown).frontier.kind==="OPEN","observed UNKNOWN does not close broader frontier");
c(!JSON.stringify(openAware(hidden)).includes("peer-external"),"open frontier does not name hidden agent");
c(!("frontier" in closedOnly(hidden)),"closure-only contract forbids meta-frontier type");
c(!("semanticHaltingOracle" in openAware(hidden)),"open report contains no omniscient classifier");
c(openAware(unknown).unqualifiedAspects[0].role==="UNKNOWN","role boundary remains unqualified");
c(openAware(unknown).roleAssertions[0].role==="B","qualified B role can still be sent");
c(JSON.stringify(openAware(hidden)).length>JSON.stringify(closedOnly(hidden)).length,"extra semantic contract may cost bytes");
return n;
}

const passed=checks();

console.log("Finite open-world composition contract assertions passed:",passed);

