#-*- coding:utf-8 -*-
from CSDN2MD import HTML2MD_LOCAL

def ParseAlg():
    url = r"file:///D:/Python_M/Code/WebPageToMD/pages/Dijsktra's%20algorithm.html"
    src_path = r"D:\Python_M\Code\WebPageToMD\pages\Dijsktra's algorithm_files"
    page1 = HTML2MD_LOCAL(url)
    srccontent = page1.parseLocalWeb(src_path=src_path)


if __name__ == "__main__":
    ParseAlg()