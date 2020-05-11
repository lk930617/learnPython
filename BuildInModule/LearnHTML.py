#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/5/11 15:30
# @Author: K
# @File: LearnHTML.py
# HTML = '''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>'''
#
# from html.parser import HTMLParser
# from html.entities import name2codepoint
#
# class MyHTML(HTMLParser):
# 	def handle_starttag(self, tag, attrs):
# 		print('<%s>' % tag)
#
# 	def handle_endtag(self, tag):
# 		print('</%s>' % tag)
#
# 	def handle_startendtag(self, tag, attrs):
# 		print('<%s/>' % tag)
#
# 	def handle_data(self, data):
# 		print(data)
#
# 	def handle_comment(self, data):
# 		print('<!--', data, '-->')
#
# 	def handle_entityref(self, name):
# 		print('&%s:' % name)
#
# 	def handle_charref(self, name):
# 		print('&#%s:' % name)
#
# parser = MyHTML()
# parser.feed(HTML)

# from html.parser import HTMLParser
# class MyHTMLParser(HTMLParser):
# 	Cof = []
# 	findName = False
# 	findLoca = False
# 	def handle_starttag(self, tag, attrs):
# 		d = dict(attrs)
# 		if (tag == 'h3') and ('class' in d):
# 			self.findName = True
# 		elif (tag == 'time') and ('datetime' in d):
# 			self.Cof.append(('CofTime: ', d['datetime']))
# 		elif (tag == 'span') and ('class' in d) and (d['class'] == 'event-location'):
# 			self.findLoca = True
# 	def handle_data(self, data):
# 		if self.findName:
# 			self.Cof.append(('CofName: ', data))
# 		if self.findLoca:
# 			self.Cof.append(('CofLoca: ', data))
#
# 	def handle_endtag(self, tag):
# 		self.findLoca = False
# 		self.findName = False
#
# with open('test.html', 'rb') as f:
# 	code = f.read().decode('utf-8')
#
# MyHTML = MyHTMLParser()
# MyHTML.feed(code)
# print(MyHTML.Cof)

from bs4 import BeautifulSoup
with open('test.html', 'rb') as f:
	soup = BeautifulSoup(f, 'html.parser', from_encoding='utf-8')
fp = soup.section.text
print(fp)