#-*- coding:utf-8 -*-
"""
    2020年5月12日
"""
print("this is a draft")

#%%
import os
filepath = r"D:\Codes\Python_MS\Jay\Src\Albums-2"
filepath = r"D:\Codes\Python_MS\Jay\Script"

if False:
    for root, dirs, files in os.walk(filepath, True):
        if not len(dirs) == 0:
            for file_1 in files:
                print(os.path.join(root, file_1))
        else:
            for file_1 in files:
                print(os.path.join(root,file_1))

if "Codes" in filepath:
    print("in")
    
    
    
#%%
from os import walk
filepath = r"D:\Codes\Python_MS\Jay\Script"
walk(filepath)