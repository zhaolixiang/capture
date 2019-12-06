# 测试使用
import hashlib

from server import SQLHelper

sql_helper=SQLHelper()
c = sql_helper.conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS OCCUPANCY
                                           (
                                           id integer PRIMARY KEY autoincrement,
                                           model        text,
                                           location        text,
                                           type        text,
                                           occ1        text,
                                           occ2        text,
                                           occ3        text,
                                           occ4        text,
                                           date        text,
                                           session     text,
                                            imagic    text,
                                            username    text
                                           );'''
                  )
sql_helper.conn.commit()
c = sql_helper.conn.cursor()
c.execute('''CREATE TABLE SESSION 
                                   (
                                   id integer PRIMARY KEY autoincrement,
                                   username            CHAR(50)   NOT NULL,
                                   imagic        CHAR(50),
                                   logout INTEGER 

                                   );'''
                      )
sql_helper.conn.commit()

c = sql_helper.conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS USERHOURS
                                           (
                                           id integer PRIMARY KEY autoincrement,
                                           name           CHAR(50)    NOT NULL,
                                           date        text,
                                           model        text,
                                           imagic    text
                                           );'''
                  )
sql_helper.conn.commit()
c = sql_helper.conn.cursor()
c.execute('''CREATE TABLE USER 
                                  (
                                  id integer PRIMARY KEY autoincrement,
                                  username            CHAR(50)   NOT NULL,
                                  password        CHAR(50)
                                  );'''
          )
sql_helper.conn.commit()


def insert(sql_helper, name, password):
    sql = """INSERT INTO USER (username ,password) VALUES ("{}","{}")""".format(name, password)
    sql_helper.insert(sql)

# 创建10个初始化用户
for i in range(1, 11):
    lines = ('password{}'.format(i)).encode('utf-8')
    magic = hashlib.md5(lines).hexdigest()
    insert(sql_helper,'test{}'.format(i), magic)