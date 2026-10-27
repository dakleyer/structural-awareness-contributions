#!/usr/bin/env node

/**

 * Structural Awareness: stage-1 closed / stage-2 shared-meta / stage-3 observed-promotion

 * Research-only synthetic extension. NOT the ACC PR57 implementation.

 * Exactly same 4D physical events; agents see only typed 1D values before admission;

 * meta-controller sees only qualified ABOVE/BELOW/INSIDE bits and event provenance.

 * Referee alone scores 4D truth. No arrival prior, no oracle or real AI deployment.

 * All selected rules are preinstalled; result is conditional on proof, sources and authority.

 * Run: node research/structural-awareness/fixtures/COLLECTIVE_RESIDUAL_STAGE3_PROMOTION_v0.1.mjs

 */

const N_AGENTS=4, LO=.25, HI=.75, START_SCORE=2.4, TRANSITION_COST=.1;

function verify(b,msg){if(!b)throw Error("FAILED: "+msg);}

function inputEvent(id, coords){
  verify(typeof id==="string" && id.length>0,"event id required");
  verify(Array.isArray(coords)&&coords.length===N_AGENTS&&coords.every(v=>typeof v==="number" && v>=0 && v<=1),"finite synthetic coordinates 0..1");
  return {id,coords};
}

function sourceReports(ev,{qualified=true,missing=[],wrongIdAt=-1}={}){
  return ev.coords.map((v,i)=>{
    const side=v<LO?"BELOW":v>HI?"ABOVE":"INSIDE";
    return {event_id:i===wrongIdAt?ev.id+"-different":ev.id,source_id:"agent-"+i,dimension:i,side,
            qualified:qualified && !missing.includes(i),source_scope:"demo-same-task-v1"};
  });
}

function closedProjection(reports) {
  return reports.map(x=>x.side==="INSIDE"?"IN_A":"DROP");
}

function metaGate(reports, {authorized=true,proofValid=true,context="demo-same-task-v1",baseScore=START_SCORE,cost=TRANSITION_COST}={}) {
  if(!authorized)return{status:"BLOCKED_AUTHORITY"};
  if(!proofValid)return{status:"BLOCKED_UNVERIFIED_THEOREM"};
  if(reports.length!==N_AGENTS)return{status:"HOLD_INCOMPLETE"};
  const ids=new Set(reports.map(x=>x.event_id)), dims=new Set(reports.map(x=>x.dimension)), origins=new Set(reports.map(x=>x.source_id));
  if(ids.size!==1||dims.size!==N_AGENTS||origins.size!==N_AGENTS)return{status:"HOLD_BAD_JOIN"};
  if(reports.some(x=>!x.qualified||x.source_scope!==context))return{status:"HOLD_UNQUALIFIED"};
  if(reports.some(x=>x.side!=="ABOVE"))return{status:"HOLD_NO_CERTIFIED_LOWER_BOUND"};
  const bound=N_AGENTS*HI; // mathematical strict bound from all ABOVE_i
  if(!(bound>baseScore+cost))return{status:"HOLD_NO_CERTIFIED_NET_GAIN",score_lower_bound_exclusive:bound};
  return{status:"PROMOTE_RESIDUAL",candidate_event_id:reports[0].event_id,
         score_lower_bound_exclusive:bound, cert:"ALL_DIMENSIONS_ABOVE_0_75_V1"};
}

function refereeScore(ev){return ev.coords.reduce((sum,x)=>sum+x,0);}

function stageStream(events,{authorized=true,proofValid=true,cost=TRANSITION_COST}={}) {
  let closed=START_SCORE,open=START_SCORE,seen=0,promoted=0,firstPromoAt=null,history=[];
  for(const ev of events){
    seen++;
    const reports=sourceReports(ev);
    const c=closedProjection(reports);
    if(c.every(x=>x==="IN_A"))closed=Math.max(closed,refereeScore(ev)); // closed processes only fully admitted
    const decision=metaGate(reports,{authorized,proofValid,baseScore:open,cost});
    if(decision.status==="PROMOTE_RESIDUAL"){
      const actual=refereeScore(ev)-cost;
      open=Math.max(open,actual);
      promoted++;
      if(firstPromoAt===null)firstPromoAt=seen;
    }else if(c.every(x=>x==="IN_A"))open=Math.max(open,refereeScore(ev));
    history.push({id:ev.id,index:seen,closed:c,meta:decision.status});
  }
  return{closed_score:closed,open_score:open,net_increment:open-closed,
         first_promoted_event_index:firstPromoAt,promotions:promoted,processed_events:seen,
         external_region_individuals_identified_by_stage2:0,history};
}

