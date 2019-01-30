# -*- coding:utf-8 -*-
# CSV数据的写入和读取
# 逗号分隔值(Comma-Separated Values，CSV，有时也称为字符分隔值，
# 因为分隔字符也可以不是逗号)，其文件以纯文本形式存储表格数据(数字和文本)
# Python自带CSV模块，可以直接import
import csv

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