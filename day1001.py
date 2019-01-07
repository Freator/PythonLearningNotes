# -*- coding:utf-8 -*-
import os
dirname = 'D:\\Python\\workplace'
multipledirname = 'D:\\Python\\workplace\\testdir'
isExist = os.path.exists(dirname)
if isExist:
	print(dirname,'has already existed')
else:
	os.mkdir(dirname)
	print("Success to create a dirname")
isExist = os.path.exists(multipledirname)
if isExist:
	print(multipledirname,'has already existed')
else:
	os.mkdir(multipledirname)
	print("Success to create a multipledirname")