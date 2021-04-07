# -*- coding:utf-8 -*-
from geopy.distance import geodesic
import pandas as pd
import numpy as np

# 原始文件
OrgPosFile = r"D:\Code\Python\Rsp\result-1.csv"
# RealPosFile = r"D:\Code\Python\Rsp\真实地址.txt"
LocationOutFile = r"D:\Code\Python\Rsp\定位结果.txt"

# 数据
RealPos = np.array([104.058595340000,30.5480360600000])
OrgPos = pd.read_csv(OrgPosFile)
(height, width) = OrgPos.shape
OrgPosLatlon = OrgPos.values
LocationOut = pd.read_csv(LocationOutFile,sep='\t').values

with open(r"D:\Code\Python\Rsp\err.txt",'w') as f:
    for j in OrgPosLatlon:
        cleveland_oh = (30.5480360600000,104.058595340000)
        newport_ri = (j[0],j[1])
        locaTemp = 1000*geodesic(newport_ri, cleveland_oh).miles/0.62137
        dia = locaTemp  - j[2]
        print(dia)
        f.write(str(locaTemp)+"\t"+str(dia)+"\n")