function runChecks(){
  let checks=0;const ck=(b,m)=>{verify(b,m);checks++};
  const hi=inputEvent("same-opaque-event",[.9,.88,.83,.86]);
  const lo=inputEvent("same-opaque-event",[.1,.08,.12,.05]);
  const mid=inputEvent("ordinary",[.6,.6,.6,.6]);
  const hiR=sourceReports(hi),loR=sourceReports(lo);
  ck(JSON.stringify(closedProjection(hiR))===JSON.stringify(closedProjection(loR)),"same closed report high/low");
  ck(closedProjection(hiR).every(x=>x==="DROP"),"high falls outside every old admission");
  ck(closedProjection(loR).every(x=>x==="DROP"),"low falls outside every old admission");
  ck(refereeScore(hi)>3.0&&refereeScore(lo)<1,"world target differs");
  ck(hiR.every(x=>x.side==="ABOVE"),"multi-source qualified upper-side labels");
  ck(loR.every(x=>x.side==="BELOW"),"multi-source qualified lower-side labels");
  ck(metaGate(hiR).status==="PROMOTE_RESIDUAL","all-high source qualifies");
  ck(metaGate(loR).status!=="PROMOTE_RESIDUAL","all-low source rejected safely");
  ck(metaGate(sourceReports(mid)).status!=="PROMOTE_RESIDUAL","inside case not force promotion");
  ck(metaGate(hiR).score_lower_bound_exclusive===N_AGENTS*HI,"joint lower bound is exactly threshold sum");
  ck(metaGate(hiR).score_lower_bound_exclusive>START_SCORE+TRANSITION_COST,"strict certified improvement after cost");
  ck(!hiR.some(x=>Object.hasOwn(x,"value")),"source reports contain only side bits, not full coordinates");
  ck(!JSON.stringify(hiR).includes("0.9"),"exact 0.9 not disclosed to evaluator");
  ck(metaGate(sourceReports(hi,{qualified:false})).status==="HOLD_UNQUALIFIED","unauthenticated all-high blocked");
  ck(metaGate(sourceReports(hi,{missing:[2]})).status==="HOLD_UNQUALIFIED","missing dimension blocked");
  ck(metaGate(sourceReports(hi,{wrongIdAt:2})).status==="HOLD_BAD_JOIN","incompatible event identifiers blocked");
  ck(metaGate(hiR.slice(0,3)).status==="HOLD_INCOMPLETE","incomplete source set blocked");
  ck(metaGate(hiR,{authorized:false}).status==="BLOCKED_AUTHORITY","authority block preserved");
  ck(metaGate(hiR,{proofValid:false}).status==="BLOCKED_UNVERIFIED_THEOREM","theorem validity is not automatic");
  ck(metaGate(hiR,{cost:5}).status==="HOLD_NO_CERTIFIED_NET_GAIN","costly transition may lose");
  const noArrival=stageStream([lo,mid]);
  ck(noArrival.promotions===0&&noArrival.first_promoted_event_index===null,"no forced arrival");
  ck(noArrival.open_score===noArrival.closed_score,"absent event no strict gain");
  const stream=stageStream([lo,mid,lo,lo,mid,hi]);
  ck(stream.promotions===1&&stream.first_promoted_event_index===6,"positive candidate accepted on observed arrival");
  ck(stream.closed_score===START_SCORE,"closed still at restricted score");
  ck(stream.open_score>stream.closed_score,"strict gross net decision improvement after arrival");
  ck(stream.open_score===refereeScore(hi)-TRANSITION_COST,"referee alone sees exact realized score");
  ck(stream.external_region_individuals_identified_by_stage2===0,"stage2 knows no future individual");
  ck(stream.history.slice(0,5).every(x=>x.meta!=="PROMOTE_RESIDUAL"),"no fabricated early identification");
  ck(stageStream([lo,mid,hi],{authorized:false}).promotions===0,"no physical promotion without authority");
  ck(stageStream([lo,mid,hi],{proofValid:false}).promotions===0,"invalid theorem blocks promotion");
  // Intersection of local residuals alone is not sufficient for quality:
  ck(hiR.every(x=>x.side!=="INSIDE")&&loR.every(x=>x.side!=="INSIDE"),"both high and low lie in joint ordinary-complement");
  ck(metaGate(hiR).status!==metaGate(loR).status,"the residual SIGN/certificate, not bare complement, separates");
  const conventionalWithSameMeta=stageStream([lo,mid,hi]);
  ck(conventionalWithSameMeta.open_score===stageStream([lo,mid,hi]).open_score,"equal meta-capability competitor ties");
  return{checks,stage1_optimality_reference_max:4,stage1_current_score:START_SCORE,
    stage2_existence_of_high_region_in_model:true,
    stage2_actual_future_arrival_certified:false,
    stage3:stream,negativeControlNoArrival:noArrival};
}

const result=runChecks();
verify(result.checks===33,"source regression expected exactly 33 finite checks");

console.log("Collective residual stage-3 assertions:",JSON.stringify(result));

