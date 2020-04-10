#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/4/10 15:25
# @Author: K
# @File: Functional.py

# def createCounter():
# 	n = [0]
# 	def counter():
# 		n[0] = n[0] + 1
# 		return n[0]
# 	return counter
#
#
# # 测试:
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
# 	print('测试通过!')
# else:
# 	print('测试失败!')

# def outer(x):
# 	def inner(y):
# 		nonlocal x
# 		x += y
# 		return x
# 	return inner
#
#
# a = outer(10)
# print(a(1))
# print(a(3))

# L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
# print(L)

import time, functools
#
# def metric(fn):
# 	@functools.wraps(fn)
# 	def log(*args, **kw):
# 		t1 = time.time()
# 		ret = fn(*args, **kw)
# 		t2 = time.time()
# 		print('%s executed in %s ms' % (fn.__name__, t2-t1))
# 		return ret
# 	return log
#
# # 测试
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y;
#
# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z;
#
# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')


# def log(something):
# 	if isinstance(something, str):
# 		def decorator(fn):
# 			functools.wraps(fn)
# 			def wrapper(*args, **kw):
# 				print('begin call %s Has Text %s' % (fn.__name__, something))
# 				fn(*args, **kw)
# 				print('end call %s Has Text %s' % (fn.__name__, something))
# 				return None
# 			return wrapper
# 		return decorator
# 	else:
# 		functools.wraps(something)
# 		def wrapper(*args, **kw):
# 			print('begin call %s Has No Text' % something.__name__)
# 			something(*args, **kw)
# 			print('end call %s Has No Text' % something.__name__)
# 			return None
# 		return wrapper
#
# @log
# def aabb(x, y):
# 	print(x * 2 + y * 2)
#
# @log('begin')
# def aacc(x, y):
# 	print(x * 2 + y)
# aabb(1, 2)
# aacc(1, 2)
