# -*- coding:utf-8 -*-
'''
class Person:
	number = 0
	def __init__(self,name,gender,age):
		self.name = name
		self.gender = gender
		self.age = age
		Person.number += 1
	def displayPerson(self):
		print('Name:',self.name,"Gender:",self.gender,'Age:',self.age)
	def displayNumber(self):
		print('Total number:',Person.number)
stu1 = Person('Tang','M',22)
stu2 = Person('Zeng','F',21)
stu1.displayPerson()
stu2.displayPerson()
print('Total number:',Person.number)
stu1.displayNumber()
print(stu1.age)

#在前面的基础上增删改属性
stu1.score = 90
print(stu1.score)
#sprint(stu2.score)
del stu1.score
print("The score:",stu1.score)
'''

'''
use function getattr(obj,property_name) to access a property
use function hasattr(obj,property_name) to check a property for presence and return True or False
use function setattr(obj,name,value) to create a property and set a value
use function delattr(obj,name) to delete a property
'''
class Car:
	salesPrice = 150000
	__manufacturePrice = 120000
	def __init__(self,brand,serial):
		self.brand = brand
		self.__serial = serial
print("Public:",Car.salesPrice)
print("Private:",Car._Car__manufacturePrice)
c1 = Car('Toyota','Karola')
print("Public Brand:",c1.brand)
print("Private Serial:",c1._Car__serial)
