#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/4/17 17:12
# @Author: K
# @File: task_master.py

import random, time, queue
from multiprocessing.managers import BaseManager

send_queue = queue.Queue()
recv_queue = queue.Queue()

class QueueManger(BaseManager):
	pass

def send_fn():
	return send_queue
def recv_fn():
	return recv_queue

if __name__ == '__main__':
 
	QueueManger.register('get_Send_queue', callable=send_fn)
	QueueManger.register('rcv_Recv_queue', callable=recv_fn)
	manager = QueueManger(address=('127.0.0.1', 5000), authkey=b'abc')

	manager.start()
	send = manager.get_Send_queue()
	recv = manager.rcv_Recv_queue()

	for i in range(10):
		n = random.randint(0, 10000)
		print('Put task %d.' % n)
		send.put(n)

	print('Try recv')
	for i in range(10):
		r = recv.get(timeout=10)
		print('Recv: %s' % r)

	manager.shutdown()
	print('master exit')
