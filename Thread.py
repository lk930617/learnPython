#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/4/17 10:50
# @Author: K
# @File: Thread.py
from multiprocessing import Process
# import os
#
# def run_proc(name):
# 	print('Run Child %s(%s)' % (name, os.getpid()))
#
# if __name__ == '__main__':
# 	print('Parent %s' % os.getpid())
# 	p = Process(target=run_proc, args=('test', ))
# 	print('Child start')
# 	p.start()
# 	p.join() #等待子进程结束
# 	print('Child end')

# from multiprocessing import Pool
# import os, time, random
#
# def long_task(name):
# 	print('Run task %s(%s)' % (name, os.getpid()))
# 	start = time.time()
# 	time.sleep(random.random() * 3)
# 	end = time.time()
# 	print('Task %s run %0.2f seconds' % (name, (end-start)))
#
# if __name__ == '__main__':
# 	print('Parent %s' % os.getpid())
# 	p = Pool(4)
# 	for i in range(5):
# 		p.apply_async(long_task, args=(i, ))
# 	print('Waiting for all done.')
# 	p.close()
# 	p.join()
# 	print('All done..')

# import subprocess
#
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)

from multiprocessing import Process, Queue
# import os, time, random
#
# def write(q):
# 	print('Process to write %s' % os.getpid())
# 	for v in ['a', 'b', 'c']:
# 		print('Put %s to queue' % v)
# 		q.put(v)
# 		time.sleep(random.random())
#
		
# def read(q):
# 	print('Process to read %s' % os.getpid())
# 	while True:
# 		v = q.get(True)
# 		print('Get %s from queue' % v)
#
# if __name__ == '__main__':
# 	q = Queue()
# 	pw = Process(target=write, args=(q,))
# 	pr = Process(target=read, args=(q,))
# 	pw.start()
# 	pr.start()
# 	pw.join()
# 	pr.terminate()

#import time, threading
# def loop():
# 	print('thread %s is running' % threading.current_thread().name)
# 	n = 0
# 	while n < 5:
# 		n = n + 1
# 		print('thread %s >>> %s' % (threading.current_thread().name, n))
# 		time.sleep(1)
# 	print('thread %s end' % threading.current_thread().name)
#
# print('thread %s is running' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('Thread %s is end' % threading.current_thread().name)

# balance = 0
# lock = threading.Lock()
# def change(n):
# 	global balance
# 	balance = balance - n
# 	balance = balance + n
#
# def run_thread(n):
# 	for i in range(1000000):
# 		lock.acquire()
# 		try:
# 			change(n)
# 		finally:
# 			lock.release()
#
#
# if __name__ == '__main__':
# 	t1 = threading.Thread(target=run_thread, args=(5, ))
# 	t2 = threading.Thread(target=run_thread, args=(8, ))
# 	t1.start()
# 	t2.start()
# 	t1.join()
# 	t2.join()
# 	print(balance)

# import threading
#
# local_school = threading.local()
#
# def student():
# 	std = local_school.std
# 	print('Hello %s (in %s)' % (std, threading.current_thread().name))
#
# def pro_thread(name):
# 	local_school.std = name
# 	student()
#
# t1 = threading.Thread(target=pro_thread, args=('aaa', ), name='ThreadA')
# t2 = threading.Thread(target=pro_thread, args=('bbb', ), name='ThreadB')
# t1.start()
# t2.start()
# t1.join()
# t2.join()