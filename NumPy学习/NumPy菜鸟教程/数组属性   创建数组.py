import numpy as np

print('数组属性')

# a = np.arange(24)
# print(a)
# print('a.ndim :', a.ndim)
# b_2d = a.reshape(2, 12)
# print(b_2d)
# print('b_2d.ndim :', b_2d.ndim)
# b = a.reshape(3, 4, 2)
# print(b)
# print('b.ndim :', b.ndim)
# c = np.array([[1, 2], [3, 4]])
# print(c)
# d = c.reshape(1, 4)
# print(d)
# print('d.ndim :', d.ndim)

# # 看看array.shape属性跟array.reshape属性有什么区别，结果，并没有什么区别
# my_shape_array = np.array([[1, 2, 3], [4, 5, 6]])
# print(my_shape_array)
# # my_shape_array.shape = (3, 2)
# print(my_shape_array)
# print(type(my_shape_array))
# my_reshape_array = my_shape_array.reshape(3, 2)
# print(my_reshape_array)
# print(type(my_reshape_array))

# x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
# print(x.itemsize)
# y = np.array([1, 2, 3, 4, 5], dtype=np.float64)
# print(y.itemsize)

print('创建数组')

# # 自定义类型
# x = np.array([(1, 2), (3, 4)], dtype=[('a', '<i4'), ('b', '<i4')])
# print(x)
# print('x[\'a\'] :', x['a'])
# print('x[\'b\'] :', x['b'])
#
# z = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
# print(z)
# print(z.itemsize)

# x = [1, 2, 3]
# print(x)
# print(type(x))
# a = np.asarray(x)
# print(a)
# print(type(a))

# s = b'Hello World'
# a = np.frombuffer(s, dtype='S1')
# print(a)

# # list是range类型的对象
# list = range(5)
# # it是range_iterator类型的对象
# it = iter(list)
# print(list)
# print(it)
# # 使用迭代器创建ndarray
# x = np.fromiter(it, dtype=float)
# print(x)

# # 等差数列
# # 10块/（5-1份）=2.5，即每块间距2.5
# b = np.linspace(10, 20, 5)
# print(b)
# # 除了最后一个“num + 1”等间距的样本外，该序列由其他所有样本组成
# # 10块/（5+1-1份）=2，即每块间距2
# a = np.linspace(10, 20, 5, endpoint=False)
# print(a)
# a = np.linspace(1, 10, 5, retstep=True)
# print(a)
# # 扩展例子
# c = np.linspace(1, 10, 10).reshape([10, 1])
# print(c)

# 等比数列
# 默认底数base = 10
a = np.logspace(1.0, 2.0, num=10)
print(a)
# 修改底数base = 2
a = np.logspace(0, 9, 10, base=2)
print(a)