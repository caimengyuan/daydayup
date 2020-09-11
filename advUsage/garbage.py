'''
    查看一个对象的引用计数
    可以查看a对象的引用计数，但是比正常计数大1，因为调用函数的时候传入a，这会让a的引用计数+1
'''
import sys
a = 'hello world'
print(sys.getrefcount(a))


'''
    循环引用导致内存泄露
    执行f2()，进程占用的内存会不断增大。
    创建了c1，c2后这两块内存的引用计数都是1，执行c1.t=c2和c2.t=c1后，这两块内存的引用计数变成2.
    在del c1后，内存1的对象的引用计数变为1，由于不是为0，所以内存1的对象不会被销毁，所以内存2的对象的引用数依然是2，
    在del c2后，同理，内存1的对象，内存2的对象的引用数都是1。
    虽然它们两个的对象都是可以被销毁的，但是由于循环引用，导致垃圾回收器都不会回收它们，所以就会导致内存泄露。
'''
import gc


class ClassA():
    def __init__(self):
        print('object born, id: %s' % str(hex(id(self))))


def f2():
    while True:
        c1 = ClassA()
        c2 = ClassA()
        c1.t = c2
        c2.t = c1
        del c1
        del c2

# 把python的gc关闭
# gc.disable()
# f2()


'''
    垃圾回收
'''
class ClassB():
    def __init__(self):
        print('object born, id:%s' % str(hex(id(self))))


def f3():
    print("-----0-------")
    c1 = ClassB()
    c2 = ClassB()
    c1.t = c2
    c2.t = c1
    print("------1------")
    del c1
    del c2
    print("-------2-------")
    print(gc.garbage)
    print("-------3-------")
    print(gc.collect())  # 显示执行垃圾回收
    print("-------4-------")
    print(gc.garbage)
    print("-------5-------")


if __name__ == '__main__':
    gc.set_debug(gc.DEBUG_LEAK)  # 设置gc模块的日志
    f3()

'''
有三种情况会触发垃圾回收：
    1.调用gc.collect(),
    2.当gc模块的计数器达到阀值的时候。
    3.程序退出的时候
'''