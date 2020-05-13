#-*- coding:utf-8 -*-
"""
    抓取虾米音乐歌手专辑信息
    2020年5月13日
"""
__author__ = "Risky Junior"

from bs4 import BeautifulSoup
from urllib.request import urlopen, HTTPError
from os.path import join


class XiaMi():
    base_url = r"https://www.xiami.com"
    album_href = list()
    album_base_url = r"https://www.xiami.com"

    def __init__(self):
        self.artistAlbum()
        self.getAlbums(self.album_base_url)

    def artistAlbum(self, artist_num="iim17edb"):
        try:
            # 歌手页面 https://www.xiami.com/artist/iim17edb
            print("try to get info from:\n%s" %
                  (self.base_url + "/artist/" + artist_num))
            html = urlopen(self.base_url + "/artist/" + artist_num)
        except HTTPError as he:
            print("urlopen failed:%s" %
                  (self.base_url + "/artist/" + artist_num))
            return None
        bsObj = BeautifulSoup(html.read(), features="lxml")
        albums = bsObj.find("div", {"class": "related-albums"})

        if albums is None:
            print("Nonetype of albums href")
            return None
        try:
            album_link = albums.find("div", {"class": "blocktitle"}).find("a")
        except:
            print("get href attr failed")
            return None
        self.album_base_url = self.album_base_url + album_link["href"]
        print(self.album_base_url)

    def getAlbums(self, album_url):
        self.album_href = list()
        # 检查专辑页有效性
        if album_url == self.base_url:
            print("所以我今生才会那么努力把最好的给你")
            return None
        try:
            # 歌手页面 https://www.xiami.com/artist/iim17edb
            print("try to get albums from:\n%s" % (album_url))
            html = urlopen(album_url)
        except:
            print("urlopen failed:%s" % (album_url))
            return None

        # 获取专辑链接
        bsObj = BeautifulSoup(html.read(), features="lxml")
        # 遍历所有专辑页面
        # 被反爬虫了
        albums = bsObj.find("ul", {"class": "rc-pagination"}).find("a")
        for album in albums:
            self.album_href.append(self.base_url + album)
            print(self.base_url + album)


if __name__ == "__main__":
    ex = XiaMi()