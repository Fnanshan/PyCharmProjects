print('----------------------sqlite-----------------')

# # 练习
# # 编写函数，在Sqlite中根据分数段查找指定的名字：
#
# import os, sqlite3
#
# db_file = os.path.join(os.path.dirname(__file__), 'test.db')
# if os.path.isfile(db_file):
#     os.remove(db_file)
#
# # init data
# # 如果文件不存在，会自动在当前目录创建:
# conn = sqlite3.connect(db_file)
# cursor = conn.cursor()
# cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
# cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
# cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
# cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
# # close保证资源不会泄露
# cursor.close()
# conn.commit()
# conn.close()
#
#
# def get_score_in(low, high):
#     # ' 返回指定分数区间的名字，按分数从低到高排序 '
#     try:
#         # 如果文件不存在，会自动在当前目录创建:
#         conn = sqlite3.connect(db_file)
#         cursor = conn.cursor()
#     except sqlite3.DatabaseError as err:
#         print(err)
#     else:
#         # 数据库默认升序，降序使用desc
#         cursor.execute(r"select name from user where score BETWEEN ? and ? order by score", (low, high))
#         # Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果;
#         # Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录
#         values = cursor.fetchall()
#         values = list(map(lambda x: x[0], values))
#         cursor.close()
#         return values
#     finally:
#         conn.close()
#
#
# # 测试:
# assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
# assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
# assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)
#
# print('Pass')

print('----------------------mysql---------------')

# import mysql.connector
#
# conn = mysql.connector.connect(user='root', password='root', database='test')
# cursor = conn.cursor()
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# # mysql的占位符是%s
# cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
# print(cursor.rowcount)
# # 执行insert等操作后要commit()
# conn.commit()
# cursor.close()
#
# # 运行查询
# cursor = conn.cursor()
# cursor.execute('select * from user where id = %s', ('1',))
# values = cursor.fetchall()
# print(values)
#
# cursor.close()
# conn.close()

print('-----------------------sqlAlchemy------------')

from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()


# 定义User对象
class User(Base):
    # 表的名字
    __tablename__ = 'user'

    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# create_engine() :初始化数据库连接
connectInfo = 'mysql+mysqlconnector://root:root@localhost:3306/test'    # '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine(connectInfo)
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

# 业务操作-增
# 创建session对象；DBSession对象可视为当前数据库连接
session = DBSession()
# 创建新User对象
new_user = User(id='5', name='Bob')
# 添加到session
session.add(new_user)
# 提交即保存到database，然后关闭
session.commit()
session.close()

# 业务操作-查
# 创建session
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，调用欧冠all()则返回所有行
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性
print('type :', type(user))
print('name :', user.name)
# 查询操作不需要session.commit()
session.close()

print('# 两个对象之间一对多关系：一个User拥有多个Book')


class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多
    books = relationship('Book')


class Book(Base):
    __table__ = 'book'

    id = Column(String(20), primary_key=True)
    name =Column(String(20))
    # ‘多’的一方的book表示通过外键关联到user表的
    user_id = Column(String(20), ForeignKey('user.id'))