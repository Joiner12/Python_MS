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


class Html2md():
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

    def donwPics(self):
        htmlobj = BeautifulSoup(self.html.content, features="lxml")
        # article title
        # <h1 class="title-article" id="articleContentId">谷歌浏览器(Chrome)查看http报文headers信息</h1>
        h1 = htmlobj.find(
            "h1", attrs={"class": "title-article", "id": "articleContentId"})
        h1_temp = h1.get_text()
        # 标准命名
        h1_temp = re.sub('[\/:*?<>"|]', '_', h1_temp)
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
        main_article = htmlobj.find(
            "div", attrs={"class": "article_content clearfix", "id": "article_content"})
        imgs = main_article.find_all("img", attrs={"alt": ""})
        if True:
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
        htmlobj = BeautifulSoup(self.html.content, features="lxml")
        main_article = htmlobj.find(
            "div", attrs={"class": "article_content clearfix", "id": "article_content"})
        if False:
            main_article = bytes(main_article.get_text(), "UTF-8")
            main_article = main_article.decode("UTF-8")
            main_article = str(main_article)
        else:
            main_article = str(main_article)
        # print(main_article)
        # save as *.md
        file_md = self.pic_dir+r".md"
        with open(file_md, mode="w", encoding="utf-8") as f:
            f.writelines(main_article)
            a = r"\n\n\n\n"
            f.writelines(a)
        print("write to file:%s succeed.\n" % (file_md))
        main_article = self.main_article
        # main_article.attrs[]

    def parseWeb(self, html=None):
        if html is None:
            return
        cur_html = html
        bs_cur_html = cur_html.content()
        ret_text = str()
        if self.html_bsobj == None:
            print("beautifulsoup object not exists\n")
            return ret_text

        h1 = self.html_bsobj.find_all("h1", attrs={"title-article"})
        main_article = self.html_bsobj.find("div", attrs={"blog-content-box"})
        if not h1 == None:
            pass
            # print(h1,isinstance(h1,list))
        if not main_article == None:
            print(main_article.text())
            return
            main_article = main_article.get_text()
            main_article = bytes(main_article, "UTF-8")
            main_article = main_article.decode("UTF-8")
            print("url parsed succeed\n")
            if True:
                print(main_article)
            ret_text = main_article
            return ret_text

    def parseLocalWeb(self):
        # 解析本地html文件
        abs_imgs_file = list()
        rel_imgs_file = list()
        curUrl = self.baseurl
        if not curUrl.startswith(r"file://") or self.html == None:
            print("not local html cache\n")
            return
        # document path
        curUrl = curUrl.replace(r"file:///", "")
        src_base_dir = os.path.abspath(curUrl)
        src_base_dir = os.path.dirname(src_base_dir)
        if not os.path.exists(src_base_dir):
            print("path not exists\n")
            return
        else:
            os.chdir(src_base_dir)
        # parse web page
        htmlobj = BeautifulSoup(self.html.read(), features="lxml")
        self.html_bsobj = htmlobj
        main_article = htmlobj.find("div", attrs={"blog-content-box"})
        main_article_content = str(main_article)
        with open(r"D:\Python_M\Code\WebPageToMD\md\路径规划_ a star， A星算法详解_DinnerHowe的博客-CSDN博客.md", mode="w", encoding="UTF-8") as f:
            f.writelines(main_article_content)

        return
        imgs = main_article.find_all("img", attrs={"alt": ""})
        for img_i in imgs:
            rel_imgs_file.append(img_i["src"])
            a = os.path.abspath(img_i["src"])
            abs_imgs_file.append(a)
            # print(a)

        # copy & move images
        # D:\Python_M\Code\WebPageToMD\src
        os.chdir(os.path.dirname(__file__))
        # D:\Python_M\Code\WebPageToMD
        tar_base_dir = os.path.abspath(r"../md")

        # D:\Python_M\Code\WebPageToMD\src
        # os.chdir()

    # save as md
    def saveText(self, src, des=r"../md/des.txt"):
        # find image files
        # os.path.exists(des)
        if src == None:
            print('no exist content \n')
            return

        # print(os.path)
        with open(des, mode="w", encoding='utf-8') as f:
            f.write(src)
            print(datetime.now(), '\nwrite src to:%s\n' % (des))


def Copyfile():
    source = 'current/test/test.py'
    target = '/prod/new'

    assert not os.path.isabs(source)
    target = os.path.join(target, os.path.dirname(source))

    # create the folders if not already exists
    os.makedirs(target)

    # adding exception handling
    try:
        shutil.copy(source, target)
    except IOError as e:
        print("Unable to copy file. %s" % e)
    except:
        print("Unexpected error:", sys.exc_info())


def splitUrlName(url):
    if isinstance(url, str):
        return url.split('/')[-1]
    else:
        return datetime.now().strftime("hhmmss")


if __name__ == "__main__":
    # url = r"file:///D:/Python_M/Code/WebPageToMD/pages/%E8%B7%AF%E5%BE%84%E8%A7%84%E5%88%92_%20a%20star%EF%BC%8C%20A%E6%98%9F%E7%AE%97%E6%B3%95%E8%AF%A6%E8%A7%A3_DinnerHowe%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.html"
    # page1 = Html2md(url)
    # srccontent = page1.parseLocalWeb()
    # page1.saveText(srccontent)
    baseurl = r"https://blog.csdn.net/DinnerHowe/article/details/79380317"
    page_md = Html2md(baseurl=baseurl)
    html = page_md.fetchUrl()
    page_md.donwPics()
    page_md.downArticle()
