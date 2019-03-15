import numpy as np
import matplotlib
from matplotlib import pyplot as plt

# fname 为 你下载的字体库路径，注意 SimHei.ttf 字体的路径
# zhfont1 = matplotlib.font_manager.FontProperties(fname="simhei.ttf")

# x = np.arange(1, 11)
# print(x)
# y = 2 * x + 5
# print(y)
# plt.title("Matplotlib demo 测试一下中文字体", fontproperties=zhfont1)
# # plt.xlabel("x axis caption")
# # plt.ylabel("y axis caption")
# # plt.xlabel("我不引入zhfont1，能不能显示中文")   # 这样的中文是乱码！！！
# plt.xlabel("X 轴", fontproperties=zhfont1)
# plt.ylabel("Y 轴", fontproperties=zhfont1)
# # 要显示圆来代表点，而不是上面示例中的线，请使用 ob 作为 plot() 函数中的格式字符串。
# # plt.plot(x, y)
# plt.plot(x, y, "ob")
# plt.show()

# 使用系统的字体
# a=sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])

# for i in a:
#     print(i)
# 打印出你的 font_manager 的 ttflist 中所有注册的名字，
# 找一个看中文字体例如：STFangsong(仿宋）,然后添加以下代码即可：
# plt.rcParams['font.family']=['STFangsong']

# 绘制正弦波
# x = np.arange(0, 3 * np.pi, 0.1)
# y = np.sin(x)
# plt.title("sine wave form")
# plt.plot(x, y)
# plt.show()

# subplot()
# subplot() 函数允许你在同一图中绘制不同的东西。
# 计算正弦和余弦曲线上的点的 x 和 y 坐标
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
# 建立 subplot 网格，高为2，宽为1
# 激活第一个subplot
plt.subplot(2, 1, 1)
# 绘制第一个图像
plt.plot(x, y_sin)
plt.title('Sine')
# 将第二个subplot激活，并绘制第二个图像
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')
# 展示图像
plt.show()

# bar()
# pyplot 子模块提供 bar() 函数来生成条形图。

