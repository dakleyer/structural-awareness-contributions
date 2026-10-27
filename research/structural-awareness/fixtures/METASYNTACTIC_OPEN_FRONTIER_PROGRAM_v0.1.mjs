#!/usr/bin/env node
/**
 * TR-15/TR-16: executable metasyntactic reporting versus A-only output grammar.
 * Same object execution K/D/V, different report-construction code and types.
 * Fully synthetic model-checking fixture; no universal-semantic oracle.
 * Referee-only outer truth remains hidden from both reporting programmes.
 * Reproduce: node research/structural-awareness/fixtures/METASYNTACTIC_OPEN_FRONTIER_PROGRAM_v0.1.mjs
 */

function assert(condition, label) {
  if (!condition) throw new Error("FAIL " + label);
}

function makeWorld(outerRelevant, innerUnresolved=false) {
  return {
    inside:[
      {id:"peer-1", distance:8, eligible:true, status:"VERIFIED"},
      {id:"peer-2", distance:12, eligible:true, status:innerUnresolved?"UNKNOWN":"VERIFIED"}
    ],
    outside:[
      {id:"peer-outside", distance:4, eligible:outerRelevant, status:"UNOBSERVED"}
    ]
  };
}

function runObjectKernel(world) {
  const inside = world.inside.map(p=>({...p}));
  const eligible = inside.filter(p=>p.eligible && p.status==="VERIFIED")
                         .sort((x,y)=>x.distance-y.distance);
  return {
    instructionTrace:["K_SELECT_ADMITTED","D_EVALUATE_OBSERVED","V_QUALIFY"],
    scope:["peer-1","peer-2"],
    nearestObserved:eligible.length?eligible[0].id:null,
    outcomes:inside.map(p=>({id:p.id,status:p.status,distance:p.distance})),
    status:"FINISHED_ON_OBSERVED"
  };
}

function closeReport(kernelRecord) {
  return {
    lang:"L_A",
    terms:[
      {kind:"Result",value:kernelRecord.nearestObserved},
      {kind:"ObservedStatus",value:kernelRecord.status},
      ...kernelRecord.outcomes.map(x=>({kind:"ObservedStatus",id:x.id,value:x.status}))
    ],
    trace:kernelRecord.instructionTrace.slice()
  };
}

function reflect(kernelRecord, questionId="globally-closest-eligible-peer") {
  return [
    {
      kind:"OpenFrontier",
      programRef:"composed-K-D-V",
      questionRef:questionId,
      scopeRef:kernelRecord.scope,
      status:"NOT_CERTIFIED_CLOSED"
    },
    {
      kind:"OutsideQuestion",
      quantifier:"EXISTS",
      formula:{
        kind:"And",
        clauses:[
          {kind:"OutsideAdmittedScope",scopeRef:kernelRecord.scope},
          {kind:"WouldChangeNearestObserved",peerRef:kernelRecord.nearestObserved}
        ]
      },
      truthStatus:"UNDETERMINED"
    },
    {kind:"RoleFrontier",role:"B-prime",status:"OPEN"},
    {kind:"UnqualifiedRole",aspect:"unseen-task-relevant-effects",status:"UNCLASSIFIED"}
  ];
}

function openReport(kernelRecord) {
  const closed=closeReport(kernelRecord);
  return {
    lang:"L_A_PLUS",
    terms:closed.terms,
    metaTerms:reflect(kernelRecord),
    trace:closed.trace
  };
}

function typecheckInside(node) {
  if (!["Result","ObservedStatus"].includes(node.kind)) throw new Error("REJECT_OUTSIDE_LANGUAGE");
  return true;
}

function typecheckOpen(node) {
  if(["Result","ObservedStatus"].includes(node.kind))return true;
  if(["OpenFrontier","OutsideQuestion","RoleFrontier","UnqualifiedRole"].includes(node.kind))return true;
  throw new Error("UNSUPPORTED_META_TERM");
}

