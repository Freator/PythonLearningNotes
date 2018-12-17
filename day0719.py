# -*- coding: utf-8 -*-
def findMinAndMax(L):
	if len(L) == 0:
		return (None,None)
	min = 99999
	max = -99999
	for i in L:
		if i > max:
			max = i
		if i < min:
			min = i
	return (min,max)
print(findMinAndMax([]))
print(findMinAndMax([1,2,3]))
print(findMinAndMax([7]))
print(findMinAndMax([7,3,2,6,9,1]))

