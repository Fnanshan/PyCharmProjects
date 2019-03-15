
import numpy as np
# 无复制
# 。 相反，它使用原始数组的相同id()来访问它。
# shape 和 reshape 的区别！ reshape会创建副本，shape不会创建副本。创建副本后，id改变。
a = np.arange(6)
b = a
# print("id(a) :", id(a))
# print("id(b) :", id(b))
# b.shape = (3, 2)
c = b.reshape((3, 2))
d = np.copy(c)
# # TEST
# if id(a) == id(b):
#     print("简单的赋值不会创建数组对象的副本，a==b")
#     print(a)
# else:
#     print("简单的赋值也会创建数组对象的副本")
#
# if id(a) == id(c):
#     print("reshape()不会创建副本，a==c")
# else:
#     print("reshape()会创建副本，a!=c")
#     print(id(c))
#     print(c)
#
# if id(c) == id(d):
#     print("copy函数没有创建副本")
# else:
#     print("copy函数会创建副本")
#     print(id(d))
#     print(d)

# 视图或浅拷贝
# ndarray.view() 方会创建一个新的数组对象，该方法创建的新数组的维数更改不会更改原始数据的维数。
testView = np.arange(6).reshape(3, 2)
print(testView)
print(id(testView))
testViewB = testView.view()
print(testViewB)
print(id(testViewB))
testViewB.shape = 2, 3
print(testViewB)