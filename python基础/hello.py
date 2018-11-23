import sys
from functools import reduce

print('-----python基础-------')
# # print ("hello world");
# # print ("please input your name------")
# # name = input()
# # print ("hello,", name)


# # 用'''...'''表示多行内容
# print ('''line1
# ...line2
# ...line3''')
#
# # 变量
# # 变量本身类型不固定的语言称之为动态语言
# a = 123
# print (a)
# a = "456"
# print (a)
# a = True
# print (a)


# # 练习
# # 小明的成绩从去年的72分提升到了今年的85分，
# # 请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
# # -*- coding: utf-8 -*-
# s1 = 72
# s2 = 85
# r = (s2 - s1) / s1
# print('%f' % r)
# print('%.1f%%' % (r * 100))
# print( 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', (r * 100)) )


# 条件判断 if ... else
# age = 20
# if age > 19:
#     print ("this is audit")
#     print ("he age is:", age)
# else:
#     print ("this is child")
#     print ("he age is:", age)
#
# print ("---------------我是一条分割线----------------")

# 条件判断 if elif
# age = 3
# if age > 19:
#     print ("audit")
# elif age >= 6:
#     print ("teenager")
# else:
#     print ("kid")
#
# print ("---------------我是一条分割线----------------")

# 条件判断 为什么打印teenager？
# age = 20
# if age >= 6:
#     print('teenager')
# elif age >= 18:
#     print('adult')
# else:
#     print('kid')
#
# print ("---------------我是一条分割线----------------")

# input
# s = input("birth:")
# birth = int(s)
# if birth < 2000:
#     print ("00前")
# else:
#     print ("00后")


print('------函数---------')
# # 函数：返回多个值
# import math
# def move(x, y, step,angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
#
# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)
#
# r = move(100, 100, 60, math.pi / 6)
# print(r)
#
# print ("---------------我是一条分割线----------------")


# def power(x, n = 2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
#
# print(power(5, 2))

# def quadratic(a, b, c):
#     s = power(b) - 4 * a * c
#     if (s >= 0):
#         x1 = (-b + math.sqrt(power(b) - 4 * a * c)) / (2 * a)
#         x2 = (-b - math.sqrt(power(b) - 4 * a * c)) / (2 * a)
#     else:
#         print("b*b-4ac < 0")
#     return x1, x2


# 测试:
# print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
# print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
#
# if quadratic(2, 3, 1) != (-0.5, -1.0):
#     print('测试失败1')
# elif quadratic(1, 3, -4) != (1.0, -4.0):
#     print('测试失败2')
# else:
#     print('测试成功0')


# 默认参数
# def enroll(name, gender, age=6, city='Beijing'):
#     print('name:', name)
#     print('gender:', gender)
#     print('age:', age)
#     print('city:', city)
#
# enroll('Sarah', 'F')
# enroll('Bob', 'M', 7)
# enroll('Adam', 'M', city='Tianjin')


# 默认参数的坑
# def add_end(L=[]):
#     L.append('END')
#     return L
#
# print(add_end())
# print(add_end())
# print(add_end())


# 解决默认参数的坑
# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L
#
# print(add_end())
# print(add_end())
# print(add_end())


# 可变参数0
# def calc0(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum

# print(calc0())
# print(calc([1, 2, 3]))
# print(calc((1, 3, 5, 7)))

# 可变参数1
# def calc1(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#
# print(calc1())
# nums = [1, 2, 3]
# print(
#     calc1(*nums)
# )

# 关键字参数

# 命名关键字参数
# def person(name, age, **kw):
#     if 'city' in kw:
#         pass
#     if 'job' in kw:
#         pass
#     print('name:', name, 'age:', age, 'other:', kw)
#
#
# person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


# 参数组合
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# def f1(a, b, c=0, *args, **kw):
#     print('a =', a, 'b =', b, 'c =',c, 'args = ', args, 'kw =', kw)
#
#
# def f2(a, b, c=0, *, d, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
#
#
# f1(1, 2)
# f1(1, 2, c=3)
# f1(1, 2, 3, 'a', 'b')
# f1(1, 2, 3, 'a', 'b', x=99)
# f2(1, 2, d=99, ext=None)


