import cv2
import numpy as np

def white_yellow_mask(frame):
    hls=cv2.cvtColor(frame,cv2.COLOR_BGR2HLS)
    white=cv2.inRange(hls,np.array([0,200,0]),np.array([255,255,255]))
    yellow=cv2.inRange(hls,np.array([15,80,80]),np.array([40,255,255]))
    return cv2.bitwise_or(white,yellow)
