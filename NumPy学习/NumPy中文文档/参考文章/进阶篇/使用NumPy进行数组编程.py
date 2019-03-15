import numpy as np
# 什么是矢量化
# # # 计数
# np.random.seed(444)
# x = np.random.choice([False, True], size=100000)
# print(x)
# print(x.ndim)
# print(x.shape)
#
#
# def count_transitions(x) -> int:    # 使用Python for循环，一种方法是成对地评估序列中每个元素的真值以及紧随其后的元素：
#     count = 0
#     for i, j in zip(x[:-1], x[1:]):
#         if j and not i:
#             count += 1
#     return count
#
#
# print('x :', x)
# print(count_transitions(x))
#
# print(np.count_nonzero(x[:-1] < x[1:]))     # 在矢量化形式中，没有明确的for循环或直接引用各个元素：
#
# from timeit import timeit
# setup = 'from __main__ import count_transitions, x; import numpy as np'
# num = 1000
# t1 = timeit('count_transitions(x)', setup=setup, number=num)
# t2 = timeit('np.count_nonzero(x[:-1] < x[1:])', setup=setup, number=num)
# print('Spped difference: {:0.1f}x'.format(t1 / t2))


# # 买低，卖高
# def profit(prices):  # O(n)解决方案，它包括迭代序列一次，找出每个价格和运行最小值之间的差异。
#     max_px = 0
#     min_px = prices[0]
#     for px in prices[1:]:   # prices[1:] : (18, 14, 17, 20, 21, 15)
#         min_px = min(min_px, px)
#         max_px = max(px - min_px, max_px)
#     return max_px
#
#
# prices = (20, 18, 14, 17, 20, 21, 15)
# print(profit(prices))


# 用Numpy实现
# # Create mostly NaN array with a few 'turning points'(local min/max)
# prices = np.full(100, fill_value=np.nan)
# prices[[0, 25, 60, -1]] = [80., 30., 75., 50.]
#
#
# # Linearly interpolate the missing values and add some noise.
# x = np.arange(len(prices))
# is_valid = ~np.isnan(prices)
# prices = np.interp(x=x, xp=x[is_valid], fp=prices[is_valid])
# prices += np.random.randn(len(prices)) * 2
# print('prices :', prices)
#
# # 下面是matplotlib的示例。俗话说：买低(绿)，卖高(红)：
import matplotlib.pyplot as plt
#
# # Warning! This isn't a fully correct solution, but it works for now.
# # If the absolute min came after the absolute max, you'd have trouble.
# mn = np.argmin(prices)  # mn :25
# mx = mn + np.argmax(prices[mn:])    # mx :60
# kwargs = {'markersize': 12, 'linestyle': ''}
#
# fig, ax = plt.subplots()
# ax.plot(prices)
# ax.set_title('Price History')
# ax.set_xlabel('Time')
# ax.set_ylabel('Price')
# ax.plot(mn, prices[mn], color='green', **kwargs)
# ax.plot(mx, prices[mx], color='red', **kwargs)
# plt.show(color='green')

# # Intermezzo:理解轴符号
# arr = np.array([[1, 2, 3],
#                 [10, 20, 30]])
# print(arr.sum(axis=0))
# print(arr.sum(axis=1))

# broadcast


# # 矩阵编程实际应用：示例
# tri = np.array([[1, 1],
#                 [3, 1],
#                 [2, 3]])
# centroid = tri.mean(axis=0)
# print(centroid)
# trishape = plt.Polygon(tri, edgecolor='r', alpha=0.2, lw=5)
# _, ax = plt.subplots(figsize=(4, 4))
# ax.add_patch(trishape)
# ax.set_ylim([.5, 3.5])
# ax.set_xlim([.5, 3.5])
# ax.scatter(*centroid, color='g', marker='D', s=70)
# ax.scatter(*tri.T, color='b', s=70)
# plt.show()