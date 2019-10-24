'''
    进程和线程的区别：
            第一：“线程开销小 进程更安全” 因为进程拥有独立的堆栈空间和数据段，所以每当启动一个新的进程必须分配给它独立的地址空间，
        建立众多的数据表来维护它的代码段、堆栈段和数据段，这对于多进程来说十分“奢侈”，系统开销比较大，
        而线程不一样，线程拥有独立的堆栈空间，但是共享数据段，它们彼此之间使用相同的地址空间，共享大部分数据，比进程更节俭，开销比较小，
        切换速度也比进程快，效率高。但是正由于进程之间独立的特点，使得进程安全性比较高，也因为进程有独立的地址空间，
        一个进程崩溃后，在保护模式下不会对其它进程产生影响，而线程只是一个进程中的不同执行路径。一个线程死掉就等于整个进程死掉。
            第二：进程的通信机制相对很复杂，譬如“管道，信号，消息队列，共享内存，套接字”等通信机制，而线程由于共享数据段所以通信机制很方便
'''

'''
    process类：
        star()方法启动进程
        join()方法实现进程间的同步，等待所有进程退出
        close()方法用来阻止多余的进程涌入进程池Pool造成进程阻塞
'''
'''
    multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
    target是函数名字
    args是函数需要的参数，以tuple的形式传入
'''
import multiprocessing
import os


def run_proc(name):
    print("Child process {0} {1} Running".format(name, os.getppid()))


if __name__ == '__main__':
    print("Parent process {0} is Running".format(os.getppid()))
    for i in range(5):
        p = multiprocessing.Process(target=run_proc, args=(str(i),))
        print("process start")
        p.start()
    p.join()
    print("Process close")
# Parent process 14532 is Running
# process start
# process start
# process start
# process start
# process start
# Child process 1 12148 Running
# Child process 0 12148 Running
# Child process 2 12148 Running
# Child process 4 12148 Running
# Child process 3 12148 Running
# Process close


'''
    Pool（进程池）:
    Pool 可以提供指定数量的进程供用户使用，默认是 CPU 核数。当有新的请求提交到 Poll 的
 时候，如果池子没有满，会创建一个进程来执行，否则就会让该请求等待。
 - Pool 对象调用 join 方法会等待所有的子进程执行完毕
 - 调用 join 方法之前，必须调用 close
 - 调用 close 之后就不能继续添加新的 Process 了
'''
'''
    pool=Pool(numprocess,initializer,initargs)
    numproxess:需要创建的进程个数，如果忽略将使用cpu_count()的值。即系统上的CPU数量。
    initializer:每个进程启动时都要调用的对象。
    initargs:为initalizer传递的参数。
'''
import multiprocessing
import os
import time


def run_task(name):
    print("Task {0} pid {1} is running, parent id is {2}".format(name, os.getpid(), os.getppid()))
    time.sleep(1)
    print("Task {0} end".format(name))


if __name__ == '__main__':
    print("current process {0}".format(os.getpid()))
    # 设定池内进程数
    p = multiprocessing.Pool(processes=3)
    for i in range(6):
        p.apply_async(run_task, args=(i,))
    print("Waiting for all subprocesses done...")
    p.close()
    p.join()
    print("All processes done!")


'''
     Queue进程间通信
'''
from multiprocessing import Process, Queue
import os, time, random


# 写数据进程执行的代码:
def proc_write(q,urls):
  print('Process(%s) is writing...' % os.getpid())
  for url in urls:
    q.put(url)
    print('Put %s to queue...' % url)
    time.sleep(random.random())


# 读数据进程执行的代码:
def proc_read(q):
  print('Process(%s) is reading...' % os.getpid())
  while True:
    url = q.get(True)
    print('Get %s from queue.' % url)


if __name__=='__main__':
  # 父进程创建Queue，并传给各个子进程：
  q = Queue()
  proc_writer1 = Process(target=proc_write, args=(q,['url_1', 'url_2', 'url_3']))
  proc_writer2 = Process(target=proc_write, args=(q,['url_4','url_5','url_6']))
  proc_reader = Process(target=proc_read, args=(q,))
  # 启动子进程proc_writer，写入:
  proc_writer1.start()
  proc_writer2.start()
  # 启动子进程proc_reader，读取:
  proc_reader.start()
  # 等待proc_writer结束:
  proc_writer1.join()
  proc_writer2.join()
  # proc_reader进程里是死循环，无法等待其结束，只能强行终止:
  proc_reader.terminate()


'''
    Pipe进程间通信
'''
from multiprocessing import Process, Pipe


def send(pipe):
  pipe.send(['spam',42, 'egg'])  # send 传输一个列表
  pipe.close()


if __name__ == '__main__':
  (con1, con2) = Pipe()              # 创建两个 Pipe 实例
  sender = Process(target=send, args=(con1, ))   # 函数的参数，args 一定是实例化之后的 Pip 变量，不能直接写 args=(Pip(),)
  sender.start()                  # Process 类启动进程
  print("con2 got: %s" % con2.recv())       # 管道的另一端 con2 从send收到消息
  con2.close()
