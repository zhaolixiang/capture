"""
Create a program (separate from the web app) called task8_out.py
that is able to query the database and indicated the number of each type of vehicle
and occupancy at each location during a period specified by a start date and time
and an end date and time. Invalid dates and times should be intentionally rejected.
The output should be delivered as a csv file with a row per
location with the format as described in Figure 1.
创建一个名为task8_out.py的程序（与web应用程序分开），该程序能够查询数据库，
并指示在由开始日期和时间以及结束日期和时间指定的期间内，每种类型的车辆的数量和每个位置的占用率。
无效的日期和时间应被故意拒绝。输出应该以csv文件的形式交付，每个位置有一行，格式如图1所示。
"""
import datetime
from operator import itemgetter

from OccupancySQL import OccupancySQL
from SQLHelper import SQLHelper


def write_csv(start,end,file='task8_out.csv'):
    """dete为指定的日期时间，形如：%d/%m/%Y"""
    select_start=datetime.datetime.strptime(start,'%d/%m/%Y %H%M')
    select_end=datetime.datetime.strptime(end,'%d/%m/%Y %H%M')
    sql_helper=SQLHelper()
    occupancy_sql = OccupancySQL(sql_helper)
    result=occupancy_sql.get_all()
    # result.sort(key=itemgetter('name'))
    content=[]
    for i in result:
        content.append("{},{},{},{},{},{}\n".format(i['location'],i['type'],i['occ1'],i['occ2'],i['occ3'],i['occ4']))
    # for name,items in groupby(result,key=itemgetter('name')):
    #     print(">>"+name+"<<")
    #     items=[i for i in items]
    #     new_items=[]
    #     before=None
    #     for i in items:
    #         if before and before['model']=='login' and i['model']=='logout':
    #             item={
    #                 'start_date':before['date'],
    #                 'end_date':i['date']
    #             }
    #             new_items.append(item)
    #         else:
    #             before=i
    #     items=new_items
    #     # day:是给定数据上的小时数，小数点后一位四舍五入。
    #     # for i in items:
    #     #     print(datetime.datetime.strftime(i['start_date'],'%d/%m/%Y'))
    #     # 当天的时间
    #     day_lists=[i for i in items if datetime.datetime.strftime(i['start_date'],'%d/%m/%Y')==datetime.datetime.strftime(select,'%d/%m/%Y')]
    #     # 当前往前再加6天的时间
    #     day_before_6=select-datetime.timedelta(days=6)
    #     day_after_1=select+datetime.timedelta(days=1)
    #     week_lists=[i for i in items if day_before_6<i['start_date']<day_after_1]
    #     # 上个月
    #     day_before_month=select-datetime.timedelta(days=getMonths(select)-select.day)
    #
    #     month_lists=[i for i in items if day_before_month<i['start_date']<day_after_1]
    #
    #     day=0
    #     for d in day_lists:
    #         day+=(d['end_date']-d['start_date']).total_seconds()
    #     day=round(day/3600,1)
    #
    #     week=0
    #     for w in week_lists:
    #         week+=(w['end_date']-w['start_date']).total_seconds()
    #     week = round(week / 3600, 1)
    #
    #     month = 0
    #     for m in month_lists:
    #         month += (m['end_date'] - m['start_date']).total_seconds()
    #     month = round(month / 3600, 1)
    #
    #     content.append("{},{},{},{}{}".format(name,day,week,month,'\n'))

    with open(file,'w') as f:
        f.writelines(content)





    # with open(file) as csvfile:
    #     for line in csvfile:
    #         name,date,time,model=line.split(',')
    #         model=model.strip()
    #         user_hours_sql.insert(name,date+" "+time,model)

if __name__ == '__main__':
    # file=os.path.join(os.getcwd(),'task9_in.csv')
    write_csv('1/6/2019 1010','1/6/2020 1010')