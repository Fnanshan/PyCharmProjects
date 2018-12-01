'''NumPy中文文档-相关代码
https://www.numpy.org.cn/article/basics/understanding_numpy.html
'''
import numpy as np

# # ------------------创建数组-------------------
# a = np.array([0, 1, 2, 3, 4])
# b = np.array((0, 1, 2, 3, 4))
# c = np.arange(5)
# d = np.linspace(0, 2*np.pi, 5)
# print(a)
# print(b)
# print(c)
# # print(d)

# MD Array,
# a = np.array([[11, 12, 13, 14, 15],
#               [16, 17, 18, 19, 20],
#               [21, 22, 23, 24, 25],
#               [26, 27, 28 ,29, 30],
#               [31, 32, 33, 34, 35]])
# # print(a[2, 4])
# print(a)

# 多维数组切片
# print(a[0, 1:4])
# print(a[1:4, 0])
# print(a[::2, ::2])
# print(a[:, 1])

# 数组属性
# print(type(a))
# print(a.dtype)
# print(a.size)
# print(a.itemsize)
# print(a.ndim)
# print(a.nbytes)

# # ---------------使用数组----------------
# # Basic Operators
# a = np.arange(25)
# a = a.reshape((5, 5))
# print('a :')
# # print(a)
#
# b = np.array([10, 62, 1, 14, 2, 56, 79, 2, 1, 45,
#               4, 92, 5, 55, 63, 43, 35, 6, 53, 24,
#               56, 3, 56, 44, 78])
# # 1D--->2D
# # b = b.reshape((5, 5))
# # 根据b数组的长度25,进行开方，要有个异常判断，如果b.size不能开方呢？
# # 根据开方数构造一个新维度的数组。
# print(b.size)
# sqrtB = int(np.math.sqrt(b.size))
# try:
#     b = b.reshape(sqrtB, sqrtB)
# except ValueError as e:
#     print('valueError :', e)
# finally:
#     print('b :')
#     # print(b)

# 对数组进行逐元素运算
# print(a + b)
# 平方
# print(a ** 2)
# print(a < b)
# print(a.dot(b))

# # 数组特殊运算符
# a = np.arange(10)
# # print(a)
# # print(a.cumsum())

# # 索引进阶
# # Fancy indexing
# a = np.arange(0, 100, 10)   # def arange(start=None, stop=None, step=None, dtype=None)
# indices = [1, 5, -1]
# b = a[indices]
# # print(a)
# # print(b)

# # Boolen masking
# # 将数组传递给涉及数组的条件，它将为你提供一个值的数组，为该条件返回true。
# # 蓝色点(在图中还包括绿点，但绿点掩盖了蓝色点)，显示值大于0的所有点。绿色点表示值大于0且小于一半π的所有点。
# import matplotlib.pyplot as plt
#
# # linspace()等差数列
# a = np.linspace(0, 2 * np.pi, 50)
# # print('a :', a)
# b = np.sin(a)
# # print('b :', b)
# plt.plot(a, b)
# # mask是一个numpy.ndarray对象
# mask = b >= 0
# # print(mask)
# print('a[mask] :', a[mask])
# print('b[mask] :', b[mask])
# plt.plot(a[mask], b[mask], 'bo')
# mask = (b >= 0) & (a <= np.pi / 2)
# # print('a[mask] :', a[mask])
# # print('b[mask] :', b[mask])
# plt.plot(a[mask], b[mask], 'go')
# plt.show()

# # pyplot.py 测试代码
# import matplotlib.pylab as plt
# x = np.linspace(-np.pi, np.pi, 201)
# plt.plot(x, np.sin(x))
# plt.xlabel('Angle [rad]')
# plt.ylabel('sin(x)')
# plt.axis('tight')
# plt.show()

# # 缺省索引
# # Incomplete Indexing
# a = np.arange(0, 100, 10)
# print(a)
# b = a[:5]
# print(b)
# c = a[a >= 50]
# print(c)

# # Where()
# a = np.arange(0, 100, 10)
# print(a)
# b = np.where(a < 50)
# print('b :', b)
# print('b :', b[0])
# print('type(b) :', type(b))
# createNumArray = np.asarray(b)
# print('createNumArray :', createNumArray)
# print(createNumArray.ndim)
# c = np.where(a >= 50)[0]
# print(c)