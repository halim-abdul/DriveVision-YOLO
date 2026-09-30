from collections import deque
import statistics

class RollingAnomaly:
    def __init__(self,size=60,z=3.0):self.values=deque(maxlen=size);self.z=z
    def update(self,value):
        if len(self.values)<10:self.values.append(value);return False
        mean=statistics.mean(self.values);std=statistics.pstdev(self.values) or 1e-9
        flag=abs(value-mean)>self.z*std;self.values.append(value);return flag
