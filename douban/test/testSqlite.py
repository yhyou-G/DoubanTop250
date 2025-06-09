# coding=utf-8
# @author: yyh
# time on: 2020/10/28 23:37

import sqlite3

# 1.连接数据库
# conn = sqlite3.connect('test.db')#打开或创建数据库文件
# print('opened database successfully')


# 2.建表
# c = conn.cursor()   #获取游标
# sql = '''
#     create table employee
#     (id int primary key not null,
#     name text not null,
#     age int not null,
#     address char(50),
#     salary real);
# '''
# c.execute(sql)      #执行sql语句
# conn.commit()       #提交数据库操作
# conn.close()        #关闭数据库连接
# print('create table successfully')


# 3.插入数据
# conn = sqlite3.connect('test.db')
# c = conn.cursor()
# sql1= '''
#     insert into employee(id,name,age,address,salary)
#     values (1,'jack',20,'北京',10000)
# '''
#
# sql2 = '''
#     insert into employee(id,name,age,address,salary)
#     values (2,'Amy',21,'福建',8000)
# '''
# c.execute(sql1)
# c.execute(sql2)
# conn.commit()
# conn.close()
# print('insert successfully')


# 4.查询数据
conn = sqlite3.connect('test.db')
c = conn.cursor()
sql = "select * from employee"
cursor = c.execute(sql)
for row in cursor:
    print('id=', row[0])
    print('name=', row[1])
    print('age=', row[2])
    print('address=', row[3])
    print('salary=', row[4])
    print()
