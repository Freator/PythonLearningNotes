# -*- coding:utf-8 -*-
def square_number(*num):
	print(num)
	out(*num)
	sum = 1
	for i in num:
		sum += i * i
	return sum
n = [1,2,3]
def out(*number):
	print('number in out:',number)
	#number.append(5)
	#return square_number(*number)
	
print(square_number(*n))
#print(out(*n))