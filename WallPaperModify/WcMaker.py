# -*- coding:utf-8 -*-
from wordcloud import WordCloud, ImageColorGenerator
import jieba
import matplotlib.pyplot as plt
from imageio import imread
from os import path
import numpy as np
import sys


def Gen_WordCloud(txt_file='./wenben.txt',
                  bg_cloud='./win10-wallpaper-2.jpg',
                  tar_cloud='./cloud.jpg',
                  tar_pic='./win10-wallpaper-1.jpg'):
    if path.isfile(txt_file) and path.isfile(tar_pic):
        print('爱的人手捧星光')
    else:
        return

    # 文本读取、分词
    with open(txt_file, mode='r', encoding='utf-8') as f:
        words = f.read()
    word_c = " ".join(jieba.cut(words))

    if path.isfile(bg_cloud):
        # 读取背景图片
        bg_pic_1 = np.array(imread(bg_cloud))
        image_colors = ImageColorGenerator(bg_cloud)
        word_cloud = WordCloud(font_path='simkai.ttf',
                               background_color='black', mask=bg_pic_1).generate(word_c)
        plt.imshow(word_cloud.recolor(color_func=image_colors),
                   interpolation='bilinear')
    else:
        # 生成图云
        # 根据输入图片调整云图大小
        tar_bg_1 = imread(tar_pic)
        shapeTemp = tar_bg_1.shape
        word_cloud = WordCloud(font_path='simkai.ttf',
                               background_color='white',
                               width=int(shapeTemp[1]/2),
                               height=int(shapeTemp[0]/2)).generate(word_c)
        plt.imshow(word_cloud, interpolation='bilinear')

    plt.axis("off")
    # plt.show()
    word_cloud.to_file(tar_cloud)
    print('word from:%s\nbase:%s\nget:%s\n' % (txt_file, bg_cloud, tar_cloud))
    # return txt_file, bg_pic, tar_cloud


def Gen_WordCloud_Matlab():
    # OSError: Python 3_7 is not supported.
    return
    import matlab
    eng = matlab.engine.start_matlab()
    print(eng)
    eng.quit()


def PassParameter(pastr):
    if isinstance(pastr, str):
        print('instance string')
    else:
        print('not instance string')


def Gen_WordCloud_V2():
    d = path.dirname(__file__)
    txt_file = path.join(d, 'wenben.txt')
    bg_pic = path.join(d, 'win10-wallpaper-1.jpg')
    # if False:
    #     tar_pic = r'H:\MatlabFiles\Blocks\MakeGif\cloud.jpg'
    # else:
    #     tar_pic = path.join(r'H:\MatlabFiles\Blocks\WallPaperHandle', 'cloud.jpg')

    # 文本读取、分词
    with open(txt_file, mode='r', encoding='utf-8') as f:
        words = f.read()
    word_c = " ".join(jieba.cut(words))

    if False:
        # 读取背景图片
        bg_pic_1 = np.array(imread(bg_pic))
        image_colors = ImageColorGenerator(bg_pic_1)
        word_cloud = WordCloud(font_path='simkai.ttf',
                               background_color='black', mask=bg_pic_1).generate(word_c)
        plt.imshow(word_cloud.recolor(color_func=image_colors),
                   interpolation='bilinear')
    else:
        # 生成图云
        word_cloud = WordCloud(font_path='simkai.ttf', background_color='',
                               width=1920, height=1080).generate(word_c)
        plt.imshow(word_cloud, interpolation='bilinear')

    plt.axis("off")
    # plt.show()
    word_cloud.to_file(tar_pic)
    print('word from:%s\nbase:%s\nget:%s\n' % (txt_file, bg_pic, tar_pic))
    return txt_file, bg_pic, tar_pic


if __name__ == "__main__":
    txt_file = 'D:\Codes\Python_MS\WallPaperModify\wenben.txt'
    bg_cloud = 'D:\Codes\Python_MS\WallPaperModify\win10-wallpaper-2.jpg'
    tar_cloud = 'D:\Codes\Python_MS\WallPaperModify\cloud.jpg'
    tar_pic = 'D:\Codes\Python_MS\WallPaperModify\win10-wallpaper-1.jpg'
    Gen_WordCloud(txt_file=txt_file,
                  tar_cloud=tar_cloud,
                  tar_pic=tar_pic)
