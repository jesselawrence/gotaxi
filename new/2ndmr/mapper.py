#!/usr/bin/env python
#-*- coding:utf-8 -*-


import sys
import datetime

data = sys.stdin

for i in data:
    try:
        i = i.strip()
        i = i.split()
        road_id = i[0]
        car_time = i[1]
        car_state = i[3]
        if car_state == '0':
            pass
        else:
            car_state = '1'
        year = car_time[0:4]
        month = car_time[4:6]
        day = car_time[6:8]
        hour = car_time[8:10]
        minute = car_time[10:12]
        temp = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute))
        weekday = temp.weekday()
        print "%s %s %s %s %s" % (road_id, weekday, hour, minute, car_state)
    except:
        pass