# 递归函数
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
#
# print(fact(1000))

# 尾递归优化
# def fact(n):
#     return fact_iter(n, 1)
#
#
# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num - 1, num * product)

# 汉诺塔递归实现
# def hanoi(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)
#     else:
#         hanoi(n - 1, a, c, b)   # 从a --> b，通过c完成
#         print(a, '-->', c)
#         hanoi(n - 1, b, a, c)   # 从b --> c，通过a完成
#
#
# # 调用
# hanoi(5, 'A', 'B', 'C')


print('------高级特性-------')
# 高级特性---切片
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
# 我的代码
# def trim(s):
#     print(s, 'len(s) :', len(s))
#     for i in range(len(s)):
#         # print('i:', i)
#         # print('s[i:i+1] :', s[i:i+1])
#         # if s[i:i+1] == ' ':
#         #     print('k')
#         if s[i:i+1] != ' ':
#             continue
#         else:
#             s[i:i+1] = ''
#     return s
#
#
# trim('hello  ')


# # 官方题解
# def trim(s):
#     if len(s) == 0:     # 首先判断 s 是否为空
#         return s
#     elif s[0] == ' ':
#         return trim(s[1:])
#     elif s[-1] == ' ':
#         return trim(s[:-1])
#     return s
#
#
# # 测试
# if trim('hello  ') != 'hello':
#     print('测试失败0!')
# elif trim('  hello') != 'hello':
#     print('测试失败1!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败2!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败3!')
# elif trim('') != '':
#     print('测试失败4!')
# elif trim('    ') != '':
#     print('测试失败5!')
# else:
#     print('测试成功!')


# # 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
# from collections import Iterable
# print(isinstance('abc', Iterable))
# print(isinstance([1, 2, 3], Iterable))
# print(isinstance(123, Iterable))
#
# for i, value in enumerate(['A', 'B', 'C']):
#     print(i, value)
#
#
# for x, y in [(1, 1), (2, 4), (3, 9)]:
#     print(x, y)


# # 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
# def findMinAndMax(L):
#     if L == []:
#         return (None, None)
#     else:
#         my_min = L[0]
#         my_max = L[0]
#         for i in L:
#             if my_min > i:
#                 my_min = i
#             if my_max < i:
#                 my_max = i
#         return (my_min, my_max)
#
#
# # 测试
# if findMinAndMax([]) != (None, None):
#     print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败!')
# else:
#     print('测试成功!')


# # 列表生成式
# print([x * x for x in range(1, 11)])
# # 加 if 判断
# print([x * x for x in range(1, 11) if x % 2 == 0])
# # 两层循环
# print([m + n for m in 'abc' for n in 'xyz'])
# # 功能0
# import os   # 导入os模块
# print([d for d in os.listdir('.')])     # os.listdir可以列出文件和目录
# # for 循环使用多个变量
# d = {'x': 'A', 'y': 'B', 'z': 'C'}
# for k, v in d.items():
#     print(k, '=', v)
# # 使用两个变量来生成list
# d = {'x': 'A', 'y': 'B', 'z': 'C'}
# print([k + '=' + v for k, v in d.items()])
# # 把一个list中所有的字符串变成小写
# L = ['Hello', 'World', 'IBM', 'Apple']
# print([s.lower() for s in L])
#
# # 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错。
# # 修改列表生成式，通过添加if语句保证列表生成式能正确地执行。
# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [s.lower() for s in L1 if isinstance(s, str)]
#
# # 测试:
# print(L2)
# if L2 == ['hello', 'world', 'apple']:
#     print('测试通过!')
# else:
#     print('测试失败!')


# 生成器
# 创建一个generator
# L = [x * x for x in range(10)]
# print(L)
# g = (x * x for x in range(10))
# print(g)
# print(next(g))
# print(next(g))
# # ...
# for n in g:
#     print(n)


# # 斐波那契数列（不用生成器）
# def fib(number):
#     n, a, b = 0, 0, 1
#     while n < number:
#         print(b)
#         a, b = b, a + b
#         n += 1
#     return 'OK!'
#
#
# print(fib(5))

