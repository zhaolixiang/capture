from server import SQLHelper, UserHoursSQL
import sys

def read_csv(file='task9_in.csv'):
    sql_helper=SQLHelper()
    user_hours_sql=UserHoursSQL(sql_helper)
    user_hours_sql.user_hours_init()
    with open(file) as csvfile:
        for line in csvfile:
            name,date,time,model=line.split(',')
            model=model.strip()
            user_hours_sql.insert(name, date+" "+time, model,'')

if __name__ == '__main__':
    read_csv(sys.argv[1])