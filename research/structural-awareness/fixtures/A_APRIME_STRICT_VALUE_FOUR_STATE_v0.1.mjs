#!/usr/bin/env node

/**

 * Four-state source-faithful PR #60 D1 example: exact risk and comparator checks.

 * Research-only: a finite constructed decision problem, no real agents.

 * All worlds, action costs, and probabilities are synthetic and declared.

 * Run: node research/structural-awareness/fixtures/A_APRIME_STRICT_VALUE_FOUR_STATE_v0.1.mjs

 */

const assert = (c,m)=>{if(!c)throw Error(m)};

const X=[0,1,2,3];

const o = x=>x%2;

const s = x=>(x+1)%4;

const f = x=>[1,1,0,3][x];

const q = x=>Number(x===2);

const t = x=>o(f(x));

const states=[0,2];

const best01loss = (obs,states,target)=>{
  const labels=states.map(x=>JSON.stringify(obs(x)));
  const unique=[...new Set(labels)];
  let best=Infinity;
  for(let mask=0;mask<Math.pow(2,unique.length);mask++){
    const risk=states.reduce((sum,x,i)=>sum+Number(((mask>>unique.indexOf(labels[i]))&1)!==target(x)),0)/states.length;
    best=Math.min(best,risk);
  }
  return best;
};

let checks=0;

const check=(x,label)=>{assert(x,label);checks++;};

check(X.every(x=>o(s(x))===1-o(x)),"old parity quotient under s");

check(o(0)===o(2),"0 and 2 same A parity");

check(t(0)===1&&t(2)===0,"new target conflicts within A fiber");

check(o(f(0))!==o(f(2)),"new operation breaks congruence");

check(q(0)!==q(2),"Q separates conflicting pair");

const oRisk=best01loss(o,states,t), enrichedRisk=best01loss(x=>[o(x),q(x)],states,t);

check(oRisk===0.5,"baseline Bayes risk 1/2");

check(enrichedRisk===0,"supplemental Q risk zero");

check(oRisk>=enrichedRisk,"weak refinement");

check(enrichedRisk<oRisk,"strict task-specific refinement");

check(best01loss(x=>[o(x),0],states,t)===oRisk,"constant A-prime tag alone no difference");

const compareC=cost=>({q_net:enrichedRisk+cost,base_net:oRisk,q_wins:enrichedRisk+cost<oRisk});

check(compareC(0.1).q_wins,"net strict if cost 0.1");

check(compareC(0.5).q_net===oRisk,"tie at cost 0.5");

check(!compareC(0.8).q_wins,"no net advantage at cost 0.8");

check(best01loss(x=>[o(x),q(x)],states,t)===enrichedRisk,"competent conventional same Q ties");

check(o(1)!==o(0),"baseline already separates odd/even; Q need not duplicate");

check(states.every(x=>Number.isInteger(f(x))),"finite outputs typed");

console.log(JSON.stringify({checks,baselineRisk:oRisk,enrichedRisk,cost01:compareC(0.1),cost05:compareC(0.5),cost08:compareC(0.8)}));

