#!/usr/bin/env node

/**

 * TR-20/21/22 finite source/U/metasyntax comparison, authoring research fixture.

 * H_OUT/H_GROWTH/H_DETECT truths and authenticity are GIVEN prequalified premises.

 * This code does not authenticate those claims, discover a hidden peer or

 * simulate a universal truth oracle. The referee's actual-world variable

 * is accessible only in synthetic test assertions, not in agent reporting.

 * Run: node research/structural-awareness/fixtures/EXTERNAL_U_METASYNTACTIC_DIAGNOSTICS_v0.1.mjs

 */

function invariant(x,msg){if(!x)throw Error("CHECK FAILED: "+msg);}

function world({extra=false,detected=false}={}) {
  return {
    physicalRelevant:extra?["peer-in","peer-outer"]:["peer-in"],
    admittedU:detected?["peer-in"]:["peer-in"],
    qualifiedResults:["peer-in"],
    objectKernelTrace:["K_ADMIT","D_QUALIFY","V_VALIDATE"]
  };
}

function initSnapshot({admitted=[],results=[],elapsed=0}={}) {
  return {admitted:[...admitted],results:[...results],elapsed,
    kernelTrace:["K_INITIALIZE","D_PROCESS","V_REPORT"]};
}

function internalComplement(record){
  return record.admitted.filter(x=>!record.results.includes(x));
}

function closedReport(record){
 return {lang:"U_ONLY",
         admitted:[...record.admitted],
         found:[...record.results],
         inUResidual:internalComplement(record),
         trace:[...record.kernelTrace]};
}

function certifiedExterior(sourceCertificate, record){
  if(!sourceCertificate || sourceCertificate.verified!==true) return false;
  if(sourceCertificate.kind==="H_OUT" && sourceCertificate.targetScope===sourceCertificateScope(record)) return true;
  if(sourceCertificate.kind==="H_GROWTH" &&
     sourceCertificate.targetScope===sourceCertificateScope(record) &&
     sourceCertificate.admitsFinite===true && Array.isArray(record.admitted)) return true;
  return false;
}

function sourceCertificateScope(record){return record.targetScope||"zone-alpha";}

function qualifiedDeadlineViolation(contract,record){
 return contract?.verified===true
  &&contract?.kind==="H_DETECT"
  &&contract?.targetScope===sourceCertificateScope(record)
  &&contract?.preconditionsMet===true
  &&record.elapsed>=contract.deadline
  &&record.results.length<contract.minimumDetections;
}

function outsideAwareReport(record,{premise=null,detectContract=null}={}){
 const closed=closedReport(record);
 const proved=certifiedExterior(premise,record);
 const meta=[
   {kind:"OutsideQuestion",target:"q-relevant constituency outside initialized U",
      truthStatus:proved?"PROVED_EXISTENTIAL":"UNDETERMINED"},
   {kind:"OpenFrontier",status:"NOT_CERTIFIED_CLOSED"},
 ];
 if(proved)meta.push({kind:"ExternalExistenceCertificate",basis:premise.kind,source:premise.source,
  conclusion:"INITIAL_SCOPE_NOT_GLOBALLY_EXHAUSTIVE"});
 if(qualifiedDeadlineViolation(detectContract,record))meta.push({
  kind:"InitContractViolation",deadline:detectContract.deadline,
  conclusion:"DETECTION_CONTRACT_NOT_MET"
 });
 return {lang:"OPEN_A_PRIME",withinU:closed,meta,trace:[...record.kernelTrace]};
}

function seeTruth(world){ // test-only referee, never passed to either source reporter
  return world.physicalRelevant.some(x=>!world.admittedU.includes(x));
}

