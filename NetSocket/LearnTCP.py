#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/5/15 16:55
# @Author: K
# @File: LearnTCP.py

import socket
import threading
import time
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('www.sina.com.cn', 80))
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#
#
# buffer = []
# while True:
# 	d = s.recv(1024)
# 	if d:
# 		buffer.append(d)
# 	else:
# 		break
#
# data = b''.join(buffer)
# s.close()
#
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
#
# with open('test.html', 'wb') as f:
# 	f.write(html)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('Wait For Connect')
def tcplink(sock, addr):
	print('Accept From %s: %s' % addr)
	sock.send(b'Welcome')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit':
			break
		sock.send(('Hello %s!' % data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print('Connect From %s:%s closed' % addr)
	
while True:
	sock, addr = s.accept()
	t = threading.Thread(target=tcplink, args=(sock, addr))
	t.start()
