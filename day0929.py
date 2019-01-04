# -*- coding:utf-8 -*-
'''
class Methods:
	def publicMethod1(self):
		print("This is a public object method1!")
	def __privateMethod1(self):
		print("This is a private object method")
	def publicMethod2(self):
		print("This is a public object method2")
		print("And calling a private object method:")
		self.__privateMethod()
	@classmethod
	def publicClassMethod(cls):
		print("This is a public class method")
	@classmethod
	def __privateClassMethod(cls):
		print("This is a private class method")
	def publicMethod(self):
		print("This is a common public method")
	def __privateMethod(self):
		print("This is a common private method")
	publicMethodToClassMethod = classmethod(publicMethod)
	privateMethodToClassMethod = classmethod(__privateMethod)
	
m = Methods()
m.publicMethod1()
print("------ONELINE-------")
m.publicMethod2()
print("--------TWOLINE--------")
m._Methods__privateMethod1()
print("-------THREELINE---------")
Methods.publicMethod1(m)
Methods._Methods__privateMethod(m)
print("END")
'''

'''
m = Methods()
m.publicClassMethod()
print("--------------------------------------one")
Methods.publicClassMethod()
print("-------------------------------------two")
m._Methods__privateClassMethod()
print("-------------------------------------three")
Methods._Methods__privateClassMethod()
print("-------------------------------------four")
m.publicMethodToClassMethod()
print("-------------------------------------five")
Methods.publicMethodToClassMethod()
print("--------------------------------------six")
m.privateMethodToClassMethod()
print("--------------------------------------seven")
Methods.privateMethodToClassMethod()
print("END")
'''


class Number:
	def __init__(self,a,b):
		self.a = a
		self.b = b
	def __add__(self,x):
		return Number(self.a - x.a,0)
	def __sub__(self,x):
		return Number(self.b + x.b,0)
n1 = Number(33,11)
print(n1.a,n1.b)
n2 = Number(88,1)
print(n2.a,n2.b)
m = n1 + n2
p = n2 + n1
print(m.a,m.b)
print(p.a,p.b)