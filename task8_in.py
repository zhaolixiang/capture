import sys

from server import SQLHelper, OccupancySQL


def read_csv(file='task8_in.csv'):
    sql_helper = SQLHelper()
    occupancy_sql = OccupancySQL(sql_helper)
    with open(file) as csvfile:
        for line in csvfile:
            date, time, session, model, location, type, occ = line.split(',')
            occ = occ.strip()
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
                                 date=date + " " + time,
                                 session=session,
                                 imagic='',
                                 username=''
                                 )


if __name__ == '__main__':
    read_csv(file=sys.argv[1])
