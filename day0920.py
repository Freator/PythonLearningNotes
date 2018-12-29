# -*- coding:utf-8 -*-

#统计一个字符串出现的次数

'''
s = 'Do not trouble trouble until trouble troubles you.'
word = input('input a word:')
times = s.count(word)
print("there is %d times \'%s\' in \'%s\'" %(times,word,s))
'''
#正则表达式
'''
import re

s = 'Do not trouble trouble until trouble troubles you.'

r = 't[a-zA-Z]+'
print(re.match(r,s))
print(re.search(r,s))
print(re.findall(r,s))

r = re.compile('t[a-zA-Z]+')
print(r.findall(s))
print(r.sub('tell',s))


s = '10.7.189.215'
r = re.compile('\.')
print(r.split(s))
print(r.split(s,1))
'''

#默认值参数
def power(*number):
	print(number)
	sum = 0
	for i in number:
		sum += i
	return sum
print(power(1,2,3))