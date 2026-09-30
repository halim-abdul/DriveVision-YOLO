def point_in_polygon(point,polygon):
    x,y=point;inside=False;j=len(polygon)-1
    for i,(xi,yi) in enumerate(polygon):
        xj,yj=polygon[j]
        if ((yi>y)!=(yj>y)) and x<(xj-xi)*(y-yi)/(yj-yi+1e-12)+xi:inside=not inside
        j=i
    return inside

def assign_zone(point,zones):
    return next((name for name,poly in zones.items() if point_in_polygon(point,poly)),None)
