"""
除了使用文件对象的read方法读取文件之外，还可以使用for-in循环逐行读取
或者用readlines方法将文件按行读取到一个列表容器中，代码如下所示

"""
import time


def main():
    # 一次性读取整个文件内容
    with open('readme.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('readme.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    # 换行处理
    print()
    """
    HelloWorld
    My Name is Jason
    Yes
    Thanks the project form github
    
    100 days learn Python
    """

    # 读取文件按行读取到列表中
    with open('readme.txt') as f:
        lines = f.readlines()
    print(lines)
    """
    ['HelloWorld\n', 'My Name is Jason\n', 'Yes\n', 'Thanks the project form github\n', '\n', '100 days learn Python\n', '\n', 'sounds interesting things']
    """


if __name__ == '__main__':
    main()

