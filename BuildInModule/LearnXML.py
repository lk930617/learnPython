#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/5/9 17:01
# @Author: K
# @File: LearnXML.py

# xml = r'''<?xml version="1.0"?>
# <ol>
#     <li><a href="/python">Python</a></li>
#     <li><a href="/ruby">Ruby</a></li>
# </ol>
# '''
#
# from xml.parsers.expat import ParserCreate
# class DefaultHandler(object):
# 	def start_element(self, name, attrs):
# 		print('sax: start_element: %s, attrs: %s' % (name, attrs))
#
# 	def end_element(self, name):
# 		print('sax: end_element: %s' % name)
#
# 	def char_data(self, text):
# 		print('sax: char_data: %s' % text)
#
#
# handler = DefaultHandler()
# parser = ParserCreate()
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
# parser.Parse(xml)

from xml.parsers.expat import ParserCreate
from urllib import request

def parseXml(xml_str):
    print(xml_str)
    return {
        'city': '?',
        'forecast': [
            {
                'date': '2017-11-17',
                'high': 43,
                'low' : 26
            },
            {
                'date': '2017-11-18',
                'high': 41,
                'low' : 20
            },
            {
                'date': '2017-11-19',
                'high': 43,
                'low' : 19
            }
        ]
    }

# 测试:
URL = 'http://flash.weather.com.cn/wmaps/xml/beijing.xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'