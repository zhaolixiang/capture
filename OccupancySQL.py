from ForTime import task9_in_time


class OccupancySQL:
    def __init__(self, sql_helper):
        self.sql_helper = sql_helper
        self.user_hours_init()

    def user_hours_init(self):
        # 信息初始化
        #
        c = self.sql_helper.conn.cursor()
        # model=add
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
                                           session     text
                                           );'''
                  )
        self.sql_helper.conn.commit()

    def insert(self, model,location,type,occ1,occ2,occ3,occ4,date,session):
        sql = """INSERT INTO OCCUPANCY (model,location,type,occ1,occ2,occ3,occ4,date,session) 
VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}")""".format(
            model, location, type, occ1,occ2,occ3,occ4,date,session)
        return self.sql_helper.insert(sql)

    # def update(self,model,location,type,occ1,occ2,occ3,occ4,delete_date):
    #     sql="update OCCUPANCY set is_delete = '1',delete_date='{}' where model = '{}' " \
    #         "and location='{}' and type='{}' and occ1='{}' and occ2='{}' and occ3='{}' and occ4='{}'"\
    #         .format(delete_date,model,location,type,occ1,occ2,occ3,occ4)
    #     return self.sql_helper.update(sql)

    def get_one(self,model,location,type,occ):
        # 获取单个
        pass
        # sql = 'select * from OCCUPANCY where model="{}" and location="{}" and type="{}" and occ="{}"'\
        #     .format(model,location,type,occ)
        # row = self.sql_helper.select(sql)
        # if not row:
        #     return None
        # item = row[0]
        # return {
        #     "id": item[0],
        #     "username": item[1],
        #     "password": item[2],
        # }

    def get_count_from_type(self,type):
        result=self.sql_helper.select("select * from OCCUPANCY where type='{}'".format(type))
        print("指定type数量",type,len(result))
        return len(result)
    def get_all(self):
        # 获取多个
        lins=self.sql_helper.select("""select * from OCCUPANCY""")
        result=[]
        for item in lins:
            son={
                "id":item[0],
                "model":item[1],
                "location":item[2],
                "type":item[3],
                "occ1":item[4],
                "occ2":item[5],
                "occ3":item[6],
                "occ4":item[7],
                "date":item[8],
                "session":item[9],
            }
            result.append(son)
        return result



