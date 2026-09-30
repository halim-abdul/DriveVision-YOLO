def event_precision(tp,fp):return tp/max(tp+fp,1)
def event_recall(tp,fn):return tp/max(tp+fn,1)
def false_alerts_per_hour(false_alerts,duration_s):return false_alerts/max(duration_s/3600.0,1e-9)
