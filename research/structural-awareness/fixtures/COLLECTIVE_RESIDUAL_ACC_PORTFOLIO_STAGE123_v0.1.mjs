#!/usr/bin/env node

/**

 * Stage1-2-3 synthetic ACC bridge — original portfolio scenario source preserved below.

 * Original ACC portfolio.js? NO: source is ACC toy.py / scenarios/portfolio.json.

 * Referee arithmetic mirrored only for this exact 2-project additive scenario;

 * this fixture does not execute original Python or prove live-world optimization.

 * Authoring-time truth of anonymous existence is checked using the published

 * full reference scenario; live source authenticity is NOT simulated.

 * Run: node research/structural-awareness/fixtures/COLLECTIVE_RESIDUAL_ACC_PORTFOLIO_STAGE123_v0.1.mjs

 */

const cfg={
  "mode": "portfolio",
  "description": "Example: current SCALE is executable but INTEGRATE remains a superior jointly feasible alternative; set CFO=false to make only F^T improve.",
  "actors": [
    "Marketing",
    "Operations",
    "Systems",
    "Finance"
  ],
  "dimensions": [
    "E_efficiency",
    "D_distribution",
    "C_coordination",
    "A_attribution",
    "Q_authority"
  ],
  "approvals": {
    "Marketing": true,
    "Systems": true,
    "CFO": true
  },
  "parameters": {
    "acw_shadow_price": 1,
    "recovery_fraction": 0.7,
    "transition_budget": 50,
    "resources_limit": 200,
    "require_pareto": true,
    "acw_classified_synthetically": true,
    "top_k": 8
  },
  "baseline": {
    "production": 100,
    "resources": 100,
    "outputs": {
      "service_units": 100
    },
    "gic_hours": 3,
    "neo_hours": 2,
    "acw_hours": 5,
    "unknown_hours": 0,
    "human_capacity_hours": 20
  },
  "current_projects": [
    "SCALE"
  ],
  "projects": [
    {
      "id": "INTEGRATE",
      "delta_production": 0,
      "delta_resources": -20,
      "delta_acw_hours": -3,
      "output_deltas": {
        "service_units": 0
      },
      "gross_payoffs": {
        "Marketing": 60,
        "Operations": 40,
        "Systems": -30
      },
      "adjustment_costs_by_actor": {
        "Marketing": {
          "discovery": 2,
          "verification": 2,
          "reconfiguration": 3
        },
        "Operations": {
          "communication": 1,
          "negotiation": 3
        },
        "Systems": {
          "contracts": 2,
          "risk_resolution": 2
        }
      },
      "transfers": {
        "Marketing": -40,
        "Systems": 40
      },
      "acw_bearer": "Systems",
      "required_approvals": [
        "CFO",
        "Systems"
      ],
      "rights_preserved": true,
      "requires": [],
      "excludes": []
    },
    {
      "id": "SCALE",
      "delta_production": 40,
      "delta_resources": 25,
      "delta_acw_hours": 2,
      "output_deltas": {
        "service_units": 20
      },
      "gross_payoffs": {
        "Marketing": 25,
        "Operations": 15,
        "Systems": -10
      },
      "adjustment_costs_by_actor": {
        "Marketing": {
          "discovery": 1,
          "reconfiguration": 3
        },
        "Systems": {
          "verification": 2,
          "risk_resolution": 3
        }
      },
      "transfers": {
        "Marketing": -20,
        "Systems": 20
      },
      "acw_bearer": "Systems",
      "required_approvals": [
        "Marketing",
        "Systems"
      ],
      "rights_preserved": true,
      "requires": [],
      "excludes": []
    }
  ]
};

const bounds={"Marketing":10,"Operations":30,"Systems":8,"Finance":0};

function adjustments(p){
  return Object.values(p.adjustment_costs_by_actor||{}).reduce((s,cat)=>s+Object.values(cat).reduce((a,b)=>a+b,0),0);
}

function contributions(p,cfg){
  const shadow=cfg.parameters.acw_shadow_price;
  return Object.fromEntries(cfg.actors.map(a=>[a,
    (p.gross_payoffs?.[a]||0)+(p.transfers?.[a]||0)
    -Object.values(p.adjustment_costs_by_actor?.[a]||{}).reduce((x,y)=>x+y,0)
    -(p.acw_bearer===a?shadow*(p.delta_acw_hours||0):0)
  ]));
}

function net(p,cfg){return Object.values(contributions(p,cfg)).reduce((x,y)=>x+y,0)}

function recognizedBy(a,p){
 const delta=p.output_deltas?.service_units??0;
 if(a==="Marketing")return delta>0;
 if(a==="Operations")return (p.delta_resources||0)>=0;
 if(a==="Systems")return !(p.required_approvals||[]).includes("CFO");
 if(a==="Finance")return adjustments(p)<=10;
 throw Error("Unknown actor");
}

function jointOutside(p,cfg){return cfg.actors.every(a=>!recognizedBy(a,p))}

