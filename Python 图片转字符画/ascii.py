'''
字符画
    是一系列字符的组合，我们可以把字符看作是比较大块的像素，
    一个字符能表现一种颜色（暂且这么理解吧），字符的种类越多，可以表现的颜色也越多，图片也会更有层次感。
灰度值：
    指黑白图像中点的颜色深度，范围一般从0到255，白色为255，黑色为0，故黑白图片也称灰度图像

'''
from PIL import Image
import argparse


# argparse 库是用来管理命令行参数输入的
# 命令行输入参数处理
parser = argparse.ArgumentParser()
# print(parser)

parser.add_argument('file')     # 输入文件
parser.add_argument('-o', '--output')    # 输出文件
parser.add_argument('--width', type=int, default=180)   # 输出字符串画宽
parser.add_argument('--height', type=int, default=80)  # 输出字符画高

# 获取参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

# 创建一个不重复的字符列表，灰度值小（暗）的用列表开头的符号，灰度值大（亮）的用列表末尾的符号
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# 将256灰度映射到70个字符上（ RGB值转字符）

def get_char(r, g, b, alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)    # 使用灰度值公式将像素的 RGB 值映射到灰度值

    unit = (256.0 + 1) / length
    return ascii_char[int(gray/unit)]


if __name__ == '__main__':

    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    # print(txt)

    # 字符画输出到文件
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open("output_gitHub_touxiang.txt", 'w') as f:
            f.write(txt)