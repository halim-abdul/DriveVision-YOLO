RANK={"normal":0,"attention":1,"warning":2,"near":2,"critical":3,"unknown":0,"far":0,"caution":1}

def aggregate_risk(labels):
    if not labels:return "normal"
    return max(labels,key=lambda x:RANK.get(x,0))

def risk_score(labels):
    return max((RANK.get(x,0) for x in labels),default=0)
