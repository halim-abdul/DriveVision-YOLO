import cv2

def video_frames(source):
    cap = cv2.VideoCapture(source)
    idx = 0
    try:
        while cap.isOpened():
            ok, frame = cap.read()
            if not ok: break
            yield idx, frame
            idx += 1
    finally:
        cap.release()
