#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/4/2 17:42
# @Author: K
# @File: Base.py

# format string
# s1 = 72
# s2 = 85
# r = (s2-s1)/s1 * 100
# print('提升了{0:.1f}%'.format(r))

# tuple and list
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# # 打印Apple:
# print(L[0][0])
# # 打印Python:
# print(L[1][1])
# # 打印Lisa:
# print(L[2][2])

# example for if
# weight = float(input('set your weight(kg): \n'))
# height = float(input('set your height(m): \n'))
# bmi = weight/height/height
# if bmi < 18.5:
# 	print('过轻')
# elif bmi <= 25:
# 	print('正常')
# elif bmi <= 28:
# 	print('过重')
# elif bmi <= 32:
# 	print('肥胖')
# else:
# 	print('严重肥胖')

# example for
# L = ['Bart', 'Lisa', 'Adam']
# for x in L:
# 	print('Hello, %s' % x)

a = {'a': 1, 'b': 2, 'c': 3}
a['d'] = 4
print(a)