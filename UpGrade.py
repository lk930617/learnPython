#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/4/9 14:25
# @Author: K
# @File: UpGrade.py

# def trim(s):
# 	if s[:1] == ' ':
# 		return trim(s[1:])
# 	elif s[-1:] == ' ':
# 		return trim(s[:-1])
# 	else:
# 		return s
#
# 	# 测试:
# if trim('hello  ') != 'hello':
# 	print('测试失败!')
# elif trim('  hello') != 'hello':
# 	print('测试失败!')
# elif trim('  hello  ') != 'hello':
# 	print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
# 	print('测试失败!')
# elif trim('') != '':
# 	print('测试失败!')
# elif trim('    ') != '':
# 	print('测试失败!')
# else:
# 	print('测试成功!')


# def findMinAndMax(L):
# 	if L:
# 		max = min = L[0]
# 		for i in L:
# 			if max < i:
# 				max = i
# 			if min > i:
# 				min = i
# 		return (min, max)
# 	else:
# 		return (None, None)
#
#
# # 测试
# if findMinAndMax([]) != (None, None):
# 	print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
# 	print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
# 	print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
# 	print('测试失败!')
# else:
# 	print('测试成功!')

# print([x * x for x in range(1, 10) if x%2 == 0])
# print([a + b for a in 'abc' for b in 'xyz'])
# import os
# print([d for d in os.listdir('.')])

# L= ['Acc', 'InTer', 'FCb']
# print([s.lower() for s in L])

# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [s.lower() for s in L1 if isinstance(s, str)]
#
# # 测试:
# print(L2)
# if L2 == ['hello', 'world', 'apple']:
#     print('测试通过!')
# else:
#     print('测试失败!')


# def fib(max):
# 	n, a, b = 0, 0, 1
# 	while n < max:
# 		yield b
# 		a,b = b, a + b
# 		n = n + 1
#
# for i in fib(10):
# 	print(i)

# def triangles():
# 	i = 1
# 	L = [1]
# 	while True:
# 		yield L
# 		L = [1] + [L[x] + L[x+1] for x in range(len(L)-1)] + [1]
# 		i = i +1
#
# # 期待输出:
# # [1]
# # [1, 1]
# # [1, 2, 1]
# # [1, 3, 3, 1]
# # [1, 4, 6, 4, 1]
# # [1, 5, 10, 10, 5, 1]
# # [1, 6, 15, 20, 15, 6, 1]
# # [1, 7, 21, 35, 35, 21, 7, 1]
# # [1, 8, 28, 56, 70, 56, 28, 8, 1]
# # [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# n = 0
# results = []
# for t in triangles():
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break
#
# for t in results:
#     print(t)
#
# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过!')
# else:
#     print('测试失败!')