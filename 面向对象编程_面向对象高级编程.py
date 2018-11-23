#!/usr/bin/env python3 　　　　　　　　　　　　　　　　# 让这个hello.py文件直接在Unix/Linux/Mac上运行
# -*- coding: utf-8 -*-　　　　　　　　　　　　　　　　# 使用标准UTF-8编码

' OOP：廖雪峰的Python教程-面向对象编程 的学习笔记及代码过程（作为以后学习的参考）'

__author__ = 'Daemon'  # 源码作者

print('---------面向对象编程---------')

# std1 = {'name': 'Daemon', 'score': 98}
# std2 = {'name': 'fss', 'score': 99}
#
#
# def print_score(std):
#     print('%s: %s' % (std['name'], std['score']))
#
#
# print_score(std1)
# print_score(std2)


# class Student(object):
#
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#
#     def print_score(self):
#         # print('%s: %s' % (self.name, self.score))
#         print('%s: %s' % (self.__name, self.__score))
#
#     def get_grade(self):
#         if self.__score >= 90:
#             return 'A'
#         elif self.__score >= 60:
#             return 'B'
#         else:
#             return 'C'
#
#     #  外部代码要获取 name、score
#     def get_name(self):
#         return self.__name
#
#     def get_score(self):
#         return self.__score
#
#     # 外部代码要修改score
#     def set_score(self, score):
#         if 0 <= score <= 100:
#             self.__score = score
#         else:
#             raise ValueError('bad score')


# bart = Student('Bart Simpson', 59)
# lisa = Student('Lisa Simpson', 87)
# bart.print_score()
# lisa.print_score()
# print(bart)
# print(lisa)
# # 数据封装
# print(' ---数据封装---')
# print(bart.get_grade())
# print(lisa.get_grade())

# 练习
# class Student2(object):
#     def __init__(self, name, gender):
#         self.__name = name
#         self.__gender = gender
#
#     def get_gender(self):
#         return self.__gender
#
#     def set_gender(self, gender):
#         self.__gender = gender
#
#
# # 测试:
# bart = Student2('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')

# # 继承和多态
# class Animal(object):
#     def run(self):
#         print('Animal is runnnig...')
#
#
# class Dog(Animal):
#     def run(self):
#         print('Dog is running')
#
#     def eat(self):
#         print('Eating meat')
#
#
# class Cat(Animal):
#     def run(self):
#         print('Cat is running')
#
#
# def run_twice(animal):
#     animal.run()
#     animal.run()
#
#
# class Tortoise(Animal):   # 乌龟
#     def run(self):
#         print('Tortoise is running slowly...')
#
#
# dog = Dog()
# dog.run()
# cat = Cat()
# cat.run()
# run_twice(Animal())
# run_twice(Dog())
# run_twice(Tortoise())
#
# # 判断对象（基本类型、指向函数或类的变量）的类型用type()
# print(type(123))
# print(type('str'))
# print(type(None))
# print(type(abs))
#
# import types
#
#
# def fn():
#     pass
#
#
# # 判断一个对象是否是函数用types方法
# print(type(fn) == types.FunctionType)
# print(type(abs) == types.BuiltinFunctionType)
# print(type(lambda x: x) == types.LambdaType)
# print(type(x for x in range(10)) == types.GeneratorType)
#
# # 判断class的类型用isinstance()
#
# # 获得一个对象的所有属性和方法，用dir()函数
# print('获得一个对象的所有属性和方法，用dir()函数', dir('ABC'))
#
#
# class MyDog(object):
#     def __len__(self):
#         return 100
#
#
# dog = MyDog()
# print(len(dog))
#
# #  getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
#
#
# class MyObject(object):
#     def __init__(self):
#         self.x = 9
#
#     def power(self):
#         return self.x * self.x
#
#
# obj = MyObject()
# # 获取对象的属性
# print(hasattr(obj, 'x'))    # 有属性'x'吗？
# print(hasattr(obj, 'y'))    # 有属性'y'吗？
# setattr(obj, 'y', 19)       # 设置一个属性'y'
# print(hasattr(obj, 'y'))
# print(getattr(obj, 'y'))    # 获取属性'y'
# # print(getattr(obj, 'z'))  # 获取不存在的属性，会抛出AttributeError的错误
# print(getattr(obj, 'z', 404))  # 传入一个default参数，如果属性不存在，就返回默认值
# # 获取对象的方法
# print(hasattr(obj, 'power'))    # 有属性'power'吗？
# print(getattr(obj, 'power'))    # 获取属性'power'
# fn = getattr(obj, 'power')      # 获取属性'power'并赋值到变量fn
# print(fn)                       # fn指向obj.power
# print(fn())                     # 调用fn()与调用obj.power()是一样的

