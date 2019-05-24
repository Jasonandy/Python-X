"""
分支结构的应用场景
迄今为止，我们写的Python代码都是一条一条语句顺序执行，这种结构的代码我们称之为顺序结构。
然而仅有顺序结构并不能解决所有的问题，比如我们设计一个游戏，游戏第一关的通关条件是玩家获得1000分，
那么在完成本局游戏后我们要根据玩家得到分数来决定究竟是进入第二关还是告诉玩家“Game Over”，这里就会产生两个分支，
而且这两个分支只有一个会被执行，这就是程序中分支结构。
类似的场景还有很多，给大家一分钟的时间，你应该可以想到至少5个以上这样的例子，赶紧试一试。

"""
from random import randint


username = input('请输入用户名: ')
password = input('请输入口令: ')
# 如果希望输入口令时 终端中没有回显 可以使用getpass模块的getpass函数
# import getpass
# password = getpass.getpass('请输入口令: ')
if username == 'admin' and password == '123456':
    print('身份验证成功!')
else:
    print('身份验证失败!')

"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
"""

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
#  %.2f 精确几位
print('f(%.2f) = %.2f' % (x, y))


value = float(input('请输入长度: '))
unit = input('请输入单位: ')
if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英寸' % (value, value / 2.54))
else:
    print('请输入有效的单位')

# random.randint 随机一个数
face = randint(1, 6)
if face == 1:
    result = '唱首歌'
elif face == 2:
    result = '跳个舞'
elif face == 3:
    result = '学狗叫'
elif face == 4:
    result = '做俯卧撑'
elif face == 5:
    result = '念绕口令'
else:
    result = '讲冷笑话'
print(result)
