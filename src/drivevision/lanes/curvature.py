import numpy as np

def curvature_radius(coeffs,y_eval,ym_per_pix=30/720,xm_per_pix=3.7/700):
    a,b,_=coeffs
    a_m=xm_per_pix/(ym_per_pix**2)*a
    b_m=xm_per_pix/ym_per_pix*b
    y_m=y_eval*ym_per_pix
    return ((1+(2*a_m*y_m+b_m)**2)**1.5)/max(abs(2*a_m),1e-9)
