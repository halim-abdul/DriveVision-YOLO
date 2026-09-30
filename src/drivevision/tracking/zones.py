def point_in_polygon(point,polygon):
    x,y=point;inside=False;j=len(polygon)-1
    for i,(xi,yi) in enumerate(polygon):
        xj,yj=polygon[j]
        if ((yi>y)!=(yj>y)) and x<(xj-xi)*(y-yi)/(yj-yi+1e-12)+xi:inside=not inside
        j=i
    return inside

def occupancy(tracks,polygon):
    count=0
    for t in tracks:
        if not t.history:continue
        if point_in_polygon(t.history[-1],polygon):count+=1
    return count
