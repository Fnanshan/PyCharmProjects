import numpy as np

# numpy.save()
# numpy.save() 函数将数组保存到以 .npy 为扩展名的文件中。
a = np.array([1, 2, 3, 4, 5])

# 保存到outfile.npy文件上
np.save('outfile.npy', a)

# 保存到outfile2.npy文件上
np.save('outfile2', a)

# load函数读取数据
b = np.load('outfile.npy')
# print(b)

# np.savez
# numpy.savez() 函数将多个数组保存到以 npz 为扩展名的文件中。
a1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
b1 = np.arange(0, 1.0, 0.1)
c1 = np.sin(b)
# c1 使用了关键字参数sin_array
# 把a1/b1/c1传入daemon.npz中，其中c1的数组名称为sin_array
np.savez("daemon.npz", a1, b1, sin_array=c1)
r1 = np.load("daemon.npz")
# print(a1)
# print(b1)
# print(c1)
# print(r1)
# print(r1.files)
# print(r1["sin_array"])
# print(r1["arr_0"])
# print(r1["arr_1"])

# savetxt()
# savetxt() 函数是以简单的文本文件格式存储数据，对应的使用 loadtxt() 函数来获取数据。
