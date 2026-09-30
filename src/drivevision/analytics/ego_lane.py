def center_x(box):
    x1,_,x2,_=box
    return (x1+x2)/2.0

def in_ego_lane(obj,left_x,right_x):
    x=center_x(obj.xyxy)
    return left_x<=x<=right_x

def ego_lane_objects(objects,left_x,right_x):
    return [o for o in objects if in_ego_lane(o,left_x,right_x)]
