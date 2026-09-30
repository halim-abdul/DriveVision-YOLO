from dataclasses import dataclass

@dataclass(frozen=True)
class CameraIntrinsics:
    fx: float
    fy: float
    cx: float
    cy: float

    def matrix(self):
        return [[self.fx,0.0,self.cx],[0.0,self.fy,self.cy],[0.0,0.0,1.0]]
