import numpy as np

def normalize_inverse_depth(values):
    x=np.asarray(values,float)
    finite=np.isfinite(x)
    if not finite.any():return np.zeros_like(x)
    lo,hi=np.percentile(x[finite],[2,98])
    return np.clip((x-lo)/max(hi-lo,1e-9),0,1)