function sourceRefereeOutsideWouldChange(world) {
  const inside=runObjectKernel(world).nearestObserved;
  const distance=world.inside.find(p=>p.id===inside)?.distance;
  return world.outside.some(p=>p.eligible&&p.distance<distance);
}

function simpleSyntacticTagger(node) {
  return ["ACK","NACK","TIMEOUT"].includes(node.type)?node.type:"UNCLASSIFIED";
}

function runChecks() {
  let checks=0;
  const ok=(condition,label)=>{assert(condition,label);checks++};
  const w0=makeWorld(false),w1=makeWorld(true),w2=makeWorld(true,true);
  const core0=runObjectKernel(w0),core1=runObjectKernel(w1),core2=runObjectKernel(w2);
  ok(JSON.stringify(core0)===JSON.stringify(core1),"core kernel observational equality");
  ok(core0.nearestObserved==="peer-1","same observed nearest");
  ok(sourceRefereeOutsideWouldChange(w0)===false,"qualified synthetic outer negative");
  ok(sourceRefereeOutsideWouldChange(w1)===true,"qualified synthetic outer positive");
  ok(JSON.stringify(closeReport(core0))===JSON.stringify(closeReport(core1)),"closed reports cannot distinguish outer");
  ok(JSON.stringify(openReport(core0).trace)===JSON.stringify(closeReport(core0).trace),"open and closed same kernel steps");
  ok(JSON.stringify(openReport(core0).terms)===JSON.stringify(closeReport(core0).terms),"all inner results preserved");
  ok(openReport(core0).metaTerms.some(n=>n.kind==="OpenFrontier"&&n.status==="NOT_CERTIFIED_CLOSED"),"meta program actually creates frontier tag");
  ok(openReport(core0).metaTerms.some(n=>n.kind==="OutsideQuestion"&&n.truthStatus==="UNDETERMINED"),"meta program actually creates question AST");
  ok(openReport(core0).metaTerms.every(typecheckOpen),"metasyntactic terms are well-typed in extended grammar");
  ok(closeReport(core0).terms.every(typecheckInside),"closed inside terms well typed");
  let rejected=false;
  try{typecheckInside(openReport(core0).metaTerms.find(n=>n.kind==="OutsideQuestion"));}catch(e){rejected=e.message==="REJECT_OUTSIDE_LANGUAGE";}
  ok(rejected,"closed typed grammar rejects external question");
  ok(!("metaTerms" in closeReport(core0)),"closed only cannot export external type");
  ok(!JSON.stringify(openReport(core1)).includes("peer-outside"),"open references exterior without discovering identity");
  ok(JSON.stringify(openReport(core0))===JSON.stringify(openReport(core1)),"meta AST is not hidden-world truth oracle");
  ok(core2.outcomes.some(x=>x.status==="UNKNOWN"),"kernel can record observed UNKNOWN");
  ok(openReport(core2).terms.some(x=>x.value==="UNKNOWN"),"open preserves observed UNKNOWN");
  ok(closeReport(core2).terms.some(x=>x.value==="UNKNOWN"),"closed comparator may also preserve observed UNKNOWN");
  ok(simpleSyntacticTagger({type:"unknown-of-unknown"})==="UNCLASSIFIED","catch-all does not semantically auto-classify novelty");
  ok(openReport(core2).metaTerms.some(x=>x.kind==="RoleFrontier"&&x.role==="B-prime"),"B-prime open qualifier");
  ok(reflect(core0)[0].scopeRef.length===2,"typed metaschema captures declared scope");
  ok(openReport(core1).lang==="L_A_PLUS"&&closeReport(core1).lang==="L_A","reporting programmes have different effective contracts");
  ok(openReport.toString()!==closeReport.toString(),"reporters are distinct source programmes");
  ok(openReport(core0).metaTerms.length===4,"finite metasignal constructible without enumeration of outside");
  return checks;
}

const passed=runChecks();
console.log("TR-15/16 finite fixture assertions passed:",passed);
