#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/5/15 17:24
# @Author: K
# @File: LearnUDP.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))
print('bind UDP on 9999')
while True:
	data, addr = s.recvfrom(1024)
	print('Received from %s:%s' % addr)
	s.sendto(b'Hello, %s' % data, addr)