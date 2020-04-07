#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/4/7 17:12
# @Author: K
# @File: Procedure.py

# n1 = 255
# n2 = 1000
#
# print(str(hex(n1)))

def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('Not a Num!')
	if x > 0:
		return x
	else:
		return -x
	
print(my_abs('a'))
