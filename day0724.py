# -*- coding: utf-8 -*-
'''
def count():
	fs = []
	for i in range(1,4):
		def f():
			return i * i
		fs.append(f)
	return fs
f1 ,f2 ,f3= count()
print(f1())
print(list(count()))
'''
'''
def createCounter():
	a = [0]
	def counter():
		a[0] += 1
		return a[0]
	return counter
A = createCounter()
print(A(),A())
'''
'''
L = list(filter(lambda n: n % 2 == 1,range(1,20)))
print(L)
'''
'''
def log(func):
	def wrapper():
		print("call %s():" %func.__name__)
		return func()
	return wrapper
@log
def now():
	print("1608")

now()
'''
import time,functools
def metric(fn):
	@functools.wraps(fn)
	def wrapper(*args,**kw):
		print('%s executed in %s ms' % (fn.__name__,time.time()))
		return fn(*args,**kw)
	return wrapper
@metric
def fast(x,y):
	time.sleep(0.0012)
	return x + y
	
@metric
def slow(x,y,z):
	time.sleep(0.1234)
	return x * y * z
print(fast(11,22))
print(slow(11,22,33))