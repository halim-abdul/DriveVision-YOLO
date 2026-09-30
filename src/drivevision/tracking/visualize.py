import cv2

def draw_tracks(frame,tracks):
    out=frame.copy()
    for t in tracks:
        x1,y1,x2,y2=map(int,t.xyxy)
        cv2.rectangle(out,(x1,y1),(x2,y2),(255,200,0),2)
        cv2.putText(out,f"#{t.track_id} {t.class_name}",(x1,max(18,y1-5)),cv2.FONT_HERSHEY_SIMPLEX,.5,(255,200,0),1,cv2.LINE_AA)
        pts=[tuple(map(int,p)) for p in t.history[-30:]]
        for a,b in zip(pts,pts[1:]):cv2.line(out,a,b,(255,200,0),1)
    return out
