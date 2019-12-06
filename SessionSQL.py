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
                                   imagic        CHAR(50),
                                   logout INTEGER 
                                   
                                   );'''
                      )
            self.sql_helper.conn.commit()

        except Exception as e:
            pass

    def insert(self,  name, imagic):
        sql = """INSERT INTO SESSION (username ,imagic,logout) VALUES ("{}","{}",0)""".format(name, imagic)
        self.sql_helper.insert(sql)

    def get_one(self,imagic):
        # 获取单个
        sql = 'select * from SESSION where imagic="{}" and logout=0 order by id desc'.format(imagic)
        row=self.sql_helper.select(sql)
        if not row:
            return None
        item= row[0]
        return{
            "id":item[0],
            "username":item[1],
            "imagic":item[2],
        }

    def delete(self,imagic):
        sql="""update  SESSION set logout=1 where imagic='{}'""".format(imagic)
        self.sql_helper.delete(sql)

    def get_all(self):
        # 获取多个
        pass
