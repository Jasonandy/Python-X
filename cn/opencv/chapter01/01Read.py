"""
read picture
"""
import cv2


def read_picture(path):
    """
    读取图片
    :return:
    """
    img = cv2.imread(path)
    cv2.namedWindow("OPEN_CV_READ_IMG")
    cv2.imshow("OPEN_CV_READ_IMG", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    path = "../media/lena/lena.jpg"
    read_picture(path)
