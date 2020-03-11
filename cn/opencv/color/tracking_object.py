import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # 获取摄像头视频

while True:
    ret, frame = cap.read()  # 读取每一帧图片
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # 将每一帧图片转化HSV空间颜色
    """
    依据之前的脚本获取的阈值设置最高值与最低值
    """
    lower = np.array([0, 104, 205])
    upper = np.array([15, 208, 255])

    mask = cv2.inRange(hsv_frame, lower, upper)
    img, conts, hier = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 找出边界
    cv2.drawContours(frame, conts, -1, (0, 255, 0), 3)  # 画出边框
    dst = cv2.bitwise_and(frame, frame, mask=mask)  # 对每一帧进行位与操作，获取追踪图像的颜色
    # cv2.imshow("mask",mask)
    # cv2.imshow("dst",dst)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xff == 27:
        break

cv2.destroyAllWindows()
