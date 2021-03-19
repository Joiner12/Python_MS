#-*- coding:utf-8 -*-
import numpy as np

a1= np.array([0,0,5,5])
a2= np.array([2,2,3,3])
print (a1.var() , a2.var()) # 6.25 0.25
print (a1.std() ,a2.std()) # 2.5 0.5
print (a1.var(ddof=1) , a2.var(ddof=1)) #ddof = 1代表样本的方差和标准差
print (a1.std(ddof=1) ,a2.std(ddof=1))   