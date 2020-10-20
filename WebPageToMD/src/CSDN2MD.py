# -*- coding:utf-8 -*-
"""
    step1:parse web
    step2:save imgs
    step3:save to markdown
    key:*path*
"""

# web save to markdown
import urllib
import sys
import os
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import shutil
import re

# 获取文件名字
"""
    e.g:src="https://csdnimg.cn/release/blogv2/dist/pc/img/reprint.png"
    → reprint.png
"""


def splitUrlName(url, spliter="/"):
    if isinstance(url, str):
        return url.split(spliter)[-1]
    else:
        return datetime.now().strftime("hhmmss")

# 规范Windows文件夹命名


def StanderdWinName(name):
    if isinstance(name, str):
        name = re.sub('[\/:*?<>"|]', '_', name)
    else:
        name = datetime.now().strftime(format="hhmmss")
    return name


class HTML2MD():
    # 初始化文件路径
    def __init__(self, baseurl="", md_dir="./md"):
        os.chdir(os.path.dirname(__file__))
        base_dir = os.path.abspath(r"../")
        self.base_dir = base_dir  # ~ abs_path
        md_dir = os.path.join(base_dir, "md")

        self.md_dir = md_dir
        if not os.path.exists(md_dir):
            os.mkdir(md_dir)
        else:
            print("doc exists\n")

        curUrl = urllib.parse.unquote(baseurl, "UTF-8")
        self.baseurl = curUrl

    # 网站检测
    def fetchUrl(self):
        cururl = self.baseurl
        if cururl == None:
            return
        print("start with:%s" % (cururl))
        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
        try:
            html = requests.get(cururl, headers=headers)
        except urllib.request.HTTPError as e:
            print(e)

        if not html is None:
            print("web get succeed\n")
        self.html = html
        return html

    def donwPics(self, downloadpic=False):
        bsobj = BeautifulSoup(self.html.content, features="lxml")
        # article title
        # <h1 class="title-article" id="articleContentId">谷歌浏览器(Chrome)查看http报文headers信息</h1>
        h1 = bsobj.find(
            "h1", attrs={"class": "title-article", "id": "articleContentId"})
        h1_temp = h1.get_text()
        # 标准命名
        h1_temp = StanderdWinName(h1_temp)
        print(h1_temp)

        # 新建文件夹保存图片
        pic_dir = os.path.join(self.md_dir, h1_temp)

        if not os.path.exists(pic_dir):
            try:
                os.mkdir(pic_dir)
            except:
                temp_name = datetime.now().strftime(format="hhmmss")
                pic_dir = os.path.join(self.md_dir, temp_name)
                os.mkdir(pic_dir)
            print("mkdir %s" % (pic_dir))

        # class="article_content clearfix" id="article_content"
        main_article = bsobj.find(
            "div", attrs={"class": "article_content clearfix", "id": "article_content"})
        imgs = main_article.find_all("img", attrs={"alt": ""})
        if downloadpic:
            for img_i in imgs:
                pic_url = img_i["src"]
                pic_name = splitUrlName(pic_url)
                # urllib.request.urlretrieve(
                #     pic_url, os.path.join(pic_dir, pic_name))
                print("save from:%s,to%s\n" %
                      (img_i["src"], os.path.join(pic_dir, pic_name)))
        print("download pictures finished..\n")

        self.main_article = main_article
        self.pic_dir = pic_dir

    # 下载文章保存为md文件
    def downArticle(self):
        bsobj = BeautifulSoup(self.html.content, features="lxml")
        main_article = bsobj.find(
            "div", attrs={"class": "article_content clearfix", "id": "article_content"})
        if False:
            main_article = bytes(main_article.get_text(), "UTF-8")
            main_article = main_article.decode("UTF-8")
            main_article = str(main_article)
        else:
            main_article = str(main_article)
        # save as *.md
        file_md = self.pic_dir+r".md"
        article_title = bsobj.find("div", attrs={"class": "article-title-box"})
        with open(file_md, mode="w", encoding="utf-8") as f:
            f.writelines(str(article_title))

        with open(file_md, mode="a", encoding="utf-8") as f:
            f.writelines(main_article)
        print("write to file:%s succeed.\n" % (file_md))


"""
    解析本地html文件
"""


