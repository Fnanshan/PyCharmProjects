# 生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产
def consumer():         # 消费者
    r = ''
    while True:
        n = yield r     # consumer通过yield拿到消息，处理，又通过yield把结果传回
        print('consumer 通过yiedl拿到的 n :', n)
        if not n:
            return
        print('[CONSUMER] Consuming %s ...' % n)
        r = '200 OK'


def produce(c):         # 生产者
    c.send(None)        # 启动生成器
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s ...' % n)
        r = c.send(n)   # 一旦生产了东西，通过c.send(n)切换到consumer执行
        print('[PRODUCER] Consumer return : %s' % r)   # produce拿到consumer处理的结果，继续生产下一条消息
    c.close()       # produce决定不生产了，通过c.close()关闭consumer，整个过程结束。

异步IO
# consumer()是一个generator，把一个consumer传入produce()
c = consumer()
produce(c)


# def addlist(alist):
#     for i in alist:
#         yield i + 1
#
#
# alist = [1, 2, 3, 4]
# for x in addlist(alist):
#     print(x)


# python3.7手册例子
# def echo(value=None):
#     print("Execution starts when 'next()' is called for the first time.")
#     try:
#         while True:
#             try:
#                 print('yield 之前，value = ', value)
#                 value = (yield value)
#                 print('yield 之后，value = ', value)
#             except Exception as e:
#                 value = e
#     finally:
#         print("Don't forget to clean up when 'close()' is called.")
#
#
# generator = echo(1)
# # next()函数获得generator的下一个返回值，也就是获得generator中yield的值
# print(next(generator))
# print(next(generator))
# print(generator.send(2))
# generator.throw(TypeError, "spam")
# generator.close()


# 高级特性-生成器
# L = [x * x for x in range(10)]
# print(type(L))
# '''
# A generator expression yields a new generator object.                           generator表达式生成一个新的generator对象
# Its syntax is the same as for comprehensions,
# except that it is enclosed in parentheses instead of brackets or curly braces.  它只能包含在()中，而不是[] or {}
# '''
# g = (x * x for x in range(10))
# for n in g:
#     print(n)


# # 斐波那契数列
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         # 我猜测python跟c类似，先计算b = a+b,再计算a = b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'


# # 举例说明generator
# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield(3)
#     print('step 3')
#     yield(5)
#
#
# o = odd()
# print(next(o))
# print(next(o))
# print(next(o))

