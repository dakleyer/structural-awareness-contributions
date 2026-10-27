#!/usr/bin/env node

/**

 * SA-FG-01 finite four-dimension Stage 1/2/3 research witness.

 * Source lineage: PR42 dimensional ACC toy, PR45 qualified cloud,

 * PR57 blocked second-order opportunity. This does not overwrite or

 * automatically reproduce any of their frozen experiments.

 * All source attestation, objective bounds and rights are synthetic

 * modeling assumptions, not measured natural agent phenomena.

 * Run: node research/structural-awareness/fixtures/CROSS_AGENT_RESIDUAL_CARTOGRAPHY_v0.1.mjs

 */

function ensure(ok,msg){if(!ok)throw Error("CHECK: "+msg)}

function approx(a,b,eps=1e-8){return Math.abs(a-b)<eps}

function case4(){
 return {
 config:{n:4,localMax:0.55,metaThreshold:0.90,error:0.01,current:[0.5,0.5,0.5,0.5],scope:"dimensional-candidate-v1",version:"v1",deadline:10,adoptionCost:0.06},
 arrivals:[
 {id:"e1",t:1,x:[.48,.48,.48,.48]},
 {id:"e2",t:2,x:[.78,.81,.25,.74]},
 {id:"e3",t:3,x:[.86,.83,.89,.79]},
 {id:"e4",t:4,x:[.94,.95,.96,.97]}]
 };
}

function total(xs){return xs.reduce((s,x)=>s+x,0)}

function sourceReports(e,c,options={}){
 let reports=e.x.map((x,i)=>({
  event:e.id,dimension:i,origin:"source-"+i,lower:Math.max(0,x-c.error),upper:Math.min(1,x+c.error),
  scope:c.scope,version:options.badVersion&&e.id==="e4"?"v2":c.version,
  expiry:options.expired&&e.id==="e4"?e.t-1:c.deadline,
  attested:!(options.badSource&&e.id==="e4"&&i===0)}));
 if(options.duplicate&&e.id==="e4")reports[3]={...reports[0]};
 return reports;
}

function localObjectAccept(reports,c){return reports.length===c.n&&reports.every((r,i)=>r.dimension===i&&r.upper<=c.localMax)}

function metaClassify(reports,c,time){
 if(reports.length!==c.n)return{eligible:false,reason:"WRONG_COUNT"};
 if(new Set(reports.map(x=>x.dimension)).size!==c.n||new Set(reports.map(x=>x.origin)).size!==c.n)
  return{eligible:false,reason:"DUPLICATE_SOURCE_OR_DIMENSION"};
 if(!reports.every(x=>x.attested&&x.scope===c.scope&&x.version===c.version&&x.expiry>=time&&Number.isFinite(x.lower)&&Number.isFinite(x.upper)&&x.lower<=x.upper&&x.lower>=0&&x.upper<=1))
  return{eligible:false,reason:"SOURCE_UNQUALIFIED"};
 const ordered=reports.slice().sort((a,b)=>a.dimension-b.dimension);
 if(!ordered.every((r,i)=>r.dimension===i))return{eligible:false,reason:"MISSING_DIMENSION"};
 const outside=ordered.every(r=>r.lower>c.localMax);
 const target=ordered.every(r=>r.lower>=c.metaThreshold);
 const lower=total(ordered.map(r=>r.lower)),upper=total(ordered.map(r=>r.upper));
 return {eligible:outside&&target,reason:outside&&target?"CERTIFIED_INTERSECTION":"INSUFFICIENT",
   lower,upper,labels:ordered.map(r=>({origin:r.origin,dimension:r.dimension,
     outsideObject:r.lower>c.localMax,nearOptLower:r.lower>=c.metaThreshold}))};
}

function policyRun(c,arrivals,policy,options={}){
 let current=total(c.current),selected="initial",certified=[],rejected=[],blocked=[],accepted=[];
 for(const e of arrivals){
  const measurements=sourceReports(e,c,options);
  if(localObjectAccept(measurements,c)){
   if(total(e.x)>current){current=total(e.x);selected=e.id;accepted.push(e.id)}
   continue;
  }
  if(policy==="CLOSED"){rejected.push(e.id);continue}
  const meta=metaClassify(measurements,c,e.t);
  if(!meta.eligible){rejected.push(e.id);continue}
  certified.push({id:e.id,lower:meta.lower,upperRegret:c.n-meta.lower});
  if(policy==="REVIEW"){blocked.push({id:e.id,reason:"NO_ACTION_CAPABILITY"});continue}
  if(options.noAuthority){blocked.push({id:e.id,reason:"NO_AUTHORITY"});continue}
  if(options.materialD){blocked.push({id:e.id,reason:"MATERIAL_D"});continue}
  if(meta.lower<=current+c.adoptionCost){blocked.push({id:e.id,reason:"NO_CERTIFIED_IMPROVEMENT"});continue}
  current=total(e.x);selected=e.id;accepted.push(e.id);
 }
 return {policy,current,selected,technicalGap:c.n-current,
 netValue:selected==="initial"?current:current-c.adoptionCost,
 certified,rejected,blocked,accepted};
}