# 菲波那切数列（用生成器）
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         # print('yield前,n :', n, ' yield前,a :', a, ' yield前,b :', b)
#         yield b
#         # print('yield后,n :', n, ' yield后,a :', a, ' yield后,b :', b)
#         a, b = b, a+b   # t = (b, a + b) ; t是一个tuple ; a = t[0]b = t[1]
#         n = n + 1
#         # print('改变n, a, b的值 :', 'n :', n, ', a :', a, ', b :', b)
#     return 'done'
#
#
# 拿generator的return语句的返回值
# g = fib(6)
# while True:
#     try:
#         x = next(g)
#         print('g:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break
#


# for n in fib(5):        # 把 fib 中的 yield b 的值传给了 n
#     print('打印 n :', n)


# 查看赋值语句：a, b = b, a + b 的执行顺序
# a = 1
# b = 2
# t = (b, a + b) # t是一个tuple
# a = t[0]
# b = t[1]
# print('a,', a, 'b,', b)

# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield (3)
#     print('step 3')
#     yield (5)
#
#
# o = odd()
# next(o)
# next(o)
# next(o)
# next(o)


# 杨辉三角TEST
# def triangles(n):
#     L = [1]     # 定义一个list[1]
#     while True:
#         # print('yield前,n :', n, ' yield前,L :', L)
#         yield L         # 打印出该list ;print(L)
#         # print('yield后,L :', L, ',len(L) :', len(L))
#         L = [L[x] + L[x+1] for x in range(len(L)-1)]   # 计算下一行中间的值（除去两边的1)
#         # print('计算L后，L :', L)
#         L.insert(0, 1)      # 在开头插入1
#         L.append(1)         # 在结尾添加1
#         # print('开头插入，结尾添加之后，L :', L)
#         if len(L) > 10:
#             break
#
#
# # 生成一个generator对象，通过for循环迭代输出每一行  # triangles(5)
# for i in triangles(5):
#     print('print i :', i)


# 杨辉三角（廖雪峰的python教程）
# def triangles():
#     L = [1]
#     while True:
#         yield L
#         L.append(0)
#         L = [L[x-1] + L[x] for x in range(len(L))]
# # 期待输出:
# # [1]
# # [1, 1]
# # [1, 2, 1]
# # [1, 3, 3, 1]
# # [1, 4, 6, 4, 1]
# # [1, 5, 10, 10, 5, 1]
# # [1, 6, 15, 20, 15, 6, 1]
# # [1, 7, 21, 35, 35, 21, 7, 1]
# # [1, 8, 28, 56, 70, 56, 28, 8, 1]
# # [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
#
# n = 0
# results = []
# for t in triangles():
#     print('-----print t :', t)
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break
#
# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过!')
# else:
#     print('测试失败!')


# 其他的一道题（从3->1）
# line = 3
# while line:
#     width = line
#     while width:
#         print('#', end='')
#         width -= 1
#     line -= 1
#     print()
# 其他的一道题（从1->3）
# user_input_line = int(input('input a line:'))
# line = 1
# while line:
#     width = line
#     while width:
#         print('#', end='')
#         width = width - 1
#     line = line + 1
#     if line > user_input_line:
#         break
#     print()
# # 10月28日请用高级方法做一遍
# cow = 1          # cow 行数,row 列数
# while cow <= 9:  # cow 行数 < 9 时
#     row = 1      # 列数 = 1
#     while row <= cow:  # 当 列数 <= 行数
#         print(row, '*', cow, '=', cow * row, end='\t')
#         row += 1
#     print()
#     cow += 1
# 用列表生成式写99乘法表，输出的结果是一个列表，外观不好看，计算是正确的。
# print([m * n for m in range(1, 10) for n in range(1, 10) if m >= n])


print('-----函数式编程-----')
# map/reduce
#
#
# def f(x):
#     return x * x
#
#
# L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# r = map(f, L)
# print(list(r))
# # 把这个list所有数字转为字符串
# print(list(map(str, L)))
# 把序列[1, 3, 5, 7, 9]变换成整数13579
from functools import reduce


# def fn(x, y):
#     return x * 10 + y
# # print(L)
# # print(reduce(fn, L))
#
#
# # 把str转换为int的函数
#
#
# S = '123456789'
# print('old S :', S)
#
#
# def char2num(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]
#
#
# print(map(char2num, S))
# print('new S ;', reduce(fn, map(char2num, S)))
# print('new S - 1 :', reduce(fn, map(char2num, S))-1)


