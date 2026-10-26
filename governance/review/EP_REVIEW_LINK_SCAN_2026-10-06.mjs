// Offline verification of the first-frontier navigation counts recorded in the audit.
// Usage: node EP_REVIEW_LINK_SCAN_2026-10-06.mjs public_source_snapshot.json
// Does not fetch the network, use credentials, modify sources or certify semantics.
import fs from 'node:fs';
const snapshot=JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const known=new Set(snapshot.tree.map(x=>x.path));
const norm=function norm(p){const a=[];for(const x of p.split("/"))if(x==="..")a.pop();else if(x&&x!==".")a.push(x);return a.join("/");};
const extract=function extract(path,body){body=body.replace(/```[\s\S]*?```/g,"");return [...body.matchAll(/!?\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)|<(?:a|img)\s+[^>]*(?:href|src)=["']([^"']+)/gi)].map(m=>m[1]||m[2]).filter(r=>!/^https?:|^mailto:|^data:/.test(r)).map(r=>({raw:r,path:r.startsWith("#")?path:norm(path.slice(0,path.lastIndexOf("/")+1)+decodeURIComponent(r.split("#")[0])),anchor:r.split("#")[1]||""}));};
const anchors=function anchors(body){body=body.replace(/```[\s\S]*?```/g,"");const all=new Set([...body.matchAll(/(?:id|name)=["']([^"']+)/g)].map(x=>x[1]));const counts=new Map();for(const line of body.split("\n")){const m=line.match(/^#{1,6}\s+(.+?)(?:\s+#+)?$/);if(!m)continue;let s=m[1].replace(/\[([^\]]+)\]\([^)]+\)/g,"$1").replace(/<[^>]*>/g,"").replace(/[`*_~]/g,"").toLowerCase().replace(/[^\p{L}\p{N}\p{M}\s_-]/gu,"").replace(/\s/g,"-");let n=counts.get(s)||0;counts.set(s,n+1);all.add(s+(n?"-"+n:""));}return all;};
const ep='architectural-contributions/ecosystem-positioning/README.md';
const body=snapshot.source_text[ep].replace(/\`\`\`[\s\S]*?\`\`\`/g,'');
const raw=[...body.matchAll(/!?\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)|<(?:a|img)\s+[^>]*(?:href|src)=["']([^"']+)/gi)].map(m=>m[1]||m[2]);
const direct=extract(ep,snapshot.source_text[ep]);
const paths=[...new Set(direct.map(x=>x.path))];
const edges=[];
for(const p of paths.filter(p=>p.endsWith('.md'))) for(const link of extract(p,snapshot.source_text[p])) edges.push({from:p,...link});
const targetPaths=[...new Set(edges.map(x=>x.path))];
const result={
baseline_commit:snapshot.baseline_commit,
readme_links:raw.length,
direct_local_paths:paths.length,
direct_markdown_paths:paths.filter(x=>x.endsWith('.md')).length,
distinct_external_urls:new Set(raw.filter(x=>/^https?:/.test(x))).size,
local_anchor_occurrences:direct.filter(x=>x.anchor).length,
missing_direct_paths:paths.filter(p=>!known.has(p)),
suspect_direct_markdown_anchors:direct.filter(x=>x.anchor&&x.path.endsWith('.md')&&!anchors(snapshot.source_text[x.path]).has(x.anchor)),
first_frontier_edges:edges.length,
first_frontier_target_paths:targetPaths.length,
missing_first_frontier_paths:targetPaths.filter(p=>!known.has(p)),
unretrieved_second_frontier_markdown_at_cut:targetPaths.filter(p=>p.endsWith('.md')&&known.has(p)&&!snapshot.source_text[p]&&!(snapshot.extra_retrieved_paths||[]).includes(p)).length
};
console.log(JSON.stringify(result,null,2));
if(result.readme_links!==212||result.direct_local_paths!==102||result.direct_markdown_paths!==95||result.first_frontier_edges!==1903||result.first_frontier_target_paths!==420||result.unretrieved_second_frontier_markdown_at_cut!==229||result.missing_direct_paths.length||result.missing_first_frontier_paths.length||result.suspect_direct_markdown_anchors.length)process.exitCode=1;