# 实例属性和类属性
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def learn(self):
#         pass
#
#
# s = Student('Bob')
# s.score = 90
# print(dir(s))


# # 练习
# # 为了统计学生人数，可以给Student类增加一个类属性，
# # 每创建一个实例，该属性自动增加
# class Student(object):
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         Student.count = Student.count + 1
#
#
# if Student.count != 0:
#     print('TEST false0')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('TEST false1')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('TEST false2')
#         else:
#             print('Students :', Student.count)
#             print('TEST successful3')

print('-----------面向对象高级编程----------')


# class Student(object):
#     __slots__ = ('name', 'age', 'set_age', 'score', 'set_score')   # 用tuple定义允许绑定的属性名称
#
#
# s = Student()
# s.name = 'Dameon'
# print(s.name)
#
#
# # 给实例绑定一个方法
# def set_age(self, age):
#     self.age = age
#
#
# from types import MethodType
# s.set_age = MethodType(set_age, s)  # 给s实例绑定一个方法
# s.set_age(26)
# print(s.age)
# s2 = Student()
# # s2.set_age(29)
#
#
# def set_score(self, score):
#     self.score = score
#
#
# Student.set_score = set_score
# s.set_score(100)
# print(s.score)
# s2.set_score(999)
# print(s2.score)

# 使用@property
# 限制score的范围:
#   通过get_score()来获取成绩
#   在set_score()就可以检查参数
# class Studnet(object):
#
#     def get_score(self):
#         return self._score
#
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0~100')
#         self._score = value
#
#
# s = Studnet()
# s.set_score(60)
# print(s.get_score())
# s.set_score(10000)
# print(s.get_score())

# # Python内置的@property装饰器就是负责把一个方法变成属性调用
# class Studnet(object):
#
#     # 把getter方法变成属性；@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0~100')
#         self._score = value
#
#     # 只定义getter方法，不定义setter方法就是一个只读属性
#     # 为什么不把age定义为可读写属性？因为age可以根据birth和当前的时间算出来
#     @property
#     def age(self):
#         return 2015 - self._birth
#
#
# s = Studnet()
# s.score = 60        # OK，实际转化为s.set_score(60)
# print(s.score)      # OK，实际转化为s.get_score()
# s.score = 999


# # 练习
# # 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
# class Screen(object):
#
#     @property
#     def width(self):
#         return self._width
#
#     @width.setter
#     def width(self, width):
#         self._width = width
#
#     @property
#     def height(self):
#         return self._height
#
#     @height.setter
#     def height(self, height):
#         self._height = height
#
#     @property
#     def resolution(self):
#         return self._width * self._height
#
#
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution = ', s.resolution)
# if s.resolution == 786432:
#     print('TEST successful')
# else:
#     print('TEST false')

# class Animal(object):
#     pass
#
#
# # 大类
# class Mammal(Animal):
#     pass
#
#
# class Bird(Animal):
#     pass
#
#
# # 各种动物
# class Dog(Mammal):
#     pass
#
#
# class Bat(Mammal):
#     pass
#
#
# class Parrot(Bird):
#     pass
#
#
# class Ostrich(Bird):
#     pass
#
#
# # 功能
# class RunnableMixIn(object):
#     def run(self):
#         print('Running ...')
#
#
# class FlyableMixIn(object):
#     def fly(self):
#         print('Flying ...')
#
#
# class CarnivorousMixIn(object):
#     pass
#
#
# class HerbivoresMixIn(object):
#     pass
#
#
# # 开始多重继承
# class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
#     pass
#
#
# class Bat(Mammal, FlyableMixIn):
#     pass


# 定制类
# # __str__
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     # 返回一个好看的字符串
#     def __str__(self):
#         return 'Student object (name: %s)' % self.name
#
#
# print(Student('Daemon'))
# s = Student('Fss')
# # 如果是在命令行，直接写 s 是不会打印字符串，而会打印出object
# # 因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
# # 解决办法是再定义一个__repr__()，即 __repr__ = __str__。（通常__str__()和__repr__()代码都是一样的）
# print(s)


