#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/4/13 14:53
# @Author: K
# @File: Class.py


# class Student(object):
# 	def __init__(self, name, gender):
# 		self.__name = name
# 		self.__gender = gender.lower()
#
# 	def get_gender(self):
# 		return self.__gender
#
# 	def set_gender(self, gender):
# 		if gender.lower() in ('male', 'female'):
# 			self.__gender = gender.lower()
#
#
# # 测试:
# bart = Student('Bart', 'Male')
# print(dir(bart))
# if bart.get_gender() != 'male':
# 	print('测试失败!')
# 	print(bart.get_gender())
# else:
# 	bart.set_gender('female')
# 	if bart.get_gender() != 'female':
# 		print('测试失败!')
# 	else:
# 		print('测试成功!')
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count = Student.count + 1
        
        
# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')