class HTML2MD_LOCAL():
    # 初始化文件路径
    def __init__(self, baseurl=""):
        os.chdir(os.path.dirname(__file__))
        base_dir = os.path.abspath(r"../")  # Code\WebPageToMD
        self.base_dir = base_dir  # ~ abs_path
        md_dir = os.path.join(base_dir, "md")

        self.md_dir = md_dir
        self.mkdir_p(md_dir)

        cururl = urllib.parse.unquote(baseurl, "UTF-8")
        self.baseurl = cururl
        self.websrc = "CSDN-1"

    def parseLocalWeb(self, src_path=r"D:\Python_M\Code\WebPageToMD\pages\路径规划_ a star， A星算法详解_DinnerHowe的博客-CSDN博客_files"):
        # 解析本地html文件
        cururl = self.baseurl
        if not cururl.startswith(r"file://"):
            print("not local html cache\n")
            return

        websrc = self.websrc
        html = urllib.request.urlopen(cururl)
        bsobj = BeautifulSoup(html.read(), features="lxml")
        # h1
        # <h1 class="title-article" id="articleContentId">谷歌浏览器(Chrome)查看http报文headers信息</h1>
        if websrc == "CSDN":
            h1 = bsobj.find(
                "h1", attrs={"class": "title-article", "id": "articleContentId"}).get_text()
        # <h1 class="entry-title"
        else:
            h1 = bsobj.find("h1", attrs={"class": "entry-title"}).get_text()
        # create dirctory for pics
        h1 = StanderdWinName(h1)
        cur_pic_dir = os.path.join(
            self.md_dir, splitUrlName(src_path, spliter='\\'))
        self.mkdir_p(cur_pic_dir)

        # down pictures
        if websrc == "CSDN":
            main_article = bsobj.find(
                "div", attrs={"class": "article_content clearfix", "id": "article_content"})
            imgs = main_article.find_all("img", attrs={"alt": ""})
        else:
            main_article = bsobj.find(
                "div", attrs={"class": "entry-content"})
            imgs = main_article.find_all("img")

        page_path = self.getPageAbsPath()
        for img_i in imgs:
            a = img_i["src"]
            src_img = os.path.join(src_path, splitUrlName(a))
            shutil.copy(src_img, cur_pic_dir)
            print("copy:%s\bto\b%s\n" % (src_img, cur_pic_dir))

        main_article_content = str(main_article)
        file_md = os.path.join(self.md_dir, h1+r".md")
        # file_md = cur_pic_dir + r".md"
        # article-title-box
        article_title = bsobj.find("div", attrs={"class": "article-title-box"})
        with open(file_md, mode="w", encoding="utf-8") as f:
            f.writelines(str(article_title))
        # article
        with open(file_md, mode="a", encoding="utf-8") as f:
            f.writelines(main_article_content)

    # 文件夹建立
    def mkdir_p(self, dir_name):
        if os.path.exists(dir_name):
            print("%s,\b already exists\n" % (dir_name))
        else:
            try:
                os.mkdir(dir_name)
                print("mkdir directory:%s\n" % (dir_name))
            except:
                print("directory creates failed\n")

    def getPageAbsPath(self):
        cur_url = self.baseurl
        page_abs_path = str()
        if cur_url.startswith(r"file:///"):
            path_temp = cur_url.replace(r"file:///", "")
            path_temp = path_temp.split("/")
            for i in path_temp:
                if i.endswith(".html"):
                    i = i.replace(".html", "")
                page_abs_path = os.path.join(page_abs_path, i)
        self.page_path = page_abs_path
        return page_abs_path


if __name__ == "__main__":
    if False:
        baseurl = r"https://blog.csdn.net/DinnerHowe/article/details/79380317"
        page_md = HTML2MD(baseurl=baseurl)
        html = page_md.fetchUrl()
        page_md.donwPics()
        page_md.downArticle()
    else:
        url = r"file:///D:/Python_M/Code/WebPageToMD/pages/%E8%B7%AF%E5%BE%84%E8%A7%84%E5%88%92_%20a%20star%EF%BC%8C%20A%E6%98%9F%E7%AE%97%E6%B3%95%E8%AF%A6%E8%A7%A3_DinnerHowe%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.html"
        page1 = HTML2MD_LOCAL(url)
        local_pagesrc = r"D:\Python_M\Code\WebPageToMD\pages\路径规划_ a star， A星算法详解_DinnerHowe的博客-CSDN博客_files"
        srccontent = page1.parseLocalWeb(src_path=local_pagesrc)
