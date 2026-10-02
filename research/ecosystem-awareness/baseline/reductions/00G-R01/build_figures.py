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
