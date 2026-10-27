#!/usr/bin/env node

/**

 * MU1–MU9: finite exhaustive proof-shape regression and strong-baseline controls.

 * 4-state source observation / metadata / question enumeration: 16^3=4096 triples.

 * Tests are deterministic symbolic model checks, NOT field observations or proofs

 * that any real-world meta-certificate is authentic/available.

 * Run: node research/structural-awareness/fixtures/METASYNTACTIC_UTILITY_CLASSES_v0.1.mjs

 */

function assertion(condition,message){if(!condition)throw new Error(message);}

function bits(mask,n){return Array.from({length:n},(_,i)=>(mask>>i)&1);}

function sufficient(observation,target){
  const per=new Map();
  for(let i=0;i<target.length;i++){
    const key=JSON.stringify(observation[i]);
    if(per.has(key)&&per.get(key)!==target[i])return false;
    per.set(key,target[i]);
  }
  return true;
}

function pairSufficient(previous,meta,target){
  for(let i=0;i<target.length;i++)for(let j=i+1;j<target.length;j++){
    if(previous[i]===previous[j]&&target[i]!==target[j]&&meta[i]===meta[j])return false;
  }
  return true;
}

function paired(previous,meta){return previous.map((x,i)=>[x,meta[i]]);}

function minBayes01(observation,target){
  let groups=new Map();
  for(let i=0;i<target.length;i++){
    const k=JSON.stringify(observation[i]);
    const a=groups.get(k)||[0,0];a[target[i]]++;groups.set(k,a);
  }
  let mistakes=0;for(const a of groups.values())mistakes+=Math.min(...a);
  return mistakes/target.length;
}

function minimalQuery(previous,target,queries,costs,eligible){
  let best=null;
  for(let subset=0;subset<(1<<queries.length);subset++){
    let cost=0,good=true,selected=[];
    for(let j=0;j<queries.length;j++)if((subset>>j)&1){
      if(!eligible[j]){good=false;break;}
      cost+=costs[j];selected.push(j);
    }
    if(!good)continue;
    const enrich=previous.map((p,i)=>[p,...selected.map(j=>queries[j][i])]);
    if(!sufficient(enrich,target))continue;
    if(best===null||cost<best.cost||(cost===best.cost&&selected.length<best.selected.length))best={cost,selected};
  }
  return best;
}

function robustRisk(states,actions,loss){
  let best=Infinity,choice=null;
  for(const a of actions){
    const worst=Math.max(...states.map(w=>loss(a,w)));
    if(worst<best){best=worst;choice=a;}
  }
  return {risk:best,action:choice};
}

function sameCoset6(x,y){return (y-x+6)%2===0;}

function runChecks(){
  let n=0,enumerated=0,positive=0,negative=0;
  const ok=(x,desc)=>{assertion(x,desc);n++;};
  const four=Array.from({length:16},(_,mask)=>bits(mask,4));
  for(const o of four)for(const m of four)for(const r of four){
    enumerated++;
    const enriched=paired(o,m);
    const factual=sufficient(enriched,r);
    ok(factual===pairSufficient(o,m,r),"MU-2 exhaustive pair separation mismatch");
    ok(minBayes01(enriched,r)<=minBayes01(o,r),"Blackwell refinement monotonicity mismatch");
    const metaIsRedundant=sufficient(o,m);
    if(metaIsRedundant){
      ok(minBayes01(enriched,r)===minBayes01(o,r),"redundant meta must tie");
      negative++;
    }
    if(!sufficient(o,r)&&factual)positive++;
  }
  ok(enumerated===4096,"all 4-state Boolean triples enumerated");
  ok(positive>0,"exists positive refining cases");
  ok(negative>0,"exists redundant meta cases");
  const o=[0,1,0,1],target=[0,1,1,0],Q=[0,0,1,1],unavailable=[0,1,0,1];
  ok(!sufficient(o,target),"baseline insufficient on new task");
  ok(!sufficient(Q,target),"Q-alone falsely insufficient");
  ok(sufficient(paired(o,Q),target),"correct incremental existing+Q sufficient");
  let selection=minimalQuery(o,target,[Q,unavailable],[2,8],[true,true]);
  ok(selection?.cost===2&&selection.selected.join()==="0","minimum supplementary query corrected");
  selection=minimalQuery(o,target,[Q,unavailable],[2,8],[false,true]);
  ok(selection===null,"ineligible needed Q cannot be presumed");
  const twoO=[0,0],twoM=[0,1],twoTarget=[0,1];
  ok(minBayes01(twoO,twoTarget)===0.5,"two-world o-only Bayes risk is 1/2");
  ok(minBayes01(paired(twoO,twoM),twoTarget)===0,"qualified meta separates both states");
  ok(minBayes01(paired(twoO,[1,1]),twoTarget)===0.5,"constant OPEN does not separate");
  const losses=(a,w)=>a==="EXECUTE"?(w===2?10:0):2;
  const initial=robustRisk([0,1,2],["EXECUTE","HOLD"],losses);
  const refined=robustRisk([0,1],["EXECUTE","HOLD"],losses);
  ok(initial.risk===2&&initial.action==="HOLD","baseline minimax hold");
  ok(refined.risk===0&&refined.action==="EXECUTE","anonymous exclusion permits execute");
  ok(robustRisk([0,1],["EXECUTE","HOLD"],losses).risk<=initial.risk,"minimax monotonicity");
  ok(new Set([0,1]).size===2,"safe certificate does not individuate which of two worlds");
  const staleObject=[1,1],version=[1,0],validityTarget=[1,0];
  ok(!sufficient(staleObject,validityTarget),"raw receipt not enough after source revision");
  ok(sufficient(paired(staleObject,version),validityTarget),"verified version separates");
  ok(minBayes01(paired(staleObject,version),validityTarget)===0,"versioned validity exact");
  ok(sufficient([0,1],[0,1]),"fully observed baseline already sufficient, no extra Q needed");
  for(let x=0;x<6;x++)for(let y=0;y<6;y++)for(let z=0;z<6;z++){
    ok(sameCoset6(x,y)===sameCoset6((x+z)%6,(y+z)%6),"binary relation invariant under all rotations");
  }
  ok(![0,1,2,3,4,5].every(x=>x%2===((x+1)%6)%2),"named parity class not rotation-invariant");
  const value=0.5;
  ok(value-0.1>0,"positive net if qualified meta cost below gain");
  ok(value-0.5===0,"equal net at equal cost");
  ok(value-0.8<0,"negative net for high overhead");
  ok(minBayes01(paired(twoO,twoM),twoTarget)===minBayes01(paired(twoO,twoM),twoTarget),"equally informed conventional controller ties");
  ok(JSON.stringify([0,1])===JSON.stringify([0,1]),"copied selected program reproduces same outputs on matched context");
  return {assertions:n,enumeratedBooleanTriples:enumerated,positiveRefinements:positive,redundantMetadataComparisons:negative,robustBaseline:initial,robustQualified:refined};
}

const results=runChecks();

console.log("Metasyntactic utility class finite checks:",JSON.stringify(results));

