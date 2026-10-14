import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const ROOT=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const CONTROL=path.join(ROOT,'audit/CAMPAIGN_CONTROL_2026-10-13.json');
const c=JSON.parse(fs.readFileSync(CONTROL,'utf8'));
const repoRoot=path.resolve(ROOT,...c.campaign_path.split('/').filter(Boolean).map(()=> '..'));
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const blob=b=>crypto.createHash('sha1').update('blob '+b.length+'\0').update(b).digest('hex');
const files=new Map(c.inventory.map(x=>[x.path,x]));
const errors=[],dependencyNotes=[],fragmentNotes=[],adj=new Map();
const expect=(test,msg)=>{if(!test)errors.push(msg);};
function walk(dir){const out=[];for(const e of fs.readdirSync(dir,{withFileTypes:true})){if(e.name==='.git'||e.name==='__pycache__')continue;const p=path.join(dir,e.name);out.push(...(e.isDirectory()?walk(p):[path.relative(ROOT,p).replaceAll('\\','/')]));}return out;}
const actual=walk(ROOT).sort(),tracked=new Set([...files.keys(),...c.excluded_self_hashes]);
for(const p of actual)expect(tracked.has(p),'UNCLASSIFIED_FILE '+p);
for(const p of tracked)expect(actual.includes(p)||p==='audit/VALIDATION_2026-10-13.json','MISSING_FILE '+p);
for(const e of c.inventory){const p=path.join(ROOT,e.path);if(!fs.existsSync(p))continue;const b=fs.readFileSync(p);expect(b.length===e.bytes,'SIZE '+e.path);expect(hash(b)===e.sha256,'HASH '+e.path);expect(blob(b)===e.git_blob,'BLOB '+e.path);expect(Boolean(e.classification&&e.purpose),'CLASSIFICATION '+e.path);}
let unchanged=0,archived=0;
for(const e of c.source_inventory){const cur=fs.existsSync(path.join(ROOT,e.path))?fs.readFileSync(path.join(ROOT,e.path)):null;expect(Boolean(cur),'ORIGINAL_PATH_LOST '+e.path);if(cur&&blob(cur)===e.git_blob){unchanged++;continue;}const a=c.preservation.find(x=>x.source_path===c.campaign_path+e.path);expect(Boolean(a),'PREDECESSOR_NOT_PRESERVED '+e.path);if(a&&fs.existsSync(path.join(ROOT,a.archive_path))){const b=fs.readFileSync(path.join(ROOT,a.archive_path));expect(blob(b)===e.git_blob&&hash(b)===e.sha256,'PREDECESSOR_MISMATCH '+e.path);archived++;}}
for(const a of c.preservation){expect(fs.existsSync(path.join(ROOT,a.archive_path)),'ARCHIVE_MISSING '+a.archive_path);if(fs.existsSync(path.join(ROOT,a.archive_path))){const b=fs.readFileSync(path.join(ROOT,a.archive_path));expect(blob(b)===a.original_blob&&hash(b)===a.sha256,'ARCHIVE_IDENTITY '+a.source_path);}}
function uncommentFences(md){let fenced=false,fence='',out=[];for(const line of md.split('\n')){const m=line.match(/^\s*(`{3,}|~{3,})/);if(m){if(!fenced){fenced=true;fence=m[1][0];}else if(m[1][0]===fence)fenced=false;out.push('');continue;}out.push(fenced?'':line);}return out.join('\n');}
function anchors(md){let cleaned=uncommentFences(md),counts=new Map(),out=new Set();for(const line of cleaned.split('\n')){const h=line.match(/^#{1,6}\s+(.+?)\s*#*$/);if(h){let slug=h[1].toLowerCase().replace(/<[^>]+>/g,'').replace(/[^\p{L}\p{N}\- _]/gu,'').replaceAll(' ','-');const n=counts.get(slug)||0;counts.set(slug,n+1);if(n)slug+='-'+n;out.add(slug);}}
for(const m of cleaned.matchAll(/\b(?:id|name)=["']([^"']+)["']/g))out.add(m[1]);return out;}
const dependent=new Map(c.repository_dependencies.map(x=>[x.path,x]));
let checkedLinks=0,checkedFragments=0;
function link(from,href){if(/^(https?:|mailto:|data:|javascript:)/.test(href))return;let [f,fragment]=href.split('#');f=decodeURIComponent(f||'');fragment=fragment?decodeURIComponent(fragment):null;const abs=f?path.resolve(path.dirname(path.join(ROOT,from)),f):path.join(ROOT,from);const rel=path.relative(ROOT,abs).replaceAll('\\','/');const local=!rel.startsWith('../');
if(local){const present=fs.existsSync(abs)||tracked.has(rel);expect(present,'LINK_MISSING '+from+' -> '+href);if(!present)return;checkedLinks++;if(tracked.has(rel)){(adj.get(from)||adj.set(from,new Set()).get(from)).add(rel);}else if(fs.existsSync(abs)&&fs.statSync(abs).isDirectory()){for(const p of tracked)if(p.startsWith(rel.replace(/\/$/,'')+'/'))(adj.get(from)||adj.set(from,new Set()).get(from)).add(p);}
if(fragment&&fs.existsSync(abs)){if(/\.html$/.test(rel)){const ids=new Set([...fs.readFileSync(abs,'utf8').matchAll(/\bid=["']([^"']+)["']/g)].map(m=>m[1]));expect(ids.has(fragment),'HTML_FRAGMENT '+from+' -> '+href);checkedFragments++;}else if(/\.md$/.test(rel)){expect(anchors(fs.readFileSync(abs,'utf8')).has(fragment),'MD_FRAGMENT '+from+' -> '+href);checkedFragments++;}}}
else {const repositoryPath=path.relative(repoRoot,abs).replaceAll('\\','/');expect(dependent.has(repositoryPath),'UNDECLARED_DEPENDENCY '+from+' -> '+href);if(fs.existsSync(abs)){expect(blob(fs.readFileSync(abs))===dependent.get(repositoryPath)?.git_blob,'DEPENDENCY_BLOB '+repositoryPath);if(fragment&&abs.endsWith('.md')){expect(anchors(fs.readFileSync(abs,'utf8')).has(fragment),'DEPENDENCY_FRAGMENT '+from+' -> '+href);checkedFragments++;}}else {dependencyNotes.push(repositoryPath);if(fragment)fragmentNotes.push(repositoryPath+'#'+fragment);if(process.argv.includes('--require-repository'))errors.push('REPOSITORY_DEPENDENCY_NOT_EXPORTED '+repositoryPath);}}
}
for(const e of c.inventory){if(!/\.(md|html)$/.test(e.path))continue;const p=path.join(ROOT,e.path);if(!fs.existsSync(p))continue;const text=fs.readFileSync(p,'utf8');if(e.path.endsWith('.md'))for(const m of uncommentFences(text).matchAll(/\[[^\]]*\]\(([^)]+)\)/g))link(e.path,m[1]);else for(const m of text.matchAll(/href=["']([^"']+)["']/g))link(e.path,m[1]);}
for(const alias of c.legacy_anchor_aliases){const found=anchors(fs.readFileSync(path.join(ROOT,alias.path),'utf8'));for(const a of alias.original_slugs)expect(found.has(a),'LEGACY_ANCHOR_LOST '+alias.path+'#'+a);}
const reached=new Set(),stack=[c.entry];while(stack.length){const p=stack.pop();if(reached.has(p))continue;reached.add(p);for(const t of adj.get(p)||[])stack.push(t);}
for(const p of tracked)expect(reached.has(p),'NOT_REACHABLE_FROM_CAMPAIGN '+p);
const record=JSON.parse(fs.readFileSync(path.join(ROOT,'CAMPAIGN.json'),'utf8'));
expect(record.campaign_handle===c.campaign_id,'CAMPAIGN_ID');expect(record.primary_trial.name==='FLORES_SAME_TEMPORAL_CLAIM_R2_FREEZE_R3','PRIMARY_TRIAL_DRIFT');expect(record.admission.stage_a_freeze===false&&record.admission.semantic_ea_pass===false,'FALSE_SCIENTIFIC_PROMOTION');
expect(record.organization.control==='audit/CAMPAIGN_CONTROL_2026-10-13.json','MACHINE_CONTROL_ROUTE');
for(const claim of c.claims){expect(c.decisions.some(d=>d.id===claim.decision),'CLAIM_DECISION '+claim.id);for(const r of claim.requirements)expect(c.documentary_audit_requirements.some(e=>e.id===r),'CLAIM_REQUIREMENT '+claim.id+' '+r);for(const p of [...claim.sources,...claim.evidence])expect(tracked.has(p),'CLAIM_ARTIFACT '+claim.id+' '+p);expect(Boolean(claim.limit&&claim.falsifier),'CLAIM_BOUNDARY '+claim.id);}
const pub=JSON.parse(fs.readFileSync(path.join(ROOT,'runtime-context/PUBLICATION_MANIFEST_2026-10-13.json'),'utf8'));
for(const e of pub.files){const p=path.join(ROOT,'runtime-context',e.path);expect(fs.existsSync(p),'RUNTIME_MANIFEST_FILE '+e.path);if(fs.existsSync(p))expect(hash(fs.readFileSync(p))===e.sha256,'RUNTIME_MANIFEST_HASH '+e.path);}
const result={schema:'FLORES_DOCUMENTARY_VALIDATION_1',version:c.version,checkedAtUTC:new Date().toISOString(),result:errors.length?'FAIL':'PASS_DOCUMENTARY_CHECKS',scientificStatus:c.scientific_status,independentScientificAudit:false,filesInventoried:tracked.size,originalFiles:c.source_inventory.length,originalPathsPresent:c.source_inventory.length,originalUnchanged:unchanged,originalPreservedInCompletePredecessorArchive:archived,completePredecessors:c.preservation.length,checkedLocalLinks:checkedLinks,checkedLocalFragments:checkedFragments,reachableFromCampaign:reached.size,unclassifiedFiles:actual.filter(p=>!tracked.has(p)),repositoryDependenciesNotInPartialExport:[...new Set(dependencyNotes)].sort(),repositoryFragmentsNotInPartialExport:[...new Set(fragmentNotes)].sort(),externalURLAvailabilityChecked:false,privateBinaryIdentityChecked:false,knownScientificAndCustodyIssues:c.open_items.map(e=>({id:e.id,state:e.state})),errors};
console.log(JSON.stringify(result,null,2));if(errors.length)process.exitCode=1;
