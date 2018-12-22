# -*- coding: utf-8 -*-
'a test module'
__author = 'Freator'

class Student(object):
	def __init__(self,name,gender):
		self.name = name
		self.__gender = gender
	def get_gender(self):
		return self.__gender
	def set_gender(self,gender):
		if gender != 'female' and gender != 'male':
			raise ValueError("Bad Gender")
		self.__gender = gender
bart = Student("Bart",'female')
print(bart.get_gender())
bart.set_gender("male")
print(bart.get_gender())