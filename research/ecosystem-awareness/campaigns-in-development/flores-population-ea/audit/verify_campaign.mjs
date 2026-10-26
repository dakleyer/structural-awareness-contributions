import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const ROOT=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const CONTROL=path.join(ROOT,'audit/CAMPAIGN_CONTROL_2026-10-13.json');
const EXPECTED_BASELINE_COMMIT='f16b3ba1ef36bb3ff62b02eb89748838c66e8073';
const BASELINE_PATH='audit/baselines/PRE_HARDENING_f16b3ba1ef36bb3ff62b02eb89748838c66e8073.json';
const EXPECTED_BASELINE_SHA256='27b752ca4173ecaa3da8f183fdad2edfe497f9aaf9ec11ba26c05f03da47fc7d';
function outputFailure(errors){console.log(JSON.stringify({schema:'FLORES_DOCUMENTARY_VALIDATION_2',result:'FAIL',verifierVersion:'0.2',independentScientificAudit:false,errors},null,2));process.exitCode=1;}
function isWithin(root,target){const rel=path.relative(root,target);return !path.isAbsolute(rel)&&rel!=='..'&&!rel.startsWith('..'+path.sep);}
function safeRelative(p){return typeof p==='string'&&p.length>0&&!p.includes('\\')&&!p.includes('\0')&&!path.posix.isAbsolute(p)&&! /^[A-Za-z]:/.test(p)&&!p.split('/').includes('..')&&path.posix.normalize(p)===p;}
function run(c){
const repoRoot=path.resolve(ROOT,...c.campaign_path.split('/').filter(Boolean).map(()=> '..'));
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const blob=b=>crypto.createHash('sha1').update('blob '+b.length+'\0').update(b).digest('hex');
const errors=[];function expect(test,msg){if(!test)errors.push(msg);}
const arrayFields=['inventory','source_inventory','preservation','legacy_anchor_aliases','repository_dependencies','claims','decisions','documentary_audit_requirements','open_items','excluded_self_hashes'];
for(const key of arrayFields)expect(Array.isArray(c[key]),'SCHEMA_ARRAY '+key);
expect(c.campaign_path==='research/ecosystem-awareness/campaigns-in-development/flores-population-ea/','SCHEMA_CAMPAIGN_PATH');expect(c.campaign_id==='DDS-A-FLORES-POP-EA-01','SCHEMA_CAMPAIGN_ID');
expect(c.scientific_status==='NOT_PREREGISTERED_NOT_EXECUTED_NOT_ADJUDICATED','CONTROL_SCIENTIFIC_STATE');
if(errors.length){outputFailure(errors);return;}
const unique=(rows,key,label)=>{const seen=new Set();for(const row of rows){expect(row&&typeof row==='object'&&typeof row[key]==='string','SCHEMA_ROW '+label);if(!row||typeof row[key]!=='string')continue;expect(!seen.has(row[key]),'DUPLICATE_'+label+' '+row[key]);seen.add(row[key]);}};
unique(c.inventory,'path','INVENTORY');unique(c.source_inventory,'path','SOURCE');unique(c.repository_dependencies,'path','DEPENDENCY');unique(c.decisions,'id','DECISION');unique(c.claims,'id','CLAIM');unique(c.documentary_audit_requirements,'id','REQUIREMENT');unique(c.open_items,'id','OPEN_ITEM');
const allowedSelf=['audit/CAMPAIGN_CONTROL_2026-10-13.json','audit/VALIDATION_2026-10-13.json'];
expect(c.excluded_self_hashes.length===2&&new Set(c.excluded_self_hashes).size===2&&c.excluded_self_hashes.every(p=>allowedSelf.includes(p)),'INVALID_SELF_HASH_EXEMPTION');
for(const row of [...c.inventory,...c.source_inventory,...c.repository_dependencies]){expect(safeRelative(row.path),'PATH_NOT_CANONICAL '+row.path);if(c.inventory.includes(row)||c.source_inventory.includes(row)){expect(Number.isSafeInteger(row.bytes)&&row.bytes>=0,'INVALID_BYTE_COUNT '+row.path);expect(/^[a-f0-9]{64}$/.test(row.sha256||''),'INVALID_SHA256 '+row.path);}expect(/^[a-f0-9]{40}$/.test(row.git_blob||''),'INVALID_GIT_BLOB '+row.path);}
for(const row of c.preservation)expect(safeRelative(row.archive_path),'ARCHIVE_PATH_NOT_CANONICAL '+row.archive_path);
for(const row of c.legacy_anchor_aliases)expect(safeRelative(row.path)&&Array.isArray(row.original_slugs),'ALIAS_SCHEMA '+row.path);
expect(c.source_inventory.length===65&&c.source_cut?.original_file_count===65,'SOURCE_COUNT_DRIFT');
if(errors.length){outputFailure(errors);return;}
const baselineBytes=fs.readFileSync(path.join(ROOT,BASELINE_PATH));expect(hash(baselineBytes)===EXPECTED_BASELINE_SHA256,'PINNED_BASELINE_HASH');
const baseline=JSON.parse(baselineBytes);expect(baseline.commit===EXPECTED_BASELINE_COMMIT,'PINNED_BASELINE_COMMIT');expect(baseline.files.length===116,'PINNED_BASELINE_CARDINALITY');
const originalByPath=new Map(baseline.sourceInventory.map(x=>[x.path,x]));
for(const row of c.source_inventory){const original=originalByPath.get(row.path);expect(Boolean(original)&&row.git_blob===original.git_blob&&row.sha256===original.sha256&&row.bytes===original.bytes,'SOURCE_DECLARATION_DRIFT '+row.path);}
for(const prior of baseline.legacyAnchorAliases){const current=c.legacy_anchor_aliases.find(e=>e.path===prior.path);expect(Boolean(current)&&prior.original_slugs.every(a=>current.original_slugs.includes(a)),'LEGACY_ALIAS_DECLARATION_DRIFT '+prior.path);}
let baselinePreserved=0;for(const prior of baseline.files){const currentPath=path.join(ROOT,prior.path);let intact=fs.existsSync(currentPath)&&hash(fs.readFileSync(currentPath))===prior.sha256;const archive=c.preservation.find(e=>e.source_path===c.campaign_path+prior.path&&e.original_blob===prior.git_blob);if(!intact&&archive){const archivedPath=path.join(ROOT,archive.archive_path);intact=fs.existsSync(archivedPath)&&hash(fs.readFileSync(archivedPath))===prior.sha256&&blob(fs.readFileSync(archivedPath))===prior.git_blob;}expect(intact,'PINNED_PREDECESSOR_LOST '+prior.path);if(intact)baselinePreserved++;}
const files=new Map(c.inventory.map(x=>[x.path,x]));
const dependencyNotes=[],fragmentNotes=[],adj=new Map();

function walk(dir){const out=[];for(const e of fs.readdirSync(dir,{withFileTypes:true})){if(e.name==='.git'||e.name==='__pycache__')continue;if(e.isSymbolicLink()){errors.push('SYMLINK_NOT_ADMITTED '+path.relative(ROOT,path.join(dir,e.name)));continue;}const p=path.join(dir,e.name);out.push(...(e.isDirectory()?walk(p):[path.relative(ROOT,p).replaceAll('\\','/')]));}return out;}
const actual=walk(ROOT).sort(),tracked=new Set([...files.keys(),...c.excluded_self_hashes]);
for(const p of actual)expect(tracked.has(p),'UNCLASSIFIED_FILE '+p);
for(const p of tracked)expect(actual.includes(p),'MISSING_FILE '+p);
for(const e of c.inventory){const p=path.join(ROOT,e.path);if(!fs.existsSync(p))continue;const b=fs.readFileSync(p);expect(b.length===e.bytes,'SIZE '+e.path);expect(hash(b)===e.sha256,'HASH '+e.path);expect(blob(b)===e.git_blob,'BLOB '+e.path);expect(Boolean(e.classification&&e.purpose),'CLASSIFICATION '+e.path);}
let unchanged=0,archived=0,originalPresent=0;
for(const e of c.source_inventory){const cur=fs.existsSync(path.join(ROOT,e.path))?fs.readFileSync(path.join(ROOT,e.path)):null;expect(Boolean(cur),'ORIGINAL_PATH_LOST '+e.path);if(cur)originalPresent++;if(cur&&blob(cur)===e.git_blob){unchanged++;continue;}const a=c.preservation.find(x=>x.source_path===c.campaign_path+e.path);expect(Boolean(a),'PREDECESSOR_NOT_PRESERVED '+e.path);if(a&&fs.existsSync(path.join(ROOT,a.archive_path))){const b=fs.readFileSync(path.join(ROOT,a.archive_path));expect(blob(b)===e.git_blob&&hash(b)===e.sha256,'PREDECESSOR_MISMATCH '+e.path);archived++;}}
for(const a of c.preservation){expect(fs.existsSync(path.join(ROOT,a.archive_path)),'ARCHIVE_MISSING '+a.archive_path);if(fs.existsSync(path.join(ROOT,a.archive_path))){const b=fs.readFileSync(path.join(ROOT,a.archive_path));expect(blob(b)===a.original_blob&&hash(b)===a.sha256,'ARCHIVE_IDENTITY '+a.source_path);}}
function uncommentFences(md){let fenced=false,fence='',out=[];for(const line of md.split('\n')){const m=line.match(/^\s*(`{3,}|~{3,})/);if(m){if(!fenced){fenced=true;fence=m[1][0];}else if(m[1][0]===fence)fenced=false;out.push('');continue;}out.push(fenced?'':line);}return out.join('\n');}
function anchors(md){let cleaned=uncommentFences(md),counts=new Map(),out=new Set();for(const line of cleaned.split('\n')){const h=line.match(/^#{1,6}\s+(.+?)\s*#*$/);if(h){let slug=h[1].toLowerCase().replace(/<[^>]+>/g,'').replace(/[^\p{L}\p{N}\- _]/gu,'').replaceAll(' ','-');const n=counts.get(slug)||0;counts.set(slug,n+1);if(n)slug+='-'+n;out.add(slug);}}
for(const m of cleaned.matchAll(/\b(?:id|name)=["']([^"']+)["']/g))out.add(m[1]);return out;}
const dependent=new Map(c.repository_dependencies.map(x=>[x.path,x]));
for(const e of c.repository_dependencies){const p=path.resolve(repoRoot,e.path);if(!fs.existsSync(p)){dependencyNotes.push(e.path);if(process.argv.includes('--require-repository'))errors.push('REPOSITORY_DEPENDENCY_NOT_EXPORTED '+e.path);}else expect(blob(fs.readFileSync(p))===e.git_blob,'DEPENDENCY_BLOB '+e.path);}
let checkedLinks=0,checkedFragments=0;
function link(from,href){if(/^(https?:|mailto:|data:|javascript:)/.test(href))return;let [f,fragment]=href.split('#');f=decodeURIComponent(f||'');fragment=fragment?decodeURIComponent(fragment):null;const abs=f?path.resolve(path.dirname(path.join(ROOT,from)),f):path.join(ROOT,from);const rel=path.relative(ROOT,abs).replaceAll('\\','/');const local=isWithin(ROOT,abs);
if(local){const present=fs.existsSync(abs);expect(present,'LINK_MISSING '+from+' -> '+href);if(!present)return;checkedLinks++;if(tracked.has(rel)){(adj.get(from)||adj.set(from,new Set()).get(from)).add(rel);}else if(fs.existsSync(abs)&&fs.statSync(abs).isDirectory()){for(const p of tracked)if(p.startsWith(rel.replace(/\/$/,'')+'/'))(adj.get(from)||adj.set(from,new Set()).get(from)).add(p);}
if(fragment&&fs.existsSync(abs)){if(/\.html$/.test(rel)){const ids=new Set([...fs.readFileSync(abs,'utf8').matchAll(/\bid=["']([^"']+)["']/g)].map(m=>m[1]));expect(ids.has(fragment),'HTML_FRAGMENT '+from+' -> '+href);checkedFragments++;}else if(/\.md$/.test(rel)){expect(anchors(fs.readFileSync(abs,'utf8')).has(fragment),'MD_FRAGMENT '+from+' -> '+href);checkedFragments++;}}}
else {const repositoryPath=path.relative(repoRoot,abs).replaceAll('\\','/');expect(isWithin(repoRoot,abs),'LINK_ESCAPES_REPOSITORY '+from+' -> '+href);expect(dependent.has(repositoryPath),'UNDECLARED_DEPENDENCY '+from+' -> '+href);if(fs.existsSync(abs)){expect(blob(fs.readFileSync(abs))===dependent.get(repositoryPath)?.git_blob,'DEPENDENCY_BLOB '+repositoryPath);if(fragment&&abs.endsWith('.md')){expect(anchors(fs.readFileSync(abs,'utf8')).has(fragment),'DEPENDENCY_FRAGMENT '+from+' -> '+href);checkedFragments++;}}else {dependencyNotes.push(repositoryPath);if(fragment)fragmentNotes.push(repositoryPath+'#'+fragment);if(process.argv.includes('--require-repository'))errors.push('REPOSITORY_DEPENDENCY_NOT_EXPORTED '+repositoryPath);}}
}
for(const e of c.inventory){if(!/\.(md|html)$/.test(e.path))continue;const p=path.join(ROOT,e.path);if(!fs.existsSync(p))continue;const text=fs.readFileSync(p,'utf8');if(e.path.endsWith('.md'))for(const m of uncommentFences(text).matchAll(/\[[^\]]*\]\(([^)]+)\)/g))link(e.path,m[1]);else for(const m of text.matchAll(/href=["']([^"']+)["']/g))link(e.path,m[1]);}
for(const alias of c.legacy_anchor_aliases){const found=anchors(fs.readFileSync(path.join(ROOT,alias.path),'utf8'));for(const a of alias.original_slugs)expect(found.has(a),'LEGACY_ANCHOR_LOST '+alias.path+'#'+a);}
const reached=new Set(),stack=[c.entry];while(stack.length){const p=stack.pop();if(reached.has(p))continue;reached.add(p);for(const t of adj.get(p)||[])stack.push(t);}
for(const p of tracked)expect(reached.has(p),'NOT_REACHABLE_FROM_CAMPAIGN '+p);
const record=JSON.parse(fs.readFileSync(path.join(ROOT,'CAMPAIGN.json'),'utf8'));
for(const [key,value] of Object.entries(record.admission||{}))expect(value===false,'FALSE_SCIENTIFIC_PROMOTION '+key);
expect(record.formal_campaign_admission==='NOT_ESTABLISHED','FALSE_FORMAL_ADMISSION');
expect(record.external_producer_experiment?.native_results_verified===false,'FALSE_NATIVE_EXECUTION');
expect(record.current_research_direction?.native_R2_freeze_R3_run===false,'FALSE_NATIVE_R2_R3_EXECUTION');
expect(record.campaign_handle===c.campaign_id,'CAMPAIGN_ID');expect(record.working_status==='IN_DEVELOPMENT_NOT_PREREGISTERED','FALSE_WORKING_STATUS');expect(record.primary_trial.name==='FLORES_SAME_TEMPORAL_CLAIM_R2_FREEZE_R3','PRIMARY_TRIAL_DRIFT');expect(record.admission.stage_a_freeze===false&&record.admission.semantic_ea_pass===false,'FALSE_SCIENTIFIC_PROMOTION');
expect(record.organization.control==='audit/CAMPAIGN_CONTROL_2026-10-13.json','MACHINE_CONTROL_ROUTE');
for(const claim of c.claims){expect(c.decisions.some(d=>d.id===claim.decision),'CLAIM_DECISION '+claim.id);for(const r of claim.requirements)expect(c.documentary_audit_requirements.some(e=>e.id===r),'CLAIM_REQUIREMENT '+claim.id+' '+r);for(const p of [...claim.sources,...claim.evidence])expect(tracked.has(p),'CLAIM_ARTIFACT '+claim.id+' '+p);expect(Boolean(claim.limit&&claim.falsifier),'CLAIM_BOUNDARY '+claim.id);}
const pub=JSON.parse(fs.readFileSync(path.join(ROOT,'runtime-context/PUBLICATION_MANIFEST_2026-10-13.json'),'utf8'));
for(const e of pub.files){const p=path.join(ROOT,'runtime-context',e.path);expect(fs.existsSync(p),'RUNTIME_MANIFEST_FILE '+e.path);if(fs.existsSync(p))expect(hash(fs.readFileSync(p))===e.sha256,'RUNTIME_MANIFEST_HASH '+e.path);}
const receiptPath=path.join(ROOT,'audit/VALIDATION_2026-10-13.json');let receiptPending=false;
if(fs.existsSync(receiptPath)){const receipt=JSON.parse(fs.readFileSync(receiptPath,'utf8'));receiptPending=process.argv.includes('--prepublication')&&receipt.result==='PREPARATION_NOT_RUN';expect(receipt.schema==='FLORES_DOCUMENTARY_VALIDATION_2','RECEIPT_SCHEMA');expect(receipt.independentScientificAudit===false,'RECEIPT_FALSE_INDEPENDENCE');expect(receipt.scientificStatus==='NOT_PREREGISTERED_NOT_EXECUTED_NOT_ADJUDICATED','RECEIPT_SCIENTIFIC_STATE');if(!receiptPending){expect(receipt.result==='PASS_DOCUMENTARY_CHECKS','RECEIPT_UNSUPPORTED_RESULT');expect(receipt.filesInventoried===tracked.size,'RECEIPT_FILE_COUNT');expect(receipt.originalPathsPresent===originalPresent,'RECEIPT_ORIGINAL_COUNT');expect(receipt.baselineFilesPreserved===baselinePreserved,'RECEIPT_BASELINE_COUNT');}}
const result={schema:'FLORES_DOCUMENTARY_VALIDATION_2',version:c.version,verifierVersion:'0.2',baselineSourceCommit:EXPECTED_BASELINE_COMMIT,baselineFilesPreserved:baselinePreserved,checkedAtUTC:new Date().toISOString(),result:errors.length?'FAIL':dependencyNotes.length?'PARTIAL_DOCUMENTARY_CHECKS':receiptPending?'PREPUBLICATION_CHECKS_READY':'PASS_DOCUMENTARY_CHECKS',scientificStatus:c.scientific_status,independentScientificAudit:false,filesInventoried:tracked.size,originalFiles:c.source_inventory.length,originalPathsPresent:originalPresent,originalUnchanged:unchanged,originalPreservedInCompletePredecessorArchive:archived,completePredecessors:c.preservation.length,checkedLocalLinks:checkedLinks,checkedLocalFragments:checkedFragments,reachableFromCampaign:reached.size,unclassifiedFiles:actual.filter(p=>!tracked.has(p)),repositoryDependenciesNotInPartialExport:[...new Set(dependencyNotes)].sort(),repositoryFragmentsNotInPartialExport:[...new Set(fragmentNotes)].sort(),externalURLAvailabilityChecked:false,privateBinaryIdentityChecked:false,knownScientificAndCustodyIssues:c.open_items.map(e=>({id:e.id,state:e.state})),errors};
console.log(JSON.stringify(result,null,2));if(errors.length)process.exitCode=1;else if(dependencyNotes.length)process.exitCode=2;

}
try{const c=JSON.parse(fs.readFileSync(CONTROL,'utf8'));run(c);}catch(error){outputFailure(['INPUT_OR_IO_FAILURE '+(error.code||error.name||'UNKNOWN')]);}
