#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/5/15 17:26
# @Author: K
# @File: LearnUDPClient.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'tast', b'tbst', b'tcst']:
	s.sendto(data, ('127.0.0.1', 9999))
	print(s.recv(1024).decode('utf-8'))

s.close()