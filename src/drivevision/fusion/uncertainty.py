import numpy as np

def local_uncertainty(depth,box):
    x1,y1,x2,y2=map(int,box)
    patch=np.asarray(depth[y1:y2,x1:x2],float)
    values=patch[np.isfinite(patch)&(patch>0)]
    if values.size<2:return float("inf")
    median=np.median(values)
    return float(1.4826*np.median(np.abs(values-median)))
