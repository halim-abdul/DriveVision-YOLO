import cv2
import numpy as np

def transform_matrices(src,dst):
    src=np.asarray(src,np.float32);dst=np.asarray(dst,np.float32)
    return cv2.getPerspectiveTransform(src,dst),cv2.getPerspectiveTransform(dst,src)

def warp(image,matrix,size=None):
    h,w=image.shape[:2]
    return cv2.warpPerspective(image,matrix,size or (w,h))
