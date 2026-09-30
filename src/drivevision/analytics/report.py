def trip_summary(events,frames,duration_s):
    severities={}
    types={}
    for e in events:
        sev=getattr(e,"severity","unknown");typ=getattr(e,"event_type","unknown")
        severities[sev]=severities.get(sev,0)+1;types[typ]=types.get(typ,0)+1
    return {"frames":frames,"duration_s":duration_s,"events":len(events),"severity_counts":severities,"event_counts":types}
