#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/4/7 17:12
# @Author: K
# @File: Procedure.py

# n1 = 255
# n2 = 1000
#
# print(str(hex(n1)))

# def my_abs(x):
# 	if not isinstance(x, (int, float)):
# 		raise TypeError('Not a Num!')
# 	if x > 0:
# 		return x
# 	else:
# 		return -x
#
# print(my_abs('a'))

# import math
# def quadratic(a, b, c):
# 	if a == 0:
# 		raise TypeError('a can not be zero')
# 	return (-b + math.sqrt(b*b - 4*a*c))/2/a, (-b - math.sqrt(b*b - 4*a*c))/2/a
#
# # 测试:
# print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
# print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
#
# if quadratic(2, 3, 1) != (-0.5, -1.0):
#     print('测试失败')
# elif quadratic(1, 3, -4) != (1.0, -4.0):
#     print('测试失败')
# else:
#     print('测试成功')

# def product(*args):
# 	if len(args) == 0:
# 		raise TypeError('at least 1 num')
# 	s = 1
# 	for i in args:
# 		s = s * i
# 	return s
#
# # 测试
# print('product(5) =', product(5))
# print('product(5, 6) =', product(5, 6))
# print('product(5, 6, 7) =', product(5, 6, 7))
# print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
# if product(5) != 5:
# 	print('测试失败!')
# elif product(5, 6) != 30:
# 	print('测试失败!')
# elif product(5, 6, 7) != 210:
# 	print('测试失败!')
# elif product(5, 6, 7, 9) != 1890:
# 	print('测试失败!')
# else:
# 	try:
# 		product()
# 		print('测试失败!')
# 	except TypeError:
# 		print('测试成功!')

def move(n, a, b, c):
	if n == 1:
		print(a, '-->', c)
	else:
		move(n-1, a, c, b)#n-1从a移动到b
		move(1, a, b, c)#把最后一个从a到c
		move(n-1, b, a, c)#把n-1个从b到c

	
# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
move(3, 'A', 'B', 'C')