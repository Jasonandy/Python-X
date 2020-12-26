import cv2 as cv

def face_detect_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY) # 在灰度图像基础上实现的
    face_detector = cv.CascadeClassifier("./haarcascade_frontalface_default.xml")  # 级联检测器获取文件
    faces = face_detector.detectMultiScale(gray, 1.1, 2)    # 在多个尺度空间上进行人脸检测
    # 第一个参数是灰度图像
    # 第二个参数是尺度变换，就是向上或者向下每次是原来的多少倍，这里是1.02倍
    # 第三个参数是人脸检测次数，设置越高，误检率越低，但是对于迷糊图片，我们设置越高，越不易检测出来，要试单降低
    for x,y,w,h in faces:
        cv.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
    cv.imshow("face_detection",image)


def video_face_detect():
    # capture = cv.VideoCapture(0)
    capture = cv.VideoCapture(0, cv.CAP_DSHOW)
    while True:
        ret, frame = capture.read()  # frame是每一帧图像，ret是返回值，为0是表示图像读取完毕
        frame = cv.flip(frame,1)
        if ret == False:
            break
        face_detect_demo(frame)
        c = cv.waitKey(10)
        if c == 27:
            break


if __name__ == '__main__':
    video_face_detect()
    cv.waitKey(0)  # 等待用户操作，里面等待参数是毫秒，我们填写0，代表是永远，等待用户操作
    cv.destroyAllWindows()  # 销毁所有窗口

