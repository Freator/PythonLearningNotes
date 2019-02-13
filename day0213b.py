# -*- coding:utf8 -*-
# 此代码承接代码文件<day0213.py>，并注意此代码文件不能直接运行，需要和day0213文件相衔接后才能正确运行。
# 对已建立的数据表进行表操作
# 连接数据库
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:root@localhost:3306/test?charset=gbk", 
						echo=True)

# 首先需要创建一个会话session
# 生成对话之后，就可以对已有的数据表进行增删改查
from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker(bind=engine)
session = DBSession()

# 添加数据
new_data = mytable(name='Li Lei', age=10, birth='2019-02-13', class_name='一年级一班')
session.add(new_data)
session.commit()
session.close()  # 注意这两个的顺序，一定是先commit 再close

# 使用update方法更新数据(建议使用update更新)
# 这里注意filter和filter_by的区别
session.query(mytable).filter_by(id=1).update({mytable.age : 12})
session.commit()
session.close()

# 使用赋值的方法更新
get_data = session.query(mytable).filter_by(id=1).first()
get_data.class_name = '三年级三班'
session.commit()
session.close()

# 查询数据
# 通用的查询函数是 session.query(表名),这就相当于 select * from 表名,all()方法是
# 将查询到的数据以列表的形式返回
get_data = session.query(myclass).all()
# 查找某个字段数据： get_data = session.query(myclass.name, myclass.class_name).all()
# 输出
for i in get_data:
	print('Name: ' + i.name)
	print('Class: ' + i.class_name)
session.close()

# 另外还有条件查找，相当于SQL语句中的where子句，方法多样

# 若涉及多表查询（内连接查询或者外连接查询），可以再加上 join 和 outerjoin函数
# 内连接，当然输出语句另写
get_data = session.query(mytable).join(myclass).filter(mytable.class_name == '三年级三班').all()
# 同样外连接语句
get_data = session.query(mytable).outerjoin(myclass).filter(mytable.class_name == '三年级三班').all()


# 一般来说，涉及复杂的查询语句，SQLAlchemy可以直接执行SQL语句
sql = 'select * from myclass'
session.excute(sql)
# 如果涉及更新或者添加数据，就要加上commit
session.commit()
session.close()



