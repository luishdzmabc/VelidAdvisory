import re
s=open('assets/logo.svg').read()
paths=['<path'+p for p in s.split('<path')[1:]]
paths=[p[:p.index('"/>')+3] for p in paths]
V=paths[0]; D=[p for p in paths if '#EB937D' in p][0]
def tr(p):
    m=re.search(r'translate\(([-\d.]+) ([-\d.]+)\) scale\(([\d.]+)\)',p); return list(map(float,m.groups()))
def xs(p):
    d=re.search(r'd="([^"]+)"',p).group(1); tx,ty,sc=tr(p)
    nums=[float(x) for x in re.findall(r'-?\d+\.?\d*',d)]
    X=nums[0::2]; return min(X)*sc+tx, max(X)*sc+tx
vx=xs(V); dx=xs(D); ux=(1550,1786)
shift=614
mv=lambda p:re.sub(r'translate\(([-\d.]+) ',lambda m:f'translate({float(m.group(1))-shift:.3f} ',p,count=1)
U=f'<rect x="{1550-shift:.1f}" y="459" width="236" height="62" rx="31" fill="#5D9382"/>'
icon=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vx[0]-20:.0f} -20 {ux[1]-shift-vx[0]+40:.0f} 580" role="img" aria-label="VeliD">{V.replace("currentColor","#1F3C54")}{mv(D)}{U}</svg>'
open('assets/icon.svg','w').write(icon); print(vx,dx,shift,len(icon))
