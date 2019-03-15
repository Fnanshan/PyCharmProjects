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
import imageio as imageio
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
print('-----Scipy-----')
print('图像操作')
# from scipy.misc import imread, imsave, imresize
# # Read an JPEG image into a numpy array
# img = imread('cat.jpg')
# print(img.dtype, img.shape)
# # We can tint(染色) the image by scaling(缩放) each of the color channels by a different scalar constant （常数）.
# # The image has shape (400, 248, 3);
# # we multiply（乘） it by the array [1, 0.95, 0.9] of shape (3,);
# # numpy broadcasting means that this leaves the red channel unchanged（红色通道不变）,
# # and multiplies（乘以） the green and blue channels by 0.95 and 0.9 respectively （分别）.
# img_tinted = img * [1, 0.95, 0.9]
#
# # Resize（调整） the tinted image（彩色图像） to be 300 by 300 pixels（300 像素）.
# img_tinted = imresize(img_tinted, (300, 300))
#
# # Write the tinted image back to disk
# imsave('cat_tinted.jpg', img_tinted)


print('点之间的距离')
# from scipy.spatial.distance import pdist, squareform
#
# # Create the following array where each row is a point in 2D space:
# # [[0 1]
# #  [1 0]
# #  [2 0]]
# x = np.array([[0, 1], [1, 0], [2, 0]])
# print(x)
# d = squareform(pdist(x, 'euclidean'))
# print(d)


print('-----Matplotlib-----')
import matplotlib.pyplot as plt

# print('# 绘制简单的sin曲线')
# # Compute the x and y coordinates（坐标） for points on a sine curve （正弦曲线上）
# x = np.arange(0, 3 * np.pi, 0.1)
# y = np.sin(x)
# print(x)
# print(y)
#
# # Plot the points using matplotlib
# plt.plot(x, y)
# plt.show()  # You must call plt.show() to make graphics appear.

print('# # 绘制多条线，添加标题，图例和轴标签')
# x = np.arange(0, 3 * np.pi, 0.1)
# y_sin = np.sin(x)
# y_cos = np.cos(x)
#
# plt.plot(x, y_sin)
# plt.plot(x, y_cos)
# plt.xlabel('x axis label')
# plt.ylabel('y axis label')
# plt.title('Sine and Cosine')
# plt.legend(['Sine', 'Cosine'])
# plt.show()

print('# 子图')
# x = np.arange(0, 3 * np.pi, 0.1)
# y_sin = np.sin(x)
# y_cos = np.cos(x)
#
# # Set up a subplot grid（绘制子图网格） that has height 2 and width 1,
# # and set the first such subplot as active.
# # subplot(nrows, ncols, index, **kwargs)
# plt.subplot(2, 1, 1)
#
# # Make the first plot
# plt.plot(x, y_sin)
# plt.title('Sine')
#
# # Set the second subplot as active, and make the second plot.
# plt.subplot(2, 1, 2)
# plt.plot(x, y_cos)
# plt.title('Cosine')
#
# plt.show()

# print('# 图片')
# import numpy as np
# from scipy.misc import imread, imresize
# import matplotlib.pyplot as plt
#
# # img = imread('cat.jpg')
# img = imageio
# img_tinted = img * [1, 0.95, 0.9]
#
# # Show the original image
# plt.subplot(1, 2, 1)
# plt.imshow(img)
#
# # Show the tinted image
# plt.subplot(1, 2, 2)
#
# # A slight gotcha（轻微的问题） with imshow is that it might give strange results（这可能会产生奇怪的结果）if presented with data that is not uint8.
# # To work around this(为了解决这个问题), we explicitly（显式） cast the image to uint8 before displaying it. (cast ... to 强制转换）
# plt.imshow(np.uint8(img_tinted))
# plt.show()