# # __iter__
# # 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现__iter__()
# # 斐波那契数列
# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1   # 初始化两个计数器a, b
#
#     def __iter__(self):
#         return self     # 实例本身就是迭代对象，故返回自己
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b  # 计算下一个值
#         if self.a > 100000:     # 退出循环的条件
#             raise StopIteration()
#         return self.a
#
#
# # Python的for循环就会不断调用该迭代对象的__next__()方法
# # 拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
# for n in Fib():
#     print(n)


# __getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，不能引用下标来取值
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()
# class Fib(object):
#     def __getitem__(self, n):
#         a, b = 1, 1
#         for x in range(n):
#             a, b = b, a + b
#         return a
#
#
# f = Fib()
# print(f[100])
# # Fib现在还不能进行切片操作
# print(f[5:10])

#
# class Fib(object):
#     def __getitem__(self, n):
#         if isinstance(n, int):  # n 是索引
#             a, b = 1, 1
#             for x in range(n):
#                 a, b = b, a + b
#             return a
#         if isinstance(n, slice):    # n 是切片
#             start = n.start
#             stop = n.stop
#             if start is None:
#                 start = 0
#             a, b = 1, 1
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a, b= b, a + b
#             return L
#
#
# f = Fib()
# print(f[0:5])
# print(f[:10])
# # 但是没有对step参数作处理，也没有作负数处理
# >>> f[:10:2]
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# __getattr__
# class Student(object):
#
#     def __init__(self):
#         self.name = 'Daemon'
#
#     # 只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找；
#     # 比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，
#     # 这样，我们就有机会返回score的值
#     def __getattr__(self, attr):
#         if attr == 'score':
#             return 99
#         # __getattr__ 返回函数也可以
#         if attr == 'age':
#             return lambda: 25
#         # 要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误
#         raise AttributeError(' \'Student\' object has no attribute \' %s \'' % attr)
#
#
# s = Student()
# print(s.name)
# print(s.score)
# # 因为__getattr__ 中返回的age是函数，所以引用的时候要用函数age()，而不能用age变量
# print(s.age())
# # print(s.abc)
#
#
# # 利用完全动态的__getattr__，我们可以写出一个链式调用
# # 无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变
# class Chain(object):
#
#     def __init__(self, path=''):
#         self._path = path
#
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))
#
#     def __str__(self):
#         return self._path
#
#     __rppr__ = __str__
#
#
# print(Chain().status.user.timeline.list)


# __call__
# 一个对象实例(s)可以有自己的属性和方法，当我们调用实例方法age()/score()/gender()时，我们用instance.method()，也就是s.score()来调用。
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     # __call__()可以不定义参数，也可以定义参数
#     def __call__(self):
#         print('My name is %s.' % self.name)
#
#
# s = Student('Daemon')
# s()  # self参数不要传入
# 判断一个对象是否能被调用(Callable对象)
# 不能用Student()来测试，会报错：TypeError: __init__() missing 1 required positional argument: 'name'
# print(callable(Student()))
# print(callable(Student))
# print(callable(s))
# print(callable(max))
# print(callable([1, 2, 3]))
# print(callable(None))
# print(callable('str'))

# 使用枚举类
# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类（导入unique）
from enum import Enum, unique
#
# # Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员。
# Month = Enum('Month',
#              ('Jan', 'Feb', 'Mar',
#               'Apr', 'May', 'Jun',
#               'Jul', 'Aug', 'Sep',
#               'Oct', 'Nov', 'Dec'))
#
#
# # value属性则是自动赋给成员的int常量，默认从1开始计数
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)


# # @unique装饰器可以帮助我们检查保证没有重复值
# @unique
# class Weekday(Enum):
#     Sun = 0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
#
#
# # 访问Weekday的若干方法
# day1 = Weekday.Mon
# print(day1)
# print(Weekday.Mon)
# print(Weekday(2))
# print(Weekday['Tue'])
# print(Weekday.Tue.value)
# print(day1 == Weekday.Mon)
# print(day1 == Weekday.Tue)
# print(Weekday(1))
# print(day1 == Weekday(1))
# # Weekday(7)
# for name, member in Weekday.__members__.items():
#     print(name, '=>', member, ',', member.value + 1)


