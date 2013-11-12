#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
import taxi
import road

data = sys.stdin



if __name__ == '__main__':
    nowid = ''
    for i in data:
        a = taxi.gpsRecord(i,road.road_index,road.road_data)
        
        if nowid = '':
            b = []
            nowid == a.carid
            b.append(a)
            continue

        if a.carid != nowid:
            nowid = a.carid
            lenb = len(b)
            if lenb > 3:
                



            b = []
            
        b.append(a)
        
