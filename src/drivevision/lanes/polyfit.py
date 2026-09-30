import numpy as np

def fit_lane(x,y,degree=2):
    if len(x)<degree+1:return None
    return np.polyfit(y,x,degree)

def evaluate(coeffs,y):
    return np.polyval(coeffs,y)
