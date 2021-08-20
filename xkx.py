# coding=utf-8
import requests as r
from lxml import etree
import time
from time import sleep

a, b, c, d, e, f, z = '', '', '', '', '', '', ''
timetamp = time.mktime(time.localtime())
timetamp = int(timetamp)

url = "http://xscfw.hebust.edu.cn/survey/ajaxLogin"
url2 = "http://xscfw.hebust.edu.cn/survey/index"
url3 = f"http://xscfw.hebust.edu.cn/survey/surveySave?timestamp={timetamp}"


def tianbao():
    try:
        timetamp = time.mktime(time.localtime())
        timetamp = int(timetamp)
        rep = r.post(url=url3, params=data, headers=header, cookies=cookies)
        a = "填报成功"
        
        return a
    except:
        a = "填报出错"
        
        return a


# 账号信息
param = {
    "stuNum": "19L0252068",
    "pwd": "9905036512",
    "vcode": "",
}
#
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62"
}

while True:
    # 登录程序
    try:
        response = r.post(url=url, params=param, headers=header)
        sleep(10)
        cookiesJAR = response.cookies  # 获取cookies
        cookies = cookiesJAR.get_dict()  # 把cookies写成字典形式
        res = r.get(url=url2, headers=header, cookies=cookies, params=param)
        b = "登录成功"
       
    except:
        b = "登录失败"
        
        sleep(5)
        break
    # 获取完成情况
    try:
        res.encoding = 'uft-8'
        html = etree.HTML(res.text)
        content = html.xpath('/html/body/ul/li[1]/div/span/text()')
        c = "获取填报表单成功"
       
    except:
        c = "获取填报表单失败"
        
        sleep(5)
        break
    # 获取当前日期要填的文档的sid
    try:
        url4 = 'http://xscfw.hebust.edu.cn/survey/index.action'
        rek = r.get(url=url4, cookies=cookies, headers=header)
        rek.encoding = 'utf-8'
        html3 = etree.HTML(rek.text)
        sid = html3.xpath('/html/body/ul/li[1]/@sid')[0]
        d = "获取当前日期要填的文档的sid成功"
        
    except:
        d = "获取当前日期要填的文档的sid失败"
        
        
        break
    #####获取stuId和qid
    try:
        url5 = f'http://xscfw.hebust.edu.cn/survey/surveyEdit?id={sid}'
        rej = r.get(url=url5, cookies=cookies, headers=header)
        sleep(5)
        rej.encoding = 'utf-8'
        html2 = etree.HTML(rej.text)
        stuId = html2.xpath('//*[@id="surveyForm"]/input[2]/@value')[0]
        qid = html2.xpath('//*[@id="surveyForm"]/input[3]/@value')[0]
        e = "获取stuId qid 成功"
        
    except:
        e = "获取stuId qid 失败"
        
        
        break
    try:
        data = {
            "id": sid,
            "stuId": stuId,
            "qid": qid,
            "location": '',
            "c0": "不超过37.3℃，正常",
            "c1": '36.5',
            "c3": "不超过37.3℃，正常",
            "c4": '36.5',
            "c6": "健康",
        }
        f = "获取信息成功"
        
        break
    except:
        f = "获取信息有误"
        
        break
if content[0] == '已完成':
    z = '无需填报'
   

if content[0] == '未完成':
    tianbao()
    z = "本次填报成功"
    

else:
    z = "填写时间未到,或填写失败，请稍后重试"
   

file = open("xkx.html", 'w+', encoding='UTF-8')
file.write(b + '*****' + c + '*****' + d + '*****' + e + '*****' + f + '*****' + z + '*****' + a)
file.close()
