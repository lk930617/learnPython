#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/4/20 15:19
# @Author: K
# @File: zhengze.py
import re
# def is_valid_email(addr):
#     return re.match(r'^([0-9a-zA-Z\.]+)@(\w+)(.com)$', addr)
#
# # 测试:
# assert is_valid_email('someone@gmail.com')
# assert is_valid_email('bill.gates@microsoft.com')
# assert not is_valid_email('bob#example.com')
# assert not is_valid_email('mr-bob@example.com')
# print('ok')

# def name_of_email(addr):
# 	r = re.match(r'([0-9a-zA-Z\<\>\s]+)(@)([a-zA-Z\.]+)', addr)
# 	L = re.split(r'\<|\>\s+', r.group(1))
# 	if len(L) > 1:
# 		return L[1]
# 	else:
# 		return L[0]
#
#
# # 测试:
# assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
# assert name_of_email('tom@voyager.org') == 'tom'
# print('ok')