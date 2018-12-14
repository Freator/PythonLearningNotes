# -*- coding: utf-8 -*-
'''
class1=[1,2,3]
print(class1[0])
# print(class1[-8])
len = len(class1)
print(len)
print(class1)
class1.append(4)
print(class1)
class1.pop()
print(class1)
'''

'''
L =[
	['Ap','Go','Mi'],
	['Ja','Py','Ru','PH'],
	['Ad','Ba','Li']
]
print(L[0][0])
print(L[1][1])
print(L[-1][-1])
'''
"""
height = 1.75
weight = input("weight : ")
weight = float(weight)
bmi = weight / (height * height)
if bmi < 18.5:
	print("too light")
elif bmi < 25:
	print("normal")
elif bmi < 28:
	print("fat")
elif bmi < 32:
	print("fatter")
else:
	print("too fat")

"""
'''
# loop
sum = 0
for x in range(101):
	sum = sum + x
print(sum)
'''

'''
L = ['Ap','Go','Mi']
for name in L:
	print(name)
i = 0	
while i < 3:
	print(L[i])
	i = i + 1
'''
'''
b = {'B':2,'D':3}
print(b['B'])
s = set([1,4,1,2,3])
print(s)
'''
'''
n1 = 255
n2 = 1000
print(hex(n1))
print(str(hex(n2)))
'''
import math
def quadratic(a,b,c):
	deta = (b * b) - (4 * a * c)
	if deta < 0:
		return "No result"
	elif deta == 0:
		return -b/(2*a)
	else:
		return (math.sqrt(deta) - b)/(2 * a),(-math.sqrt(deta) - b)/(2 * a)
print('quadratic(2,3,1) = ',quadratic(2,3,1))
print('quadratic(1,3,-4) = ',quadratic(1,3,-4))



