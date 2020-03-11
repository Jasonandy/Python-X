import cv2
import sys
import os
import numpy as np


# 从图像列表创建数据矩阵
def createDataMatrix(images):
    print('Creating data matrix', end='...')
    '''
    在一个数据矩阵中为所有图像分配空间。
   数据矩阵的大小是

   （w * h * 3，numImages）
     其中：
   w：数据集中图像的宽度。
   h：数据集中图像的高度。
   3：3颜色通道。
    '''
    numImages = len(images)
    sz = images[0].shape
    data = np.zeros((numImages, sz[0] * sz[1] * sz[2]), dtype=np.float32)

    for i in range(0, numImages):
        image = images[i].flatten()
        data[i, :] = image

    print('DONE')
    return data


# 从文件目录读取图片
def readImages(path):
    print('Reading images from ' + path, end='...')
    # 创建一个图片数组
    images = []
    # 列出目录中的所有文件，逐个从文本文件中读取点
    for filePath in sorted(os.listdir(path)):
        fileExt = os.path.splitext(filePath)[1]
        if fileExt in ['.jpg', '.jpeg']:
            # 将读取的图片添加到图片数组
            imagePath = os.path.join(path, filePath)
            im = cv2.imread(imagePath)

            if im is None:
                print('image:{} not read properly'.format(imagePath))
            else:
                # 将图片转换为浮点类型
                im = np.float32(im) / 255.0
                # 将图片添加到数组中
                images.append(im)
                # 翻转图片
                imFlip = cv2.flip(im, 1)
                # 将翻转后的图片添加到数组中
                images.append(imFlip)

    numImages = len(images) / 2
    # 当没有图片时退出
    if numImages == 0:
        print('No images found')
        sys.exit(0)

    print(str(numImages) + ' files read.')
    return images


# 将加权的eigen faces添加到mean faces
def createNewFace(*args):
    # 从mean image开始
    output = averageFace

    # 将权值添加到Eigen Faces
    for i in range(0, NUM_EIGEN_FACES):
        '''
        OpenCV不允许滑块值为负数。
        所以使用weight = sliderValue  -  MAX_SLIDER_VALUE / 2
        '''
        sliderValues[i] = cv2.getTrackbarPos("Weight" + str(i), 'Trackbars')
        weight = sliderValues[i] - MAX_SLIDER_VALUE / 2
        output = np.add(output, eigenFaces[i] * weight)

    # 用2x大小显示结果
    output = cv2.resize(output, (0, 0), fx=2, fy=2)
    cv2.imshow('Result', output)


#     cv2.imwrite('result.jpg', output)


def resetSliderValues(*args):
    for i in range(0, NUM_EIGEN_FACES):
        cv2.setTrackbarPos('Weight' + str(i), 'Trackbars', int(MAX_SLIDER_VALUE / 2))
    createNewFace()


# EigenFaces的数量
NUM_EIGEN_FACES = 10

# 最大的权值
MAX_SLIDER_VALUE = 255

# 图片路径
dirName = './'

# 读取图片
images = readImages(dirName)

# 为PCA创建数组矩阵
data = createDataMatrix(images)

# 从创建的图像堆栈中计算特征向量（eigenvectors）
print('Calculating PCA ', end='...')
mean, eigenVectors = cv2.PCACompute(data, mean=None, maxComponents=NUM_EIGEN_FACES)
print('DONE')

#  images 的大小
sz = images[0].shape
averageFace = mean.reshape(sz)

eigenFaces = []

for eigenVector in eigenVectors:
    eigenFace = eigenVector.reshape(sz)
    eigenFaces.append(eigenFace)

# 创建一个窗口用于显示mean face
cv2.namedWindow("Result", cv2.WINDOW_AUTOSIZE)
# 显示结果
output = cv2.resize(averageFace, (0, 0), fx=2, fy=2)
cv2.imshow('Result', output)
# cv2.imwrite('result1.jpg', output)

sliderValues = []
# 创建Trackbars
for i in range(0, NUM_EIGEN_FACES):
    sliderValues.append(MAX_SLIDER_VALUE / 2)
    cv2.createTrackbar('Weight' + str(i), 'Trackbars', int(MAX_SLIDER_VALUE / 2), MAX_SLIDER_VALUE, createNewFace)

# 通过鼠标点击事件重置slider
cv2.setMouseCallback('Result', resetSliderValues)
print('''Usage:
Change the weights using the sliders
Click on the result window to reset sliders
Hit ESC to terminate program.''')

cv2.waitKey(0)
cv2.destroyAllWindows()