# 整理成一个str2int的函数式：
# from functools import reduce
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#
#
# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#
#     def char2num(s):
#         return DIGITS[s]
#     return reduce(fn, map(char2num, s))


# 用 lambda函数进一步简化
# from functools import reduce
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#
#
# def char2num(s):
#     return DIGITS[s]
#
#
# def str2int(s):
#     return reduce(lambda x, y: x * 10 + y, map(char2num, s))


# 练习
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
# 其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，
# 输出：['Adam', 'Lisa', 'Bart']：
#
#
# def normalize(name):
#     name = name[0].upper() + name[1:].lower()
#     return name
#
# # 测试:
#
#
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)


# # Python提供的sum()函数可以接受一个list并求和，
# # 请编写一个prod()函数，可以接受一个list并利用reduce()求积
#
#
# def prod(L):
#     def fn(x, y):
#         return x * y
#     return reduce(fn, L)
#
#
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')


# # 利用map和reduce编写一个str2float函数，
# # 把字符串'123.456'转换成浮点数123.456
# # digits　是字典（key-value），用在 return {}[] 这里
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#
#
# def str2float(s):
#     # char2int
#     def g(s):
#         return DIGITS[s]
#
#     # 整数部分
#     def h(x, y):
#         return 10 * x + y
#
#     # 小数部分
#     def a(x, y):
#         return x / 10 + y
#
#     # 将原始字符串数据分割成两部分
#     L = s.split('.')
#     # char2int
#     q = list(map(g, L[0]))
#     u = list(map(g, L[1]))
#     b = u[::-1]
#     return reduce(h, q) + reduce(a, b)/10
#
#
# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')


# # filter
# # 在一个list中，删掉偶数，只保留奇数
# def is_odd(n):
#     return n % 2 == 1
#
#
# L = [1, 2, 3, 4, 5, 6, 9, 10, 15]
# S = ['A', '', 'B', None, 'C', ' ']
# print(list(filter(is_odd, L)))


# # 把一个序列中的空字符串删掉
# def not_empty(s):
#     return s and s.strip()
#
#
# v = list(filter(not_empty, S))
# print(v)


# # 用filter求素数
# # 用生成器构造一个从3开始的奇数序列（一个无限序列）
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
#
#
# # 定义一个筛选函数
# # 循环取出序列的第一个数，如果是素数，则返回
# def _not_divisible(n):
#     return lambda x: x % n > 0
#
#
# # 定义一个生成器，不断返回下一个素数
# # 先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。
# def primes():
#     yield 2
#     it = _odd_iter()    # 初始化序列
#     while True:
#         n = next(it)    # 返回序列的第一个数
#         yield n
#         it = filter(_not_divisible(n), it)      # 构造新序列
#
#
# # 打印1000以内的素数
# # 由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件
# for n in primes():
#     if n < 10:
#         print(n)
#     else:
#         break


# # 匿名函数 lambda()
# def edit_story(words, func):
#     for word in words:
#         print(func(word))
#
#
# # def enliven(word):
# #     return word.capitalize() + '!'
#
#
# stairs = ['thud', 'meow', 'thud', 'hiss']
# # edit_story(stairs, enliven)
# edit_story(stairs, lambda word: word.capitalize() + '!')


# # 练习
# # 回数是指从左向右读和从右向左读都是一样的数，
# # 例如12321，909。请利用filter()筛选出回数
# # 方法一
# def is_palindrome(n):
#     nn = str(n)
#     return nn == nn[::-1]
#
#
# # 测试:
# L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == L:
#     print('测试成功!')
# else:
#     print('测试失败!')
# # 方法二
# print(list(filter(lambda n: str(n) == str(n)[::-1], range(1, 1000))))


# # sorted
# L = [36, 5, -12, 9, -21]
# S = ['bob', 'about', 'Zoo', 'Credit']
# print(sorted(L))
# print(sorted(L, key=abs))
# print(sorted(S))
# print(sorted(S, key=str.lower))
# print(sorted(S, key=str.lower, reverse=True))


