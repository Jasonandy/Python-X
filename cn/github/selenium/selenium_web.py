"""
操作浏览器
"""
from selenium import webdriver
import time
from tkinter.constants import CURRENT
"""
Message: 'chromedriver' executable needs to be in PATH.
"""


def open_browser():
    # 打开firefox浏览器
    driver = webdriver.Chrome()
    # 打开百度页面
    driver.get("https://www.baidu.com/")
    # 等待页面加载完毕
    time.sleep(5)
    # 刷新页面
    driver.refresh()
    # 打开hao123页面
    driver.get("https://www.hao123.com/")
    time.sleep(5)
    driver.refresh()
    # 返回上一页
    driver.back()
    time.sleep(5)
    # 返回下一页
    driver.forward()
    time.sleep(5)
    # 设置屏幕尺寸
    driver.set_window_size(560, 960, CURRENT)
    time.sleep(5)
    # 最大化窗口
    driver.maximize_window()
    time.sleep(5)
    driver.refresh()
    # 截图并指定路径、文件名保存
    driver.get_screenshot_as_file("../captcha.jpg")
    # 退出浏览器，close()是关闭当前访问页面，quit()是退出浏览器，结束进程，且回收临时文件
    driver.quit()


def main():
    open_browser()


if __name__ == '__main__':
    main()

