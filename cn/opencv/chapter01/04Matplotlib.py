"""
利用matplotlib去显示图像。

"""
import cv2
from matplotlib import pyplot as plt


def show_image():
    img = cv2.imread('../media/lena/lena.jpg', cv2.IMREAD_COLOR)
    plt.imshow(img)
    plt.show()


if __name__ == '__main__':
    show_image()

