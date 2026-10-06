import fs from "node:fs";
import path from "node:path";
import { execFileSync } from "node:child_process";

function computeGraph(commit,tree,files){
function norm(p){const a=[];for(const x of p.split("/"))if(x==="..")a.pop();else if(x&&x!==".")a.push(x);return a.join("/")}
function strip(body){return body.replace(/(^|\n)(`{3,}|~{3,})[^\n]*\n[\s\S]*?\n\2[^\n]*(?=\n|$)/g,"$1")}
function anchors(body){body=strip(body);const all=new Set([...body.matchAll(/(?:id|name)=["']([^"']+)/g)].map(x=>x[1]));const counts=new Map();for(const line of body.split("\n")){const m=line.match(/^#{1,6}\s+(.+?)(?:\s+#+)?$/);if(!m)continue;let s=m[1].replace(/\[([^\]]+)\]\([^)]+\)/g,"$1").replace(/<[^>]*>/g,"").replace(/[`*_~]/g,"").toLowerCase().replace(/[^\p{L}\p{N}\p{M}\s_-]/gu,"").replace(/\s/g,"-");let n=counts.get(s)||0;counts.set(s,n+1);all.add(s+(n?"-"+n:""))}return all}
function parse(body){body=strip(body);const found=[];for(const m of body.matchAll(/!?\[[^\]\n]*\]\((<[^>\n]+>|[^\s)]+)(?:\s+["'][^\n]*?["'])?\)|<(?:a|img)\s+[^>]*(?:href|src)=["']([^"']+)|<(https?:\/\/[^>\s]+)>/gi))found.push(m[1]?.replace(/^<|>$/g,"")||m[2]||m[3]);const defs=new Map([...body.matchAll(/^\s*\[([^\]]+)\]:\s*(<[^>]+>|[^\s]+).*$/gm)].map(m=>[m[1].toLowerCase(),m[2].replace(/^<|>$/g,"")]));for(const m of body.matchAll(/!?\[([^\]\n]+)\](?:\[([^\]\n]*)\])?/g)){const k=(m[2]||m[1]).toLowerCase();if(defs.has(k))found.push(defs.get(k))}for(const m of body.matchAll(/https?:\/\/[^\s<>"`)\]]+/g))found.push(m[0].replace(/[.,;]+$/,""));return [...new Set(found)]}
const entries=new Map(tree.tree.map(e=>[e.path,e]));const paths=Object.keys(files);const edge=[],external=[],historical=[],other=[];
for(const p of paths)for(const raw of parse(files[p].content)){let target=raw,absolute=false;if(/^https?:\/\//i.test(target)){const m=target.match(/^https:\/\/(?:github\.com\/dakleyer\/structural-awareness-contributions\/(?:blob|tree)|raw\.githubusercontent\.com\/dakleyer\/structural-awareness-contributions)\/([^/]+)\/(.+)$/);if(m){if(!["main",commit].includes(m[1])){historical.push({from:p,ref:m[1],raw,path:m[2].split("#")[0].split("?")[0]});continue}target="/"+m[2];absolute=true}else{external.push({from:p,url:raw});continue}}if(/^[a-z][a-z0-9+.-]*:/i.test(target)){other.push({from:p,url:raw});continue}let [dest,anchor=""]=target.split("#");dest=dest.split("?")[0];try{dest=decodeURIComponent(dest);anchor=decodeURIComponent(anchor)}catch{}const resolved=dest?norm((absolute||dest.startsWith("/")?"":p.slice(0,p.lastIndexOf("/")+1))+dest):p;const ent=entries.get(resolved);let status=ent?"exists":"missing";if(ent&&anchor&&files[resolved]&&!anchors(files[resolved].content).has(anchor))status="anchor_candidate";edge.push({from:p,raw,to:resolved,anchor,status,type:ent?.type||null})}
const reachable=new Set(["architectural-contributions/ecosystem-positioning/README.md"]);let changed=true;while(changed){changed=false;for(const e of edge)if(e.status!=="missing"&&reachable.has(e.from)&&files[e.to]&&!reachable.has(e.to)&&!e.to.startsWith("governance/preserved-public-snapshots/")){reachable.add(e.to);changed=true}}
return {commit,markdownFilesScanned:paths.length,totalTreeEntries:tree.tree.length,edge,external,historical,other,reachableMarkdown:[...reachable].sort(),summary:{internal:edge.length,missing:edge.filter(e=>e.status==="missing").length,anchorCandidates:edge.filter(e=>e.status==="anchor_candidate").length,external:external.length,reachableMarkdown:reachable.size,historical:historical.length}}}

const [repoArg, commitArg, outputArg, gitArg] = process.argv.slice(2);
if (!repoArg || !/^[a-f0-9]{40}$/i.test(commitArg || "") || !outputArg) {
  throw new Error("Usage: node link_review.mjs REPOSITORY_ROOT FULL_COMMIT_SHA OUTPUT_JSON [GIT_EXECUTABLE]");
}
const root = path.resolve(repoArg);
const git = gitArg || "git";
const args = ["-c", "safe.directory=" + root, "-C", root];
const options = { maxBuffer: 128 * 1024 * 1024 };
const resolved = execFileSync(git, [...args, "rev-parse", "--verify", commitArg + "^{commit}"], options).toString("utf8").trim();
if (resolved !== commitArg.toLowerCase()) throw new Error("Commit mismatch");
const listing = execFileSync(git, [...args, "ls-tree", "-r", "-t", "-z", "--full-tree", resolved], options).toString("utf8");
const tree = { truncated: false, tree: listing.split("\0").filter(Boolean).map(record => {
  const tab = record.indexOf("\t");
  const [mode, type, sha] = record.slice(0, tab).split(" ");
  return { mode, type, sha, path: record.slice(tab + 1) };
}) };
const docs = tree.tree.filter(e => e.type === "blob" && /\.md$/i.test(e.path) && !e.path.startsWith("governance/preserved-public-snapshots/"));
const raw = execFileSync(git, [...args, "cat-file", "--batch"], { ...options, input: docs.map(e => e.sha).join("\n") + "\n" });
const files = {};
let offset = 0;
for (const doc of docs) {
  const end = raw.indexOf(10, offset);
  if (end < 0) throw new Error("Missing batch header");
  const [sha, type, sizeText] = raw.subarray(offset, end).toString("utf8").split(" ");
  const size = Number(sizeText);
  if (sha !== doc.sha || type !== "blob" || !Number.isSafeInteger(size)) throw new Error("Invalid batch object");
  offset = end + 1;
  files[doc.path] = { sha, content: raw.subarray(offset, offset + size).toString("utf8") };
  offset += size + 1;
}
const report = computeGraph(resolved, tree, files);
fs.writeFileSync(path.resolve(outputArg), JSON.stringify(report, null, 2) + "\n", "utf8");
process.stdout.write(JSON.stringify(report.summary) + "\n");
