#coding=utf-8
import requests
#变量
text=""
n='   <br>    '
r=requests.get('http://api.rosysun.cn/zhihu/')
print("是否成功：",r.status_code)
a=r.json()
for key,values in  a.items():
    for i in range(len(values)):
        date=values[i]
        for key, values2 in date.items():

            text=text+values2+n
file=open("mydata.html",'w+')
file.write(text)
