"""

"""
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../media/lena/lena.jpg', cv2.IMREAD_COLOR)


def mtd_one():
    b, g, r = cv2.split(img)
    img2 = cv2.merge([r, g, b])
    plt.imshow(img2)
    plt.show()


def mtd_two():
    img3 = img[:, :, ::-1]
    plt.imshow(img3)
    plt.show()


def mtd_three():
    img4 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img4)
    plt.show()


def main():
    mtd_one()
    mtd_two()
    mtd_three()


if __name__ == '__main__':
    main()

