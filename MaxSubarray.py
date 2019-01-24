# -*- coding:utf-8 -*-
def FMCS(A,low,mid,high):
	leftmax = -9999
	sum = 0
	for i in reversed(range(low,mid + 1)):
		sum += A[i]
		#print(A[i])
		if sum > leftmax:
			leftmax = sum
			leftpoint = i
	rightmax = -9999
	sum = 0
	for j in range(mid + 1,high + 1):
		sum += A[j]
		if sum > rightmax:
			rightmax = sum
			rightpoint = j
	return (leftpoint,rightpoint,leftmax + rightmax)

def FMS(A,low,high):
	if low == high:
		return (low,high,A[low])
	else:
		mid = (low + high)//2
		#print(mid)
		(leftlow,lefthigh,leftsum) = FMS(A,low,mid)
		(rightlow,righthigh,rightsum) = FMS(A,mid+1,high)
		(crosslow,crosshigh,crosssum) = FMCS(A,low,mid,high)
		if leftsum > rightsum and leftsum > crosssum:
			return (leftlow,lefthigh,leftsum)
		elif rightsum > leftsum and rightsum > crosssum:
			return (rightlow,righthigh,rightsum)
		else:
			return (crosslow,crosshigh,crosssum)
A=(13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7)
print(A[0],A[15])
print(FMS(A,0,15))