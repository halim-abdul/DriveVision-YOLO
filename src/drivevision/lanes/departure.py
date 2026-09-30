def departure_state(offset_m,warning=0.35,critical=0.65):
    a=abs(offset_m)
    if a>=critical:return "critical"
    if a>=warning:return "warning"
    return "centered"
