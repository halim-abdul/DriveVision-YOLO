def lane_width_valid(left_x,right_x,min_px=350,max_px=900):
    width=right_x-left_x
    return min_px<=width<=max_px

def curvature_consistent(left_radius,right_radius,ratio_limit=3.0):
    small=max(min(left_radius,right_radius),1e-9)
    return max(left_radius,right_radius)/small<=ratio_limit