function runAll(){
 let count=0;function ok(v,m){ensure(v,m);count++}
 const {config:c,arrivals}=case4();
 const a=policyRun(c,arrivals,"CLOSED");
 const b=policyRun(c,arrivals,"REVIEW");
 const d=policyRun(c,arrivals,"OPEN");
 const equivalent=policyRun(c,arrivals,"CONVENTIONAL_SAME_META");
 ok(approx(a.current,2),"stage1 suboptimal baseline");
 ok(approx(b.current,2),"stage2 meta-sharing without action no improvement");
 ok(approx(d.current,3.82),"stage3 actual candidate adoption");
 ok(approx(equivalent.current,d.current),"strong equally informed conventional ties");
 ok(d.selected==="e4","stage3 found eventual candidate");
 ok(a.rejected.includes("e4"),"stage1 discarded exactly same candidate");
 ok(b.certified.some(x=>x.id==="e4"),"read-only stage2 recognizes candidate");
 ok(b.blocked.some(x=>x.id==="e4"),"stage2 unresolved action remains blocked");
 ok(d.certified.some(x=>x.id==="e4"&&approx(x.lower,3.78)),"lower quality bound is 3.78");
 ok(d.certified.some(x=>x.id==="e4"&&x.upperRegret<.25),"near-optimal bound valid");
 ok(d.technicalGap>0&&d.technicalGap<.25,"does not reach optimum");
 ok(a.technicalGap===2,"referee stage1 gap equals 2");
 ok(approx(d.netValue,3.76),"cost charged separately from physical quality");
 ok(approx(policyRun(c,arrivals,"OPEN",{badSource:true}).current,2),"bad source blocks");
 ok(approx(policyRun(c,arrivals,"OPEN",{badVersion:true}).current,2),"version mismatch blocks");
 ok(approx(policyRun(c,arrivals,"OPEN",{expired:true}).current,2),"expiry blocks");
 ok(approx(policyRun(c,arrivals,"OPEN",{duplicate:true}).current,2),"duplicate source cannot supply missing dimension");
 ok(approx(policyRun(c,arrivals,"OPEN",{noAuthority:true}).current,2),"authority matters");
 ok(approx(policyRun(c,arrivals,"OPEN",{materialD:true}).current,2),"material unknown dependency blocks actuation");
 ok(approx(policyRun(c,arrivals.slice(0,3),"OPEN").current,2),"no arrival no guaranteed improvement");
 ok(!metaClassify(sourceReports(arrivals[2],c),c,3).eligible,"weak bands do not certify near-opt");
 ok(metaClassify(sourceReports(arrivals[3],c),c,4).labels.every(x=>x.outsideObject&&x.nearOptLower),"intersection carries all qualified per-dimension labels");
 const P=false,Q=true;
 ok(!(P&&Q)===(!P||!Q),"De Morgan correct disjunction");
 ok(!(P&&Q)!==(!P&&!Q),"cannot infer both failed predicates from composite residual");
 ok(Array(c.n).fill(1).every(x=>x>=c.metaThreshold),"mathematical intersection nonempty in declared cube");
 const optionalArrivalProb=1-Math.pow(1-1e-4,100);
 ok(optionalArrivalProb>0&&optionalArrivalProb<1,"even iid p>0 not certain by fixed horizon");
 ok(b.certified[0].upperRegret<=.25,"second order documented bound not added to first gap");
 return {passed:count,source:"Four-dimensional mathematical illustration grounded in ACC dimensionality and PR45 qualified cloud",
  conditionalModel:{objective:"sum of 4 normalized quality attributes",technicalMaximum:4,
    defaultLocalThreshold:c.localMax,metaThreshold:c.metaThreshold,
    witnessTime:4,arrivalLaw:"not inferred; fixed synthetic candidate"},
  stage1:a,stage2:b,stage3:d,equivalentConventional:equivalent};
}

const result=runAll();

console.log(JSON.stringify(result,null,2));

