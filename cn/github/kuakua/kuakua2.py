"""
夸夸群 V1.0.0

"""
import itchat
import re
from itchat.content import *
import random

groupName = '中央巡视组'
peopleName = '冯浩'
peopleName2 = '刘中坡'


REPLY = {
    "default": [
        "你真厉害",
        "没什么好说的了，我送你一道彩虹屁吧",
        "不知道该说什么，那就对了，语言是苍白的，完全无法表达您内涵的深度！",
        "这么优秀的人，让我们的语言也顿时显得匮乏了起来，没有语言能真正地说尽你的优秀，没有任何夸奖能真正配得上你！",
        "上天太偏心了，为什么要把所有的优点都集中在你身上"
    ],
    "dot": [
        "这个省略号用得好，千言万语尽在其中，懂得留白，人生更精彩",
        "哇，太厉害了，这两个句号比我用圆规画出来的还要圆润、有光泽，就好似两颗珍珠，又像极了小姐姐的眼眸，清澈透亮"
    ],
    "man": [
        "人间人爱，花见花开。"
    ],
    "money": [
        "非常有经济头脑，理财一定日进斗金吧！我想和你学理财！",
        "你是我见过最有时间观念的人了！"
    ],
    "question": [
        "面对这未知的群，小姐姐有问题就问，这种直率和勇气不可多得",
        "您这个发问，展示了强烈的好奇心，好奇心是进步的源泉，相信生活中你也是一个充满好奇心的人，用于探索未知，有一双发现新奇的眼睛，你真棒"
    ],
    "spot": [
        "每一句都会用逗号和句号，看来是一位知书达理，性格严谨有度，丝毫不拖泥带水的大家闺秀。"
    ],
    "study": [
        "这么多优秀的同龄人相聚在这里，一定是场思想交流的盛宴。",
        "看到群友们的发言，真是排山倒海，气宇轩昂之势！",
        "你这句话完美的表达了你想被夸的坚定信念，你一定是一个执着追求自己理想的人！"
    ],
    "time": [
        "充实的人生，棒！",
        "优秀如你"
    ],
    "women": [
        "哇小姐姐的头像真好看",
        "如出水芙蓉，天然雕饰，天哪，这世间怎么会有这么好看的人",
        "你是今天这么漂亮，还是每天都这么漂亮啊",
        "在人流中，我一眼就发现了你，我不敢说你是他们中最漂亮的一个，可是我敢说，你是她们中最出色的一个",
        "每天都是在想想想你的，爆炸的想你"
    ],
    "work": [
        "且不说你的工作多么认真，我并没有见过，但是从你的字里行间，我发现了乔布斯的影子和小扎的气息，这已经不是一份工作那么简单，而是一场精神饕餮！",
        "你拥有了这个年龄段近半数人无法拥有的理想职业，太优秀了！",
        "工作这件事，大家都习以为常，只有你让大家开始思考这个问题，说明你善于反思和质疑当前的制度，你的公司会因为你这样的人变得更好！"
    ]
}


def check_work(msg):
    """
    检测work
    :param msg:
    :return:
    """
    return re.search(r'加班', msg) or re.search(r'上班', msg) or re.search(r'工作', msg)


def check_study(msg):
    """
    学习
    :param msg:
    :return:
    """
    return re.search(r'学习', msg) or re.search(r'上课', msg) or re.search(r'作业', msg)


def check_question(msg):
    """
    提问
    :param msg:
    :return:
    """
    return re.search('\?', msg) or re.search('？', msg) or re.search('吗?', msg)


def check_dot(msg):
    """
    checkDot
    :param msg:
    :return:
    """
    return re.search('\.\.', msg) or re.search('。。', msg)


def check_spot(msg):
    """
    checkSpot
    :param msg:
    :return:
    """
    return re.search(',+', msg) or re.search('，+', msg) or re.search('。+', msg)


def check_money(msg):
    """
    checkMoney
    :param msg:
    :return:
    """
    return re.search(r'经济', msg) or re.search(r'钱', msg) or re.search(r'利润', msg)


def check_time(msg):
    """
    checktTime
    :param msg:
    :return:
    """
    return re.search(r'时间', msg) or re.search(r'忙', msg) or re.search(r'闲', msg)


# 监听获取消息
@itchat.msg_register(TEXT, isGroupChat=True)
def getNoteGroup(msg):
    if(msg['User']['NickName']==groupName):
        print('receive: %s ' % msg['Text'])
        print('from:%s ' % msg['ActualNickName'])
        if(msg['ActualNickName'] == peopleName or msg['ActualNickName'] == peopleName2):
            # pprint.pprint(msg)
            print('receive:'+msg['Text'])
            matchDefault = False
            try:
                match_work = check_work(msg['Text'])
                match_study = check_study(msg['Text'])
                match_question = check_question(msg['Text'])
                match_dot = check_dot(msg['Text'])
                match_spot = check_spot(msg['Text'])
                match_money = check_money(msg['Text'])
                match_time = check_time(msg['Text'])
                if(not(match_study or match_work or match_question or match_dot or match_spot or match_money or match_time )):
                    matchDefault = True
                if(match_work):
                    itchat.send(random.choice(REPLY['work']), msg['User']['UserName'])
                if(match_study):
                    itchat.send(random.choice(REPLY['study']), msg['User']['UserName'])
                if(match_question):
                    itchat.send(random.choice(REPLY['question']), msg['User']['UserName'])
                if(match_dot):
                    itchat.send(random.choice(REPLY['dot']), msg['User']['UserName'])
                if(match_spot):
                    itchat.send(random.choice(REPLY['spot']), msg['User']['UserName'])
                if(match_money):
                    itchat.send(random.choice(REPLY['money']), msg['User']['UserName'])
                if(match_time):
                    itchat.send(random.choice(REPLY['time']), msg['User']['UserName'])
            except:
                matchDefault = True
            if(matchDefault):
                itchat.send(random.choice(REPLY['default']+REPLY['women']), msg['User']['UserName'])


def main():
    # 登录
    itchat.auto_login(hotReload=True)
    # 运行监控
    itchat.run()
    # 退出登录
    itchat.logout()


# execute it
if __name__ == '__main__':
    main()

