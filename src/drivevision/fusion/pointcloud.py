import numpy as np

def depth_to_points(depth,intrinsics,stride=8):
    h,w=depth.shape[:2];points=[]
    for v in range(0,h,stride):
        for u in range(0,w,stride):
            z=float(depth[v,u])
            if not np.isfinite(z) or z<=0:continue
            x=(u-intrinsics.cx)*z/intrinsics.fx;y=(v-intrinsics.cy)*z/intrinsics.fy
            points.append((x,y,z))
    return np.asarray(points,float)
