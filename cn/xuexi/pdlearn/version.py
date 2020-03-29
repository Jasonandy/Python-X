import requests


# 获取当前版本信息
def up_info():
    print("\n正在联网获取更新信息...")
    # 版本信息
    __Version = "v2.5"
    # 版本描述
    __INFO = "开源学习强国地址 https://github.com/Alivon/Panda-Learning"
    try:
        # 联网获取最新版本号
        updata_log = requests.get(
        "https://raw.githubusercontent.com/Alivon/Panda-Learning/master/Update%20log").content.decode("utf8")
        updata_log = updata_log.split("\n")
        print(__INFO)
        print("程序版本为：{}，\n最新版本为：{}".format(__Version, updata_log[1].split("=")[1]))
        print("="*120)
        # 如果版本不一致表示不是同一个版本 那么需要更新版本
        if __Version != updata_log[1].split("=")[1]:
            print("当前不是最新版本，建议更新")
            print("=" * 120)
            print("更新提要：")
            # 打印更新的内容
            for i in updata_log[2:]:
                print(i)
        print("=" * 120)
        print("更新显示不会打断之前输入等操作，请继续......（若已输入用户标记直接enter）")
    except:
        print("版本信息网络错误")


# 主函数入口 提示更新信息
if __name__ == '__main__':
    up_info()

