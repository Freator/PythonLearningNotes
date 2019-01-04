# -*- coding:utf-8 -*-
try:
	#fh = open('testfile.txt','w')
	#fh.write("This is a test file to test a IOError\n")
	#fh.write("This is used to test file operation!")
	f = open('testfile.txt','r')
	fcontent = f.read()
	print(fcontent)
	f.seek(0)
	flines = f.readlines()
	f.seek(3)
	
	fcon = f.read(9)
	#print(flines)
	for oneline in flines:
		print(oneline)
	print(fcon)
except IOError:
	print("Error:No file or failed to access file")
finally:
	#print("The contents are successful to write in the file")
	#print("Done")
	#fh.close()
	f.close()