# 练习
# 把Student的gender属性改造为枚举类型（两种写法），可以避免使用字符串
# @unique
# class Gender(Enum):
#     Male = 0
#     Female = 1
# # Gender = Enum('gender', ['Male', 'Female'])
#
#
# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         if not isinstance(gender, Gender):
#             raise TypeError('input type error！')
#         self.gender = gender
#
#
# bart = Student('Bart', Gender.Male)
# if bart.gender == Gender.Male:
#     print('TEST successful')
# else:
#     print('TEST false')


# 使用元类

print('-----------error-debug-test---------')


# error
# 返回一个错误代码
# 缺点：函数本身应该返回的正常结果和错误码混在一起，造成调用者必须用大量的代码来判断是否出错
# def foo():
#     r = some_function()
#     if r == (-1):
#         return (-1)
#     # do something
#     return r
#
#
# def bar():
#     r = foo()
#     if r == (-1):
#         print('error')
#     else:
#         pass


# try...except...finally...错误处理机制
# try:
#     print('try...')
#     r = 10 / 2
#     print('result:', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')


# 如果发生了不同类型的错误，应该由不同的except语句块处理
# try:
#     print('try...')
#     r = 10 / int('a')
#     print('result:', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# # 如果没有错误发生，则执行else
# else:
#     print('no error!')
# finally:
#     print('finally...')
# print('END')


# 记录错误
# logging还可以把错误记录到日志文件里，方便事后排查
# import logging
#
#
# def foo(s):
#     return 10 / int(s)
#
#
# def bar(s):
#     return foo(s) * 2
#
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
#     finally:
#         print('finally...')
#
#
# main()


# # 抛出错误
# class FooError(ValueError):
#     pass
#
#
# def foo(s):
#     n = int(s)
#     if n == 0:
#         # 用 raise语句抛出一个错误的实例
#         raise FooError('invalid value: %s' % s)
#     return 10 / n
#
#
# foo('0')


# # 另一种错误处理的方式
# # Q：
# # 在bar()函数中，已经捕获了错误，
# # 但是，打印一个ValueError!后，为什么又把错误通过raise语句抛出去了？
# # A:
# # 捕获错误目的只是记录一下；
# # 由于当前函数不知道应该怎么处理该错误，
# # 所以，最恰当的方式是继续往上抛，让顶层调用者去处理。
# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n
#
#
# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError')
#         # raise语句如果不带参数，就会把当前错误原样抛出
#         raise
#
#
# bar()


# 练习
# 运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复
from functools import reduce
import types


def str2num(s):
    try:
        return int(s)
    except Exception as e:
        return float(s)


def calc(exp):
    ss = exp.split('+')
    print('ss :', ss)
    ns = map(str2num, ss)
    print('ns :', ns)
    print('list(ns) :', list(ns))
    print('list(ns) :', list(ns))
# 经过打印ns，知道ns是一个map object,
    # reduce第二个参数只接受列表，
    return reduce(lambda a, b: a + b, ns)
    # 所以如果reduce(functions, ns)会报错TypeError: reduce() of empty sequence with no initial value



def main():
    try:
        r = calc('100 + 200 + 345')
        print('100 + 200 + 345 =', r)
        r = calc('99 + 88 + 7.6')
        print('99 + 88 + 7.6 =', r)
    except TypeError as e:
        print('TypeError :', e)


main()


# def f(x, y):
#     r = x * 10 + y
#     return int(r)
#
#
# def f1(L):
#     return reduce(f, L)
#
#
# ff = f1('3')
# print(ff)
lambdaX = lambda x, y: int(x * 10 + y)

# 当列表成员个数为1时，程序不会报错，但reduce没有正常运行
f1 = reduce(lambdaX, '3')
print(f1)
print(f1, '->', type(f1))

# reduce引用的列表成员，至少是两个才会正常执行
f2 = reduce(lambdaX, [1, 2, 3])
print(f2)
print(f2, '->', type(f2))
f20 = reduce(lambdaX, '12')
print(f20)
print(f20, '->', type(f20))

f3 = reduce(lambdaX, [1.0])
print(f3)
print(f3, '->', type(f3))

# 当列表成员个数为0时，程序报错
# f4 = reduce(lambdaX, [])
# print(f4)
# print(f4, '->', type(f4))


