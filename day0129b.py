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

'''
# 输出title
print('html title is ' + soup.title.getText())
# 查找第一个标签p，并输出
find_p = soup.find('p', id="python")
print('The first <p> is ' + find_p.getText())
# 查找全部p标签，并输出
find_all_p = soup.find_all('p')
for i, k in enumerate(find_all_p):
	print('The ' + str(i + 1) + ' p is ' + k.getText())
'''

'''
# 以下是找某一个标签的方法
# 获取头部信息，返回<head></head>之间的全部内容
print("HEAD = " , soup.head)

# 获取标题信息，返回<title></title>之间的全部内容
print("TITLE = " , soup.title)

# 这是一个获取tag的小窍门，可以在文档树的tag中多次调用这个方法
# 下面的代码可以获取<body>标签中的第一个<b>标签
# 也就是说，soup不一定是整个HTML的内容，可以先定位某个部分，然后用这个简洁的方式获取
# 返回<body>中第一个<b></b>之间的内容
print("FIRST <b> = " , soup.body.b)

# 直接指定标签类别，返回第一个标签的内容。
print("FIRST <a> = " , soup.a)

# 获取所有的这个标签的内容
print("ALL <a> = " , soup.find_all("a"))
'''

# 以下是获取去掉HTML代码的内容的方法
# 通过getText()函数获取标签的值
print("HEAD = " , soup.head.getText()) # 直接返回头部名称值，不含'<head>'等这些信息
# 通过先转换成字符串的形式再截取数据
# 因为soup.head等这样的数据格式类型是 <class 'bs4.element.Tag'>
print("Before use str() : ", type(soup.head))
# 所以要截取中间的字符必须先转换成字符串格式，用函数str()
print("After use str() : ", type(str(soup.head)))