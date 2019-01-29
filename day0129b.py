# -*- coding:utf-8 -*-

# 引入 BeautifulSoup
from bs4 import BeautifulSoup
# 读取MySoup.html文件
Open_file = open('MySoup.html', 'r', encoding='utf-8')
# 将MySoup的内容赋值给 Html_Content,并关闭文件
Html_Content = Open_file.read()
Open_file.close()
# 使用html5lib解释器解释 Html_Content的内容
soup = BeautifulSoup(Html_Content, "html5lib")
# 输出title
print('html title is ' + soup.title.getText())
# 查找第一个标签p，并输出
find_p = soup.find('p', id="python")
print('The first <p> is ' + find_p.getText())
# 查找全部p标签，并输出
find_all_p = soup.find_all('p')
for i, k in enumerate(find_all_p):
	print('The ' + str(i + 1) + ' p is ' + k.getText())