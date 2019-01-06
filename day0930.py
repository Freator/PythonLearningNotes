# -*- coding:utf-8 -*-
f = open("mytest0930.txt",'w+')
strlist = ['abc','edf','ghi']
f.writelines(strlist)
print("Present location pointer:",f.tell())
f.seek(0)
print("Present location pointer:",f.tell())
fc = f.read(2)
print("fc = ",fc)
print("Present location pointer:",f.tell())