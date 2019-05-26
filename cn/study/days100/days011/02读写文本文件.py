"""
读取文本文件时，需要在使用open函数时指定好带路径的文件名（可以使用相对路径或绝对路径）并将文件模式设置为'r'（如果不指定，默认值也是'r'），
然后通过encoding参数指定编码（如果不指定，默认值是None，那么在读取文件时使用的是操作系统默认的编码），
如果不能保证保存文件时使用的编码方式与encoding参数指定的编码方式是一致的，那么就可能因无法解码字符而导致读取失败。
下面的例子演示了如何读取一个纯文本文件。

"""


def no_exception():
    """
    为了使程序更加健壮  加入异常判断机制
    :return:
    """
    f = open('readme.txt', 'r', encoding='utf-8')
    print(f.read())
    f.close()


def has_exception():
    """
    加入异常的判断机制
    :return:
    """
    f = None
    try:
        # f = open('read.me.txt', 'r', encoding='utf-8')
        f = open('readme.txt', 'r', encoding='utf-8')
    except FileNotFoundError:
        print('FileNotFoundError!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        """
         finally块的代码不论程序正常还是异常都会执行到（甚至是调用了sys模块的exit函数退出Python环境
         finally块都会被执行，因为exit函数实质上是引发了SystemExit异常），因此我们通常把finally块称为“总是执行代码块”，
         它最适合用来做释放外部资源的操作
        """
        if f:
            f.close()


def main():
    no_exception()
    has_exception()


if __name__ == '__main__':
    main()

