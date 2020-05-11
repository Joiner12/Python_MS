#-*- coding:utf-8 -*-

albumlink = "file:D:\Python_M\Code\Jay\Src\Album\虾米音乐 - 发现音乐新世界.html"
songlink = "file:D:\Python_M\Code\Jay\Src\List\虾米音乐 - 发现音乐新世界.html"
debug_c = True
# open html
from urllib.request import urlopen,urlretrieve
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
        print("Jay Chou crawler start working at: %s\n"%(cur_tick))
        self.Get_Album(albumlink)

    def Get_Album(self,url_album="http://google.com"):
        # HTTPError
        try:
            html = urlopen(url_album)
        except HTTPError as httperror:
            print("not get right html page\n",httperror)
            return
        # get nothing of html page
        if html is None:
            print("null html")
            return
        else:
            html_bs = BeautifulSoup(html.read().decode(),features="lxml")
            # print(html_bs)
            albums = html_bs.findAll("div",{"class":{"name","image"}})
            for i in albums:
                # sleep(3)
                try:
                    i_temp = i.find("img")["src"]
                    urlretrieve(i_temp,r"D:\Python_M\Code\Jay\Script\log.jpg")
                    print(i_temp)
                except:
                    pass
                else:
                    pass
                
                # print(type(i_temp))
            """
            covers = html_bs.find_all("div",{"class":"image"})
            if len(albums) > 0 and len(covers) > 0:
                for album,cover in zip(albums,covers):
                    print("%s\n%s\n"%(album,cover))
            """
        
        debug_c = "ths"



if __name__ == "__main__":
    ex = JayChou()
    

