import numpy as np

def abs_rel(pred,target):
    p=np.asarray(pred,float);t=np.asarray(target,float);m=np.isfinite(p)&np.isfinite(t)&(t>0)
    return float(np.mean(np.abs(p[m]-t[m])/t[m])) if m.any() else float("nan")

def rmse(pred,target):
    p=np.asarray(pred,float);t=np.asarray(target,float);m=np.isfinite(p)&np.isfinite(t)
    return float(np.sqrt(np.mean((p[m]-t[m])**2))) if m.any() else float("nan")