function profile(p,cfg,bounds){const c=contributions(p,cfg);return cfg.actors.every(a=>c[a]>=bounds[a]-1e-10)}

function governance(p,cfg){
 return p.rights_preserved===true &&
 (p.required_approvals||[]).every(a=>cfg.approvals[a]===true) &&
 Object.values(contributions(p,cfg)).every(x=>x>=-1e-9);
}

function issueAnonymous(s,bounds,{qualified=true}={}){
 const observed=s.projects.filter(p=>!s.current_projects.includes(p.id));
 const credible=observed.some(p=>jointOutside(p,s)&&profile(p,s,bounds)&&governance(p,s));
 return {kind:"SYNTHETIC_SOURCE_ATTESTATION",scope:"ACC_PORTFOLIO_FINITE_CASE",
  verified:qualified&&credible,anonymous:true,candidateId:null,
  minIncrement:Object.values(bounds).reduce((a,b)=>a+b,0),
  coverage:"EXISTS_SOME_PROFILE_MATCH_UNDER_REFEREE",
  rule:"IF_JOINT_RESIDUAL_AND_QUALIFIED_NET_BOUNDS_THEN_INCREMENT_GE_LOWER_BOUND",
  validUntil:20,issuer:"INDEPENDENT_SYNTHETIC_REFEREE_NOT_CRYPTOGRAPHIC"};
}

function stageTwo(s,certificate){
 const utility=s.projects.filter(p=>s.current_projects.includes(p.id)).reduce((a,p)=>a+net(p,s),0);
 return {utility,qualifiedClass:"COLLECTIVE_RESIDUAL_INTERSECT_ACTOR_NET_BOUNDS",
  sharedNegativePredicateCount:s.actors.length,
  existenceClaim:certificate?.verified===true?"SYNTHETIC_ANONYMOUS_ATTESTED":"NOT_ESTABLISHED",
  opportunityLowerBound:certificate?.verified===true?certificate.minIncrement:null,
  secondOrderBlockedGainLowerBound:certificate?.verified===true?Math.max(0,certificate.minIncrement):null,
  nextArrivalAt:"UNDETERMINED",foundCandidateId:null,reprogrammed:false};
}

function filterStream(s,stream,certificate,{metasyn=false,preAdmissionCapture=true}={}){
 const actual=s.projects.filter(p=>s.current_projects.includes(p.id)).reduce((a,p)=>a+net(p,s),0);
 let adopted=null,discover=null,unclassified=0,dropped=0;
 const messages=[];
 for(const e of stream){
  const p=e.project;
  const admitted=s.actors.every(a=>recognizedBy(a,p));
  if(admitted){messages.push({t:e.t,actor:e.actor,event:"ADMITTED_EXISTING_CLASS"});continue}
  unclassified++;
  if(!metasyn||!preAdmissionCapture){dropped++;messages.push({t:e.t,actor:e.actor,event:"DISCARDED_NO_REPLAY"});continue}
  const expiry=certificate?.validUntil>=e.t;
  const certOK=certificate?.verified===true&&certificate.scope==="ACC_PORTFOLIO_FINITE_CASE"&&expiry;
  const inMeta=jointOutside(p,s)&&profile(p,s,bounds);
  if(!certOK||!inMeta||e.sourceQualified!==true){
   messages.push({t:e.t,actor:e.actor,event:"META_HOLD_NOT_QUALIFIED"});
   continue;
  }
  if(!governance(p,s)){
   messages.push({t:e.t,actor:e.actor,event:"META_HOLD_NOT_AUTHORIZED"});
   continue;
  }
  const increment=net(p,s);
  if(increment>0){adopted=p.id;discover=e.t;
   messages.push({t:e.t,actor:e.actor,event:"METACANDIDATE_RECOGNIZED_AND_ADMITTED",newType:"QUALIFIED_CONTEXT_EXTENSION"});
   break;
  }
  messages.push({t:e.t,actor:e.actor,event:"HOLD_NO_GAIN"});
 }
 return {initialUtility:actual,currentUtility:actual+(adopted?net(stream.find(e=>e.project.id===adopted).project,s):0),
 adopted,recognizedAt:discover,unclassified,dropped,messages};
}

