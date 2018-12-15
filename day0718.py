# -*- coding: utf-8 -*-
'''
def product(x,*y):
	count = 1
	for i in y:
		count = count * i
	return count * x
print(product(1))
try:
	product(3)
	print("ERROR")
except TypeError:
	print("RIGHT")
'''
'''
# hanoi algoorithm
def move(n,a,b,c):
	if n == 1:
		print(a,'-->',c)
	else:
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)
move(3,'A','B','C')
'''
d = {'A':1,'B':2,'C':3}
for q in d.values():
	print(q)


