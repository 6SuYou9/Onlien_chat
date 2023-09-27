# Author: Su
# -*- coding: utf-8 -*-

# 发送邮件服务
import zmail

# from_mail 发件人
# passwd 使用qq邮箱时，passwd是开启IMAP/SMTP的十六位秘钥而不是密码，使用其他邮箱时可以使用密码
# to_mail 收件人
# subject 主题
# text 正文文本

def Send_Mail(from_mail: str, passwd: str, to_mail: str, subject: str, text: str):
    # 构建发送邮件的服务
    server = zmail.server(from_mail, passwd)
    # 通过邮件服务去发送邮件
    server.send_mail(to_mail, {'subject': subject, 'content_text': text})
