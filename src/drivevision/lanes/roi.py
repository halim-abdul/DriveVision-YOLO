import cv2
import numpy as np

def polygon_mask(image,points):
    mask=np.zeros_like(image)
    cv2.fillPoly(mask,[np.asarray(points,np.int32)],255)
    return cv2.bitwise_and(image,mask)
