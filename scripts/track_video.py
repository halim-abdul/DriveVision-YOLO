import argparse
import cv2
from drivevision.tracking.tracker import MultiObjectTracker
from drivevision.tracking.visualize import draw_tracks

p=argparse.ArgumentParser();p.add_argument("source");a=p.parse_args()
cap=cv2.VideoCapture(a.source);tracker=MultiObjectTracker()
while cap.isOpened():
    ok,frame=cap.read()
    if not ok:break
    # Connect detector outputs here: tracker.update(detections)
    vis=draw_tracks(frame,tracker.tracks)
    cv2.imshow("DriveVision tracking",vis)
    if cv2.waitKey(1)&0xFF==27:break
cap.release();cv2.destroyAllWindows()
