#coding=utf-8
import requests
text=""
n='   <br>    '
r=requests.get('http://api.rosysun.cn/zhihu/')
a=r.json()
for key,values in  a.items():
    for i in range(len(values)):
        date=values[i]
        for key, values2 in date.items():
            text=text+values2+n
file=open("mydata.html",'w+')
file.write(text)
file.close()
