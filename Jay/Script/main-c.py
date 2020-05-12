#-*- coding:utf-8 -*-

# open html
from urllib.request import urlopen,urlretrieve
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from datetime import datetime
import os.path as ospath
from time import sleep


albumlink = "file:D:\Python_M\Code\Jay\Src\Album\虾米音乐 - 发现音乐新世界.html"
# album 
albumlink_1 = "file:D:\Python_M\Code\Jay\Src\Album-1\专辑列表 - 周杰伦 - 虾米音乐.html"
# album detail
songlink = "file:D:\Python_M\Code\Jay\Src\List\虾米音乐 - 发现音乐新世界.html"
# entry link
entry_jay = "file:D:\Python_M\Code\Jay\Src\Entry-Jay\周杰伦 - 虾米音乐.html"

# example link 
ex_link = "file:D:\Python_M\Code\Jay\Script\example.html"
debug_c = True

class JayChou():
    albums = list()
    songs = list()
    def __init__(self):
        cur_tick = datetime.now()
        cur_tick = cur_tick.strftime(format="%Y-%m-%d  %H:%M:%S")
        print("Jay Chou crawler start working at: %s\n"%(cur_tick))
        self.Get_Album(ex_link)

    def Get_Album(self,url_album):
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
            print(html_bs)
            
            '''
            # 通过属性查找标签
            <span class="green"></span>
            class(id):属性  <span>:标签
            
            ''' 
            albums = html_bs.findAll(class_ = "count")
            for i in albums:
                print(i)
            
        debug_c = "ths"

    # 创建保存文件
    def __NewMdfile__(self,file_name = "..//Jay-out.md"):
        with open(file_name,mode='w',encoding="utf-8") as mdf:
            statement = "# Jay Chou"
            mdf.write(statement+"\n")

            if not mdf.closed:
                mdf.close()
    # hotlinking
    

if __name__ == "__main__":
    ex = JayChou()
    

