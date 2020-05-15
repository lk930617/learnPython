#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/5/13 14:26
# @Author: K
# @File: LearnChardet.py

import chardet

# print(chardet.detect(b'Hello'))
# data = '离离原上草，一岁一枯荣'.encode('gbk')
# data = '离离原上草，一岁一枯荣'.encode('utf-8')
data = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))