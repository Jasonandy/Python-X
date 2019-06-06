"""
注意：
1.image[i,j,c]   i表示图片的行数，j表示图片的列数，c表示图片的通道数（0代表B，1代表G，2代表R    一共是RGB三通道）。坐标是从左上角开始
2.每个通道对应一个灰度值。灰度值概念：把白色与黑色之间按对数关系分成若干级，称为“灰度等级”。
范围一般从0到255，白色为255，黑色为0。要详细了解灰度值和通道的概念，
请参考这篇博客：https://blog.csdn.net/silence2015/article/details/53789748
上述代码实现像素取反的运行时间较长，下面代码运用opencv自带的库函数可以使运行时间大大减少。
"""
import cv2 as cv


def inverse(img):
    """
    反转
    :param img:
    :return:
    """
    # 函数cv.bitwise_not可以实现像素点各通道值取反
    img = cv.bitwise_not(img)
    cv.imshow("second_image", img)


def main():
    # blue, green, red
    src = cv.imread("../media/lena/lena.jpg")
    cv.namedWindow('first_image', cv.WINDOW_AUTOSIZE)
    cv.imshow('first_image', src)
    # getTickCount 函数返回从操作系统启动到当前所经过的毫秒数
    t1 = cv.getTickCount()
    inverse(src)
    t2 = cv.getTickCount()
    # getTickFrequency函数返回CPU的频率,就是每秒的计时周期数
    time = (t2-t1)/cv.getTickFrequency()
    # 输出运行时间
    print("time : %s ms" % (time*1000))
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()

