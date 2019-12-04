import sqlite3

class SQLHelper():
    def __init__(self):
        self.conn=sqlite3.connect('1.db')

    def insert(self,sql):
        print("inset",sql)
        c=self.conn.cursor()
        c.execute(sql)
        self.conn.commit()

    def select(self,sql):
        print("select",sql)
        c=self.conn.cursor()
        cursor=c.execute(sql)
        result=[]
        for row in cursor:
            result.append(row)
        return result

    def update(self,sql):
        c = self.conn.cursor()
        c.execute(sql)
        self.conn.commit()

    def delete(self,sql):
        c = self.conn.cursor()
        c.execute(sql)
        self.conn.commit()

    def __del__(self):
        self.conn.close()


if __name__ == '__main__':
    sqlHelper=SQLHelper()
    result=sqlHelper.select("""SELECT id,name,password from USER""")
    print(result)