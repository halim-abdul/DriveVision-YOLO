import cv2
import numpy as np

def overlay_lane(frame,polygon,alpha=.3):
    layer=frame.copy();pts=np.asarray(polygon,np.int32)
    cv2.fillPoly(layer,[pts],(0,180,0))
    return cv2.addWeighted(layer,alpha,frame,1-alpha,0)
