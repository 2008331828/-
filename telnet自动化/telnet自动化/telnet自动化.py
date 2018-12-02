#!/usr/bin/python3.4
# -*- coding=utf-8 -*-
import sys
sys.path.append('/usr/local/lib/python3.4/dist-packages/PyQYT/ExtentionPackages')
sys.path.append('/usr/lib/python3.4/site-packages/PyQYT/ExtentionPackages')
sys.path.append('../../ExtentionPackages')

from telnetlib import Telnet
import re 
import time

def QYT_TelnetClient(ip, username, password, *cmds):
	tn = Telnet(ip, 23)
	rackreply = tn.expect([],timeout=1)[2].decode().strip()
	print(rackreply)
	tn.write(username.encode())
	rackreply = tn.expect([],timeout=1)[2].decode().strip()
	print(rackreply)
	tn.write(password.encode())	
	tn.write(b'\n')
	#time.sleep(1)
	#rackreply = tn.expect([],timeout=1)[2].decode().strip()
	#print(rackreply)
	#tn.write(b'\n')
	#time.sleep(1)
	rackreply = tn.expect([],timeout=1)[2].decode().strip()
	print(rackreply)
	#tn.write(enable.encode())
	#tn.write(b'\n')
	rackreply = tn.expect([],timeout=1)[2].decode().strip()
	print(rackreply)
	#time.sleep(1)

	for cmd in cmds:
		tn.write(cmd.encode() + b'\n')
		rackreply = tn.expect([],timeout=1)[2].decode().strip()
		print(rackreply)
		
	#tn.write(b'quit\n')
	rackreply = tn.expect([],timeout=1)[2].decode().strip()
	print(rackreply)
	tn.close()


if __name__ == "__main__":
	QYT_TelnetClient('192.168.2.1', 'admin', 'google9', 'sys', 'dis cu ')