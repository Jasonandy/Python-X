from time import time
from threading import Thread

import requests


# 继承Thread类创建自定义的线程类
class DownloadHanlder(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        start_time = time()
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('/' + filename, 'wb') as f:
            f.write(resp.content)
        end_time = time()
        print('Download cost time :%f.2 (s) ' % (end_time - start_time))


def main():
    # 通过requests模块的get函数获取网络资源
    # 下面的代码中使用了天行数据接口提供的网络API
    # 要使用该数据接口需要在天行数据的网站上注册
    # 然后用自己的Key替换掉下面代码的中APIKey即可
    api_url = "http://api.tianapi.com/meinv/?key=APIKey&num=10"
    resp = requests.get(api_url)
    # 将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()
    print(data_model)
    # for mm_dict in data_model['newslist']:
    #     url = mm_dict['picUrl']
    #     # 通过多线程的方式实现图片下载
    #     DownloadHanlder(url).start()


if __name__ == '__main__':
    main()
