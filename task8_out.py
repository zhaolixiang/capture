import datetime
import sys

from server import SQLHelper, OccupancySQL


def write_csv(start,end,file='task8_out.csv'):
    start=datetime.datetime.strptime(start, '%d/%m/%Y/%H%M')
    end=datetime.datetime.strptime(end, '%d/%m/%Y/%H%M')
    sql_helper=SQLHelper()
    occupancy_sql = OccupancySQL(sql_helper)
    result=occupancy_sql.get_all()
    content=[]
    for i in result:
        if start<datetime.datetime.strptime(i['date'], '%d/%m/%Y %H%M')<end:
            content.append("{},{},{},{},{},{}\n".format(i['location'],i['type'],i['occ1'],i['occ2'],i['occ3'],i['occ4']))
    with open(file,'w') as f:
        f.writelines(content)


if __name__ == '__main__':
    write_csv(sys.argv[1],sys.argv[2])