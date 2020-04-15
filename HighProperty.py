#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/4/15 15:00
# @Author: K
# @File: HighProperty.py
# from types import MethodType
# class Student(object):
# 	__slots__ = ('name', 'score')
# 	pass
#
# def setS(self, score):
# 	self.score = score
#
# s1 = Student()
# Student.setS = setS
# s1.setS(10)
# print(Student.setS, setS)

# class Screen(object):
#     @property
#     def width(self):
#         return self._width
#     @width.setter
#     def width(self, width):
#         if isinstance(width, int):
#             self._width = width
#     @property
#     def height(self):
#         return self._height
#     @height.setter
#     def height(self, height):
#         if isinstance(height, int):
#             self._height = height
#     @property
#     def resolution(self):
#         return self._height * self._width
#
#
#
# # 测试:
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')

# class Fib(object):
# 	def __init__(self):
# 		self.a, self.b = 0, 1
#
# 	def __iter__(self):
# 		return self
#
# 	def __next__(self):
# 		self.a, self.b = self.b, self.a + self.b
# 		if self.a > 10000:
# 			raise StopIteration()
# 		return self.a
# 	def __str__(self):
# 		return 'class of Fib'
#
# 	def __getitem__(self, n):
# 		if isinstance(n, int):
# 			a, b = 1, 1
# 			for x in range(n):
# 				a, b = b, a + b
# 			return a
# 		elif isinstance(n, slice):
# 			start = n.start
# 			stop = n.stop
# 			if start is None:
# 				start = 0
# 			a, b = 1, 1
# 			L = []
# 			for x in range(stop):
# 				if x >= start:
# 					L.append(a)
# 				a, b = b, a+b
# 			return L
#
# f = Fib()
# print(f[10:15])
# for i in f:
# 	print(i)

# from enum import Enum
# Month = Enum('Month', ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'))
# for name, member in Month.__members__.items():
# 	print(name, '=>', member, ',', member.value)

from enum import Enum, unique
@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        if isinstance(gender, Gender):
            self.gender = gender
        else:
            raise TypeError('wrong Type!')


# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')