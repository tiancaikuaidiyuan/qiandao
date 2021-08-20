# coding=utf-8
import requests as r
from lxml import etree
import time
from time import sleep

a, b, c, d, e, f, z = '', '', '', '', '', '', ''
timetamp = time.mktime(time.localtime())
timetamp = int(timetamp)
y=''
url = "http://xscfw.hebust.edu.cn/survey/ajaxLogin"
url2 = "http://xscfw.hebust.edu.cn/survey/index"
url3 = f"http://xscfw.hebust.edu.cn/survey/surveySave?timestamp={timetamp}"


# 账号信息
param = {
    "stuNum": "19L0252071",
    "pwd": "0102022011",
    "vcode": "",
}
#
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62"
}


try:
    response = r.post(url=url, params=param, headers=header)
    sleep(20)
    cookiesJAR = response.cookies  # 获取cookies
    cookies = cookiesJAR.get_dict()  # 把cookies写成字典形式
    res = r.get(url=url2, headers=header, cookies=cookies, params=param)
    b = "正在登录，即学校网页可以正常进入"

except:
    b = "登录失败，即学校网页无法进入"



# 获取完成情况
try:
    res.encoding = 'uft-8'
    html = etree.HTML(res.text)
    content = html.xpath('/html/body/ul/li[1]/div/span/text()')
    y=content[0]
    c = "获取填报表单成功，即登录成功"

except:
    c = "获取填报表单失败，即登录失败"



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


except:
    f = "获取信息有误"


if y == '已完成':
    z = '早已完成填报，无需填报'


elif y == '未完成':
    try:
        timetamp = time.mktime(time.localtime())
        timetamp = int(timetamp)
        rep = r.post(url=url3, params=data, headers=header, cookies=cookies)
        a = "填报成功"
    except:
        a = "填报出错"



else:
    z = "填写时间未到，或填写失败"

file = open("zzx.html", 'w+', encoding='UTF-8')
file.write(b + '*****' + c + '*****' + d + '*****' + e + '*****' + f + '*****' + z + '*****' + a)
file.close()
