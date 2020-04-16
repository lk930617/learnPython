#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/4/16 11:20
# @Author: K
# @File: Execption.py

# from functools import reduce
#
# def str2num(s):
#     if s.find('.'):
#         return float(s)
#     return int(s)
#
# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)
#
# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)
#
# main()


# def fn(s):
# 	n = int(s)
# 	assert n != 0, 'n is zero'
# 	return 10/n
#
# fn('0')

def fact(n):
	'''
	Calculate 1*2*...*n

	>>> fact(1)
	1
	>>> fact(10)
	3628800
	>>> fact(-1)
	Traceback (most recent call last):
	...
	ValueError
	'''
	if n < 1:
		raise ValueError()
	if n == 1:
		return 1
	return n * fact(n - 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()