import argparse
import cv2
from drivevision.lanes.pipeline import LanePipeline

p=argparse.ArgumentParser();p.add_argument("source");a=p.parse_args()
cap=cv2.VideoCapture(a.source);pipeline=LanePipeline()
while cap.isOpened():
    ok,frame=cap.read()
    if not ok:break
    mask=pipeline.binary(frame)
    cv2.imshow("DriveVision lanes",mask)
    if cv2.waitKey(1)&0xFF==27:break
cap.release();cv2.destroyAllWindows()
