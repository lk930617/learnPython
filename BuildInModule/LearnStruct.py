#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/4/21 17:10
# @Author: K
# @File: LearnStruct.py

# import struct
# print(struct.pack('>I', 10240099))
# print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))

# import base64, struct
# bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAA' +
#                    'AAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3/' +
#                    '/f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/A' +
#                    'HwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9' +
#                    '//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f' +
#                    '/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHw' +
#                    'AfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//' +
#                    '38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9' +
#                    '//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAf' +
#                    'AB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHw' +
#                    'AfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//' +
#                    '3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')
#
# def bmp_info(data):
# 	t = struct.unpack('<ccIIIIIIHH', data[:30])
# 	if t[0] == b'B' and t[1] == b'M':
# 		return {
# 			'width': t[6],
# 			'height': t[7],
# 			'color': t[9]
# 		}
#
# # 测试
# bi = bmp_info(bmp_data)
# assert bi['width'] == 28
# assert bi['height'] == 10
# assert bi['color'] == 16
# print('ok')