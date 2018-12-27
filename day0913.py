# -*- conding : utf-8 -*-

'''
 百元百鸡问题:
 一共一百元，公鸡5元/只，母鸡3元/只，小鸡1元/3只
 求正好一百元买100只鸡的各个鸡的数量

for i in range(1,21):
	for j in range(1,34):
		z = 100 - i - j
		if 5 * i + 3 * j + z / 3 == 100:
			print("cock = ",i," hen = ",j," and chicken = ",z)
print('End')
'''

'''
自幂数，一个n位数每个位上的n次幂加起来等于这个数本身
求所有n=4的自幂数（四叶玫瑰数）
'''

'''
count = 0
for i in range(1000,10000):
	a = i % 10
	b = (i % 100) // 10
	c = (i // 100) % 10
	d = i // 1000
	if i == a ** 4 + b ** 4 + c ** 4 + d ** 4:
		count += 1
		print("count = ",count,"\tnum = ",i)
print("End")
'''

'''
输出#组成的菱形
'''
from time import sleep
n = eval(input("Please enter an odd number:"))
up = int((n + 1) / 2)
down = int ((n - 1 )/2)

for i in range(1,up+1):
	print(" " * (up - i))
	print("#" * (2 * i - 1))
sleep(0.5)
for i in range(1,down + 1):
	print(" " * i,end = "")
	print("#" * (n - 2 * i))
sleep(0.5)