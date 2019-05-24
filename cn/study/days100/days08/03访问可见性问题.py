"""
对于上面的代码，有C++、Java、C#等编程经验的程序员可能会问，我们给Student对象绑定的name和age属性到底具有怎样的访问权限（也称为可见性）。
因为在很多面向对象编程语言中，我们通常会将对象的属性设置为私有的（private）或受保护的（protected），简单的说就是不允许外界访问，
而对象的方法通常都是公开的（public），因为公开的方法就是对象能够接受的消息。
在Python中，属性和方法的访问权限只有两种，也就是公开的和私有的，如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头，下面的代码可以验证这一点。
"""

"""
Python并没有从语法上严格保证私有属性或方法的私密性，它只是给私有的属性和方法换了一个名字来“妨碍”对它们的访问，
事实上如果你知道更换名字的规则仍然可以访问到它们，下面的代码就可以验证这一点。
之所以这样设定，可以用这样一句名言加以解释，就是“We are all consenting adults here”。
因为绝大多数程序员都认为开放比封闭要好，而且程序员要自己为自己的行为负责.
"""


# AccessView  访问可见性
class AccessView(object):

    # __ 下划线 python 只有 公开的  和 私有的
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')

    def study(self, what):
        print("--- hello world %s ---" % what)


class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    access_view = AccessView('hello')
    # AttributeError: 'Test' object has no attribute '__bar'
    #accessView.__bar()
    # AttributeError: 'Test' object has no attribute '__foo'
    #print(accessView.__foo)
    access_view.study("python 100 days .")

    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)


if __name__ == "__main__":
    main()


