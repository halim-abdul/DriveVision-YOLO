import math

def path_length(points):
    return sum(math.dist(a,b) for a,b in zip(points,points[1:]))

def smooth(points,window=5):
    if window<=1:return list(points)
    out=[]
    for i in range(len(points)):
        chunk=points[max(0,i-window+1):i+1]
        out.append((sum(p[0] for p in chunk)/len(chunk),sum(p[1] for p in chunk)/len(chunk)))
    return out
