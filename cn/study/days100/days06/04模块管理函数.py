"""
对于任何一种编程语言来说，给变量、函数这样的标识符起名字都是一个让人头疼的问题，因为我们会遇到命名冲突这种尴尬的情况。
最简单的场景就是在同一个.py文件中定义了两个同名函数，由于Python没有函数重载的概念，
那么后面的定义会覆盖之前的定义，也就意味着两个函数同名函数实际上只有一个是存在的。
"""


def foo():
    print("HelloWorld-foo-1!")


def foo():
    print("HelloWorld-foo-2!")


def bar():
    print("=== bar ===")


# 猜想一下 这里会打印出什么
foo()


"""
 那么如何来避免上述的情况呢？
 很显然我们知道每个文件的名字都是不同的
 那么我们可以用模块的方式引用不同的方法语句
"""

# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    foo()
    print("*******************")
    bar()
    print("*******************")


