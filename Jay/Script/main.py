#-*- coding:utf-8 -*-

albumlink = "file:D:\Python_M\Code\Jay\Src\Album\虾米音乐 - 发现音乐新世界.html"
songlink = "file:D:\Python_M\Code\Jay\Src\List\虾米音乐 - 发现音乐新世界.html"
debug_c = True
# open html
from urllib.request import urlopen, urlretrieve
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from datetime import datetime
import os.path as ospath
from time import sleep


class JayChou():
    albums = list()
    songs = list()

    def __init__(self):
        cur_tick = datetime.now()
        cur_tick = cur_tick.strftime(format="%Y-%m-%d  %H:%M:%S")
        print("Jay Chou crawler start working at: %s\n" % (cur_tick))
        self.Get_Album()

    def Get_Album(
        self,
        url_album=r"https://www.xiami.com/list?scene=artist&type=album&query={%22artistId%22:%221260%22}"
    ):
        # HTTPError
        try:
            html = urlopen(url_album)
        except HTTPError as httperror:
            print("not get right html page\n", httperror)
            return
        # get nothing of html page
        if html is None:
            print("null html")
            return
        else:
            html_bs = BeautifulSoup(html.read().decode(), features="lxml")
            # print(html_bs)
            albums = html_bs.findAll("div", {"class": "name"})
            for i in albums:
                print(i)

        debug_c = "ths"


if __name__ == "__main__":
    ex = JayChou()
