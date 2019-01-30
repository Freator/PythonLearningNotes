# -*- coding:utf-8 -*-
# CSV数据的写入和读取
# 逗号分隔值(Comma-Separated Values，CSV，有时也称为字符分隔值，
# 因为分隔字符也可以不是逗号)，其文件以纯文本形式存储表格数据(数字和文本)
# Python自带CSV模块，可以直接import
import csv

'''
# 数据写入CSV
# 如若存在文件则打开CSV文件，如果不存在，则新建文件
# 如果不设置newline=''，则每行数据会隔一行空白
csvfile = open('csvtest.csv', 'w', newline='')
# 将文件加载到csv对象中
write = csv.writer(csvfile)
# 写入一行数据
write.writerow(['Name', 'Age', 'PhoneNumber'])
# 多行写入
data = [('Tang', '21', '12345678901'),
		('Zeng', '20', '12323453456')]
write.writerows(data)
# 关闭csv对象
csvfile.close()
'''

'''
# 读取CSV文件(全部数据)
# 读取函数有两种：reader 和 DictReader
# 两者都是接受可迭代的对象，reader函数返回列表，
# 另一个函数返回字典（值为单元格的值，键是单元格的标题，列头）
csvfile = open('csvtest.csv', 'r')

# 方法1：以列表形式输出
reader = csv.reader(csvfile)
rows1 = [row1 for row1 in reader]
print(rows1)

# 方法2：以字典形式输出，第一行作为字典的键
readerDict = csv.DictReader(csvfile)
rows2 = [row2 for row2 in readerDict]
print(rows2)

# ！！！注意，以上两种方法同时使用时，会有一些小错误，同时出现时，第一个方法执行输出的结果是正确的
#       第二个方法输出为空，这是因为csvfile第一次迭代后迭代指针已经指向了文末。
# 方法2：简单粗暴解决上述问题
new_csvfile = open('csvtest.csv', 'r')
new_readerDict = csv.DictReader(new_csvfile)
new_rows2 = [new_row2 for new_row2 in new_readerDict]
print(new_rows2)
'''


# 读取文件中部分数据（某行数据）
csvfile = open('csvtest.csv', 'r')
'''
# 以列表形式输出
reader = csv.reader(csvfile)
for row in reader:
	if 'Zeng' in row:
		print(row)

'''
# 以字典形式输出，第一行作为字典的键
reader = csv.DictReader(csvfile)
for row in reader:
	if row['Name'] == 'Zeng':
		print(row)
