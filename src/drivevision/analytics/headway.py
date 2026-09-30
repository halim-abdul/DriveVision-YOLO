def time_headway(distance_m,ego_speed_mps):
    if ego_speed_mps<=0:return float("inf")
    return max(0.0,distance_m/ego_speed_mps)

def headway_state(seconds):
    if seconds<1.0:return "critical"
    if seconds<2.0:return "warning"
    return "normal"
