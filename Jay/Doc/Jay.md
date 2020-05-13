# Scrawler-Jay

<center>
    <img src="D:\Python_M\Code\Jay\Doc\Figure\66531471859003-bad.jpg">
</center>

## 1.Questions

1.1 urllib3 .vs. urllib

1.2 GBK `error`

```python
发生异常: UnicodeDecodeError
'gbk' codec can't decode byte 0x8c in position 593: illegal multibyte sequence
  File "D:\Python_M\Code\Jay\Script\main.py", line 27, in OpenLink
    html = html_f.readlines()
  File "D:\Python_M\Code\Jay\Script\main.py", line 40, in <module>
    OpenLink(r"D:\Python_M\Code\Jay\Src\Album\res.txt")
```

1.3 post 和 get 的差异

1.4 "span" "class"关系

1.5 数据类型分辨

1.6 dict

1.7 “None” vs None

1.8 HTTPError 所有的错误码

1.9 AttributeError 所有的错误码

2.0 差异

```python
from datetime import datetime
import datetime.datetime 
```

2.1 lib-time or lib.datetime

2.2 python struct(结构体)

2.2 路径转换（abusolute to relative）

2.3 脚本文件查看

2.4 多重for使用技巧

```python
for i,j,k in XXX:
  print(i,j,k)
```
2.5 from .vs. import

2.6 判断文件(夹)是否存在



---
---

## 2.笔记

### 2.1 find & findall 

### 函数原型

```python
from bs4 import BeautifulSoup
# find 
find(tag,attributes,recursive,text,keywords)

# findAll
findAll(tag,attributes,recursive,limit,keywords)

# tag：由一个或多个标签组成的序列
find({'h1','h2','h3'})

# attributes:python字典封装一个标签的若干属性对应的属性值
findAll("span",{"class":{"red","green"}})

# recursive:定义查找标签的深度，False只查找一级标签，True查找所有的标签
findAll("span",{"class","red"},True)

# text:用标签的文本内容去匹配标签，而不是标签的属性
bsObj.findAll(text="the price")

# limit:只适用于findAll,find等价于limit=1。限制搜索的标签结果总数

# keywords:选择具有指定属性的标签
# 通过tag属性进行标签选择，其实是“或”关系，通过keyword可以增加一个”与“
# 关系。
bsObj.findAll(id="text")

```

---

### 2.2 BeautifulSoup对象

```python
from bs4 import BeautifulSoup

# BeautifulSoup对象
bsObj = BeautifulSoup(html.read())
# 标签Tag对象
tagObj =  bsObj.findAll("span",{"class":"green"})
tagHObj = bsObj.div.h1
# NavigableString对象
print(标签内部的文字)
# Comment对象
print(“查找HTML注释”)

```

---

### 2.3 导航树（Navigating Tree）
#### 2.3.1 导航树
findAll通过标签属性和标签名字查找标签。通过标签在文档中的位置查找标签的方法需要用到导航树。
整个HTML网页可以映射成一颗树。$ ^{[3]} $

#### 2.3.2 子标签（Children）和后代标签(desendants)
子标签是指父代标签的下一级，后代标签是指一个父标签下所有的标签。

#### 2.3.3 兄弟标签（siblings）
BeautifulSoup兄弟标签用于处理表格。
```python
# next_siblings()
from bs4 import BeautifulSoup

```

#### 2.3.4 查找父级标签(parent)

---


### 2.4 绝对路径or相对路径
```python
#1.绝对路径转相对路径
#是根据当前路径的相对路径
print os.path.relpath("d:/MyProj/MyFile.txt")
#..\MyProj\MyFile.txt

# 2.相对路径转绝对路径
# 注意用os.chdir(dir)改变当前比较路径
path = "..\MyProj\MyFile.txt"
print os.path.abspath(path)
#D:\MyProj\MyFile.txt
```



## Reference:

[1] Python urllib、urllib2、urllib3用法及区别  https://www.cnblogs.com/onefine/p/10499342.html

[2] 使用dict 和set  https://www.liaoxuefeng.com/wiki/1016959663602400/1017104324028448

[3] 绝对|相对路径转换 https://www.cnblogs.com/hont/p/5412432.html