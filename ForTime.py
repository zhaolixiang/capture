import calendar
import datetime


def task9_in_time(date):
    # result = datetime.datetime.strptime(str, '%Y-%m-%d %H:%M:%S:%f')
    result = datetime.datetime.strptime(date, '%d/%m/%Y %H%M')
    return result

# 获取上个月天数
def getMonths(d):
    c = calendar.Calendar()
    year = d.year
    month = d.month
    if month == 1:
        month = 12
        year -= 1
    else:
        month -= 1
    months = calendar.monthrange(year, month)[1]
    return months

if __name__ == '__main__':
    print(getMonths(task9_in_time('1/6/2019 1212')))
