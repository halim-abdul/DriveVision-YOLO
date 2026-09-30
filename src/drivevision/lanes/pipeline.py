import cv2
from .config import LaneConfig
from .edges import lane_edges
from .color import white_yellow_mask

class LanePipeline:
    def __init__(self,config=None): self.config=config or LaneConfig()
    def binary(self,frame):
        edges=lane_edges(frame,self.config.blur_kernel,self.config.canny_low,self.config.canny_high)
        color=white_yellow_mask(frame)
        return cv2.bitwise_or(edges,color)
