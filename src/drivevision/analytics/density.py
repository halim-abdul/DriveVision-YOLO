def traffic_density(objects,area_px):
    return len(objects)/max(float(area_px),1.0)

def class_counts(objects):
    out={}
    for obj in objects:
        name=getattr(obj,"class_name","unknown")
        out[name]=out.get(name,0)+1
    return out
