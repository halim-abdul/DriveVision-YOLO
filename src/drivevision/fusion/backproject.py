def backproject(u,v,depth,intrinsics):
    x=(u-intrinsics.cx)*depth/intrinsics.fx
    y=(v-intrinsics.cy)*depth/intrinsics.fy
    return (x,y,depth)
