#!/usr/bin/python3.4
# -*- coding=utf-8 -*-

import sys
sys.path.append('/usr/local/lib/python3.4/dist-packages/PyQYT/ExtentionPackages')
sys.path.append('/usr/lib/python3.4/site-packages/PyQYT/ExtentionPackages')
sys.path.append('../../ExtentionPackages')

import paramiko
import time
import sys
import smtplib
import email.utils

import smtplib, email.utils
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.application import MIMEApplication

def SSHClient_MultiCMD(ip, username, password, *cmds):
	ssh=paramiko.SSHClient()#创建SSH Client
	ssh.load_system_host_keys()#加载系统SSH密钥
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())#添加新的SSH密钥
	ssh.connect(ip,port=22,username=username,password=password,timeout=5,compress=True)#SSH连接

	chan=ssh.invoke_shell()#激活交互式shell
	time.sleep(1)
	x = chan.recv(2048).decode()#接收回显信息

	for cmd in cmds:#读取命令
		chan.send(cmd.encode())#执行命令，注意字串都需要编码为二进制字串
		chan.send(b'\n')#一定要注意输入回车
		time.sleep(2)#由于有些回显可能过长，所以可以考虑等待更长一些时间
		x = chan.recv(40960).decode()#读取回显，有些回想可能过长，请把接收缓存调大
		print(x)#打印回显
		
	chan.close()#退出交互式shell
	ssh.close()

def qyt_smtp_attachment(mailserver, username, password, From, To, Subj, Main_Body, files=None):
	Tos = To.split(';')#把多个邮件接受者通过';'分开
	Date = email.utils.formatdate()#格式化邮件时间
	msg = MIMEMultipart() 
	msg["Subject"] = Subj  
	msg["From"]    = From  
	msg["To"]      = To
	msg["Date"]    = Date

	part = MIMEText(Main_Body)  
	msg.attach(part)

	if files:
		for file in files:
			part = MIMEApplication(open(file,'rb').read())
			part.add_header('Content-Disposition', 'attachment', filename=file)  
			msg.attach(part) 

	server = smtplib.SMTP(mailserver)#连接邮件服务器
	server.login(username, password)#通过用户名和密码登录邮件服务器
	failed = server.sendmail(From, Tos, msg.as_string())#发送邮件
	server.quit()#退出会话
	if failed:
		print('Falied recipients:', failed)#如果出现故障，打印故障原因！
	else:
		print('邮件已经成功发出！')#如果没有故障发生，打印‘No errors.’！
	#print('Bye.')



if __name__ == '__main__':


    files= None
	method_name()('ss1.caosong.pw', 'root', 'google99868668','pwd','ifconfig')

    qyt_smtp_attachment('smtp.163.com',
					  	'kuku65ma@163.com',
					  	'google99868668', 
					  	'kuku65ma@163.com',
					  	'kuku65ma@11.com;717596873@qq.com',
					  	'test',
					  	'test1',
					  	files)







 