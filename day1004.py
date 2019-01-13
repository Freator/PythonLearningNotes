# -*- coding:utf-8 -*-

# 第一个爬虫代码
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read())
print(bsObj.h1)
print('----------------------------')
print(bsObj.body)
print('----------------------------')
print(bsObj)
'''

#改进后的爬虫代码
'''
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPEror as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read())
		title = bsObj.body.h1
	except AttributeError as e:
		return None
	return title
title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
	print("Title could not be found")
else:
	print(title)
'''
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)
nameList = bsObj.findAll('span',{'class':'green'})
for name in nameList:
	print(name)