function checkAll() {
 let n=0;
 const ok=(x,msg)=>{invariant(x,msg);n++};
 const w0=world(),w1=world({extra:true});
 const r0=initSnapshot({admitted:["peer-in"],results:["peer-in"]});
 const r1=initSnapshot({admitted:["peer-in"],results:["peer-in"]});
 ok(JSON.stringify(closedReport(r0))===JSON.stringify(closedReport(r1)),"identical U-only observations");
 ok(internalComplement(r0).length===0,"U minus A empty");
 ok(seeTruth(w0)===false && seeTruth(w1)===true,"referee distinguishes actual unseen peer");
 ok(closedReport(r1).inUResidual.length===0&&seeTruth(w1),"in-U complement cannot discover external peer");
 const bare=outsideAwareReport(r0);
 ok(bare.meta[0].truthStatus==="UNDETERMINED","no source certificate implies only meta-question");
 ok(bare.meta[1].status==="NOT_CERTIFIED_CLOSED","open frontier remains without witness");
 ok(JSON.stringify(bare).includes("OutsideQuestion"),"typed meta AST exists");
 ok(JSON.stringify(bare.withinU)===JSON.stringify(closedReport(r0)),"in-U content recoverable");
 const h={verified:true,kind:"H_OUT",targetScope:"zone-alpha",source:"verified-world-assumption"};
 const rich=outsideAwareReport(r1,{premise:h});
 ok(rich.meta[0].truthStatus==="PROVED_EXISTENTIAL","H_OUT premise enables proved exterior existence");
 ok(rich.meta.some(x=>x.kind==="ExternalExistenceCertificate"),"external existence certificate reported");
 ok(!JSON.stringify(rich).includes("peer-outer"),"unknown individual remains unnamed");
 ok(JSON.stringify(rich.withinU)===JSON.stringify(closedReport(r1)),"same object kernel");
 ok(JSON.stringify(rich.trace)===JSON.stringify(r1.kernelTrace),"no changed execution kernel");
 ok(!("meta" in closedReport(r1)),"U-only language has no meta operator");
 const bogus={verified:false,kind:"H_OUT",targetScope:"zone-alpha",source:"not verified"};
 ok(outsideAwareReport(r1,{premise:bogus}).meta[0].truthStatus==="UNDETERMINED","unverified existence cannot be asserted");
 const mismatched={...h,targetScope:"different-zone"};
 ok(outsideAwareReport(r1,{premise:mismatched}).meta[0].truthStatus==="UNDETERMINED","certificate scope mismatch prevents assertion");
 const g={verified:true,kind:"H_GROWTH",targetScope:"zone-alpha",source:"axiomatized-unboundedness",admitsFinite:true};
 ok(outsideAwareReport(r1,{premise:g}).meta[0].truthStatus==="PROVED_EXISTENTIAL","H_GROWTH plus finite admitted U implies exterior");
 const zero=initSnapshot({admitted:[],results:[],elapsed:2});
 const e=outsideAwareReport(zero,{premise:h});
 ok(e.meta.some(x=>x.kind==="ExternalExistenceCertificate"),"no discovery refutes exhaustiveness under H_OUT");
 ok(!e.meta.some(x=>x.kind==="InitContractViolation"),"no detection guarantee means no inferred code fault");
 const reach={verified:true,kind:"H_REACH",targetScope:"zone-alpha",source:"eventually-accessible"};
 ok(outsideAwareReport(zero,{premise:reach}).meta[0].truthStatus==="UNDETERMINED","reachability without finite bound not enough");
 const detect={verified:true,kind:"H_DETECT",targetScope:"zone-alpha",
 deadline:1,minimumDetections:1,preconditionsMet:true};
 ok(outsideAwareReport(zero,{premise:h,detectContract:detect}).meta.some(x=>x.kind==="InitContractViolation"),"finite detection contract violation diagnosed");
 ok(!outsideAwareReport(initSnapshot({elapsed:0}),{premise:h,detectContract:detect}).meta.some(x=>x.kind==="InitContractViolation"),"before deadline no fault");
 ok(!outsideAwareReport(zero,{premise:h,detectContract:{...detect,preconditionsMet:false}}).meta.some(x=>x.kind==="InitContractViolation"),"unsatisfied detection preconditions prevent diagnosis");
 ok(!outsideAwareReport(zero,{premise:h,detectContract:{...detect,targetScope:"elsewhere"}}).meta.some(x=>x.kind==="InitContractViolation"),"unmatched contract scope prevents diagnosis");
 ok(!outsideAwareReport(initSnapshot({admitted:["peer-in"],results:["peer-in"],elapsed:2}),{premise:h,detectContract:detect}).meta.some(x=>x.kind==="InitContractViolation"),"successful obligated detection is compliant");
 ok(JSON.stringify(e.withinU.found)==="[]","zero run local result remains empty");
 ok(JSON.stringify(e.meta).length>JSON.stringify(closedReport(zero)).length/2,"additional meta data has nonzero transmission burden");
 ok(outsideAwareReport(r1,{premise:g}).meta[0].truthStatus===rich.meta[0].truthStatus,"two distinct external proof routes yield equivalent existential type");
 return {passed:n,notes:"Typed meta-constructor finite checks, not external-premise verification or actual agent operation"};
}

const result=checkAll();

console.log("TR20-22 external-U finite assertions:",JSON.stringify(result));