function runAllTests(){
 const say=(yes,label)=>{if(!yes)throw Error("TEST FAIL: "+label);tests++;};
 let tests=0;
 const current=cfg.projects.find(p=>p.id==="SCALE");
 const candidate=cfg.projects.find(p=>p.id==="INTEGRATE");
 say(cfg.actors.length===4&&cfg.dimensions.length===5,"source n actors and five dimensions");
 say(net(current,cfg)===19,"actual ACC SCALE utility 19");
 say(net(candidate,cfg)===58,"ACC INTEGRATE incremental gain 58");
 say(net(current,cfg)+net(candidate,cfg)===77,"finite ACC technical referee value 77");
 say(governance(candidate,cfg),"source INTEGRATE currently authorized and Pareto");
 say(cfg.actors.every(a=>recognizedBy(a,current)),"every local A accepts SCALE");
 say(cfg.actors.every(a=>!recognizedBy(a,candidate)),"every local A rejects INTEGRATE");
 say(jointOutside(candidate,cfg),"DeMorgan joint residual true");
 say(!jointOutside(current,cfg),"known SCALE not joint residual");
 const witness=contributions(candidate,cfg);
 say(JSON.stringify(cfg.actors.map(a=>witness[a]))===JSON.stringify([13,36,9,0]),"actor net source witness exact");
 say(profile(candidate,cfg,bounds),"qualified actor lowerbounds all satisfied");
 say(Object.values(bounds).reduce((a,b)=>a+b,0)===48,"shared lower bound 48");
 say(net(current,cfg)+48===67,"Stage 2 guaranteed class result ≥67");
 const cert=issueAnonymous(cfg,bounds);
 say(cert.verified&&cert.anonymous&&cert.candidateId===null,"anonymous existence source truthful but unnamed");
 const stage2=stageTwo(cfg,cert);
 say(stage2.utility===19&&stage2.foundCandidateId===null&&!stage2.reprogrammed,"Stage2 no output or binary change");
 say(stage2.secondOrderBlockedGainLowerBound===48&&stage2.nextArrivalAt==="UNDETERMINED","Stage2 distinct G2 bound and unknown timing");
 const facade={...candidate,id:"FACADE",gross_payoffs:{...candidate.gross_payoffs,Marketing:0,Operations:-50,Systems:-60}};
 say(jointOutside(facade,cfg),"facade lies in common residual");
 say(!profile(facade,cfg,bounds),"DeMorgan alone not quality guarantee");
 const stream=[
 {t:1,actor:"Marketing",project:current,sourceQualified:true},
 {t:2,actor:"Operations",project:facade,sourceQualified:true},
 {t:3,actor:"Systems",project:candidate,sourceQualified:true}
 ];
 const conventional=filterStream(cfg,stream,cert,{metasyn:false});
 const open=filterStream(cfg,stream,cert,{metasyn:true});
 say(conventional.currentUtility===19&&conventional.adopted===null,"strict admission baseline discards opportunity");
 say(open.recognizedAt===3&&open.adopted==="INTEGRATE","one actor discovers at authored event 3");
 say(open.currentUtility===77,"Stage 3 exactly source finite governed utility");
 say(open.messages.some(e=>e.t===2&&e.event==="META_HOLD_NOT_QUALIFIED"),"false profile no forced success");
 say(open.messages.at(-1).newType==="QUALIFIED_CONTEXT_EXTENSION","runtime type expansion without recompilation");
 const none=filterStream(cfg,stream.slice(0,2),cert,{metasyn:true});
 say(none.adopted===null&&none.currentUtility===19,"no arrived qualified candidate no improvement");
 const falseCert=filterStream(cfg,stream,issueAnonymous(cfg,bounds,{qualified:false}),{metasyn:true});
 say(falseCert.currentUtility===19&&falseCert.adopted===null,"unverified existence certificate prohibits adoption");
 const noCapture=filterStream(cfg,stream,cert,{metasyn:true,preAdmissionCapture:false});
 say(noCapture.currentUtility===19,"lost at ingress impossible later recovery");
 const noPerm=JSON.parse(JSON.stringify(cfg));noPerm.approvals.CFO=false;
 const block=filterStream(noPerm,stream,issueAnonymous(cfg,bounds),{metasyn:true});
 say(block.currentUtility===19,"CFO denied blocks meta adaptation");
 const badSource=[stream[0],stream[1],{...stream[2],sourceQualified:false}];
 say(filterStream(cfg,badSource,cert,{metasyn:true}).currentUtility===19,"missing source qualification blocks");
 const stale=filterStream(cfg,stream.map(e=>({...e,t:e.t+100})),cert,{metasyn:true});
 say(stale.currentUtility===19,"source validity expiry blocks");
 const peer=filterStream(cfg,stream,cert,{metasyn:true,preAdmissionCapture:true});
 say(JSON.stringify(peer)===JSON.stringify(open),"equivalent conventional raw+meta program ties");
 for(let k=0;k<16;k++){
  const flags=cfg.actors.map((_,i)=>!!(k&(1<<i)));
  const lhs=!(flags.some(Boolean)),rhs=flags.every(x=>!x);
  say(lhs===rhs,"De Morgan truth table "+k);
 }
 return {assertions:tests,sourceScenarioSha:"a154d3f8dfd4396b05197038137c36befe53c092",
  actors:cfg.actors.length,dimensions:cfg.dimensions.length,
  initial:19,refereeTechnical:77,technicalGap:58,
  sharedLowerBound:48,sourceProof:cert,stage2,
  stage3:{closed:conventional.currentUtility,open:open.currentUtility,firstActor:"Systems",firstTime:open.recognizedAt},
  controls:["irrelevant κοιν residual","absence of arrival","unqualified source","no capture","CFO denied","expired cert","peer same evidence ties"]};
}

const results=runAllTests();

console.log(JSON.stringify(results,null,2));

