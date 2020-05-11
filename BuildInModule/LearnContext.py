#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/4/23 16:53
# @Author: K
# @File: LearnContext.py

# class Query(object):
# 	def __init__(self, name):
# 		self.name = name
#
# 	def __enter__(self):
# 		print('Begin')
# 		return self
#
# 	def __exit__(self, exc_type, exc_val, exc_tb):
# 		if exc_type:
# 			print('Error')
# 		else:
# 			print('End')
#
# 	def query(self):
# 		print('Query %s' % self.name)
#
# with Query('123') as q:
# 	q.query()

# from contextlib import contextmanager
# class Query(object):
# 	def __init__(self, name):
# 		self.name = name
# 	def query(self):
# 		print('Query %s' % self.name)
#
# @contextmanager
# def create_query(name):
# 	print('Begin')
# 	q = Query(name)
# 	yield q
# 	print('End')
#
# with create_query('123') as q:
# 	q.query

# @contextmanager
# def tag(name):
# 	print('<%s>' % name)
# 	yield
# 	print('</%s>' %name)
#
# with tag('h1'):
# 	print('Hello')
# 	print('123')

# from contextlib import closing
# from urllib.request import urlopen
#
# with closing(urlopen('http://www.baidu.com')) as page:
# 	for line in page:
# 		print(line)
#