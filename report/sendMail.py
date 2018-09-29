# -*- coding: UTF-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os

dir = os.path.dirname(os.path.abspath(__file__))

mail_host = "smtp.163.com"  # 设置服务器
mail_user = "18707155894"  # 用户名
mail_pass = "ftq1691839"  # 口令


def mail(receivers, sub, content):  # to_list：收件人；sub：主题；content：邮件内容
    sender = "18707155894@163.com"
    message = MIMEMultipart()
    message['From'] = Header(mail_user)
    message['To'] = ','.join(receivers)
    subject = sub
    message['Subject'] = Header(subject, 'utf-8')
    message.attach(MIMEText(content, 'plain', 'utf-8'))
    to_list = message['To'].split(',')


    file = find_new_file(dir)
    att1 = MIMEText(open(file, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="result.html"'
    message.attach(att1)

    try:
        server = smtplib.SMTP()
        server.connect(mail_host)  # 连接smtp服务器
        server.login(mail_user, mail_pass)  # 登陆服务器
        server.sendmail(sender, to_list, message.as_string())  # 发送邮件
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False

def find_new_file(dir):
    file_lists = os.listdir(dir)
    file_lists.sort(key=lambda fn: os.path.getmtime(dir + "\\" + fn) if not os.path.isdir(dir + "\\" + fn) else 0)
    file = os.path.join(dir, file_lists[-1])
    print(file)
    return file

def send(receivers, sub, content):
    if mail(receivers, sub, content):
        print "邮件发送成功"
    else:
        print "邮件发送失败"


if __name__ == '__main__':

    receivers = ['18707155894@163.cn','623727633@qq.com']
    sub = "yanss API's result"
    content = "hi all:" + "\n" + "    " + "请查收附件！\n     error可忽略，无fail项则为通过！"
    send(receivers,  sub, content)

