#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/4/17 17:20
# @Author: K
# @File: task_worker.py
import time, sys, queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
	pass


QueueManager.register('get_Send_queue')
QueueManager.register('rcv_Recv_queue')
server = '127.0.0.1'
print('Connect to Server %s' % server)
m = QueueManager(address=(server, 5000), authkey=b'abc')
m.connect()
send = m.get_Send_queue()
recv = m.rcv_Recv_queue()

for i in range(10):
	try:
		n = send.get(timeout=1)
		print('run send %d * %d' % (n, n))
		r = '%d * %d = %d' %(n, n, n*n)
		time.sleep(1)
		recv.put(r)
	except Queue.Empty:
		print('send is empty')

print('worker exit')