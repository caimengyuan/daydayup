'''
    new_作用于_init_之前
    前者可以决定是否调用后者，或者说可以决定调用哪个类的_init_方法。
    实例化基本遵循 创建实例对象，初始化实例对象，最后返回实例对象 的过程
    _new_方法负责创建一个实例对象，
    _init_方法负责将该实例对象进行初始化
'''


class A(object):
    def __init__(self):
        print('initA')


class B(A):
    def __init__(self):
        super(B, self).__init__()
        print("init")

    def __new__(cls, *args, **kwargs):  # *args,**kwargs—前者是tuple，后者是dict
        print("new %s" % cls)
        # return object.__new__(cls)
        return A.__new__(B)


b = B()
print(type(b))

# ​_init_有一个参数self，就是这个_new_返回的实例，_init_在_new_的基础上可以完成一些其它初始化的动作，_init_不需要返回值;
# 若new没有正确返回当前类cls的实例，那当前类的init是不会被调用的，即使是父类的实例也不行。