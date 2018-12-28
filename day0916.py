# -*- coding: utf-8 -*-
from random import choice
str = 'abcdefghijklmnopqrstuvwxyz'
Dict = dict()
for i in range(500):
	r = choice(str)
	Dict[r] = Dict.get(r,0) + 1
print(Dict)