import cv2
import numpy as np

def depth_colormap(depth):
    d=np.asarray(depth,float);finite=np.isfinite(d)
    if not finite.any():return np.zeros((*d.shape,3),dtype=np.uint8)
    lo,hi=np.percentile(d[finite],[2,98]);norm=np.clip((d-lo)/max(hi-lo,1e-9),0,1)
    return cv2.applyColorMap((255*(1-norm)).astype(np.uint8),cv2.COLORMAP_TURBO)

def draw_distances(frame,objects):
    out=frame.copy()
    for obj in objects:
        x1,y1,x2,y2=map(int,obj.xyxy)
        cv2.putText(out,f"{obj.class_name} {obj.distance_m:.1f}m",(x1,max(18,y1-5)),cv2.FONT_HERSHEY_SIMPLEX,.5,(0,255,255),1)
    return out
