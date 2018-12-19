# -*- coding: utf-8 -*-

'''
def _odd_iter():
	n = 3
	while(True):
		yield n
		n = n + 2
def _not_divisible(n):
	return lambda x: x % n > 0
def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n),it)

for n in primes():
	if n < 100:
		print(n)
	else:
		break
'''
def number_iter():
	n = 1
	while(True):
		yield n
		n = n + 1
def is_palindrome(n):
	'''
	n_str = str(n)
	length = len(n_str)
	for i in range((length // 2) + 1):
		if n_str[i] != n_str[length - i - 1]:
			return False
	return True
	#return lambda n: n_str[i] == n_str[length - i - 1] for i in range(length)
	'''
	return str(n)[:] == str(n)[::-1] # 别人的思想
print(list(filter(is_palindrome,range(1,200))))

	
