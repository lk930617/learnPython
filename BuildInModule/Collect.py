#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/4/21 15:25
# @Author: K
# @File: Collect.py


# from collections import namedtuple
# Point = namedtuple('Point', ['x', 'y'])
# p = Point(1, 2)
# print(p.y)
# print(isinstance(p, tuple))

# from collections import deque
# q = deque(['a', 'b', 'c'])
# q.append('x')
# q.appendleft('y')
# print(q)

# from collections import defaultdict
# dd = defaultdict(lambda: 'None')
# dd['key1'] = 'abc'
# print(dd['key1'])
# print(dd['key2'])

# from collections import OrderedDict
# # d = dict([('a', 1), ('b', 2), ('c', 3)])
# # print(d)
# # od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# # print(od)
# class FIFOdict(OrderedDict):
# 	def __init__(self, capacity):
# 		super(FIFOdict, self).__init__()
# 		self._capacity = capacity
#
# 	def __setitem__(self, key, value):
# 		containsKey = 1 if key in self else 0
# 		if len(self) - containsKey >= self._capacity:
# 			last = self.popitem(last=False)
# 			print('remove', last)
# 		if containsKey:
# 			del self[key]
# 			print('set:', (key, value))
# 		else:
# 			print('add:', (key, value))
# 		OrderedDict.__setitem__(self, key, value)
#
# L = FIFOdict(3)
# L['key1'] = 1
# L['key2'] = 2
# L['key3'] = 3
# L['key4'] = 4
# print(L)

# from collections import ChainMap
# import os, argparse
#
# defaults = {
# 	'color': 'red',
# 	'user': 'me'
# }
#
#
# parser = argparse.ArgumentParser()
# parser.add_argument('-u', '--user')
# parser.add_argument('-c', '--color')
# name = parser.parse_args()
# command = {k: v for k, v in vars(name).items() if v}
# combined = ChainMap(command, os.environ, defaults)
# print('color=%s' % combined['color'])
# print('user=%s' % combined['user'])

# from collections import Counter
# c = Counter()
# for ch in 'programing':
# 	c[ch] = c[ch] + 1
#
# print(c)
# c.update('hello')
# print(c)