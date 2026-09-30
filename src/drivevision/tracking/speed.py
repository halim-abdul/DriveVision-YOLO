import math

def pixel_speed(history,fps):
    if len(history)<2:return 0.0
    return math.dist(history[-2],history[-1])*fps

def metric_speed(history,fps,meters_per_pixel):
    return pixel_speed(history,fps)*meters_per_pixel
