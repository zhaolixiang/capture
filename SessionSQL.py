class SessionSQL:
    def __init__(self, sql_helper):
        self.sql_helper = sql_helper
        self.user_init()

    def user_init(self):
        # 用户表信息初始化
        # 创建用户表
        try:
            c = self.sql_helper.conn.cursor()
            c.execute('''CREATE TABLE SESSION 
                                   (
                                   id integer PRIMARY KEY autoincrement,
                                   username            CHAR(50)   NOT NULL,
                                   imagic        CHAR(50)
                                   );'''
                      )
            self.sql_helper.conn.commit()

        except Exception as e:
            pass

    def insert(self,  name, password):
        sql = """INSERT INTO SESSION (username ,imagic) VALUES ("{}","{}")""".format(name, password)
        self.sql_helper.insert(sql)

    def get_one(self,username):
        # 获取单个
        sql = 'select * from SESSION where username="{}"'.format(username)
        row=self.sql_helper.select(sql)
        if not row:
            return None
        item= row[0]
        return{
            "id":item[0],
            "username":item[1],
            "imagic":item[2],
        }

    def delete(self,username):
        sql="""delete from SESSION where username='{}'""".format(username)
        self.sql_helper.delete(sql)

    def get_all(self):
        # 获取多个
        pass
