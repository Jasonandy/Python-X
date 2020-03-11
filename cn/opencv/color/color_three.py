import numpy as np
import cv2

red_lower = np.array([0,43,46])
red_upper = np.array([10,255,255])
blue_lower = np.array([100,43,46])
blue_upper = np.array([124,255,255])
cap = cv2.VideoCapture(0)

cap.set(3,320)
cap.set(4,240)
def ChestRed():
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, red_lower, red_upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.GaussianBlur(mask, (3, 3), 0)
    return mask
def ChestBule():
    ret, frame = cap.read()
    frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, blue_lower, blue_upper)
    mask = cv2.GaussianBlur(mask, (3, 3), 0)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    if 25 < len(cnts) < 29:
        print("Blue!")
while 1:
    ret,frame = cap.read()
    frame = cv2.GaussianBlur(frame,(5,5),0)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = ChestRed()
    ChestBule()
    res = cv2.bitwise_and(frame,frame,mask=mask)
    cnts = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    if 20<len(cnts)<30:
        print("Red!")

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    if cv2.waitKey(5) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()