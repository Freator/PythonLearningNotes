# -*- coding:utf-8 -*-
# 导入urllib库
import urllib.request
# 打开 URL
response = urllib.request.urlopen('https://movie.douban.com/', None, 2)
# 读取返回内容
html = response.read().decode('utf-8')
# 写入txt文件中
f = open('html.txt', 'w', encoding='utf8')
f.write(html)
f.close()
print("File write, OK!")