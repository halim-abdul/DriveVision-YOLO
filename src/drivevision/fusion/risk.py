def distance_risk(distance_m, near=8.0, caution=20.0):
    if distance_m != distance_m: return "unknown"
    if distance_m < near: return "near"
    if distance_m < caution: return "caution"
    return "far"
