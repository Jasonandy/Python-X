# 语音播报模块
import pyttsx3

# 模块初始化
engine = pyttsx3.init()

print('准备开始语音播报...')

for num in range(1, 20):

    # 设置要播报的Unicode字符串
    engine.say("黄莹 黄莹 你是大傻子 黄莹 莹 黄莹 黄莹 黄莹 ")

# 等待语音播报完毕
engine.runAndWait()
