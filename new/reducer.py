#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
import taxi
import road

data = sys.stdin

b = []

if __name__ == '__main__':
    for i in data:
        a = taxi.gpsRecord(i,road.road_index,road.road_data)
        b.append(a)
        #a.display_full()
        print a.candiate

