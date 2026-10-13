import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
const ROOT=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const stable=x=>Array.isArray(x)?x.map(stable):x&&typeof x==='object'?Object.fromEntries(Object.keys(x).sort().map(k=>[k,stable(x[k])])):x;
export const hash=x=>crypto.createHash('sha256').update(JSON.stringify(stable(x))).digest('hex');
const copy=x=>structuredClone(x);
const expected={ 'UC17-01':'permit','UC17-02':'permit','UC17-03':'remediate','UC17-04':'remediate','UC17-05':'block','UC17-06':'escalate','UC17-07':'indeterminate','UC17-09':'remediate' };
const LABELS=['J1','J2','J3','J4','J5','J6'];
// Public authored deterministic example, NOT source generate.py or native output.
// Scripted patterns are illustrative of the published gross mechanism.
// No roles, hidden truth, or sealed source key are delivered to the detector.
export function sampleVotes(){
 return Object.fromEntries(Object.entries(expected).map(([c,v])=>[c,Object.fromEntries(LABELS.map((j,i)=>{
 let out=v;
 if(c==='UC17-02'&&i<4)out='remediate';
 if(i===5&&['UC17-03','UC17-04','UC17-05','UC17-06','UC17-09'].includes(c))out='permit';
 return [j,out];
 }))]));
}
export function nativeRuleProxy(votes){
 const counts=Object.fromEntries(LABELS.map(j=>[j,0]));
 for(const row of Object.values(votes)){
  for(const j of LABELS){
   const freq=new Map();
   for(const k of LABELS)if(k!==j)freq.set(row[k],(freq.get(row[k])||0)+1);
   const majority=[...freq].find(([,n])=>n>=3);
   if(majority&&row[j]!==majority[0])counts[j]++;
  }
 }
 return {evidence_mode:'AUTHOR_SYNTHETIC_RULE_PROXY_NOT_NATIVE_RUN',rounds:1,
 counts,flags:LABELS.filter(j=>counts[j]>2.1186),context_qualification:'NOT_ASSESSED'};
}
function witness(epoch,value='permit',subject='decisionA',source='context-source-1'){
 const payload={epoch,value,subject,source,reference:'SYNTHETIC-CONTEXT-REFERENCE-1',validFrom:0,validUntil:100};
 return {...payload,commitment:hash(payload)};
}
const AUTHORIZED=new Set(['context-source-1','context-source-2']);
function payloadOf(r){const {commitment,...payload}=r;return payload;}
export function packet(){
 return {schema:'AUTHOR_SYNTHETIC_CONTEXT_1',evidence_mode:'AUTHOR_SYNTHETIC_NOT_NATIVE',
 target:'decisionA',claimedValue:'permit',currentEpoch:'e0',now:10,
 votes:sampleVotes(),receipts:[witness('e0')],displayNote:'ordinary',
 history:[{at:0,epoch:'e0',subject:'decisionA'}]};
}
// Conventional direct validity joins. Source authority is a stipulated fixture,
// not cryptographic authentication or an independent factual judgment.
export function strongB2(p){
 const good=p.receipts.filter(r=>AUTHORIZED.has(r.source)&&r.subject===p.target
 &&r.reference==='SYNTHETIC-CONTEXT-REFERENCE-1'&&r.epoch===p.currentEpoch
 &&r.validFrom<=p.now&&p.now<r.validUntil&&r.commitment===hash(payloadOf(r)));
 const values=[...new Set(good.map(r=>r.value))];
 if(values.length!==1)return {status:'NOT_ESTABLISHED',identifiable:false,affected:[p.target],
 reason:values.length?'conflicting eligible source values':'no current eligible source witness',sourceResultPreserved:true};
 return {status:values[0]===p.claimedValue?'SUPPORTED':'REFUTED',identifiable:true,affected:[p.target],
 reason:'current eligible source witness',sourceResultPreserved:true};
}
// Candidate requirement reference model: finite possible-world filtering.
// This is a conventional finite constraint enumerator, NOT an EA implementation.
export function requirementReference(p){
 let worlds=['permit','block'].map(value=>({epoch:p.currentEpoch,value}));
 const eligible=[];
 for(const r of p.receipts){
  if(!AUTHORIZED.has(r.source))continue;
  if(r.subject!==p.target||r.reference!=='SYNTHETIC-CONTEXT-REFERENCE-1')continue;
  if(r.epoch!==p.currentEpoch||p.now<r.validFrom||p.now>=r.validUntil)continue;
  if(hash(payloadOf(r))!==r.commitment)continue;
  eligible.push(r);
 }
 if(eligible.length){
  for(const r of eligible)worlds=worlds.filter(w=>w.value===r.value);
 }
 const values=[...new Set(worlds.map(w=>w.value))];
 if(values.length!==1)return {status:'NOT_ESTABLISHED',identifiable:false,affected:[p.target],
 reason:worlds.length?'multiple compatible current-context worlds':'inconsistent source constraints',
 sourceResultPreserved:true};
 return {status:values[0]===p.claimedValue?'SUPPORTED':'REFUTED',identifiable:true,affected:[p.target],
 reason:'single compatible current-context value',sourceResultPreserved:true};
}
function run(){
 const cases=[];
 const add=(id,description,mutate,want)=>{const p=packet();mutate(p);cases.push({id,description,p,want});};
 add('K00','t0 valid current-context witness',()=>{},'SUPPORTED');
 add('K01','benign display change',p=>p.displayNote='changed decoration','SUPPORTED');
 add('K02','t1 epoch changes and current witness is absent',p=>p.currentEpoch='e1','NOT_ESTABLISHED');
 add('K03','t2 same epoch legitimate current witness supplied',p=>{p.currentEpoch='e1';p.receipts.push(witness('e1'));p.history.push({at:10,epoch:'e1',subject:'decisionA'});},'SUPPORTED');
 add('K04','witness withdrawn without any replacement',p=>p.receipts=[],'NOT_ESTABLISHED');
 add('K05','alternate legitimate source preserves support',p=>p.receipts=[witness('e0','permit','decisionA','context-source-2')],'SUPPORTED');
 add('K06','wrong subject cannot establish target',p=>p.receipts=[witness('e0','permit','decisionB')],'NOT_ESTABLISHED');
 add('K07','untrusted author cannot establish target',p=>p.receipts=[witness('e0','permit','decisionA','untrusted')],'NOT_ESTABLISHED');
 add('K08','same source copied does not become another truth',p=>p.receipts.push(copy(p.receipts[0])),'SUPPORTED');
 add('K09','material payload tampering without new digest',p=>p.receipts[0].value='block','NOT_ESTABLISHED');
 add('K10','properly bound contrary current source refutes receiving claim',p=>p.receipts=[witness('e0','block')],'REFUTED');
 add('K11','conflicting legitimate source preserves indeterminacy',p=>p.receipts.push(witness('e0','block','decisionA','context-source-2')),'NOT_ESTABLISHED');
 add('K12','expiry boundary cannot retain old support',p=>p.now=100,'NOT_ESTABLISHED');
 add('K13','future source witness not yet eligible',p=>{const r=witness('e0');r.validFrom=11;r.commitment=hash(payloadOf(r));p.receipts=[r];},'NOT_ESTABLISHED');
 add('K14','wrong reference cannot support target',p=>{p.receipts[0].reference='OTHER';p.receipts[0].commitment=hash(payloadOf(p.receipts[0]));},'NOT_ESTABLISHED');
 add('K15','independence decoration cannot establish absent witness',p=>{p.currentEpoch='e1';p.independence='independent';},'NOT_ESTABLISHED');
 add('K16','replayed earlier witness stays historical',p=>{p.currentEpoch='e1';p.receipts.push(copy(p.receipts[0]));},'NOT_ESTABLISHED');
 add('K17','material loss limited to decisionA leaves decisionB valid',p=>{p.currentEpoch='e1';p.receipts.push(witness('e1','permit','decisionB'));},'NOT_ESTABLISHED');
 add('K18','valid baseline at final pre-expiry instant',p=>p.now=99,'SUPPORTED');
 add('K19','receipt observation order is immaterial',p=>{p.receipts=[witness('e0','permit','decisionA','context-source-2'),witness('e0')];p.receipts.reverse();},'SUPPORTED');
 const native=hash(nativeRuleProxy(sampleVotes()));
 const rows=cases.map(c=>{
  const b=strongB2(c.p),e=requirementReference(c.p),n=nativeRuleProxy(c.p.votes);
  assert.equal(b.status,c.want,c.id+' B2');assert.equal(e.status,c.want,c.id+' reference');
  assert.equal(b.identifiable,e.identifiable,c.id+' identification parity');
  assert.equal(hash(n),native,c.id+' native proxy invariant');
  assert.deepEqual(Object.keys(c.p.votes),Object.keys(expected),'eight scored cases preserved');
  return {id:c.id,description:c.description,expected:c.want,B2:b,reference:e,native:n,
   visiblePacketSha256:hash(c.p),voteSha256:hash(c.p.votes),packet:c.p};
 });
 // Distinct hidden truths, byte-identical complete candidate packet.
 // World truth is kept outside packet and never passed to either monitor.
 const nullPairs=[];
 for(let bits=0;bits<64;bits++){
  const p=packet();p.currentEpoch='e1';p.receipts=[];
  p.votes['UC17-01']=Object.fromEntries(LABELS.map((j,i)=>[j,((bits>>i)&1)?'permit':'block']));
  const w0={packet:copy(p),oracleOnly:{currentTruth:'permit'}};
  const w1={packet:copy(p),oracleOnly:{currentTruth:'block'}};
  assert.notEqual(w0.oracleOnly.currentTruth,w1.oracleOnly.currentTruth);
  assert.equal(hash(w0.packet),hash(w1.packet));
  for(const f of [nativeRuleProxy]){
   assert.deepEqual(f(w0.packet.votes),f(w1.packet.votes));
  }
  for(const f of [strongB2,requirementReference]){
   assert.deepEqual(f(w0.packet),f(w1.packet));
   assert.equal(f(w0.packet).status,'NOT_ESTABLISHED');
  }
  nullPairs.push({pair:bits,truth0:w0.oracleOnly.currentTruth,truth1:w1.oracleOnly.currentTruth,
   visibleHash:hash(p),native:nativeRuleProxy(p.votes),B2:strongB2(p),reference:requirementReference(p)});
 }
 // Alternate recovery and affected/unaffected continuity are actually exercised.
 const impacted=copy(cases.find(c=>c.id==='K17').p);
 const unaffected=copy(impacted);unaffected.target='decisionB';
 assert.equal(strongB2(unaffected).status,'SUPPORTED');
 assert.equal(requirementReference(unaffected).status,'SUPPORTED');
 const baseline=rows.find(x=>x.id==='K00'),loss=rows.find(x=>x.id==='K02'),recovery=rows.find(x=>x.id==='K03');
 assert.notEqual(baseline.visiblePacketSha256,loss.visiblePacketSha256);
 assert.equal(baseline.voteSha256,loss.voteSha256);
 assert.equal(loss.voteSha256,recovery.voteSha256);
 const summary={
 schema:'FLORES_RUNTIME_CONTEXT_AUTHOR_PREFLIGHT_0.1',
 evidence_mode:'AUTHOR_SYNTHETIC_FINITE_MODEL_AND_RULE_PROXY',
 source_native_run:false,EA_implementation:false,blind_campaign:false,independent_adjudication:false,
 named_controls:rows.length,hidden_truth_pair_controls:nullPairs.length,
 control_result:'PASS_IN_DECLARED_FINITE_MODEL',
 reference_vs_strong_B2:'20_OF_20_STATUS_PARITY_NOT_A_SCIENTIFIC_DIFFERENTIAL',
 native_proxy_context_assessment:'NOT_ASSESSED',
 source_native_accuracy_or_independence:'NOT_ESTABLISHED',
 identifier_warning:'K labels identify public calibration fixtures and must not be used as blinded campaign inputs',
 unaffected_decision_control:'PASS',
 null_pair_truth_distinct:true,null_pair_complete_visible_packets_identical:true,
 core_timeline:{t0:'SUPPORTED',t1:'NOT_ESTABLISHED',t2:'SUPPORTED',sameVotes:true},
 controls:rows,null_pairs:nullPairs
 };
 fs.mkdirSync(path.join(ROOT,'preflight'),{recursive:true});
 fs.writeFileSync(path.join(ROOT,'preflight','RESULTS_2026-10-13.json'),JSON.stringify(summary,null,2)+'\n');
 fs.writeFileSync(path.join(ROOT,'preflight','CONTROL_MATRIX_2026-10-13.csv'),
 'id,expected,B2,reference,native_context,visible_sha256,votes_sha256\n'+rows.map(r=>[r.id,r.expected,r.B2.status,r.reference.status,r.native.context_qualification,r.visiblePacketSha256,r.voteSha256].join(',')).join('\n')+'\n');
 console.log(JSON.stringify({result:summary.control_result,namedControls:rows.length,
 nullPairs:nullPairs.length,parity:summary.reference_vs_strong_B2,sourceNativeRun:false,EAImplementation:false}));
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url))run();

