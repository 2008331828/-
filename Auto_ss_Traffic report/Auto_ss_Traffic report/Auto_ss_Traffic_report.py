#!/usr/bin/python3.4
# -*- coding=utf-8 -*-

import sys


import getpass
import re
import paramiko
import time
import os
import sys
import email.utils
import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.application import MIMEApplication

'''
def sshcmd(ip, username, password, *cmds):
	ssh=paramiko.SSHClient()
	ssh.load_system_host_keys()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(ip,port=22,username=username,password=password,timeout=5,compress=True)
	chan=ssh.invoke_shell()
	time.sleep(1)
	x = chan.recv(2048).decode()

	for cmd in cmds:
		chan.send(cmd.encode())
		chan.send(b'\n')
		time.sleep(2)
		x = chan.recv(40960).decode()
		print(x)
	chan.close()
	ssh.close()
    ''' #备用！


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
   sy = os
   sy.system('./ssrmu.sh > 1.txt')
   sy.system('5 > 1.txt')


def load_txt():

   
    



    smtp_attachment('smtp.163.com','kuku64ma','5887415157', 'kuku65ma@163.com','717596873@qq.com','te','dlkfh dshgi')
    
if __name__ == '__main__':
    load_txt()
