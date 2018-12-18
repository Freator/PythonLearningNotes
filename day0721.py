# -*- coding: utf-8 -*-
'''
L1 = ['adam','LISA','barT']
def normalize(name):
	def func(s):
		return s.capitalize()
	L2 = list(map(func,name))
	return L2
print(normalize(L1))		
'''
'''
from functools import reduce
def prod(L):
	def func(x,y):
		return x * y
	return reduce(func,L)
print('3 * 5 * 7 * 9 = ',prod([3,5,7,9]))
'''

from functools import reduce

def str2float(s):
    def fn(x,y):
        return x*10+y
    n=s.index('.')
    s1=list(map(int,[x for x in s[:n]]))
    s2=list(map(int,[x for x in s[n+1:]]))
    return reduce(fn,s1) + reduce(fn,s2)/10**len(s2)
print('\'123.4567\'=',str2float('123.4567'))  