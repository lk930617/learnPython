#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/5/6 16:14
# @Author: K
# @File: LearnUrl.py
# from urllib import request
#
# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))

# from urllib import request, parse
#
# print('Login')
# email = input('Email: ')
# passwd = input('Password: ')
# loginData = parse.urlencode([
# 	('username', email),
# 	('password', passwd),
# 	('entry', 'mweibo'),
# 	('client_id', ''),
# 	('savestate', '1'),
# 	('ec', ''),
# 	('pagerefer',  'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
#
# ])
#
# req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
#
# with request.urlopen(req, data=loginData.encode('utf-8')) as f:
# 	print('Status: ', f.status, f.reason)
# 	for k, v in f.getheaders():
# 		print('%s::%s' %(k, v))
# 	print('Data: ', f.read().decode('utf-8'))
# from urllib import request
# import json
#
#
# def fetch_data(url):
# 	with request.urlopen(URL) as f:
# 		return json.loads(f.read().decode('utf-8'))
#
#
# URL = 'https://yesno.wtf/api'
# data = fetch_data(URL)
# print(data)
# assert data['forced'] == False
# print('ok')

from urllib import request

url = 'https://www.taobao.com/search?q=psn'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
req = request.Request(url, headers=header)
with request.urlopen(req) as f:
	data = f.read()

with open('test.html', 'wb') as f:
	f.write(data)