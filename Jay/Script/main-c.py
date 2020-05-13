#-*- coding:utf-8 -*-
"""
    Jay:
    albums & songs
"""

from datetime import datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen
from os import walk, chdir
from os.path import abspath, join
from time import sleep


class Jay_VerOne():
    fontpage_link = r"file:/Src/Albums-2/FrontPage/周杰伦 - 虾米音乐.html"
    html_link = r"file:/Src/Albums-2/Initial J/周杰伦 - 虾米音乐.html"
    rootpath = r"./Src/Albums-2"
    tar = r"D:\Python_M\Code\Jay\Doc\Album-Jay.md"

    # 根据不同的运行环境设置根目录
    if True:
        tar_root = r"D:\Python_M\Code\Jay"
        album_root = r"D:\Python_M\Code\Jay\Src\Albums-2"
    else:
        tar_root = r"D:\Python_M\Code\Jay"

    def __init__(self):
        # 设置脚本运行根目录
        chdir(self.tar_root)
        timeStand = datetime.now()
        timeStand = timeStand.strftime("%Y-%m-%d %H:%M:%S")
        # htmls
        file_html = list()
        print("Jay Chou Scrawler start at:%s" % (timeStand))
        for i in range(5):
            print(".")
        print(abspath(self.rootpath))
        # depart line
        self.__initmdfile__()
        self.__searchhtml__(self.album_root)
        if True:
            for html_i in self.file_html:
                html_i = "file:" + html_i
                print(html_i)
                self.GetInfoFromLocalFile_v1(html_i)

    def __initmdfile__(self):
        with open(self.tar, mode="w", encoding='utf-8') as mdf:
            mdf.write("# Jay Chou \n")
            if not mdf.closed:
                mdf.close()

    # *.html
    def __searchhtml__(self, rootpath):
        album_cnt = 1
        self.file_html = list()
        for root, dirs, files in walk(rootpath, True):
            if not len(dirs) == 0:
                for file_1 in files:
                    file_name = join(root, file_1)
                    if r"虾米音乐.html" in file_name:
                        self.file_html.append(file_name)
                        print(file_name)
                        album_cnt += 1
            else:
                for file_1 in files:
                    file_name = join(root, file_1)
                    if r"虾米音乐.html" in file_name:
                        self.file_html.append(file_name)
                        print(file_name)
                        album_cnt += 1

        print(album_cnt)

    # 找出front page中的专辑列表图片|链接|名字
    # info：专辑信息 wrapper：专辑封面
    def FrontPage(self):
        html_fp = urlopen(self.fontpage_link)
        if html_fp is None:
            print("get null page code")
            return
        bsObj = BeautifulSoup(html_fp.read(), features="lxml")
        temp_bs = bsObj.findAll("div", {"class": "info"})

        for album_i in temp_bs:
            print(album_i)
            # print(album_i.find("div",{"cover":"img"}))
        if True and False:
            artist_view = bsObj.findAll("div", {"class": "wrapper"})
            debug_a = artist_view

    '''
        从本地HTML文件中提取信息
    '''

    def GetInfoFromLocalFile_v1(self, html_link):
        retdict = dict()
        # print("get album info from local html files")
        htmllink = html_link
        html = urlopen(htmllink)
        if html is None:
            print("warning:null web page")
            return
        bsObj = BeautifulSoup(html.read(), features='lxml')

        albummaini = bsObj.find("div", {"data-spm": "albummaini"})
        if albummaini is None:
            print("didn't find object ,return")
            return
        # album
        album_name = albummaini.find("div", {"class": "titleInfo-name"})
        album_name = album_name.get_text()
        # singer
        singer_name = albummaini.find("div", {"class": "singer-name"})
        singer_name = singer_name.get_text()

        # pulish date
        publish_date = albummaini.find(
            "div",
            {"style": "color: gray; font-weight: 300; margin-top: 10px;"})
        publish_date = publish_date.get_text()
        # cover
        album_cover = bsObj.find("div", {"class": "cover"}).find("img")["src"]
        # songs
        song_detail = list()
        songs = bsObj.findAll("div", {"class": "song-name em"})
        for song in songs:
            song_detail.append(song.get_text())
        chdir(r"D:\Python_M\Code\Jay\Src\Albums-2")
        print(abspath(r"../" + album_cover))
        # print(album_name, singer_name, publish_date, song_detail,
        #       abspath(album_cover))

    """
        遍历文件html并列出歌单
    """

    def WriteAlbumList(self, tar=r"./Doc/Album-Jay.md"):
        pass


if __name__ == "__main__":
    ex = Jay_VerOne()