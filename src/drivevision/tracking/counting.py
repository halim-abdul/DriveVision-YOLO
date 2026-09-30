def side(p,a,b):
    return (b[0]-a[0])*(p[1]-a[1])-(b[1]-a[1])*(p[0]-a[0])

def crossed(prev,curr,a,b):
    return side(prev,a,b)*side(curr,a,b)<0

def count_crossings(tracks,a,b):
    return sum(1 for t in tracks if len(t.history)>=2 and crossed(t.history[-2],t.history[-1],a,b))
