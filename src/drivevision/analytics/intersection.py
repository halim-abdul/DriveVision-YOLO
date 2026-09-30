def movement_counts(tracks,entry_zones,exit_zones):
    counts={}
    for t in tracks:
        if len(t.history)<2:continue
        start=t.history[0];end=t.history[-1]
        a=next((n for n,p in entry_zones.items() if _inside(start,p)),None)
        b=next((n for n,p in exit_zones.items() if _inside(end,p)),None)
        if a and b:counts[(a,b)]=counts.get((a,b),0)+1
    return counts

def _inside(point,poly):
    x,y=point;inside=False;j=len(poly)-1
    for i,(xi,yi) in enumerate(poly):
        xj,yj=poly[j]
        if ((yi>y)!=(yj>y)) and x<(xj-xi)*(y-yi)/(yj-yi+1e-12)+xi:inside=not inside
        j=i
    return inside
