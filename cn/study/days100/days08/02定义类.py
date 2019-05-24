"""
定义类对象
"""


# 定义student 对象
class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    # self 有点类似java的this? init 类似Java构造函数?
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # study 学习这个动作
    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是很多程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    # 养成良好的习惯 严格按照标准来执行
    def watch_av(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情动作片.' % self.name)


def main():
    jason = Student("Jason", 16)
    jason.study("Python 100 days.")
    andy = Student("Andy", 23)
    andy.study("爱国动作")
    andy.watch_av()


if __name__ == '__main__':
    main()
