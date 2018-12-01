# # String对象的方法
# s = 'hello'
# print(s.capitalize())
# print(s.upper())
# print(s.lower())
# print(s.rjust(7))
# print(s.center(7))

# # Containers
# xs = [3, 1, 2]
# # help(enumerate)
# d = {(x, x+1): x for x in range(10)}
# print(d)
# print(type(d))
# t = (5, 6)
# print(t)
# print(type(t))
# print(d[t])

# NumPy
import numpy as np

# # Arrays
# c = np.full((2, 2), 7)
# print(c)
# d = np.eye(2)
# print(d)
# e = np.random.random((2, 2))
# print(e)
'----------------------------------'
# # Broadcasting
# # 例如，假设我们要向矩阵的每一行添加一个常数向量。
# x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# v = np.array([1, 0, 1])
# y = np.empty_like(x)  # Create an empty matrix with the same shape as x
# print(x)
# print(v)
# print(y)
# for i in range(4):
#     y[i, :] = x[i, :] + v
# print(y)
'-------------------------------'
# # 但是当矩阵 x 非常大时，
# # 在Python中计算显式循环可能会很慢。
# # 注意，向矩阵 x 的每一行添加向量 v 等同于
# # 通过垂直堆叠多个 v 副本来形成矩阵 vv，
# # 然后执行元素的求和x 和 vv。
# x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# v = np.array([1, 0, 1])
# vv = np.tile(v, (4, 1))
# # print('len :', len((4, 1)))
# # print('v-shape :', v.shape)
# # print('v-dimension :', v.ndim)
# # print('vv-dimension :', vv.ndim)
# print(x)
# print(v)
# print(vv)
# y = x + vv
# print(y)
'---------------------------------'
# # 使用broadcasting
# x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# v = np.array([1, 0, 1])
# y = x + v
# print(y)
'---------------------------------'
# # Compute outer product of vectors  计算向量的外积
# v = np.array([1, 2, 3])
# w = np.array([4, 5])
# print(v)
# print(np.reshape(v, (3, 1)))
# print(np.reshape(v, (3, 1)) * w)
#
# # Add a vector to each row of a matrix  向矩阵的每一行添加一个向量
# x = np.array([[1, 2, 3], [4, 5, 6]])
# print(x + v)
#
# # Add a vector to each column of a matrix  在矩阵的每一列加一个向量
# print((x.T + w).T)
#
# print(x + np.reshape(w, (2, 1)))
#
# print(x * 2)
'----------------------------------'
print('Scipy')

from scipy.misc import imread, imsave, imresize
img = imread('cat.jpg')
print(img.dtype, img.shape)
# print(img)
print('--------------------------')
# img_tinted = img * [1, 0.95, 0.9]
# print(img_tinted)
t = np.array([1, 0.95, 0.9])
print(t)
print(t.shape)
t.reshape((1, ))
print(t)
print(t.shape)
