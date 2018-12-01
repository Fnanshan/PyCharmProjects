import numpy as np

print('------------------------broadcast-------------')
# # 形状相同，不管是几维数组
# a = np.array([[1, 2], [3, 4]])
# b = np.array([[10, 20], [30, 40]])
# c = a * b
# print(a)
# print(b)
# print(c)

# # 形状不同，numpy自动触发广播机制
# a = np.array([[0, 0, 0],
#               [10, 10, 10],
#               [20, 20, 20],
#               [30, 30, 30]])
# b = np.array([0, 1, 2])
# print(a)
# print(b)
# print('a.shape :', a.shape)
# print('b.shape :', b.shape)
# t = a + b
# print(t)
# print('t.shape :', t.shape)

a = np.array([[0, 0, 0],
              [10, 10, 10],
              [20, 20, 20],
              [30, 30, 30]])
A = np.array([1, 2, 3])
# print('A.ndim :', A.ndim)
# reps = (4, 1)
# print('reps :', reps)
# # print(help(reps))
# # print(reps.__len__())
AA = np.tile(A, (2, 2))
# print(A)
# print(AA)

print('对np.tile的研究')
# def tile(A, reps):
#     try:
#         tup = tuple(reps)
#         print('tup :', tup)
#     except TypeError:
#         tup = (reps,)
#         print('except tup :', tup)
#     d = len(tup)
#     print('tup len :', d)
#     c = np.array(A, copy=False, subok=True, ndmin=d)
#     print('c :', c)
#     print('c.shape :', c.shape)
#     shape_out = tuple(s*t for s, t in zip(c.shape, tup))
#     for s, t in zip(c.shape, tup):
#         print('s ', s, '*', 't ', t)
#     print('shape_out :')
#     print(shape_out)
#     n = c.size
#     print('n = c.size :', n)
#     if n > 0:
#         print('n :', n)
#         for dim_in, nrep in zip(c.shape, tup):
#             print('dim_in :', dim_in)
#             print('nrep :', nrep)
#             if nrep != 1:
#                 print('if nrep != 1')
#                 c = c.reshape(-1, n).repeat(nrep, 0)
#                 print('c -->')
#                 print('c.shape :', c.shape)
#                 print(c)
#             n //= dim_in
#             print('n -->')
#             print(n)
#     y = c.reshape((2, 6))
#     print('c最后：')
#     print(y)
#     print(y.shape)
#
#
# AA = tile(A, (2, 2))
#
# print('----------------------')
# c = np.array([[1, 2, 3],
#               [1, 2, 3],
#               [1, 2, 3],
#               [1, 2, 3]])
# d = c.reshape((2, 6))
# print(c)
# print(d)

print('------------------迭代数组---------------')

# a = np.arange(6).reshape(2, 3)
# b = np.array(a, order='F')
# print(a)
# for x in np.nditer(b):
#     print(x, end=', ')
# print(b.flags)

a = np.arange(6).reshape(2, 3)
print(a)
print(a.T)
print(a.T.flags)
for x in np.nditer(a.T):
    print(x, end=', ')
print('\n')
# #
# # t = a.T.copy(order='F')
# # print(t)
# # for x in np.nditer(t):
# #     print(x, end=', ')

# # 修改数组中元素的值: np.nditer参数op_flags
# a = np.arange(0, 60, 5).reshape((3, 4))
# print(a)
# for x in np.nditer(a, op_flags=['readwrite']):
#     x[...] = 2 * x
#     print(x)
# print(a)

# 使用外部循环： np.nditer参数flags
# a = np.arange(0, 60, 5).reshape((3, 4))
# print(a)
# for x in np.nditer(a, flags=['external_loop'], order='F'):
#     print(x, end=', ')
# for x in np.nditer(a, flags=['f_index']):
#     print(x, end=', ')

# # Tracking an Index or Multi-Index¶
# a = np.arange(6).reshape(2, 3)
# print(a)
# it = np.nditer(a, flags=['f_index'])
# while not it.finished:
#     print('%d <%d>' % (it[0], it.index), end=' ')
#     print(it.iternext())

# # it.multi_index里面放的是一个元组
# it = np.nditer(a, flags=['multi_index'])
# while not it.finished:
#     print('%d <%s>' % (it[0], it.multi_index), end=' ')
#     print(it.iternext())

# it = np.nditer(a, flags=['multi_index'], op_flags=['writeonly'])
# with it:
#     while not it.finished:
#         print('it[0] :', it[0])
#         print('it.multi_index[0] :', it.multi_index[0])
#         print('it.multi_index[1] :', it.multi_index[1])
#         it[0] = it.multi_index[1] - it.multi_index[0]
#         print(it.iternext())
#
# print(a)