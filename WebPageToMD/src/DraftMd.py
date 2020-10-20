# -*- coding:utf-8 -*-
import os


def splitRelpath(cur_path):
    cu = cur_path.split('/')


def getPageAbsPath(baseurl):
    cur_url = baseurl
    if cur_url.startswith(r"file:///"):
        path_temp = cur_url.replace(r"file:///", "")
        path_temp = path_temp.split("/")
        page_abs_path = str()
        for i in path_temp:
            page_abs_path = os.path.join(page_abs_path, i)


if __name__ == "__main__":
    url = r"file:///D:/Python_M/Code/WebPageToMD/pages/%E8%B7%AF%E5%BE%84%E8%A7%84%E5%88%92_%20a%20star%EF%BC%8C%20A%E6%98%9F%E7%AE%97%E6%B3%95%E8%AF%A6%E8%A7%A3_DinnerHowe%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.html"
    getPageAbsPath(url)
