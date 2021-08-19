#coding=utf-8
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import requests
#变量
my_email = "z1564356842@163.com" #此处是python发送邮件利用的邮箱
send_mail = "1564356842@qq.com" #此处是接收填写情况的邮箱
license_code = "ZMYBZUFNFWWMWKHZ" #发送邮箱的pop授权码
smtp_server = "smtp.163.com"  # qq smtp 的服务器
time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
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


def send_email():
    #发送邮件函数
    try:

        msg = MIMEText(f"{text}", "plain", "utf-8")
        #判断填写情况并发送邮件
        msg['From'] = Header(my_email)
        msg['To'] = Header(send_mail)
        msg['Subject'] = Header(f"{time}知乎热搜")
        server = smtplib.SMTP_SSL(host=smtp_server)
        server.connect(smtp_server,465)
        server.login(my_email,password=license_code)
        server.sendmail(my_email,send_mail,msg.as_string())
        server.quit()
        print("发送成功")
        #连接服务器
    except:
        print('error')
        #程序运行失败的报错信息
if __name__ == '__main__':

    send_email()

