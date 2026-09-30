import cv2

def lane_edges(frame,blur_kernel=5,canny_low=50,canny_high=150):
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(blur_kernel,blur_kernel),0)
    return cv2.Canny(blur,canny_low,canny_high)
