#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/4/21 16:13
# @Author: K
# @File: LearnBase64.py
import base64
# print(base64.b64encode(b'binary\x00string'))
# print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))
def safe_base64_decode(s):
    c = len(s) % 4
    s = s + b'=' * (4-c)
    return base64.b64decode(s)

# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')