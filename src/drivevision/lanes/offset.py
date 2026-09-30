def lateral_offset_m(left_x,right_x,image_width,xm_per_pix=3.7/700):
    lane_center=(left_x+right_x)/2.0
    vehicle_center=image_width/2.0
    return (vehicle_center-lane_center)*xm_per_pix
