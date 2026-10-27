#!/usr/bin/env node

/**

 * SA-MATH-TR-01 consolidated v1.0 universal-open-frame fixture.

 * 128 finite-frame subsets tested as bounded representatives in N.

 * Model assumes the natural numbers are infinite; this is NOT a proof

 * that a physical environment is infinite or contains another agent.

 * Russell-type contradiction is carried only as attributed proof data.

 * Run: node research/structural-awareness/fixtures/UNIVERSAL_FRAME_OPENNESS_AND_TYPED_META_REPORT_v0.1.mjs

 */

function assertUniversal(value, message){if(!value)throw Error("FAIL: "+message);}

function frameFromMask(mask,max=7){return Array.from({length:max},(_,i)=>i).filter(i=>(mask>>i)&1);}

function naturalWitness(frame){return frame.length===0?0:Math.max(...frame)+1;}

function semanticWorld(hasPeer){
  return {domain:"NONNEGATIVE_INTEGERS",
    peerRule:hasPeer?"PEER_AT_42":"NO_PEERS",
    sensorInterface:"KNOWN_COMPATIBLE_AGENT_ONLY"};
}

function peerObserved(world,finiteFrame){return finiteFrame.filter(n=>world.peerRule==="PEER_AT_42"&&n===42);}

function reportUniversal(frame,observed,modelCertificate){
  const justified=!!modelCertificate&&modelCertificate.model==="NONNEGATIVE_INTEGERS"&&modelCertificate.qualified===true&&modelCertificate.proof==="INFINITE_DOMAIN";
  const result={
    object:{admittedFrame:[...frame],qualifiedPeers:[...observed]},
    meta:{
      schema:"FOR_EVERY_ADMISSIBLE_FINITE_FRAME_EXISTS_EXTERIOR",
      instanceStatus:justified?"EXTERIOR_EXISTS_IN_MODEL":"UNDETERMINED",
      outsidePeerExists:"UNDETERMINED",
      outsideCommunicable:"UNDETERMINED",
      sensorFault:"NOT_ESTABLISHED",
      possibleDesignReview:"REVIEW_REPRESENTATIONAL_SCOPE"
    }
  };
  return result;
}

function checkedMetaContradiction(proof1,proof2){
  const valid=p=>p?.theoryId==="NAIVE_COMPREHENSION"&&p?.valid===true&&
    ["P","NOT_P"].includes(p.proves);
  if(valid(proof1)&&valid(proof2)&&
     new Set([proof1.proves,proof2.proves]).size===2){
    return {hostFacts:["OBJECT_THEORY_INCONSISTENT"],
      attributedTo:"NAIVE_COMPREHENSION",
      hostAssertsP:false,
      hostAssertsNotP:false,
      hostArbitraryQ:false};
  }
  return {hostFacts:["UNQUALIFIED_OBJECT_EVIDENCE"],hostArbitraryQ:false};
}

function universalChecks(){
  let passed=0;
  const ck=(x,n)=>{assertUniversal(x,n);passed++;};
  const cert={model:"NONNEGATIVE_INTEGERS",qualified:true,proof:"INFINITE_DOMAIN"};
  for(let mask=0;mask<(1<<7);mask++){
    const F=frameFromMask(mask),w=naturalWitness(F);
    ck(!F.includes(w),"finite-frame witness external");
    ck(reportUniversal(F,[],cert).meta.instanceStatus==="EXTERIOR_EXISTS_IN_MODEL","universal schema properly instantiated");
    ck(reportUniversal(F,[],cert).meta.outsidePeerExists==="UNDETERMINED","existence of exterior does not imply another peer");
    ck(reportUniversal(F,[],cert).meta.sensorFault==="NOT_ESTABLISHED","no sensor-fault inference from exterior");
  }
  const none=semanticWorld(false),extra=semanticWorld(true),F=[];
  ck(peerObserved(none,F).length===0&&peerObserved(extra,F).length===0,"same empty peer run despite different actual populations");
  ck(JSON.stringify(reportUniversal(F,peerObserved(none,F),cert))===JSON.stringify(reportUniversal(F,peerObserved(extra,F),cert)),"metasyntactic report independent of hidden peer truth");
  ck(reportUniversal(F,[],null).meta.instanceStatus==="UNDETERMINED","without universal premise no exterior assertion");
  ck(reportUniversal(F,[],{...cert,qualified:false}).meta.instanceStatus==="UNDETERMINED","unqualified infinite-domain certificate rejected");
  ck(reportUniversal(F,[],{...cert,model:"KNOWN_FINITE_DOMAIN"}).meta.instanceStatus==="UNDETERMINED","mismatched domain cannot derive exterior");
  ck(reportUniversal(F,[],cert).meta.outsideCommunicable==="UNDETERMINED","communication not implied");
  const isolated=checkedMetaContradiction(
    {theoryId:"NAIVE_COMPREHENSION",valid:true,proves:"P"},
    {theoryId:"NAIVE_COMPREHENSION",valid:true,proves:"NOT_P"}
  );
  ck(isolated.hostFacts.includes("OBJECT_THEORY_INCONSISTENT"),"finite proof pair yields object inconsistency report");
  ck(!isolated.hostAssertsP&&!isolated.hostAssertsNotP&&!isolated.hostArbitraryQ,"no explosion in separate host data model");
  const bad=checkedMetaContradiction({theoryId:"WRONG",valid:true,proves:"P"},
    {theoryId:"NAIVE_COMPREHENSION",valid:true,proves:"NOT_P"});
  ck(!bad.hostFacts.includes("OBJECT_THEORY_INCONSISTENT"),"wrong source attribution rejected");
  ck(!bad.hostArbitraryQ,"bad proof never grants arbitrary host conclusion");
  return {passed,frames:128,worldsCompared:2,objectContradictionCheck:"typed attribution only"};
}

const out=universalChecks();

console.log("Universal frame and no-explosion finite contract tests:",JSON.stringify(out));

