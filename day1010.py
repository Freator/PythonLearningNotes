# -*- coding:utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import datetime

#html = urlopen("http://en.wikipedia.org//wiki//Kevin_Bacon")
random.seed(datetime.datetime.now())
def getLinks(articleUrl):
	html = urlopen("https://en.wikipedia.org" + articleUrl)
	bsObj = BeautifulSoup(html)
	return bsObj.find("div",{"id" : "bodyContent"}).findAll("a",href = re.compile("^(/wiki/)((?!:).)*$"))
links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
	newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
	print(newArticle)
	links = getLinks(newArticle)