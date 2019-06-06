"""
改变通道 图片的 改变图片每个像素点每个通道的灰度值
"""
import cv2 as cv


# 遍历访问图片每个像素点，并修改相应的RGB
def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("width: %s  height: %s  channels: %s" % (width, height, channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                # 获取每个像素点的每个通道的数值
                pv = image[row, col, c]
                # 灰度值是0-255   这里是修改每个像素点每个通道灰度值
                image[row, col, c] = 255 - pv
    cv.imshow("second_image", image)


def main():
    # blue, green, red
    src = cv.imread("../media/lena/lena.jpg")
    cv.namedWindow('first_image', cv.WINDOW_AUTOSIZE)
    cv.imshow('first_image', src)
    # GetTickCount函数返回从操作系统启动到当前所经过的毫秒数
    t1 = cv.getTickCount()
    # 处理后的图片
    access_pixels(src)
    t2 = cv.getTickCount()
    # getTickFrequency 函数返回CPU的频率,就是每秒的计时周期数
    time = (t2 - t1) / cv.getTickFrequency()
    # 输出运行时间
    print("time : %s ms" % (time * 1000))
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()

