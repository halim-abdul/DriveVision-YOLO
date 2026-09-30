from collections import deque
import numpy as np

class LaneHistory:
    def __init__(self,size=8): self.left=deque(maxlen=size);self.right=deque(maxlen=size)
    def update(self,left,right):
        if left is not None:self.left.append(left)
        if right is not None:self.right.append(right)
    def mean(self):
        l=np.mean(self.left,axis=0) if self.left else None
        r=np.mean(self.right,axis=0) if self.right else None
        return l,r
