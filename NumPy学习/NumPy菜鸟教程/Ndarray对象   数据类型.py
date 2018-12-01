print('# Ndarray对象')

import numpy as np
# a = np.array([1, 2, 3])
# print(a)
# print('ndim :', a.ndim)
# 多于一个维度
# a = np.array([[1, 2], [3, 4]])
# print(a)
# print('ndim :', a.ndim)
# 最小维度
# b = np.array([[11, 12], [14, 16, 17]])
# print(b)
# print(type(b))
a = np.array([[1, 2, 3], [4, 5, 6]], dtype=complex, order='K')
print(a)
print('shape :', a.shape)
print('ndim :', a.ndim)
print('flags :', a.flags)

# a = np.zeros((5,))
# print(a)
# print('shape :', a.shape)
# my_random_array = np.random.random((5))
# print(my_random_array)

print('# NumPy数据类型')

# import numpy as np
# dt = np.dtype(np.int32)
# print(dt)
# print(type(dt))
#
# # int8, int16, int64 四种数据类型可以使用字符串'i1', 'i2', 'i4', 'i8'代替
# dt = np.dtype('i4')
# print(dt)
#
# # 字节顺序标注
# dt = np.dtype('>i4')
# print(dt)
# print(type(dt))
#
# # 结构化数据类型的使用，类型字段和对应的实际类型将被创建
# import numpy as np
#
# dt = np.dtype([('age', np.int8)])
# print(dt)
#
# 将数据类型应用于ndarray对象
import numpy as np
dt = np.dtype([('age', np.int8)])
# print('dt :', dt)
# print('type(dt) :', type(dt))
a = np.array([(10,), (20,), (30,)], dtype=dt)
# print(a)
# 类型字段名可以用于存取实际的 age 列
# print(a['age'])
b = np.array([(10,), (20,), (30,)])
# print(b)
# 定义一个结构化数据类型 student,
# 包含字符串字段 name，整数字段 age，及浮点字段 marks，
# 并将这个 dtype 应用到 adarray 对象。
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
# print(student)
a = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
# print(a)