import numpy as np
import scipy as sci

print('# L2难度')

# 1.将numpy导入为 np 并打印版本号。
# print(np.__version__)
# print(sci.__version__)

# 2.创建从0到9的一维数字数组
# a = np.arange(10)
# print(a)
# print(type(a))

# 3.创建一个numpy数组元素值全为True（真）的数组
# a = np.full((3, 4), True)
# print(a)
# b = np.full((3, 4), True, dtype=bool)
# print(b)
# c = np.ones((3, 3), dtype=bool)
# print(c)

# 4.从 arr 中提取所有的奇数
# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# # print(arr[arr % 2 == 1])
#
# 5.将arr中的所有奇数替换为-1。
# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# arr[arr % 2 != 0] = -1
# print(arr)

# 6.将arr中的所有奇数替换为-1，而不改变arr，输出 out
# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# out = np.array(arr)
# out[out % 2 != 0] = -1
# print(arr)
# print(out)
# out2 = np.where(arr % 2 != 0, -1, arr)
# print(arr)
# print(out2)

# 7.将一维数组转换为2行的2维数组
# arr = np.arange(10)
# print(arr)
# print(np.reshape(arr, (2, 5)))
# print(arr.reshape(2, -1)) # # Setting to -1 automatically decides the number of cols

print('# L2难度')

# 8.如何垂直堆叠数组a和数组b？
# # 我的方法
# a = np.arange(10).reshape(2, -1)
# b = np.repeat(1, 10).reshape(2, -1)
# # print(a)
# # print(b)
# c = np.append(a, b, 0)
# print(c)
# # Method1
# print(np.concatenate([a, b], axis=0))
# # Method2
# print(np.vstack([a, b]))
# # Method3
# print(np.r_[a, b])  # Translates slice objects to concatenation along the first axis.

# # 9.如何水平叠加两个数组？
# a = np.arange(10).reshape(2, -1)
# b = np.repeat(1, 10).reshape(2, -1)
# print(a)
# print(b)
#
# # Answers
# # Method 1:        Join a sequence of arrays along an existing axis.
# c = np.concatenate([a, b], axis=1)
# print(c)
#
# # Method 2:        Stack arrays in sequence horizontally (column wise).
# #                  This is equivalent to concatenation along the second axis.
# d = np.hstack([a, b])
# print(d)
#
# # Method 3:
# e = np.c_[a, b]
# print(e)

# # 10. 如何在无硬编码的情况下生成numpy中的自定义序列？
# a = np.array([1, 2, 3])
# print(a)                    # 输出[1 2 3]
# print(np.repeat(a, 3))      # 输出[1 1 1 2 2 2 3 3 3]
# print(np.r_[np.repeat(a, 3), np.tile(a, 3)])

# # 11. 如何获取两个numpy数组之间的公共项？
# a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
# b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
# print(np.intersect1d(a, b))

# 12. 如何从一个数组中删除存在于另一个数组中的项？
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 6, 7, 8, 9])
# From 'a' remove all of 'b'
print(np.setdiff1d(a, b))
