"""创建第四个名为task9_in.py的python程序（独立于web应用程序），
该程序能够读取图4所示表单的CSV文件，
并更新数据库以反映指定的用户计数会话。"""
import os
from itertools import groupby
from operator import itemgetter

from SQLHelper import SQLHelper
from UserHoursSQL import UserHoursSQL


def read_csv(file='task9_in.csv'):
    sql_helper=SQLHelper()
    user_hours_sql=UserHoursSQL(sql_helper)
    user_hours_sql.user_hours_init()
    lists=[]
    with open(file) as csvfile:
        for line in csvfile:
            name,date,time,model=line.split(',')
            model=model.strip()
            # lists.append({
            #     'name':name,
            #     'date':date+" "+time,
            #     'model':model
            # })
            user_hours_sql.insert(name, date+" "+time, model)
    # lists.sort(key=itemgetter('name'))
    # for name,items in groupby(lists,itemgetter('name')):
    #     items=[i for i in items]
    #     for i in range(0,len(items),2):
    #         print(items[i])
    #         print(items[i+1])
    #         if items[i]['model']=='login' and items[i+1]['model']=='logout':
    #             user_hours_sql.insert(name, items[i]['date'],items[i+1]['date'])

    #user_hours_sql.insert(name,date+" "+time,model)

if __name__ == '__main__':
    # file=os.path.join(os.getcwd(),'task9_in.csv')
    read_csv()