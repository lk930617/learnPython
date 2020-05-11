#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/4/22 16:50
# @Author: K
# @File: LearnIter.py

import itertools
# natual = itertools.count(1, 2)
# for n in natual:
# 	if n > 100:
# 		break
# 	print(n)

# cs = itertools.cycle('abc')
# n = 0
# for i in cs:
# 	if n > 100:
# 		break
# 	n = n + 1
# 	print(i)

# ns = itertools.repeat('abc', 3)
# for n in ns:
# 	print(n)

# for c in itertools.chain('abc', 'ddd'):
# 	print(c)

# for key, group in itertools.groupby('aaaAbbcd', lambda x: x.upper()):
# 	print(key, list(group))

# def pi(N):
# 	c = itertools.count(1, 2)
# 	L = list(itertools.takewhile(lambda x: x < 2*N, c))
# 	S = []
# 	for i in range(N):
# 		S.append(4 / (pow(-1, i) * L[i]))
# 	return sum(S)
#
# # 测试:
# print(pi(10))
# print(pi(100))
# print(pi(1000))
# print(pi(10000))
# assert 3.04 < pi(10) < 3.05
# assert 3.13 < pi(100) < 3.14
# assert 3.140 < pi(1000) < 3.141
# assert 3.1414 < pi(10000) < 3.1415
# print('ok')