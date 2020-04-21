#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/4/20 17:20
# @Author: K
# @File: DateTime.py
#from datetime import datetime, timedelta, timezone
#print(datetime.now())
#print(datetime(2020,4,20,17,22,50).timestamp())
#print(datetime.fromtimestamp(13544364300.0))
#print(datetime.utcfromtimestamp(13544364300.0))
# cday = datetime.strptime('2020-4-20 17:26:00', '%Y-%m-%d %H:%M:%S')
# print(cday)

#print(datetime.now().strftime('%A, %B %d %H:%M'))
# now = datetime.now()
# print(now + timedelta(hours=10))
# print(now - timedelta(days=1))
# print(now + timedelta(days=2, hours=12))

# import re
# from datetime import datetime, timezone, timedelta
#
# def to_timestamp(dt_str, tz_str):
# 	t = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
# 	tz = re.match(r'UTC(.*):00', tz_str)
# 	hour = int(tz.group(1))
# 	tz_utc = timezone(timedelta(hours=hour))
# 	return t.replace(tzinfo=tz_utc).timestamp()
#
# # 测试:
# t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
# assert t1 == 1433121030.0, t1
#
# t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
# assert t2 == 1433121030.0, t2
#
# print('ok')