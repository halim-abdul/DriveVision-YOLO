from dataclasses import dataclass

@dataclass
class LaneConfig:
    blur_kernel:int=5
    canny_low:int=50
    canny_high:int=150
    history:int=8
    lane_width_m:float=3.7
    ym_per_pix:float=30/720
    xm_per_pix:float=3.7/700
