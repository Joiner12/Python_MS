# -*- coding:utf-8 -*-
from wordcloud import WordCloud, ImageColorGenerator
import jieba
import matplotlib.pyplot as plt
from imageio import imread
from os import path
import numpy as np


def Gen_WordCloud():
    d = path.dirname(__file__)

    # 文件路径
    txt_file = path.join(d, 'wenben.txt')
    bg_pic = path.join(d, 'win10-wallpaper-2.jpg')
    tar_pic = path.join(
        r'D:\Codes\MatlabFiles\Blocks\WallPaperHandle', 'cloud.jpg')

    # 文本读取、分词
    with open(txt_file, mode='r', encoding='utf-8') as f:
        words = f.read()
    word_c = " ".join(jieba.cut(words))

    if True:
        # 读取背景图片
        bg_pic = np.array(imread(bg_pic))
        image_colors = ImageColorGenerator(bg_pic)
        word_cloud = WordCloud(font_path='simkai.ttf',
                               background_color='white', mask=bg_pic).generate(word_c)
        plt.imshow(word_cloud.recolor(color_func=image_colors),
                   interpolation='bilinear')
    else:
        # 生成图云
        word_cloud = WordCloud(font_path='simkai.ttf', background_color='white',
                               width=1920, height=1080).generate(word_c)
        plt.imshow(word_cloud, interpolation='bilinear')

    plt.axis("off")
    # word_cloud.to_file(tar_pic)
    plt.show()
    print('word from:%s\nbase:%s\nget:%s\n' % (txt_file, bg_pic, tar_pic))


def Gen_WordCloud_Matlab():
    # OSError: Python 3_7 is not supported.
    return
    import matlab
    eng = matlab.engine.start_matlab()
    print(eng)
    eng.quit()


if __name__ == "__main__":
    Gen_WordCloud()
