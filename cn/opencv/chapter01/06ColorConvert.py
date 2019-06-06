"""
彩色空间转换
"""
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2 as cv
from pylab import subplot, plt, imshow, title, axis, show
from matplotlib.font_manager import FontProperties


def convert_color():
    font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=14)
    # 载入图像
    im = cv.imread('../media/lena/lena.jpg')
    # 颜色空间转换
    gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
    # 显示原始图像
    plt.figure()
    subplot(121)
    plt.gray()
    imshow(im)
    title(u'THIS IS 彩色图', fontproperties=font)
    axis('off')
    # 显示灰度化图像
    plt.subplot(122)
    plt.gray()
    imshow(gray)
    title(u'THIS IS 灰度图', fontproperties=font)
    axis('off')
    show()


def main():
    convert_color()


if __name__ == '__main__':
    main()

