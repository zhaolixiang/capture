"""
创建第二个名为task8_in.py的程序（与web应用程序分开），
该程序使用包含图2所示表单条目的csv文件，并更新数据库以包含这些流量观测记录。
运行此任务的第一个程序时，应正确反映更新的记录。
您不需要维护用户/会话的详细信息，这些信息超出了使给定数据库架构可以执行此任务所需的范围。它们不会被提取。
"""

import os
from itertools import groupby
from operator import itemgetter

from OccupancySQL import OccupancySQL
from SQLHelper import SQLHelper
from UserHoursSQL import UserHoursSQL


def read_csv(file='task8_in.csv'):
    sql_helper=SQLHelper()
    occupancy_sql = OccupancySQL(sql_helper)
    lists=[]
    with open(file) as csvfile:
        for line in csvfile:
            date,time,session,model,location,type,occ=line.split(',')
            occ=occ.strip()
            occ1 = '1' if occ == '1' else '0'
            occ2 = '1' if occ == '2' else '0'
            occ3 = '1' if occ == '3' else '0'
            occ4 = '1' if occ == '4' else '0'
            occupancy_sql.insert(model=model,
                             location=location,
                             type=type,
                                 occ1=occ1,
                                 occ2=occ2,
                                 occ3=occ3,
                                 occ4=occ4,
                             date=date+" "+time,
                             session=session,)
            # lists.append({
            #     'name':name,
            #     'date':date+" "+time,
            #     'model':model
            # })
            # user_hours_sql.insert(name, date+" "+time, model)
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