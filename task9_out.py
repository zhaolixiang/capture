"""该程序能够查询数据库并指示每个用户参与计数的总小时数，以便确定工资。
它应允许提供一个日期，并提供该日期、该日期结束的一周和该日期结束的上一个月的总数。
输出应该以csv文件的形式传递
User
Day 是给定数据上的小时数，小数点后一位四舍五入。
Week 是包括日期在内的前一周的小时数，小数点后一位四舍五入。
Month 是上个月的小时数，包括小数点后一位四舍五入的日期。
一个月指上一个月的同一天，但不包括同一天。
"""
import datetime
from itertools import groupby
from operator import itemgetter

from ForTime import getMonths
from SQLHelper import SQLHelper
from UserHoursSQL import UserHoursSQL


def write_csv(date,file='task9_out.csv'):
    """dete为指定的日期时间，形如：%d/%m/%Y"""
    select=datetime.datetime.strptime(date,'%d/%m/%Y')
    sql_helper=SQLHelper()
    user_hours_sql=UserHoursSQL(sql_helper)
    result=user_hours_sql.get_all()
    result.sort(key=itemgetter('name'))
    content=[]
    for name,items in groupby(result,key=itemgetter('name')):
        print(">>"+name+"<<")
        items=[i for i in items]
        new_items=[]
        before=None
        for i in items:
            if before and before['model']=='login' and i['model']=='logout':
                item={
                    'start_date':before['date'],
                    'end_date':i['date']
                }
                new_items.append(item)
            else:
                before=i
        items=new_items
        # day:是给定数据上的小时数，小数点后一位四舍五入。
        # for i in items:
        #     print(datetime.datetime.strftime(i['start_date'],'%d/%m/%Y'))
        # 当天的时间
        day_lists=[i for i in items if datetime.datetime.strftime(i['start_date'],'%d/%m/%Y')==datetime.datetime.strftime(select,'%d/%m/%Y')]
        # 当前往前再加6天的时间
        day_before_6=select-datetime.timedelta(days=6)
        day_after_1=select+datetime.timedelta(days=1)
        week_lists=[i for i in items if day_before_6<i['start_date']<day_after_1]
        # 上个月
        day_before_month=select-datetime.timedelta(days=getMonths(select)-select.day)

        month_lists=[i for i in items if day_before_month<i['start_date']<day_after_1]

        day=0
        for d in day_lists:
            day+=(d['end_date']-d['start_date']).total_seconds()
        day=round(day/3600,1)

        week=0
        for w in week_lists:
            week+=(w['end_date']-w['start_date']).total_seconds()
        week = round(week / 3600, 1)

        month = 0
        for m in month_lists:
            month += (m['end_date'] - m['start_date']).total_seconds()
        month = round(month / 3600, 1)

        content.append("{},{},{},{}{}".format(name,day,week,month,'\n'))

    with open(file,'w') as f:
        f.writelines(content)





    # with open(file) as csvfile:
    #     for line in csvfile:
    #         name,date,time,model=line.split(',')
    #         model=model.strip()
    #         user_hours_sql.insert(name,date+" "+time,model)

if __name__ == '__main__':
    # file=os.path.join(os.getcwd(),'task9_in.csv')
    write_csv('1/6/2019')