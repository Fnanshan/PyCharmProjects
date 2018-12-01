import numpy as np

# a = np.arange(10)
# print(a)
# s = slice(2, 7, 2)
# print(type(s))
# print(a[s])

# # 索引提取
# a = np.arange(10)
# print(a)
# b = a[2:7:2]
# print(b)
# b = a[2]
# print(b)
# b = a[2:]
# print(b)
# b = a[2:7]
# print(b)

# # 多维数组的索引提取
# a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
# print(a)
# print(a[0::2])

# ...的使用
# a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
# print(a)
# print(a[..., 1])
# print(a[1, ...])
# print(a[1:])
# print(a[..., 1:])

# 高级索引
# # 整数数组索引
# x = np.array([[1, 2], [3, 4], [5, 6]])
# print(x)
# t = np.array([[0, 1, 2], [0, 1, 0]])
# print(t)
# y = x[[0, 1, 2], [0, 1, 0]]
# print(y)

# # 这题我不会啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
# x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
# print('x :')
# print(x)
# t = np.array([[0, 0, 3, 3], [0, 2, 0, 2]])
# print('t :')
# print(t)
# rows = np.array([[0, 0], [3, 3]])
# print('rows :')
# print(rows)
# cols = np.array([[0, 2], [0, 2]])
# print('cols :')
# print(cols)
# y = x[rows, cols]
# print('y :')
# print(y)

# # 借助 切片: 或 ... 与 索引数组 组合
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(a)
# b = a[1:3, 1:3]
# print(b)
# c = a[1:3, [1, 2]]
# print(c)
# d = a[..., 1:]
# print(d)

# # 布尔索引
# x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
# print(x)
# print(x[x > 5])
# # 使用了 ~（取补运算符）来过滤 NaN。
# a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
# print(a)
# print(a[~np.isnan(a)])
# # 如何从数组中过滤掉非复数元素
# a = np.array([1, 2+6j, 5, 3.5+5j])
# print(a)
# print('非复数 :', a[~np.iscomplex(a)])
# print('复数 :', a[np.iscomplex(a)])

# 花式索引
x = np.arange(32).reshape((8, 4))
print(x)
# 传入顺序索引数组
# print(x[[4, 2, 1, 7]])
# 传入倒序索引数组
# print(x[[-4, -2, -1, -7]])
# 传入多个索引数组（使用np.ix_）
# 根据下标找数据[1,0]/[1,3]/[1,1]/[1,2];[5,0]/[5,3]/[5,1]/[5,2]。。。
# print(x[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])])