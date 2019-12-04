import hashlib


class UserSQL:
    def __init__(self, sql_helper):
        self.sql_helper = sql_helper
        self.user_init()

    def user_init(self):
        # 用户表信息初始化
        # 创建用户表
        try:
            c = self.sql_helper.conn.cursor()
            c.execute('''CREATE TABLE USER 
                                   (
                                   id integer PRIMARY KEY autoincrement,
                                   username            CHAR(50)   NOT NULL,
                                   password        CHAR(50)
                                   );'''
                      )
            self.sql_helper.conn.commit()
            # 创建10个初始化用户
            for i in range(1, 11):
                lines = ('password{}'.format(i)).encode('utf-8')
                magic = hashlib.md5(lines).hexdigest()
                self.insert('test{}'.format(i), magic)
        except Exception as e:
            pass

    def insert(self,  name, password):
        sql = """INSERT INTO USER (username ,password) VALUES ("{}","{}")""".format(name, password)
        self.sql_helper.insert(sql)

    def get_one(self,username):
        # 获取单个
        sql = 'select * from USER where username="{}"'.format(username)
        row = self.sql_helper.select(sql)
        if not row:
            return None
        item= row[0]
        return{
            "id":item[0],
            "username":item[1],
            "password":item[2],
        }

    def get_all(self):
        # 获取多个
        pass
