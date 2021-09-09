# coding=utf-8
import requests as r
from lxml import etree
import time
from time import sleep

timetamp = time.mktime(time.localtime())
timetamp = int(timetamp)

url = "http://xscfw.hebust.edu.cn/survey/ajaxLogin"
url2 = "http://xscfw.hebust.edu.cn/survey/index"
url3 = f"http://xscfw.hebust.edu.cn/survey/surveySave?timestamp={timetamp}"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62"
}

# 账号信息
name1 = {
    "0": "马月玲",
    "1": "郝秋月",
    "2": "刘玉洁",
    "3": "乔岚涓",
    "4": "王菁菁",
    "5": "折  艳",
    "6": "王梓慧",
    "7": "郭心雨",
    "8": "贾雯淋",
    "9": "顾嘉宁",
    "10": "陈  远",
    "11": "陈  垚",
    "12": "郭杰伟",
    "13": "刘泽琨",
    "14": "罗  磊",
    "15": "张  臻",
    "16": "丁  勇",
    "17": "付浩宇",
    "18": "郝培阳",
    "19": "胡进宝",
    "20": "鲁  响",
    "21": "陈  璞",
    "22": "杜世千",
    "23": "孔  伟",
    "24": "张志轩",
    
}
xinxi = {
     "0": {"stuNum": "19L0252048", "pwd": "Lc2#0101263646"},
    "1": {"stuNum": "19L0252020", "pwd": "Lc2#0004121024"},
    "2": {"stuNum": "19L0252077", "pwd": "Lc2#0107200025"},
    "3": {"stuNum": "19L0252078", "pwd": "Lc2#0005281668"},
    "4": {"stuNum": "19L0252080", "pwd": "Lc2#0111171086"},
    "5": {"stuNum": "19L0252084", "pwd": "Lc2#0010210027"},
    "6": {"stuNum": "19L0252025", "pwd": "Lc2#0109080062"},
    "7": {"stuNum": "19L0252044", "pwd": "Lc2#0011060668"},
    "8": {"stuNum": "19L0252045", "pwd": "Lc2#0010300322"},
    "9": {"stuNum": "19L0252073", "pwd": "Lc2#0010283825"},
    "10": {"stuNum": "19L0252001", "pwd": "Lc2#9912033155"},
    "11": {"stuNum": "19L0252002", "pwd": "Lc2#0006160019"},
    "12": {"stuNum": "19L0252004", "pwd": "Lc2#9909204211"},
    "13": {"stuNum": "19L0252007", "pwd": "Lc2#0108223310"},
    "14": {"stuNum": "19L0252008", "pwd": "Lc2#0010016111"},
    "15": {"stuNum": "19L0252016", "pwd": "Lc2#0107087271"},
    "16": {"stuNum": "19L0252029", "pwd": "Lc2#991217521X"},
    "17": {"stuNum": "19L0252030", "pwd": "Lc2#0010069210"},
    "18": {"stuNum": "19L0252032", "pwd": "Lc2#0011064515"},
    "19": {"stuNum": "19L0252033", "pwd": "Lc2#000223451X"},
    "20": {"stuNum": "19L0252036", "pwd": "Lc2#0106107017"},
    "21": {"stuNum": "19L0252056", "pwd": "Lc2#0204070412"},
    "22": {"stuNum": "19L0252057", "pwd": "Lc2#0008062156"},
    "23": {"stuNum": "19L0252060", "pwd": "Lc2#0008165038"},
    "24": {"stuNum": "19L0252071", "pwd": "Lc2#0102022011"}
}


def tiwen(name):
    a, p, c, d, e, f, z = '', '', '', '', '', '', ''
    y = ''
    param = xinxi[name]
    newparam=str(param)
    tname=name1[name]
 
    try:
        response = r.post(url=url, params=param, headers=header)
        sleep(15)
        cookiesJAR = response.cookies  # 获取cookies
        cookies = cookiesJAR.get_dict()  # 把cookies写成字典形式
        res = r.get(url=url2, headers=header, cookies=cookies, params=param)
        b = "学校网页可以正常进入"

    except:
        b = "学校网页无法进入"

    # 获取完成情况
    try:
        res.encoding = 'uft-8'
        html = etree.HTML(res.text)
        content = html.xpath('/html/body/ul/li[1]/div/span/text()')
        y = content[0]
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
    file = open("yes.html", 'a', encoding='UTF-8')
    file.close()
    file = open("no.html", 'a', encoding='UTF-8')
    file.close()
    if a=="填报成功":
        file = open("yes.html", 'a', encoding='UTF-8')
        file.write(tname+newparam+ '==><br>' + b + '==><br>' + c + '==><br>' + d + '==><br>' + e + '==><br>' + f + '==><br>' + z + '==><br>' + a+"<br><hr>")
        file.close()
    else:
        file = open("no.html", 'a', encoding='UTF-8')
        file.write(
            tname + newparam + '==><br>' + b + '==><br>' + c + '==><br>' + d + '==><br>' + e + '==><br>' + f + '==><br>' + z + '==><br>' + a + "<br><hr>")
        file.close()


if __name__ == '__main__':
    for i in range(len(name1)):
        newi=str(i)
        tiwen(newi)
