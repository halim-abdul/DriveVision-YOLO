import numpy as np

class Heatmap:
    def __init__(self,height,width):self.map=np.zeros((height,width),dtype=np.float32)
    def add(self,x,y,weight=1.0):
        x=int(round(x));y=int(round(y))
        if 0<=y<self.map.shape[0] and 0<=x<self.map.shape[1]:self.map[y,x]+=weight
    def normalized(self):
        m=self.map.max();return self.map/max(float(m),1e-9)
