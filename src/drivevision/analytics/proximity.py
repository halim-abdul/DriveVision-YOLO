def nearest_object(objects):
    valid=[o for o in objects if getattr(o,"distance_m",float("nan"))==getattr(o,"distance_m",float("nan"))]
    return min(valid,key=lambda o:o.distance_m) if valid else None

def objects_within(objects,distance_m):
    return [o for o in objects if getattr(o,"distance_m",float("inf"))<=distance_m]
