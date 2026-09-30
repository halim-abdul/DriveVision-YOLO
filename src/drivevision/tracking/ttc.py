def ttc_from_distance(distance_m,closing_speed_mps):
    if closing_speed_mps<=0:return float("inf")
    return max(0.0,distance_m/closing_speed_mps)

def risk_level(ttc):
    if ttc<1.5:return "critical"
    if ttc<3.0:return "warning"
    if ttc<6.0:return "attention"
    return "normal"
