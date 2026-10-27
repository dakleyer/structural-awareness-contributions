#!/usr/bin/env node

/**

 * SA-MATH-TR-01 weak informational dominance: finite research fixture.

 * It checks deterministic forgetting, task-conditioned strict gain and

 * the non-oracular B'/C'/D' role boundaries using two toy ecosystems.

 * It does not machine-check the open-world theorems or authenticate source

 * evidence, and its unit-free extra cost is only a counterexample.

 * Run: node research/structural-awareness/fixtures/A_APRIME_WEAK_INFORMATION_DOMINANCE_v0.1.mjs

 */

function check(condition,message){if(!condition)throw Error(message)}

function sourceWorld(observedUnresolved,hiddenOutcome=0){
 return {procedure:{id:"nearest-peer",target:"resolve-eligible-peer",scope:"city-zone-1"},
  observedMatches:["peer-1","peer-2"], observedUnresolved:observedUnresolved?["peer-3"]:[],
  hiddenOutcome, qualifiedRoleAssertions:[{aspect:"verified-evaluation-reserve",role:"B",basis:"certificate"}],
  unsettledRole:[{aspect:"unspecified-possible-relation",role:"UNKNOWN"}]};
}

function reducedSignal(world){return {procedure:world.procedure, observedMatches:world.observedMatches}}

function richSignal(world){return {core:reducedSignal(world), boundary:{
  globalCoverage:"OPEN",observedUnresolved:world.observedUnresolved,
  qualifiedRoleAssertions:world.qualifiedRoleAssertions,
  roleUnqualified:world.unsettledRole,
  primedRoleFrontiers:{B:"OPEN",C:"OPEN",D:"OPEN"}}}}

function forgetRich(signal){return signal.core}

function minBinaryError(worlds,signal,label){
  const vals=worlds.map(w=>JSON.stringify(signal(w)));const keys=[...new Set(vals)];
  let best=Infinity;
  for(let mask=0;mask<2**keys.length;mask++){
   let wrong=0;
   for(let i=0;i<worlds.length;i++){
     const predicted=(mask>>keys.indexOf(vals[i]))&1;
     if(predicted!==label(worlds[i]))wrong++;
   }
   best=Math.min(best,wrong/worlds.length);
  }
  return best;
}

function runChecks(){
 let total=0;
 const ok=(test,label)=>{check(test,label);total++;};
 const w0=sourceWorld(false,0),w1=sourceWorld(true,1);
 ok(JSON.stringify(reducedSignal(w0))===JSON.stringify(reducedSignal(w1)),"reduced source signals collapse worlds");
 ok(JSON.stringify(richSignal(w0))!==JSON.stringify(richSignal(w1)),"rich signals distinguish observed boundary");
 ok(JSON.stringify(forgetRich(richSignal(w0)))===JSON.stringify(reducedSignal(w0)),"recover reduced from rich world 0");
 ok(JSON.stringify(forgetRich(richSignal(w1)))===JSON.stringify(reducedSignal(w1)),"recover reduced from rich world 1");
 ok(richSignal(w0).boundary.globalCoverage==="OPEN"&&richSignal(w1).boundary.globalCoverage==="OPEN","global frontier persists in both");
 ok(richSignal(w0).boundary.observedUnresolved.length===0,"run 0 has clean observed set");
 ok(richSignal(w1).boundary.observedUnresolved.length===1,"run 1 has one indeterminate observed");
 const worlds=[w0,w1],meta=w=>Number(w.observedUnresolved.length>0);
 const riskReduced=minBinaryError(worlds,reducedSignal,meta);
 const riskRich=minBinaryError(worlds,richSignal,meta);
 ok(riskReduced===0.5,"garbled signal minimum Bayes risk 1/2");
 ok(riskRich===0,"richer signal minimum Bayes risk 0");
 ok(riskRich<=riskReduced,"weak dominance inequality");
 ok(riskRich<riskReduced,"strict gain for independent run-scoped meta-task");
 const worldsHidden=[sourceWorld(true,0),sourceWorld(true,1)];
 ok(minBinaryError(worldsHidden,richSignal,w=>w.hiddenOutcome)===0.5,"rich signal is not an oracle for hidden semantic truth");
 ok(minBinaryError(worldsHidden,reducedSignal,w=>w.hiddenOutcome)===0.5,"reduced also ignorant of hidden truth");
 ok(riskRich+0.75>riskReduced,"cost may reverse net preferred implementation");
 ok(richSignal(w1).boundary.qualifiedRoleAssertions[0].role==="B","qualified finite B claim retained");
 ok(richSignal(w1).boundary.roleUnqualified[0].role==="UNKNOWN","unqualified aspect must not be forced B/C/D");
 ok(Object.values(richSignal(w1).boundary.primedRoleFrontiers).every(x=>x==="OPEN"),"B/C/D prime frontiers remain open");
 ok(Object.values(richSignal(w0).boundary.primedRoleFrontiers).every(x=>x==="OPEN"),"absence of encountered unknown does not close B/C/D primes");
 ok(JSON.stringify(richSignal(w0)).length>JSON.stringify(reducedSignal(w0)).length,"more information can cost more bytes");
 return {passed:total,riskReduced,riskRich,hiddenRisk:0.5};
}

const summary=runChecks();

console.log("A/A-prime weak dominance finite fixture:",JSON.stringify(summary));

