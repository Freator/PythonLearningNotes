# -*- coding:utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
'''

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
images = bsObj.findAll("img",{"src" : re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
	print(image["src"])
'''
#html = urlopen("http://en.wikipedia.org//wiki//Kevin_Bacon")
html = urlopen("https://baike.baidu.com/item/%E6%9E%97%E6%9B%B4%E6%96%B0/9213807")
bsObj = BeautifulSoup(html)
for link in bsObj.find("div",{"class" : "info"}).findAll("a",
						href = re.compile("^(/item/)")):
	if 'href' in link.attrs:
		print(link.attrs['href'])