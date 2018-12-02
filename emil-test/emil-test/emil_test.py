#!/usr/bin/python3.4
# -*- coding=utf-8 -*-

import sys
sys.path.append('/usr/local/lib/python3.4/dist-packages/PyQYT/ExtentionPackages')
sys.path.append('/usr/lib/python3.4/site-packages/PyQYT/ExtentionPackages')
sys.path.append('../../ExtentionPackages')

import getpass
import re
import paramiko
import time
import sys
import email.utils
import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.application import MIMEApplication

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

def main():

    sshcmd('ss1.c*******ng.pw', 'root', 'go99*****868', 'ifconfig','pwd' )

    smtp_attachment('smtp.163.com','kuk*****5ma','o******668', 'kuk****ma@163.com','717******3@qq.com','今日无线密码','dlkfh dshgi')
    
if __name__ == '__main__':
	main()
