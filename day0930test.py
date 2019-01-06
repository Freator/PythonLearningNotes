# -*- coding:utf-8 -*-
'''
def ins(A):
	for j in reversed(range(0,len(A))):
		key = A[j]
		i = j + 1
		while (i < len(A)) and A[i] > key:
			A[i - 1] = A[i]
			i = i + 1
		A[i - 1] = key
	for x in A:
		print(x,end = ' ')
A = [2,3,1,6,9,4,10]
ins(A)
'''
def add_binary(A,B):
	C = []
	carry = 0
	for i in reversed(range(0,len(A))):
		temp = ((A[i] + B[i]) + carry) % 2
		carry = (A[i] + B[i] + carry) // 2
		C.insert(0,temp)
	C.insert(0,carry)
	return C
A = [1,0,0,1]
B = [0,1,0,1]
print(add_binary(A,B))