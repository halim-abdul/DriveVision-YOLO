import numpy as np

def robust_box_depth(depth,box,trim=0.1):
    x1,y1,x2,y2=map(int,box)
    patch=np.asarray(depth[y1:y2,x1:x2],float)
    values=patch[np.isfinite(patch)&(patch>0)]
    if values.size==0:return float("nan")
    values=np.sort(values);k=int(values.size*trim)
    if k>0 and 2*k<values.size: values=values[k:-k]
    return float(np.median(values))
