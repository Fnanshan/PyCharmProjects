import numpy.matlib
import numpy as np

# np.matlib 模块中返回的是一个矩阵 <class 'numpy.matrixlib.defmatrix.matrix'>，而不是ndarray对象
# matlib.empty()
a = np.matlib.empty((2, 2))
print(a)

# numpy.matlib.zeros()
print(np.matlib.zeros((2, 2)))

# numpy.matlib.ones()
print(np.matlib.ones((2, 2)))

# numpy.matlib.eye()
'''
# 对角线元素为 1，其他位置为零
# eye(n,M=None, k=0, dtype=float, order='C')
# n行，M列
#     k : int, optional
#         Index of the diagonal: 0 refers to the main diagonal,
#         a positive value refers to an upper diagonal,
#         and a negative value to a lower diagonal.
          对角线的索引：0指的是主对角线，
          正值是指上对角线，
          和较低对角线的负值
'''
print(np.matlib.eye(3, 4, 0))

# numpy.matlib.identity()
# 单位矩阵是个方阵，从主对角线上的元素均为 1，除此以外全都为 0。
print(np.matlib.identity(n=5))

# numpy.matlib.rand()
# 返回给定形状的随机值矩阵。
print(np.matlib.rand(2, 3))

# 矩阵总是二维的，而 ndarray 是一个 n 维数组。 两个对象都是可互换的。
i = np.matrix('1,2;3,4')
print(i)
print(type(i))  # <class 'numpy.matrixlib.defmatrix.matrix'>
j = np.asarray(i)
print(j)
print(type(j))  # <class 'numpy.ndarray'>
k = np.asmatrix(j)
print(k)
print(type(k))  # <class 'numpy.matrixlib.defmatrix.matrix'>