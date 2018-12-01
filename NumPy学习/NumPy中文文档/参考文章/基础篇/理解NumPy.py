import numpy as np

print('理解NumPy')

# NumPy中的数组
my_2d_array = np.zeros((2, 3))
print(my_2d_array)

my_array = np.array([[4, 5], [6, 1]])
print(my_array[0][1])

my_array_column_2 = my_array[:, 1]
print(my_array_column_2)

# NumPy中的数组操作
a = np.array([[1.0, 2.0], [3.0, 4.0]])
b = np.array([[5.0, 6.0], [7.0, 8.0]])
sum = a + b
difference = a - b
product = a * b
quotient = a / b
print(sum)
print(difference)
print(product)
print(quotient)

# 矩阵乘法
matrix_product = a.dot(b)
print(matrix_product)