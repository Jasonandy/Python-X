"""
通过上面的讲解，我们已经知道如何将文本数据和二进制数据保存到文件中，那么这里还有一个问题，
如果希望把一个列表或者一个字典中的数据保存到文件中又该怎么做呢？答案是将数据以JSON格式进行保存
。JSON是“JavaScript Object Notation”的缩写，它本来是JavaScript语言中创建对象的一种字面量语法，
现在已经被广泛的应用于跨平台跨语言的数据交换，原因很简单，因为JSON也是纯文本，任何系统任何编程语言处理纯文本都是没有问题的。
目前JSON基本上已经取代了XML作为异构系统间交换数据的事实标准。

关于JSON的知识，更多的可以参考JSON的官方网站，
从这个网站也可以了解到每种语言处理JSON数据格式可以使用的工具或三方库，下面是一个JSON的简单例子。

object	dict
array	list
string	str
number (int / real)	int / float
true / false	True / False
null	None


Python	JSON
dict	object
list, tuple	array
str	string
int, float, int- & float-derived Enums	number
True / False	true / false
None	null

dump - 将Python对象按照JSON格式序列化到文件中
dumps - 将Python对象处理成JSON格式的字符串
load - 将文件中的JSON数据反序列化成对象
loads - 将字符串的内容反序列化成Python对象

"""
import json


def main():
    mydict = {
        'name': 'Jason',
        'age': 38,
        'qq': 957658,
        'friends': ['Andy', 'Tuna'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
        # with open('data.json', 'r', encoding='utf-8') as fsr:
            # json.dumps(mydict, fsr)
    except IOError as e:
        print(e)
    print('保存数据完成!')


if __name__ == '__main__':
    main()
