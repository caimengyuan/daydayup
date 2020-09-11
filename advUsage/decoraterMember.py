'''
装饰器
'''
import time

def timeit(fun):
    def res():
        start_time = time.time()
        fun()
        end_time = time.time()
        print('the function use time: %.2f'%(end_time - start_time))
    return res

@timeit
def f():
    time.sleep(3)

f()
# the function use time: 3.00

