import requests as r
from lxml import etree
import time
import smtplib
import random


from time import sleep
a = random.uniform(36.3,36.7)
a= str(a)[:4:]
#设填写的体温a是36.3~36.7的随机数

#此处是找到当前时间戳定位url
timetamp = time.mktime(time.localtime())
timetamp = int(timetamp)
#各个链接
url="http://xscfw.hebust.edu.cn/survey/ajaxLogin" #登录链接
url2="http://xscfw.hebust.edu.cn/survey/index"   #获取sid链接
url3=f"http://xscfw.hebust.edu.cn/survey/surveySave?timestamp={timetamp}" #填报体温的地址

        #程序运行失败的报错信息
def tianbao():
    #填报程序
    try:
        timetamp = time.mktime(time.localtime())
        timetamp = int(timetamp)
        rep= r.post(url=url3,params=data,headers=header,cookies=cookies)
        print("填报成功")

    except:
        print("填报出错")

#账号信息
name="张志轩"
xuehao="19L0252071"
param={
    "stuNum": "19L0252071",#学号
    "pwd": "0102022011",#密码
    "vcode": "",
}
#
header={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62"
}


while True:
    #登录程序
    try:
        response=r.post(url=url,params=param,headers=header)
        cookiesJAR = response.cookies#获取cookies
        cookies = cookiesJAR.get_dict()#把cookies写成字典形式
        res = r.get(url=url2,headers=header,cookies=cookies,params=param)
        print("登录成功")
    except:
        print("登录失败")
    #获取完成情况
    try:
        res.encoding = 'uft-8'
        html = etree.HTML(res.text)
        content = html.xpath('/html/body/ul/li[1]/div/span/text()')
    except:
        print("获取失败")
    #获取当前日期要填的文档的sid
    try:
        url4 = 'http://xscfw.hebust.edu.cn/survey/index.action'
        rek =r.get(url=url4,cookies=cookies,headers=header)
        rek.encoding = 'utf-8'
        html3 =etree.HTML(rek.text)
        sid = html3.xpath('/html/body/ul/li[1]/@sid')[0]
        print(f"获取sid成功：{sid}")
    except:
        print("获取sid失败")
    #####获取stuId和qid
    try:
        url5 = f'http://xscfw.hebust.edu.cn/survey/surveyEdit?id={sid}'
        rej = r.get(url=url5,cookies=cookies,headers=header)
        rej.encoding = 'utf-8'
        html2 =etree.HTML(rej.text)
        stuId = html2.xpath('//*[@id="surveyForm"]/input[2]/@value')[0]
        qid = html2.xpath('//*[@id="surveyForm"]/input[3]/@value')[0]
        print(f"获取stuId成功：{stuId}")
        print(f"获取qid成功:{qid}")
    except:
        print("获取stuId qid 失败")
    #####要填写的数据,其中a是36.3~36.7的随机数
    try:
        data={
        "id":sid,
        "stuId":stuId,
        "qid":qid,
        "location":'',
        "c0":"不超过37.3℃，正常",
        "c1":a,
        "c3":"不超过37.3℃，正常",
        "c4":a,
        "c6":"健康",
        }
    except:
        print("获取信息有误")
    #判断程序
    try:
        now_time=time.strftime("%H%M%S",time.localtime())
        now_time = int(now_time)
        if 100000 <= now_time <= 170000:
            print("符合时间要求，开始执行")
            if content[0] == '已完成':
                print('您已填写完毕，不用填写')
                sleep(100)

                break
            if content[0] =='未完成':
                    print('您为填写，为您填写')
                    tianbao()
                    sleep(100)
                    break
        else:
            print("填写时间未到")
            break
    except:
        print("判断失败")
        break
