#-*- coding:utf-8 -*-
"""
    Jay:
    albums & songs
"""

from datetime import datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os.path as ospath


class Jay_VerOne():
    fontpage_link = r"file:D:\Python_M\Code\Jay\Src\Albums-2\FrontPage\周杰伦 - 虾米音乐.html"
    html_link = r"file:D:\Python_M\Code\Jay\Src\Albums-2\Initial J\周杰伦 - 虾米音乐.html"
    rootpath = r"D:\Python_M\Code\Jay\Src\Albums-2"

    def __init__(self):
        timeStand = datetime.now()
        timeStand = timeStand.strftime("%Y-%m-%d %H:%M:%S")
        print("Jay Chou Scrawler start at:%s"%(timeStand))
        # self.GetInfoFromLocalFile(self.html_link)


    # *.html
    def __searchhtml__(self,rootpath=r"D:\Python_M\Code\Jay\Src\Albums-2"):
        

    # 找出front page中的专辑列表图片|链接|名字
    # info：专辑信息 wrapper：专辑封面
    def FrontPage(self):
        html_fp = urlopen(self.fontpage_link)
        if html_fp is None:
            print("get null page code")
            return 
        bsObj = BeautifulSoup(html_fp.read(),features="lxml")
        temp_bs = bsObj.findAll("div",{"class":"info"})

        for album_i in temp_bs:
            print(album_i)
            # print(album_i.find("div",{"cover":"img"}))
        if True and False:
            artist_view = bsObj.findAll("div",{"class":"wrapper"})
            debug_a = artist_view

        
    '''
        从本地HTML文件中提取信息
    '''
    def GetInfoFromLocalFile(self,html_link,html_path):
        retdict = dict()
        print("get album info from local html files")
        htmllink = html_link
        html = urlopen(html_link)
        if html is None:
            print("warning:null web page")
            return
        bsObj = BeautifulSoup(html.read(),features='lxml')
        
        albummaini = bsObj.find("div",{"data-spm":"albummaini"})    
        # album
        album_name = albummaini.find("div",{"class":"titleInfo-name"})
        album_name = album_name.get_text()
        # singer
        singer_name = albummaini.find("div",{"class":"singer-name"})
        singer_name = singer_name.get_text()
        # pulish date
        publish_date = albummaini.find("div",{"style":"color: gray; font-weight: 300; margin-top: 10px;"})
        publish_date = publish_date.get_text()
        # cover
        album_cover = bsObj.find("div",{"class":"cover"}).find("img")["src"]
        # songs
        song_detail = list()
        songs = bsObj.findAll("div",{"class":"song-name em"})
        for song in songs:
            song_detail.append(song.get_text())
        os.chdir(html_path)
        print(ospath.abspath(album_cover))
        # print(album_name,singer_name,publish_date,song_detail)
        debug_a = 0

if __name__ == "__main__":
    ex = Jay_VerOne()