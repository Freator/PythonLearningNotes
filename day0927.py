# -*- coding:utf-8 -*-
#统计天龙八部小说中人物出现的次数

import jieba

excludes = {"说道","自己","一个","什么","不是",
			"武功","甚么","一声","咱们","不知",
			"师父","心中","知道","出来","如何",
			"姑娘","他们","便是","突然","如此",
			"之中","只见","不能","大理","丐帮",
			"只是","不敢","弟子"}
txt = open("天龙八部.txt","r",encoding = 'utf-8').read()
words = jieba.lcut(txt)
counts = {}
for word in words:
	if len(word) != 1:
		counts[word] = counts.get(word,0) + 1
'''
for word in excludes:
	del(counts[word])
'''
listitem = list(counts.items())
listitem.sort(key = lambda x : x[1],reverse = True)
#print("{0:<10}{1:>8}".format("人物","出场次数"))
	word, count = listitem[i]
	print("{0:-<10}{1:->10}".format(word,count))