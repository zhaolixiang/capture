from ForTime import task9_in_time


class UserHoursSQL:
    def __init__(self, sql_helper):
        self.sql_helper = sql_helper
        self.user_hours_init()

    def user_hours_init(self):
        # 信息初始化
        #
        c = self.sql_helper.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS USERHOURS
                                           (
                                           id integer PRIMARY KEY autoincrement,
                                           name           CHAR(50)    NOT NULL,
                                           date        text,
                                           model        text,
                                           imagic    text
                                           );'''
                  )
        self.sql_helper.conn.commit()

    def insert(self, name, date,model,imagic):
        sql = """INSERT INTO USERHOURS (name,date,model,imagic) VALUES ("{}","{}","{}","{}")""".format(name, date,model,imagic)
        self.sql_helper.insert(sql)

    def get_one(self):
        # 获取单个
        pass

    def get_all(self):
        # 获取多个
        lins=self.sql_helper.select("""select * from USERHOURS""")
        result=[]
        for item in lins:
            son={
                "id":item[0],
                "name":item[1],
                "date":task9_in_time(item[2]),
                "model":item[3],
            }
            result.append(son)
        return result



