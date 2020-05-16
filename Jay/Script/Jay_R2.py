#-*- coding:utf-8 -*-
"""
    抓取虾米音乐歌手专辑信息
    2020年5月13日
"""
__author__ = "Risky Junior"

from bs4 import BeautifulSoup
from urllib.request import urlopen, HTTPError
from os.path import join
from random import choice
import requests

# 客户端
user_agent = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Openwave/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
    # iPhone 6：
    "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",
]


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


"""
    1.cookie处理
    2.header处理
    3.ip地址处理
"""


class XiaMi_v2():
    base_url = r"https://www.xiami.com"
    album_href = list()

    # header 测试
    def __init__(self):
        self.headers = {
            "User-Agent":
            choice(user_agent),
            "accept":
            'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'cookie':
            'cookie: _xm_umtoken=TD2FCBDC5430262D1BF7ACFFE3F79431E436049955DC629BF5B0FD8847A; _xm_ncoToken_login=web_login_1589615117101_0.5026784781247458; xmgid=14b38c97-72ec-4a2e-8b7d-7b8fe396c371; cna=cM3UFn3fh3wCAW+6NvHWumkZ; gid=158920635881939; _xiamitoken=a8a4c0334cc9e197ecda7c13eba43aa6; _unsign_token=8e823efe831145edfee85e850055db06; xm_sg_tk=4c269cfdea6736a544bb356aab194d47_1589615091499; xm_sg_tk.sig=D8mwauSl4YFN82rbaWz8Nzgu3MGXyXO5Q3SBO6DP8Q4; xm_token=c68ea0edaca476ff236c8d6698cb59317gu33a; uidXM=338819591; member_auth=2TDNGtlI4j06x9bsJ%2FN5AFof%2BpqzfHHmgIkyzd1pz1lbbvhRFcGe2%2BnAJ2MTpUiT1z9qGYSf3jNGHudYItiZq%2FDIRArEHSI; EGG_SESS=L7PgHwg2HZS1Elhrfyvmigpf7vQa7RKWSHpGgXJuT8br1pe3bUELgUVVU2tUEkA2rlJuzkVnOyEOdz0S_iLmUHs1AbguBucy1KAE2jSUVxX9VG0bBniOorIZa1cl4cq7; xm_traceid=0b0fe03b15896151501573436e5168; xm_oauth_state=005fbbc900cc6317b39ced98c4df74aa; _xm_umtoken=T52738671330F07AA4DC43AB0B8F5A347259BC65AB56A8387032FA2B039; l=eBx7wCZVQ3EYV_KCKO5wlurza7793IOf11PzaNbMiIHca175nF6CBNQc-0_vqdtjgtfbPp-zEdARfdhw82a38KwYW5Fi-Y7VgDv9-; isg=BP7-GuHyLBYeTXg10qIistwzTxRAP8K5fo_FG6gGecE8S50lM87nyH8pxxeH9LrR; _xm_cf_=xA9PzJwTkeAFyLB-u8eYegu-',
            'referer':
            "https://passport.xiami.com/?redirectURL=https%3A%2F%2Fwww.xiami.com%2Fartist%2Fiim17edb&uuid=e5984c1f36149cf6127df0b65fad34a1"
        }
        r = requests.get(self.base_url, headers=self.headers, timeout=5)
        print("try base url,status code:%s" % (r.status_code))

        # 获取专辑
        self.album_href = list()
        self.artistAlbum()

    def artistAlbum(self, artist_num="iim17edb"):
        try:
            # 歌手页面 https://www.xiami.com/artist/iim17edb
            print("try to get info from:\n%s" %
                  (self.base_url + "/artist/" + artist_num))
            cur_url = self.base_url + "/artist/" + artist_num
            r = requests.get(cur_url, headers=self.headers, timeout=5)
            print("status code:%s" % (r.status_code))
        except:
            print("urlopen failed:%s" %
                  (self.base_url + "/artist/" + artist_num))
            return None
        try:
            bsObj = BeautifulSoup(r.text, features="lxml")
            print(bsObj)
        except:
            print("get failed")
            return None
        # 获取专辑列表
        albums = bsObj.find("div", {"id": "app"})

        if albums is None:
            print("None type of albums href")
            return None
        try:
            album_link = albums.find("div", {"class": "blocktitle"}).find("a")
        except:
            print("get href attr failed")
            return None
        self.album_base_url = self.album_base_url + album_link["href"]
        print(self.album_base_url)


if __name__ == "__main__":
    ex = XiaMi_v2()