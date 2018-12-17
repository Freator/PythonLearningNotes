# -*- coding: utf-8 -*-
'''
L = ['Hello','WORLD',18,'APPLE',None]
print([x.lower() for x in L if isinstance(x,str)])
'''


def triangles():
	L = [1]
	while True:
		yield L
		L = L[:]
		L.append(0)
		L = [L[i - 1] + L[i] for i in range(len(L))]
n = 0
result = []
for t in triangles():
	print(t)
	#print(isinstance(t,list))
	result.append(t)
	n = n + 1
	if n == 10:
		break
print(result)

'''
def getRow(self, rowIndex):
    
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1, 1]
    out = [1, 1]
    for j in range(2, rowIndex+1):
        a = out[0]
        for i in range(1, len(out)):
            b = out[i]
            out[i] += a
            a = b
        out = out + [1]
    return out
'''