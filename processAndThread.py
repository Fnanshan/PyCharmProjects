print('----------multiprocessing--------')

# '''
# fork()
#     fork()调用一次，返回两次。
#     原因：当前进程fork()调用一次，就会复制一份子进程，分别在父进程和子进程内返回。
#             父进程：返回子进程的ID
#             子进程:可以调用getppid()拿到父进程ID，返回0
#     作用：一个进程在接到新任务时就可以复制出一个子进程来处理新任务，
#           常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，
#           就fork出子进程来处理新的http请求。
# '''
#
# import os
#
#
# def linuxMultiProcessing():
#     print('Process (%s) start...' % os.getpid())
#     # Only works on Unix/Linux/Mac:
#     pid = os.fork()
#     if pid == 0:
#         print('I am child process (%s) and my parent is %s..' % (os.getpid(), os.getppid()))
#     else:
#         print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
#
#
# # multiprocessing
# # multiprocessing模块提供了一个Process类来代表一个进程对象
# # 演示启动一个子进程并等待其结束
# from multiprocessing import Process
# import os
#
#
# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     # 创建子进程：只需要传入一个执行函数和函数的参数
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     # 创建一个Process实例，用start()启动
#     p.start()
#     print('---')
#     # join()可以等待子进程结束后再继续往下运行，通常用于进程间的同步
#     p.join()
#     print('Child process end.')
#
# # 用进程池（pool）的方式批量创建子进程
# from multiprocessing import Pool
# import os, time, random
#
#
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     # 对Pool对象调用join()方法会等待所有子进程执行完毕，
#     # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
#     # task 0，1，2，3是立刻执行的，
#     # 而task 4要等待前面某个task完成后才执行，
#     # 这是因为Pool的默认大小在我的电脑上是4，
#     # 因此，最多同时执行4个进程。这是Pool有意设计的限制。
#     p.close()
#     p.join()
#     print('All subprocesses done.')
#
# # 子进程
# # 很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
# # subprocesas 模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
#
# import subprocess
#
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
#
# print('Exit code:', r)
#
# # communicate()控制子进程的输入
# pc = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = pc.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', pc.returncode)
#
# # 进程间通信
# from multiprocessing import Process, Queue
# import os, time, random
#
#
# # 写数据进程执行的代码
# def write(q):
#     print('Process to write : %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
#
# # 读数据进程执行的代码
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
#
# if __name__ == '__main__':
#     # 父进程创建Queue，并传给各个子进程
#     q = Queue()
#     # 创建子进程：只需要传入一个执行函数和函数的参数
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw,写入：
#     pw.start()
#     # 启动子进程pr,读取
#     pr.start()
#     # 等待pw结束
#     # join()可以等待子进程结束后再继续往下运行，通常用于进程间的同步
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止
#     pr.terminate()

print('-------------multithreading------------')

import time, threading

# # 多线程执行的代码：
# # 新线程执行的代码：
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n += 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#
#
# # 任何进程默认会启动一个线程（MainThread),MainThread可以启动新的线程。
# print('thread %s is running...' % threading.current_thread().name)
# # 子线程的名字在创建时命名。
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)


# # lock
# import time, threading
#
# # 假定这是你的银行存款
# balance = 0
#
#
# def change_it(n):
#     # 先存后取，结果应该为0
#     global balance
#     balance = balance + n
#     balance = balance - n
#
#
# # 加锁
# # 优势：确保了某段关键代码只能由一个线程从头到尾完整地执行
# # 劣势：阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降
# lock = threading.Lock()
#
#
# def run_thread(n):
#     for i in range(100000):
#         # 先要获取锁
#         lock.acquire()
#         try:
#             # 放心地改吧:
#             change_it(n)
#         finally:
#             # 如果不释放锁，其他等待锁的线程永远等下去，成为死线程
#             lock.release()
#
# # 没加锁
# # def run_thread(n):
# #     for i in range(100000):
# #         change_it(n)
#
#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print('balance :', balance)

print('-----------ThreadLocal------------')


# # 线程尽量用自己的局部变量，可是局部变量也有问题（函数调用的时候）
# def process_student(name):
#     std = Student(name)
#     # std是局部变量，但是每个函数都要用它，因此必须传出去
#     do_task_1(std)
#     do_task_2(std)
#
#
# def do_task_1(std):
#     do_task_1(std)
#     do_task_2(std)
#
#
# def do_task_2(std):
#     do_task_1(std)
#     do_task_2(std)


# # 用一个全局的dict存放所有的Student对象，以thread作为key获取对应的Student对象
# # 最大的优点是消除了std对象在每层函数中的传递问题，但是，每个函数获取std的代码有点丑
# global_dict = {}
#
#
# def std_thread(name):
#     std = Student(name)
#     # 把std放到全局变量global_dict中:
#     global_dict[threading.current_thread()] = std
#     do_task_1()
#     do_task_2()
#
#
# def do_task_1():
#     # 不传入std,而是根据当前线程查找：
#     std = global_dict[threading.current_thread()]
#     ...
#
#
# def do_task_2():
#     # 任何函数都可以查找出当前线程的std变量
#     std = global_dict[threading.current_thread()]
#     ...

# import threading
#
# # 创建全局ThreadLocal对象
# # 每个Thread对它都可以读写student属性，但互不影响
# # 一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
# local_school = threading.local()
#
#
# def process_student():
#     # 获取当前线程关联的student:
#     std = local_school.student
#     print('Hello, %s (in %s)' % (std, threading.current_thread().name))
#
#
# def process_thread(name):
#     # 绑定ThreadLocal的student
#     local_school.student = name
#     process_student()
#
#
# t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
# t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()

print('-----------process VS. thread--------------')
