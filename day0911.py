# -*- coding: utf-8 -*-
'''
n = 0
str = "Life is short,YOU need Python!"
for i in str:
	if i == 'O' or i == 'o':
		n += 1
print(n)
'''

from random import *
price = randint(10,100)
guess = int(input("Guess a number:"))
while guess != price:
	if guess > price:
		guess = int(input("Bigger than price,guess another number:"))
	else:
		guess = int(input("Smaller than price,guess another number:"))
#	guess = int(input())
print("Guess right,congrats!")