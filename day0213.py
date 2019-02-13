# -*- coding:utf8 -*-
# ORM框架（对MySQL的连接和操作）
# 注意应先在电脑端安装好MySQL并打开服务器连接端口（默认3306）

# 连接数据库
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:root@localhost:3306/test?charset=gbk", 
						echo=True)   # 注意这里的字符集，一般用utf8，但已有的test数据集是gbk,故先用gbk
# 创建数据表方法之一
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class mytable(Base):
	# 表名
	__tablename__ = 'mytable'
	# 字段和属性
	id = Column(Integer, primary_key=True)
	name = Column(String(50), unique=True)
	age = Column(Integer)
	birth = Column(DateTime)
	class_name = Column(String(50))
	
Base.metadata.create_all(engine)

# 创建数据表方法之二
from sqlalchemy import Column, MetaData, ForeignKey, Table
from sqlalchemy.dialects.mysql import (INTEGER, CHAR)
meta = MetaData()
myclass = Table('myclass', meta, 
				Column('id', INTEGER, primary_key=True), 
				Column('name', CHAR(50), ForeignKey(mytable.name)), 
				Column('class_name', CHAR(50))
				)
myclass.create(bind=engine)

# 删除数据表
# myclass.drop(bind=engine)
# Base.metadata.drop_all(engine)