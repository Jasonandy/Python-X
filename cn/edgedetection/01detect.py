"""
边缘检测学习
参考：https://www.jianshu.com/p/baffc1e30952

Canny边缘检测方法常被誉为边缘检测的最优方法

"""
import cv2


def read_image(image_path):
    """
    读取图片
    :param image_path:
    :return:
    """
    img = cv2.imread(image_path, 0)
    return img


def show_image(image_path):
    """
    展示图片
    :param image_path: 图片路径
    :return:
    """
    src = cv2.imread(image_path, 0)
    cv2.namedWindow('first_image', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('first_image', src)
    cv2.waitKey(0)


def edges_image(image):
    """
    图片边缘检测
    :param image:
    :return:
    """
    # 其实有时候阈值分割后在边缘会比较好 丢弃第一个返回值
    _, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # canny边缘检测
    edges = cv2.Canny(thresh, 30, 70)
    cv2.namedWindow('second_image', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('second_image', edges)
    cv2.waitKey(0)
    print(edges)


def show_all_image():
    """
    展示所有的图片
    :return:
    """
    show_image()
    edges_image()
    cv2.destroyAllWindows()


def run(image_path):
    show_image(image_path)
    edges_image(read_image(image_path))


if __name__ == '__main__':
    # run("media/lena/lena.jpg")
    run("media/13.jpg")


