SIGN_GROUPS={
    "speed_limit": {"speed_20","speed_30","speed_50","speed_60","speed_80","speed_100","speed_120"},
    "priority": {"yield","stop","priority_road"},
    "restriction": {"no_entry","no_overtaking","end_restrictions"},
    "warning": {"pedestrian_crossing","road_work","children","slippery_road"},
}

def sign_group(label):
    return next((group for group,labels in SIGN_GROUPS.items() if label in labels),"other")
