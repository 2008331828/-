#!/usr/bin/python3.4
# -*- coding=utf-8 -*-
import sys
from socket import *

myHost = '192.168.2.9'
myPort = 6666

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(5)

while True:
    connection, address = sockobj.accept()
    print('Server Connected by', address)
    while True:
        data = connection.recv(1024)
        if not data: break
        connection.send(b'Echo==>' + data)
    connection.close()