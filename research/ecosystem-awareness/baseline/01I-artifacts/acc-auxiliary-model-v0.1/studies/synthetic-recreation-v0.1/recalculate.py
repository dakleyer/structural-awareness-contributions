"""New closed-form recreation of declared toy parameters; no historical-run authentication."""
from pathlib import Path
import hashlib,json,math

def calculate():
    p,h,b,r=.2,3.,10.,.15
    retirement=0.;rows=[]
    for t in range(1,21):
        dense=h*p*t*(t+1)/2
        sparse=h*p*t
        retirement=(1-r)*retirement+h*p*t
        if t in [5,10,15,20]:
            rows.append({'t':t,'N':dense,'L_and_E':sparse,'R':retirement,'credit_q05':.5*dense+.5*retirement,'credit_q08':.8*dense+.2*retirement,'V_N_lambda1':b*t-dense})
    sensitivity=[{'benefit':bb,'lambda':ll,'marginal20':bb-ll*h*p*20,'V20_minus_V16':4*bb-ll*h*p*(20*21-16*17)/2} for bb in [5,10,20] for ll in [.5,1,2]]
    result={'status':'NEW_ANALYTICAL_RECREATION_ONLY','original_runs_authenticated':False,
        'parameters':{'p':p,'h':h,'benefit':b,'retirement_hazard':r,'horizon':20},'rows':rows,
        'cumulative_N':sum(h*p*t*(t+1)/2 for t in range(1,21)),
        'cumulative_map':sum(h*p*t for t in range(1,21)),
        'negative_marginal20_probability':sum(math.comb(20,k)*p**k*(1-p)**(20-k) for k in range(4,21)),
        'marginal_zero_index':b/(h*p),'continuous_V_maximum':b/(h*p)-.5,
        'sensitivity':sensitivity,'E_incremental_cost_at20':[{'K':k,'saving':114-k} for k in [0,50,114,150]],
        'unanimity_q09_v20':{'independent':.9**20,'perfectly_coincident':.9,'marginals_only_bounds':[0,.9]},
        'limits':['Dense topology incompatibility and persistence are assumptions','Credit protection is a stipulated rule, not estimated behavior','Lambda converts units only within this declared toy','No representative organization or measured human welfare'],
    }
    assert abs(result['cumulative_N']-924)<1e-9
    assert abs(result['cumulative_map']-126)<1e-9
    assert abs(rows[-1]['R']-58.21188270458233)<1e-9
    return result

if __name__=='__main__':
    path=Path(__file__).resolve()
    result=calculate();result['implementation_sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
    (path.parent/'results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'status':result['status'],'N20':result['rows'][-1]['N'],'R20':result['rows'][-1]['R'],'original_runs_authenticated':False}))
