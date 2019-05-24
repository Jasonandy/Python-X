"""
循环结构

"""
from random import randint

sums = 0
for x in range(1, 10):
    print("%s" % x)
    sums += x
print(sums)

# 2 - 101 步长为2
oods = 0
for x in range(2, 101, 2):
    oods += x
print(oods)


# 随机问题
answer = randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入: '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了!')
        break
print('你总共猜了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足')

