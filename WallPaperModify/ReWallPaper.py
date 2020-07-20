# -*- coding:utf-8 -*-


__author__ = "Risky Junior"
__date__ = "2020-5-22"

from os import path, listdir, walk, rename, sep, system


class RegularWallPaper():
    img_Format = ['.jpg', '.jpeg', '.bmp', '.png']
    img_files = list()
    img_fullfile = list()
    re_flag = dict()
    img_name = list()

    def __init__(self, filepath=r"D:\壁纸"):
        self.filepath = filepath
        self.img_files = list()
        self.img_fullfile = list()
        self.re_flag = dict()
        self.img_name = list()

        if path.isdir(filepath):
            print("input dir exists")
        else:
            print("input file path:%s is not exist,check it\n" % (filepath))
            return None
        self.GetImagePath()
        self.CheckFileName()
        self.StandardRe()

    def GetImagePath(self):
        for root, dir, files in walk(self.filepath):
            for j in files:
                if path.splitext(j)[1] in self.img_Format:
                    self.img_name.append(path.splitext(j)[0])
                    self.img_files.append(j)
                    self.img_fullfile.append(path.join(root, j))

    def CheckFileName(self, standardPrefix="WallPaper_"):
        max_val = 0
        renameFlag = False
        if len(self.img_files) == 0:
            return
        for img in self.img_files:
            # postfix
            file_name = path.splitext(img)[0]
            if standardPrefix in file_name:
                temp = file_name.split('WallPaper_')
                temp = int(temp[1])
                if temp > max_val:
                    max_val = temp
            else:
                renameFlag = True
        if (not renameFlag) and (max_val != len(self.img_files) - 1):
            renameFlag = True
            self.re_flag["reFlag"] = True
            self.re_flag["reType"] = "type1:max serial error"
        elif renameFlag:
            self.re_flag["reFlag"] = True
            self.re_flag["reType"] = "type2:not standard error"
        else:
            self.re_flag["reFlag"] = False
            self.re_flag["reType"] = ""

    def StandardRe(self, standardPrefix="WallPaper_"):
        if not self.re_flag["reFlag"]:
            print("All files standards")
            return
        else:
            print(self.re_flag["reType"])
        reneed_name = list()
        # & 操作
        standardName = [standardPrefix + str(i)
                        for i in range(len(self.img_name))]
        for name_i in self.img_name:
            if not name_i in standardName:
                reneed_name.append(
                    self.img_fullfile[self.img_name.index(name_i)])
            else:
                standardName.remove(name_i)

        cnt_i = 0
        for name_j in reneed_name:
            try:
                pre_fullname = name_j
                cur_full_path = str()
                for j in name_j.split(sep)[:-1]:
                    cur_full_path += (j + "\\")
                new_fullname = cur_full_path + \
                    standardName[cnt_i] + \
                    path.splitext(name_j.split(sep)[-1])[-1]
                cnt_i += 1
                rename(pre_fullname, new_fullname)
                print("rename:%s\t → %s\n" % (pre_fullname, new_fullname))
            except:
                pass


if __name__ == "__main__":
    handle_choice = input("Get Windows Focus On|Rename WallPaper:[0]|[1]: ")
    if handle_choice == "0":
        print(handle_choice)
        system(r"D:\壁纸\GETwindowfocus.bat")
    else:
        print("Start to Rename Target WallPaper img files")
        ex = RegularWallPaper()
