from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

root=Path(__file__).resolve().parent/'figures'
root.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10})
ink='#263D4D'; edge='#668295'; pale='#EDF3F6'; rust='#8B4D2F'
def canvas(h):
    fig,ax=plt.subplots(figsize=(6.9,h),dpi=240)
    fig.subplots_adjust(left=0,right=1,top=1,bottom=0)
    ax.set_xlim(0,6.9); ax.set_ylim(0,h); ax.axis('off')
    return fig,ax
def box(ax,x,y,w,h,title,detail,highlight=False):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=0.055',linewidth=.9,edgecolor=rust if highlight else edge,facecolor='#FBF1EA' if highlight else pale))
    ax.text(x+w/2,y+h*.69,title,ha='center',va='center',fontsize=9.1 if title=='Execute and communicate' else 10.1,fontweight='bold',color=ink)
    ax.text(x+w/2,y+h*.30,detail,ha='center',va='center',fontsize=9.1,color=ink,linespacing=1.25)
def arrow(ax,a,b,dashed=False,rad=0):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=11,linewidth=1,color=edge,linestyle=(0,(4,3)) if dashed else '-',connectionstyle=f'arc3,rad={rad}'))
fig,ax=canvas(2.65)
w=2.02;h=.65;xs=[.10,2.44,4.78]
box(ax,xs[0],1.82,w,h,'Position and memory','Task and budget')
box(ax,xs[1],1.82,w,h,'Explore','Observe candidates')
box(ax,xs[2],1.82,w,h,'Select','Provisional choice')
box(ax,xs[2],.72,w,h,'Review','Own check',True)
box(ax,xs[1],.72,w,h,'Decide','Applicable evidence')
box(ax,xs[0],.72,w,h,'Execute and communicate','Effect and subsequent signal')
arrow(ax,(2.17,2.145),(2.40,2.145));arrow(ax,(4.51,2.145),(4.74,2.145))
arrow(ax,(5.79,1.78),(5.79,1.42))
arrow(ax,(4.74,1.045),(4.51,1.045));arrow(ax,(2.40,1.045),(2.17,1.045))
arrow(ax,(1.11,1.41),(1.11,1.78))
ax.text(1.27,1.60,'Memory and received messages',fontsize=8.4,va='center',color=ink)
ax.text(3.45,.34,'Rejection or insufficient evidence → another candidate, more review or abstention',ha='center',fontsize=8.5,color=ink)
fig.savefig(root/'ciclo-decision.png',facecolor='white');plt.close(fig)

fig,ax=canvas(2.85)
box(ax,2.10,2.08,2.70,.61,'00G family','Displaced framework and obligation')
box(ax,.13,1.05,2.72,.65,'Napoleon','Published illustrative instance')
box(ax,4.04,1.05,2.72,.65,'C-V-G subfamily','C-V traces with the 00G kernel')
box(ax,4.04,.05,2.72,.65,'HF trace representation','Only episodes passing audit')
arrow(ax,(2.60,2.03),(1.80,1.74));arrow(ax,(4.28,2.03),(5.08,1.74),True)
arrow(ax,(5.40,1.0),(5.40,.75),True)
ax.plot([.20,.58],[.59,.59],color=edge,lw=1)
ax.text(.70,.59,'Documented instance',va='center',fontsize=9,color=ink)
ax.plot([.20,.58],[.29,.29],color=edge,lw=1,linestyle=(0,(4,3)))
ax.text(.70,.29,'Candidate relation',va='center',fontsize=9,color=ink)
fig.savefig(root/'relacion-00g.png',facecolor='white');plt.close(fig)
print(root)


# Practical evaluation diagram. Kept separate from the two original figures.
plt.rcParams['svg.fonttype']='none'
fig,ax=plt.subplots(figsize=(11,9),dpi=180)
fig.subplots_adjust(left=0,right=1,top=1,bottom=0)
ax.set(xlim=(0,11),ylim=(0,9));ax.axis('off')
blue='#243B53';muted='#52677A';line='#728A9E'
def stage(x,y,w,h,title,details,fill='#EDF3F8',stroke='#9AB0C1'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=0.08',linewidth=1.1,edgecolor=stroke,facecolor=fill))
    ax.text(x+w/2,y+h*.73,title,ha='center',va='center',fontsize=12,fontweight='bold',color=blue)
    ax.text(x+w/2,y+h*.32,details,ha='center',va='center',fontsize=10.3,color=blue,linespacing=1.35)
def link(a,b,rad=0):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=14,linewidth=1.25,color=line,connectionstyle=f'arc3,rad={rad}'))
ax.text(.30,8.66,'From the practical problem to acceptance',fontsize=18,fontweight='bold',color=blue)
ax.text(.30,8.35,'All rules, means and acceptance thresholds are declared before evaluation.',fontsize=10.5,color=muted)
stage(.30,7.05,4.80,1.00,'Problem parameters','Task, obligations, routes M / I / P\nDistances, dispersion, segments, constraints')
stage(5.90,7.05,4.80,1.00,'Technology or combination','Available means and effective parameter changes\nInformation, review, coordination, costs, timing')
stage(2.60,5.70,5.80,.85,'Operating scenario · θ','Problem considered with the declared technological means')
link((2.70,7.00),(4.00,6.60));link((8.30,7.00),(7.00,6.60))
stage(.30,4.15,4.80,1.05,'Execution strategy · π','What each agent or the group does\nUsing only permitted information and operations')
stage(5.90,4.15,4.80,1.05,'Performance · (c, r, s)','Complete cost ceiling · campaign risk\nProbability of legitimate success')
link((4.00,5.65),(2.70,5.25));link((5.15,4.675),(5.85,4.675))
stage(.30,2.55,4.80,1.00,'Acceptance policies · (b, δ, p)','Maximum cost · maximum tolerated risk\nMinimum legitimate efficacy',fill='#F4F0FA',stroke='#B1A2C8')
stage(5.90,2.55,4.80,1.00,'Compare with the accepted region','c ≤ b     r ≤ δ     s ≥ p')
link((8.30,4.10),(8.30,3.60));link((5.15,3.05),(5.85,3.05))
stage(5.90,1.10,2.20,.90,'Inside','This strategy is accepted',fill='#E8F5EF',stroke='#76A98F')
stage(8.50,1.10,2.20,.90,'Outside','A threshold is unmet',fill='#FCF0E9',stroke='#C49A7A')
link((7.45,2.50),(7.00,2.05));link((9.15,2.50),(9.60,2.05))
ax.text(.30,1.51,'Scenario-level conclusion',fontsize=11.3,fontweight='bold',color=blue)
ax.text(.30,1.04,'One accepted strategy establishes viability.\nOne rejected strategy does not establish impossibility.',fontsize=10.2,color=muted,linespacing=1.5)
ax.text(.30,.40,'Risk and efficacy are probabilities over executions; cost is a ceiling, not expected cost.',fontsize=10.2,color=muted)
fig.savefig(root/'escenario-aceptacion.svg',facecolor='white',metadata={'Date':None});plt.close(fig)
