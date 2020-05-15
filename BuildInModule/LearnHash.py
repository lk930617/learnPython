#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/4/22 14:58
# @Author: K
# @File: LearnHash.py
# import hashlib
# md5 = hashlib.md5()
# md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())

# db = {
#     'michael': 'e10adc3949ba59abbe56e057f20f883e',
#     'bob': '878ef96e86145580c38c87f0410ad153',
#     'alice': '99b1c2188db85afee403b1536010c2c9'
# }
#
# def login(user, password):
#     md5 = hashlib.md5()
#     md5.update(password.encode('utf-8'))
#     return db[user] == md5.hexdigest()
#
# # 测试:
# assert login('michael', '123456')
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
# print('ok')

# import hashlib, random
# def get_md5(s):
#     return hashlib.md5(s.encode('utf-8')).hexdigest()
#
# class User(object):
#     def __init__(self, name, password):
#         self.name = name
#         self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
#         self.password = get_md5(password + self.salt)
#
# db = {
#     'michael': User('michael', '123456'),
#     'bob': User('bob', 'abc999'),
#     'alice': User('alice', 'alice2008')
# }
#
# def login(username, password):
#     user = db[username]
#     return user.password == get_md5(password + user.salt)
#
# # 测试:
# assert login('michael', '123456')
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
# print('ok')