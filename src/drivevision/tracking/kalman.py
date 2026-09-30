import numpy as np

class KalmanBox:
    def __init__(self,x,y):
        self.x=np.array([x,y,0.,0.],dtype=float)
        self.P=np.eye(4)*10
        self.F=np.array([[1,0,1,0],[0,1,0,1],[0,0,1,0],[0,0,0,1]],float)
        self.H=np.array([[1,0,0,0],[0,1,0,0]],float)
        self.Q=np.eye(4)*0.01; self.R=np.eye(2)*1.0
    def predict(self):
        self.x=self.F@self.x; self.P=self.F@self.P@self.F.T+self.Q; return self.x[:2]
    def update(self,z):
        z=np.asarray(z,float); y=z-self.H@self.x; S=self.H@self.P@self.H.T+self.R
        K=self.P@self.H.T@np.linalg.inv(S); self.x=self.x+K@y; self.P=(np.eye(4)-K@self.H)@self.P
        return self.x[:2]
