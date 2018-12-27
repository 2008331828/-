#!/usr/bin64/python2.7
# -*- coding=utf-8 -*-
import sys
import getpass
import re
import time
import os
import email.utils
import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.application import MIMEApplication


#发送模块
def smtp_attachment(mailserver, username, password, From, To, Subj, Main_Body, ):
	Tos = To.split(';')
	Date = email.utils.formatdate()
	msg = MIMEMultipart() 
	msg["Subject"] = Subj  
	msg["From"]    = From  
	msg["To"]      = To
	msg["Date"]    = Date

	part = MIMEText(Main_Body)  
	msg.attach(part)

	#if files:
		#for file in files:
			#part = MIMEApplication(open(file,'rb').read())
			#part.add_header('Content-Disposition', 'attachment', filename=file)  
			#msg.attach(part) 

	server = smtplib.SMTP(mailserver)
	server.login(username, password)
	failed = server.sendmail(From, Tos, msg.as_string())
	server.quit()
	if failed:
		print('Falied recipients:', failed)
	else:
		print('邮件已经成功发出！')

#检查流量
def Check_traffic():
   os.system('/root/ssrmu.sh>1.txt && 5 >1.txt')
  # os.system('./ssrmu.sh')
   #os.system('5 > /root/1.txt')
   pass
#读取流量
def load_txt():
     title = time.strftime('流量报告'+'%Y-%m-%d %H:%M',time.localtime(time.time()))
     with open('/root/1.txt', 'r') as f:
        text = f.read()
        f.close()
        smtp_attachment('smtp.163.com','kuku64ma','5887415157', 'kuku65ma@163.com','717596873@qq.com',title,text)
     pass


if __name__ == '__main__':
    Check_traffic()