# # 练习
# from operator import itemgetter
# student = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# student_name = []
# student_score = []
# # 按名字排序
#
#
# def by_name(t):
#     return t[0]
#
#
# def by_name_arg(t):
#     for i in range(len(t)):
#         student_name.append(t[i][0])
#     # return student_name      # TypeError: 'list' object is not callable
#
#
# # key = by_name(student)
# # print(key)
# print('old student info :', student)
# print('new student info sorted_by_name :', sorted(student, key=by_name))
# print('new student info sorted_by_name_arg :', sorted(student, key=by_name_arg(student)))
#
# # 按成绩从高到低排序
#
#
# def by_score(t):
#     return t[1]
#
#
# print('sorted_by_score :')
# # print(student[1])
# # print(sorted(student, key=itemgetter(0)))
# # print(sorted(student, key=lambda t: t[1]))
# # print(sorted(student, key=itemgetter(1), reverse=True))
# print('old student info :', student)
# print('new student info sorted_by_score :', sorted(student, key=by_score))
# print('new student info sorted_by_score_reverse :', sorted(student, key=by_score, reverse=True))


# # python 3.7.0 手册有关sorted()的练习
# student_tuples = [
#     ('john', 'A', 15),
#     ('yane', 'B', 11),
#     ('dave', 'B', 10),
#     ('abc', 'A', 10),
#     ('abc', 'A', 11)
#
# ]
# print('student_tuples :', student_tuples)
# print(sorted(student_tuples, key=lambda student: student[2]))
# print('key=itemgetter(1) :', sorted(student_tuples, key=itemgetter(1)))
# print('key=itemgetter(2) :', sorted(student_tuples, key=itemgetter(2)))
# print('key=itemgetter(1, 2) :', sorted(student_tuples, key=itemgetter(1, 2)))


# # 返回结果
# def calc_sum(*args):
#     ax = 0
#     for n in args:
#         ax = ax + n
#     return ax
#
#
# # c = calc_sum(1, 3, 5, 7, 9)
# # print('print c :', c)
#
#
# # 返回函数
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
#
#
# f = lazy_sum(1, 3, 5, 7, 9)
# # print('print f :', f)
# # print('print f() :', f())
#
#
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#             return i * i
#         fs.append(f)
#     return fs
#
#
# # f1, f2, f3 = count()
# # print('print count1 :', count1)
# # print('print count1() :', count1())
# # print('f1() :', f1())
# # print('f2() :', f2())
# # print('f3() :', f3())
# # print('print count() :', count1())
#
#
# def count2():
#     def f(j):
#         def g():
#             return j * j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i))
#     print('print fs :', fs)
#     return fs
#
#
# # f1, f2, f3 = count2()
# # print(f1())
# # print(f2())
# # print(f3())
# # 练习
# # 利用闭包返回一个计数器函数，每次调用它返回递增整数：
#
#
# def createCounter():
#     f = [0]
#     print('f :', f)
#     print('f[0] :', f[0])
#
#     def counter():
#         f[0] = f[0] + 1
#         return f[0]
#     return counter
#
#
# # 测试:
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')


# # 匿名函数的使用
# def is_odd(n):
#     return n % 2 == 1
#
#
# L = list(filter(is_odd, range(1, 20)))
# print('不适用匿名函数 :')
# print(L)
#
#
# # 直接传入匿名函数
# print('# 直接传入匿名函数（map()获得的是TRUE、FALSE值，filter是筛选器） :')
# print(list(map(lambda x: x % 2 == 1, range(1, 20))))
# print(list(filter(lambda x: x % 2 == 1, range(1, 20))))
#
#
# # 使用1：函数的 return 使用 匿名函数
# def is_odd_lambda(n):
#     return lambda x: x % 2 == 1
#
#
# print('# 函数的 return 使用 匿名函数 :')
# print(list(filter(is_odd, range(1, 20))))
#
#
# # 使用2：把匿名函数赋值给一个变量，再利用变量来调用该函数
# L2 = lambda x: x % 2 == 1
#
#
# def is_odd_lambda(n):
#     return L2(n)
#
#
# print('# 把匿名函数赋值给一个变量，再利用变量来调用该函数 :')
# print(list(filter(is_odd, range(1, 20))))


