#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/4/16 15:17
# @Author: K
# @File: IO.py
# with open('test.txt', 'a') as f:
#  	f.write("HHHHHHHH\n")

# fpath = r'C:\Windows\system.ini'
# with open(fpath, 'r') as f:
# 	for line in f.readlines():
# 		print(line.strip())


# from io import StringIO
#
# f = StringIO('Hello\nMy\nWorld')
# while True:
# 	s = f.readline()
# 	if s == '':
# 		break
# 	else:
# 		print(s.strip())

# from io import BytesIO
# f = BytesIO('中文'.encode('utf-8'))
# print(f.getvalue())


# from io import StringIO
#
# f= StringIO('abc')
# f.seek(3, 0)#此时指针是0，需要移动到末尾，否则write会覆盖初始化内容
# f.write('def')
# print(f.getvalue())

import os
# print(type(os.environ))
#print(os.environ.get('Path'))
#print(os.listdir('D:\learnPython\.git'))

# def findS(s, path):
# 	L = []
# 	for x in os.listdir(path):
# 		newpath = os.path.join(path, x)
# 		if os.path.isfile(newpath):
# 			if os.path.splitext(x)[0].find(s) >= 0:
# 				L.append(os.path.abspath(x))
# 		elif os.path.isdir(newpath):
# 			L = L + findS(s, newpath)
# 	return L
#
#
# f = findS('sql', '.')
# for n in f:
# 	print(n)

#import pickle
# d = dict(name = '111', age =20)
# with open('dump.txt', 'wb') as f:
# 	pickle.dump(d, f)

# with open('dump.txt', 'rb') as f:
# 	d = pickle.load(f)
# print(d)

import json
# d = dict(name = '111', age = 20)
# # print(json.dumps(d))
# with open('json.txt', 'w') as f:
# 	json.dump(d, f)
#
#
# class Std(object):
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
#
# s = Std('123', 12)
# print(json.dumps(s, default=lambda obj: obj.__dict__))

# obj = dict(name='小明', age=20)
# s = json.dumps(obj, ensure_ascii=False)
# print(s)