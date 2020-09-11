'''
   1.单例模式（singleton pattern）:某一个类只有一个实例存在
   某个服务器的配置文件
'''


class Singleton(object):
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        # hasattr() 函数用于判断对象是否包含对应的属性
        if not hasattr(Singleton, "_instance"):  # 反射
            Singleton._instance = object.__new__(cls)
        return Singleton._instance


obj1 = Singleton()
obj2 = Singleton()
print(obj1, obj2)
# <__main__.Singleton object at 0x00000162ABACA3C8>
# <__main__.Singleton object at 0x00000162ABACA3C8>


'''
    2.工厂模式：超类提供一个抽象化的接口来创建一个特定类型的对象
    需要创建一个工厂类创建并返回
'''


class Person:
    def __init__(self):
        self.name = None
        self.gender = None

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender


class Male(Person):
    def __init__(self, name):
        print('Hello Mr.' + name)


class Female(Person):
    def __init__(self, name):
        print('Hello Miss.' + name)


class Factory:
    def getPerson(self, name, gender):
        if gender == 'M':
            return Male(name)
        if gender == 'F':
            return Female(name)


if __name__ == '__main__':
    factory = Factory()
    person = factory.getPerson('caicai', 'F')
# 当程序运行输入一个“类型”的时候，需要创建于此相应的对象。
# 在如此情形中，实现代码基于工厂模式，可以达到可扩展，可维护的代码。
# 当增加一个新的类型，不在需要修改已存在的类，只增加能够产生新类型的子类


'''
    3.建造者模式：将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示
'''
from abc import ABCMeta, abstractmethod


# @abstractmethod：抽象方法，含abstractmethod方法的类不能实例化，继承了含abstractmethod方法的子类必须复写所有abstractmethod装饰的方法，未被装饰的可以不重写
class Builder():
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw_left_arm(self):
        pass

    @abstractmethod
    def draw_right_arm(self):
        pass

    @abstractmethod
    def draw_left_foot(self):
        pass

    @abstractmethod
    def draw_right_foot(self):
        pass

    @abstractmethod
    def draw_head(self):
        pass

    @abstractmethod
    def draw_body(self):
        pass


class Thin(Builder):
    def draw_left_arm(self):
        print('画左手')

    def draw_right_arm(self):
        print('画右手')

    def draw_left_foot(self):
        print('画左脚')

    def draw_right_foot(self):
        print('画右脚')

    def draw_head(self):
        print('画头')

    def draw_body(self):
        print('画瘦身体')


class Fat(Builder):
    def draw_left_arm(self):
        print('画左手')

    def draw_right_arm(self):
        print('画右手')

    def draw_left_foot(self):
        print('画左脚')

    def draw_right_foot(self):
        print('画右脚')

    def draw_head(self):
        print('画头')

    def draw_body(self):
        print('画胖身体')


class Director():
    def __init__(self, person):
        self.person = person

    def draw(self):
        self.person.draw_left_arm()
        self.person.draw_right_arm()
        self.person.draw_left_foot()
        self.person.draw_right_foot()
        self.person.draw_head()
        self.person.draw_body()


if __name__ == '__main__':
    thin = Thin()
    fat = Fat()
    director_thin = Director(thin)
    director_thin.draw()
    director_fat = Director(fat)
    director_fat.draw()
# 画左手
# 画右手
# 画左脚
# 画右脚
# 画头
# 画瘦身体
# 画左手
# 画右手
# 画左脚
# 画右脚
# 画头
# 画胖身体


'''
    4.原型模式：指定创建对象的种类，并且通过拷贝这些原型创建新的对象
    本质就是克隆对象，所以在对象初始化操作比较复杂的情况下，很实用，能大大降低耗时，提高性能
'''
import copy
from collections import OrderedDict


class Book:
    def __init__(self, name, authors, price, **rest):
        '''rest的例子有：出版商、长度、标签、出版日期'''
        self.name = name
        self.authors = authors
        self.price = price
        self.__dict__.update(rest)

    def __str__(self):
        mylist = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            mylist.append('{}:{}'.format(i, ordered[i]))
            if i == 'price':
                mylist.append('$')
            mylist.append('\n')
            return ''.join(mylist)


class Prototype:
    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attr):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError('Incorrect object identifier:{}'
                             .format(identifier))
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj


def main():
    b1 = Book('The C Programming Language', ('Brian W. Kernighan', 'Dennis M.Ritchie'),
              price=118, publisher='Prentice Hall', length=228, publication_date='1978-02-22',
              tags=('C', 'programming', 'algorithms', 'data structures'))
    prototype = Prototype()
    cid = 'k&r-first'
    prototype.register(cid, b1)
    b2 = prototype.clone(cid, name='The C Programming Language(ANSI)', price=48.99,
                         length=274, publication_date='1988-04-01', edition=2)
    for i in (b1, b2):
        print(i)
    print("ID b1 : {} != ID b2 : {}".format(id(b1), id(b2)))


if __name__ == '__main__':
    main()
"""
>>> python3 prototype.py
authors: ('Brian W. Kernighan', 'Dennis M. Ritchie')
length: 228
name: The C Programming Language
price: 118$
publication_date: 1978-02-22
publisher: Prentice Hall
tags: ('C', 'programming', 'algorithms', 'data structures')


authors: ('Brian W. Kernighan', 'Dennis M. Ritchie')
edition: 2
length: 274
name: The C Programming Language (ANSI)
price: 48.99$
publication_date: 1988-04-01
publisher: Prentice Hall
tags: ('C', 'programming', 'algorithms', 'data structures')

ID b1 : 140004970829304 != ID b2 : 140004970829472
"""

'''
    5.适配器模式：复用一些现存的类，但是接口又与复用环境要求不一致的情况，比如在需要对早期代码复用一些功能等应用上很有实际价值
'''


# 客户端希望调用的接口
class Target(object):
    def request(self):
        print('普通请求')


# 需要适配的类
class Adaptee(object):
    def specific_request(self):
        print('特殊请求')


# 通过在内部包装一个adaptee对象，把源接口转换成目标接口
class Adapter(Target):
    def __init__(self):
        self.adaptee = Adaptee()

    def request(self):
        self.adaptee.specific_request()


if __name__ == '__main__':
    target = Adapter()
    target.request()


'''
    6.修饰器模式：通常用于扩展一个对象的功能
    装饰器：他们是修改其他函数的功能的函数
'''
import functools

def memoize(fn):
    known = dict()
    @functools.wraps(fn)
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]
    return memoizer

@memoize
def nsum(n):
    '''返回前n个数字的和'''
    assert(n >= 0), 'n must be >= 0'
    return 0 if n == 0 else n + nsum(n-1)

@memoize
def fibonacci(n):
    '''返回斐波那契数列的第n个数'''
    assert (n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    from timeit import Timer
    measure = [{'exec': 'fibonacci(100)', 'import': 'fibonacci',
    'func': fibonacci}, {'exec': 'nsum(200)', 'import': 'nsum',
    'func': nsum}]
    for m in measure:
        t = Timer('{}'.format(m['exec']), 'from __main__ import {}'.format(m['import']))
        print('name: {}, doc: {}, executing: {}, time:{}'.format(m['func'].__name__, m['func'].__doc__, m['exec'], t.timeit()))
