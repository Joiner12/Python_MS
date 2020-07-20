# -*- coding:utf-8 -*-

'''
    Script Name:Rename.py
    Description:
    1.重命名壁纸文件（D:\壁纸 - 副本）
    2.将脚本打包成exe文件

    reference:
    [1] <os库>https://docs.python.org/zh-cn/3/library/os.html
    [2] <os库常用函数>https://www.jianshu.com/p/812fd4d0d71d
    [3] <split函数>https://blog.csdn.net/ydyang1126/article/details/75050175
    [4] <字符串>https://www.runoob.com/python/python-strings.html
    [5] <break|return>https://stackoverflow.com/questions/28854988/what-is-the-difference-between-return-and-break-in-python
    [6] <数据类型转换>https://www.cnblogs.com/shockerli/p/python3-data-type-convert.html
    [7] <文件相关操作>https://juejin.im/post/5c57afb1f265da2dda6924a1
    [8] <' " "' 的区别> https://blog.csdn.net/woainishifu/article/details/76105667
    [9] <生成exe文件> https://blog.csdn.net/zengxiantao1994/article/details/76578421
    [10] <bat 运行脚本> https://zhuanlan.zhihu.com/p/81042686
    [11] <查看文件夹> https://www.cnblogs.com/strongYaYa/p/7200357.html
'''

import os
# import shutil


def Re_WallPaper():
    filepath = r"D:\壁纸-1"
    std_name = r'Wallpaper_'
    pic_Format = ['png', 'gif', 'jpg', 'bpm']
    std_fileCnt = 1
    re_stdfileCnt = 0
    if CheckName(filepath, std_name):
        print('start to rename')
        # rename
        detail_2 = os.listdir(filepath)
        picsRe = []

        # 统计标准文件个数
        for file_1 in detail_2:
            if file_1.find(std_name) == -1:
                sepNameTemp = SeperateName(file_1)
                if pic_Format.count(sepNameTemp[1]) != 0:
                    picsRe.append(file_1)
            else:
                std_fileCnt = std_fileCnt + 1
        for pic in picsRe:
            re_stdfileCnt = re_stdfileCnt + 1
            sepNameTemp = SeperateName(pic)
            if pic_Format.count(sepNameTemp[1]) != 0:
                origin_name = filepath + '\\' + pic
                new_name = filepath + '\\' + \
                    std_name + str(re_stdfileCnt+std_fileCnt) + \
                    '.' + sepNameTemp[1]
                os.rename(origin_name, new_name)
                print(origin_name, '->', new_name)
            else:
                pass
    else:
        print('no need to rename handle')
    debug_a = 1


def SeperateName(origin_name):
    if isinstance(origin_name, str):
        splt_str = origin_name.split('.', 1)
        out_name = splt_str
        return out_name
    else:
        return ''


'''
是否需要启动重命名
'''


def CheckName(filepath, std_name):
    renameFlag = False
    detail_1 = os.listdir(filepath)

    for i in detail_1:
        if i.find(std_name) == -1:
            # 区别是否为图片格式bmp,jpg,png,tif,gif
            SepTemp_1 = SeperateName(i)
            pic_Format = ['png', 'gif', 'jpg', 'bpm']
            if pic_Format.count(SepTemp_1[1]) != 0:
                renameFlag = True
                break
        else:
            pass
    return renameFlag


if __name__ == "__main__":
    # os.system('cls')
    # print('你紧紧拉住我衣袖')

    if False:
        Re_WallPaper()
