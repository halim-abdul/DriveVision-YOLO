import numpy as np
from .geometry import bbox_iou

def iou_cost(tracks,detections):
    cost=np.ones((len(tracks),len(detections)),dtype=float)
    for i,t in enumerate(tracks):
        for j,d in enumerate(detections):
            cost[i,j]=1.0-bbox_iou(t.xyxy,d.xyxy)
    return cost

def greedy_match(cost,max_cost=0.7):
    pairs=[]
    if cost.size==0:return pairs
    work=cost.copy()
    while True:
        idx=np.unravel_index(np.argmin(work),work.shape)
        if work[idx]>max_cost:break
        i,j=map(int,idx);pairs.append((i,j));work[i,:]=2;work[:,j]=2
    return pairs
