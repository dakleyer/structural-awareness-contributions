import fs from 'node:fs';import path from 'node:path';import os from 'node:os';import crypto from 'node:crypto';import {fileURLToPath} from 'node:url';import {spawnSync} from 'node:child_process';import assert from 'node:assert/strict';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..'),cPath='audit/CAMPAIGN_CONTROL_2026-10-13.json';
const original=JSON.parse(fs.readFileSync(path.join(root,cPath),'utf8')),temp=fs.mkdtempSync(path.join(os.tmpdir(),'flores-audit-v02-'));
const repoRoot=path.resolve(root,...original.campaign_path.split('/').filter(Boolean).map(()=> '..')),clone=path.join(temp,original.campaign_path);
fs.cpSync(root,clone,{recursive:true});for(const e of original.repository_dependencies){const src=path.join(repoRoot,e.path),dest=path.join(temp,e.path);fs.mkdirSync(path.dirname(dest),{recursive:true});fs.copyFileSync(src,dest);}
const raw=fs.readFileSync(path.join(clone,cPath)),hash=b=>crypto.createHash('sha256').update(b).digest('hex'),blob=b=>crypto.createHash('sha1').update('blob '+b.length+'\0').update(b).digest('hex');
const run=(args=['--require-repository'],at=clone)=>{const p=spawnSync(process.execPath,[path.join(at,'audit/verify_campaign.mjs'),...args],{encoding:'utf8',maxBuffer:12*1024*1024});let out;try{out=JSON.parse(p.stdout);}catch{throw Error('Unstructured verifier result: '+p.stderr);}return {code:p.status,out};};
const baseline=run();assert.equal(baseline.code,0,JSON.stringify(baseline.out));assert.equal(baseline.out.result,'PASS_DOCUMENTARY_CHECKS');
const rows=[];
function test(id,name,mutate,code,args=['--require-repository'],extraCheck=()=>{}){
 const c=JSON.parse(raw),saved=new Map(),omissions=new Set(),save=p=>{if(!saved.has(p))saved.set(p,fs.existsSync(p)?fs.readFileSync(p):null);};
 const edit=(rel,fn,refresh=true)=>{const p=path.join(clone,rel);save(p);const b=Buffer.from(fn(fs.readFileSync(p,'utf8')));fs.writeFileSync(p,b);if(refresh){const e=c.inventory.find(e=>e.path===rel);if(e)Object.assign(e,{bytes:b.length,sha256:hash(b),git_blob:blob(b)});}};
 const omit=rel=>{omissions.add(path.join(clone,rel));};
 const omitRepository=rel=>{omissions.add(path.join(temp,rel));};
 const add=(rel,data)=>{const p=path.join(clone,rel);save(p);fs.writeFileSync(p,data);};
 mutate(c,{edit,omit,omitRepository,add,save,clone,temp});fs.writeFileSync(path.join(clone,cPath),JSON.stringify(c));
 const executedRepo=fs.mkdtempSync(path.join(os.tmpdir(),'fv2-run-'));fs.cpSync(temp,executedRepo,{recursive:true,filter:src=>!omissions.has(src)});const r=run(args,path.join(executedRepo,original.campaign_path));
 if(code==='PARTIAL'){assert.equal(r.code,2,name);assert.equal(r.out.result,'PARTIAL_DOCUMENTARY_CHECKS',name);assert(r.out.repositoryDependenciesNotInPartialExport.length>0,name);}else {assert.equal(r.code,1,name);assert.equal(r.out.result,'FAIL',name);assert(r.out.errors.some(e=>e.startsWith(code)),name+': '+JSON.stringify(r.out.errors));}
 extraCheck(r.out);rows.push({id,name,expected:code,result:'REJECTED_AS_REQUIRED',exitCode:r.code,diagnostics:r.out.errors||[]});
 fs.writeFileSync(path.join(clone,cPath),raw);for(const [p,b] of saved){if(b===null){if(fs.existsSync(p))fs.unlinkSync(p);}else fs.writeFileSync(p,b);}
}
test('N01','Fictitious Stage B acceptance',(c,{edit})=>edit('CAMPAIGN.json',t=>{const r=JSON.parse(t);r.admission.stage_b=true;return JSON.stringify(r);}), 'FALSE_SCIENTIFIC_PROMOTION stage_b');
test('N02','Duplicate artifact identity',c=>c.inventory.push({...c.inventory[0]}),'DUPLICATE_INVENTORY');
test('N03','Erase original inventory and change its declared count',c=>{c.source_inventory=[];c.source_cut.original_file_count=0;},'SOURCE_COUNT_DRIFT');
test('N04','Missing published receipt',(c,{omit})=>omit('audit/VALIDATION_2026-10-13.json'),'MISSING_FILE');
test('N05','Missing dependency with default flags',(c,{omitRepository})=>{const dep=c.repository_dependencies.find(e=>e.path!=='DOCUMENT_CONTROL.md');omitRepository(dep.path);},'PARTIAL',[]);
test('N06','Duplicate decision',c=>c.decisions.push({...c.decisions[0]}),'DUPLICATE_DECISION');
test('N07','Missing dependency array',c=>delete c.repository_dependencies,'SCHEMA_ARRAY repository_dependencies');
test('N08','Actual original-path count after loss',(c,{omit})=>omit('runtime-context/code/preflight.mjs'),'ORIGINAL_PATH_LOST',['--require-repository'],r=>assert.equal(r.originalPathsPresent,64));
test('N09','False scientific control status',c=>c.scientific_status='ACCEPTED','CONTROL_SCIENTIFIC_STATE');
test('N10','Path outside campaign',c=>c.inventory[0].path='../outside','PATH_NOT_CANONICAL');
test('N11','Malformed SHA-256',c=>c.inventory[0].sha256='short','INVALID_SHA256');
test('N12','Unauthorized self-hash exception',c=>c.excluded_self_hashes.push('technical/code/qualifier.py'),'INVALID_SELF_HASH_EXEMPTION');
test('N13','Forged pinned baseline even with updated inventory hash',(c,{edit})=>edit(c.hardening.baseline_manifest,t=>{const b=JSON.parse(t);b.commit='0'.repeat(40);return JSON.stringify(b);}), 'PINNED_BASELINE_HASH');
test('N14','Orphan claim decision',c=>c.claims[0].decision='NONEXISTENT','CLAIM_DECISION');
test('N15','Duplicate claim',c=>c.claims.push({...c.claims[0]}),'DUPLICATE_CLAIM');
test('N16','False declared dependency blob',c=>c.repository_dependencies[0].git_blob='0'.repeat(40),'DEPENDENCY_BLOB');
test('N17','Lost authenticated old checker',(c,{omit})=>{const a=c.preservation.find(e=>e.source_path===c.campaign_path+'audit/verify_campaign.mjs'&&e.original_commit===c.hardening.predecessor_commit);assert(a);omit(a.archive_path);},'PINNED_PREDECESSOR_LOST');
test('N18','Forged original source declaration',c=>c.source_inventory[0].git_blob='0'.repeat(40),'SOURCE_DECLARATION_DRIFT');
test('N19','Unclassified file',(c,{add})=>add('UNCLASSIFIED_TEST_ONLY.txt','test probe'),'UNCLASSIFIED_FILE');
test('N20','Broken current route despite refreshed inventory',(c,{edit})=>edit('CAMPAIGN.md',t=>t.replace('](SCIENTIFIC_DESIGN.md)','](MISSING_CURRENT_DESIGN.md)')),'LINK_MISSING');
test('N21','Lost old fragment despite refreshed document hash',(c,{edit})=>{const t=fs.readFileSync(path.join(clone,'CAMPAIGN.md'),'utf8'),a=c.legacy_anchor_aliases.find(e=>e.path==='CAMPAIGN.md').original_slugs.find(a=>t.includes('<a id="'+a+'"></a>'));assert(a);edit('CAMPAIGN.md',t=>t.replace('<a id="'+a+'"></a>',''));},'LEGACY_ANCHOR_LOST');
test('N22','Erase old anchor declarations',c=>c.legacy_anchor_aliases=[],'LEGACY_ALIAS_DECLARATION_DRIFT');
test('N23','Receipt falsely claims independence',(c,{edit})=>edit('audit/VALIDATION_2026-10-13.json',t=>{const r=JSON.parse(t);r.independentScientificAudit=true;return JSON.stringify(r);},false),'RECEIPT_FALSE_INDEPENDENCE');
test('N24','Receipt falsely claims scientific PASS',(c,{edit})=>edit('audit/VALIDATION_2026-10-13.json',t=>{const r=JSON.parse(t);r.result='PASS_SCIENTIFIC';return JSON.stringify(r);},false),'RECEIPT_UNSUPPORTED_RESULT');
test('N25','Fictitious working admission',(c,{edit})=>edit('CAMPAIGN.json',t=>{const r=JSON.parse(t);r.working_status='ADMITTED';return JSON.stringify(r);}),'FALSE_WORKING_STATUS');
const recovery=run();assert.equal(recovery.code,0,JSON.stringify(recovery.out));
console.log(JSON.stringify({schema:'FLORES_VERIFIER_V02_ADVERSARIAL_TESTS',result:'PASS_ADVERSARIAL_DOCUMENTARY_CONTROLS',baselinePass:true,negativeCases:rows.length,restoredValidCasePass:true,independentScientificAudit:false,nativeRun:false,rows},null,2));
// Temporary isolated probes are not source artifacts; all source and result evidence remain in GitHub.
