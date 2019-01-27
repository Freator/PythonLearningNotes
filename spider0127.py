# -*- coding:utf-8 -*-
''' ######非自定义请求头
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
'''

# ####自定义请求头Header格式

import urllib.request
url = 'https://movie.douban.com/'
# 自定义 headers
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
			'Referer': 'https://movie.douban.com/',
			'Connection': 'keep-alive'}
# 设置请求头
req = urllib.request.Request(url, headers=headers)
# 打开 req
html = urllib.request.urlopen(req).read().decode('utf8')
# 写入文件
f = open ('html.txt', 'w', encoding='utf-8')
f.write(html)
f.close()
print("Write OK")