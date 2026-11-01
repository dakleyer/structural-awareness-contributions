"""Local Markdown anchor checker used for the guide and the premium kit.

Usage: python3 -B anchor_check.py <file.md> [more.md ...]
Reports links of the form path.md#fragment whose fragment does not match a
GitHub heading anchor or an explicit <a id="..."> / <a name="..."> anchor
in the target file. Exit code 1 if any link is broken. Writes nothing.
"""
import re, sys, unicodedata, collections, os
def slug(h):
    h=re.sub(r'`','',h).strip().lower()
    out=''.join(c for c in h if c in '-_ ' or unicodedata.category(c)[0] in 'LMN' or unicodedata.category(c)=='Pc')
    return out.replace(' ','-')
def anchors(path):
    seen=collections.Counter(); res=set(); infence=False
    for line in open(path,encoding='utf-8'):
        if line.lstrip().startswith(('```','~~~')): infence=not infence
        if infence: continue
        for a_id in re.findall(r'<a\s+(?:id|name)="([^"]+)"', line): res.add(a_id)
        m=re.match(r'^(#{1,6})\s+(.*?)\s*#*\s*$', line)
        if m:
            t=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',m.group(2)); s=slug(t)
            res.add(s if seen[s]==0 else f"{s}-{seen[s]}"); seen[s]+=1
    return res
def check(path):
    base=os.path.dirname(path); txt=open(path,encoding='utf-8').read(); bad=[]
    txt_nofence=re.sub(r'```.*?```','',txt,flags=re.S)
    for m in re.finditer(r'\]\(([^)\s]*#[^)\s]+)\)', txt_nofence):
        href=m.group(1)
        if href.startswith('http'): continue
        f,frag=href.split('#',1)
        tgt=os.path.normpath(os.path.join(base,f)) if f else path
        if not os.path.exists(tgt) or not tgt.endswith('.md'): continue
        if frag not in anchors(tgt): bad.append((href))
    return bad
total=0
for p in sys.argv[1:]:
    b=check(p); total+=len(b); print(os.path.basename(p), 'broken local anchors:', len(b))
    for x in b: print('   ', x[:160])
sys.exit(1 if total else 0)
