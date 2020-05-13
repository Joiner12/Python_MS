#-*- coding:utf-8 -*-
"""
    Jay:
    albums & songs
    从本地html文件提取信息
"""

from datetime import datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen
from os import walk, chdir
from os.path import abspath, join
from time import sleep


class Jay_VerOne():
    fontpage_link = r"file:D:\Codes\Python_MS\Jay\Src\Albums-2\FrontPage\周杰伦 - 虾米音乐.html"
    html_link = r"file:D:\Codes\Python_MS\Jay\Src\Albums-2\Initial J\周杰伦 - 虾米音乐.html"
    rootpath = r"D:\Codes\Python_MS\Jay\Src\Albums-2"
    tar = r"D:\Codes\Python_MS\Jay\Doc\Album-Jay.md"

    def __init__(self):
        timeStand = datetime.now()
        timeStand = timeStand.strftime("%Y-%m-%d %H:%M:%S")
        # htmls
        file_html = list()

        print("Jay Chou Scrawler start at:%s" % (timeStand))
        for i in range(5):
            print(".")

        # depart line
        self.__initmdfile__()
        self.__searchhtml__()
        for html_i in self.file_html:
            html_i = "file:" + html_i
            print(html_i)
            self.GetInfoFromLocalFile(
                html_i, r"D:\Codes\Python_MS\Jay\Src\Albums-2\Initial J")

    """
        初始化tar = r"D:\Codes\Python_MS\Jay\Doc\Album-Jay.md"
    """

    def __initmdfile__(self):
        with open(self.tar, mode="w", encoding='utf-8') as mdf:
            mdf.write("# Jay Chou \n")
            if not mdf.closed:
                mdf.close()

    # *.html
    def __searchhtml__(self, rootpath=r"D:\Codes\Python_MS\Jay\Src\Albums-2"):
        self.file_html = list()
        for root, dirs, files in walk(rootpath, True):
            if not len(dirs) == 0:
                for file_1 in files:
                    file_name = join(root, file_1)
                    if r"周杰伦 - 虾米音乐.html" in file_name:
                        self.file_html.append(file_name)
                        # print(file_name)
            else:
                for file_1 in files:
                    file_name = join(root, file_1)
                    if r"周杰伦 - 虾米音乐.html" in file_name:
                        self.file_html.append(file_name)
                        # print(file_name)

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

    def GetInfoFromLocalFile(self, html_link, html_path):
        retdict = dict()
        print("get album info from local html files")
        htmllink = html_link
        html = urlopen(html_link)
        if html is None:
            print("warning:null web page")
            return
        bsObj = BeautifulSoup(html.read(), features='lxml')

        albummaini = bsObj.find("div", {"data-spm": "albummaini"})
        # album
        if not albummaini is None:
            with open(self.tar, mode="a+", encoding='utf-8') as mdf:
                album_name = albummaini.find("div",
                                             {"class": "titleInfo-name"})
                album_name = album_name.get_text()
                mdf.write("## " + album_name + "\n")
                # singer
                singer_name = albummaini.find("div", {"class": "singer-name"})
                singer_name = singer_name.get_text()

                # pulish date
                publish_date = albummaini.find("div", {
                    "style":
                    "color: gray; font-weight: 300; margin-top: 10px;"
                })
                publish_date = publish_date.get_text()
                mdf.write(singer_name + ":" + publish_date + "\n")
                # cover
                chdir(r"C:\Users\10520\Desktop\FrontPage")
                album_cover = bsObj.find("div", {
                    "class": "cover"
                }).find("img")["src"]
                #<img src="D:\Python_M\Code\Jay\Doc\Figure\66531471859003-bad.jpg">
                mdf.write('<img src="' + abspath(album_cover) + '">' + "\n")
                # songs
                song_detail = list()
                songs = bsObj.findAll("div", {"class": "song-name em"})
                for song in songs:
                    song_detail.append(song.get_text())
                    mdf.write(song.get_text() + "\n")

                print(album_name, singer_name, publish_date, song_detail,
                      abspath(album_cover))

            if not mdf.closed:
                mdf.close()

    """
        遍历文件html并列出歌单
    """

    def WriteAlbumList(self, tar=r"D:\Codes\Python_MS\Jay\Doc\Album-Jay.md"):
        pass


if __name__ == "__main__":
    ex = Jay_VerOne()