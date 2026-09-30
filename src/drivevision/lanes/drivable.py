import numpy as np

def lane_polygon(left_x,right_x,ys):
    left=np.stack([left_x,ys],axis=1)
    right=np.stack([right_x,ys],axis=1)[::-1]
    return np.concatenate([left,right],axis=0)

def area_ratio(mask):
    return float((mask>0).mean())
