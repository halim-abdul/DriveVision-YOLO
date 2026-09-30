from drivevision.tracking.geometry import bbox_iou,center

def test_bbox_iou(): assert abs(bbox_iou((0,0,2,2),(0,0,2,2))-1)<1e-9
def test_center(): assert center((0,0,4,2))==(2.0,1.0)
