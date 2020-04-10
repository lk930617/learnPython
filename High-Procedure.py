#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/4/10 11:07
# @Author: K
# @File: High-Procedure.py

# def myF(x, y, f):
# 	return f(x) + f(y)
#
# print(myF(-5, 10, abs))


# def f(x):
# 	return x * x
#
# r = map(f, [1, 2, 3, 4, 5])
# print(list(r))

# from functools import reduce
# def f(x, y):
# 	return x*10 + y
#
# r = reduce(f, [1, 3, 5, 7, 9])
#
# print(r)

# def normalize(name):
# 	return name[:1].upper() + name[1:].lower()
#
# # 测试:
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

# from functools import reduce
#
#
# def prod(l):
#     def f(x, y):
#         return x * y
#     return reduce(f, l)
#
#
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

# from functools import reduce
#
#
# def str2float(s):
# 	DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# 	pos = i =  0
# 	while i < len(s):
# 		if s[i] == '.':
# 			pos = i
# 			break
# 		else:
# 			i = i+1
#
# 	def str2int(x):
# 		return DIGITS[x]
# 	def f1(x, y):
# 		return x * 10 + y
# 	def f2(x, y):
# 		return x * 0.1 + y
# 	return reduce(f1, map(str2int, s[:pos])) + reduce(f2, map(str2int, s[:pos:-1]))*0.1
#
# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
# 	print('测试成功!')
# else:
# 	print('测试失败!')

# def is_palindrome(n):
#     s = str(n)
#     return s[::-1] == s
#
# # 测试:
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    #return t[0]
	return t[1]

L2 = sorted(L, key=by_name, reverse=True)
print(L2)