# # 装饰器
# def log0(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
#
# # 自定义log的文本
# def log1(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
#
# # 一个完整的decorator的写法：
# import functools
#
#
# def log2(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
#
# # 针对带参数的decorator的写法：
# def log3(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
#
# @log0    # 相当于执行了语句：now0 = log0(now0)
# def now0():
#     print('2015-3-25')
#
#
# @log1('execute')    # 相当于执行了语句：now1 = log1('execute')(now1)
# def now1():
#     print('2018-10-30')
#
# @log2
# def now2():
#     print('2018年10月31日')
#
#
# @log3('eeeee')
# def now3():
#     print('aaaaaa')
#
#
# now0()
# print('now0.__name__ :', now0.__name__)
# print('------')
# now1()
# print('now1.__name__ :', now1.__name__)
# print('------下面是完整的decorator的使用------')
# now2()
# print('now2.__name__ :', now2.__name__)
# now3()
# print('now3.__name__ :', now3.__name__)
#
# print('------------下面是decorator练习--------------')
# # 练习
# # 请设计一个decorator，它可作用于任何函数上，
# # 并打印该函数的执行时间
# import time, functools
#
#
# def metric(fn):
#     def wrapper(*args, **kw):
#         start = time.time()
#         res = fn(*args, **kw)
#         end = time.time()
#         print('%s executed %s ms' % (fn.__name__, (end - start) * 1000))
#         return res
#     return wrapper
#
#
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y
#
#
# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z
#
#
# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f == 33:
#     print('f :TEST SUCCESSFUL')
# elif f != 33:
#     print('f :TEST FALSE')
#
# if s == 7986:
#     print('s :TEST SUCCESSFUL')
# elif s != 7986:
#     print('s :TEST FALSE')
#
# print('-----下面是decorator练习，在函数调用前后打印 begin call 和 end call 的日志-----')
#
#
# def log4(func):
#         def wrapper(*args, **kwargs):
#             print('begin call %s' % func.__name__)
#             res = func(*args, **kwargs)
#             print('end call %s' % func.__name__)
#             return res
#         return wrapper
#
#
# @log4
# def func4():
#     print('fn() call')
#
#
# func4()
# print('-----下面是decorator练习，既支持不传入参数，又支持传入参数-----')
#
#
# def log5(text):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print('begin call %s' % func.__name__)
#             print('func is : %s , it text is : %s' % (func.__name__, text))
#             res = func(*args, **kwargs)
#             print('end call %s' % func.__name__)
#             return res
#         return wrapper
#     return decorator
#
#
# @log5('my is a text info')
# def func5():
#     print('fn() call')
#
#
# func5()
#
#
# def log6(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             if text != None:
#                 print('the text is %s and the call %s():' % (text, func.__name__))
#                 res = func(*args, **kw)
#                 return res
#             else:
#                 print('call %s ():' % func.__name__)
#                 res = func(*args, **kw)
#                 return res
#         return wrapper
#
#     if isinstance(text, str):       # 首先如果有参数 就跟原来一样直接返回decorator即可
#         return decorator
#     else:                           # 如果没有参数 其实log(func)就是log里边其实直接传的参数就是func 返回的应该是wrapper
#         func = text
#         text = None
#         return decorator(func)      # 所以这里的应该是直接decorator(func) 返回wrapper
#
#
# @log6('there is a parameter in this edition')
# def f1(x, y):
#     return x * y
#
#
# def main1():
#     result = f1(2, 3)
#     print('the result is {}'.format(result))
#     print('the name of this function(no_parameter) is ', f1.__name__)
#
#
# @log6
# def f2(x, y):
#     return x + y
#
#
# def main2():
#     result = f2(5, 8)
#     print('the result of this function(with parameter) is {}'.format(result))
#     print('the name of thsi function si ', f2.__name__)
#
#
# def main():
#     number = eval(input('please input a number to decide which the function to run :'))
#     if number == 1:
#         main1()
#         print('run successfully!')
#     else:
#         main2()
#         print('run successfully!')
#
#
# main()


# # 偏函数
# import functools
# import hello2
# int2 = functools.partial(int, base=2)
# print(int2('1000000'))
# int()
# hello2.test()



