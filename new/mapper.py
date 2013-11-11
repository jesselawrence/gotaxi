#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys

gps_data = sys.stdin

for i in gps_data:
    try:
        i = i.strip()
        i = i.split(',')
        temp = eval(i[4])
        if temp == 0:
            continue
        swap_temp = i[1] 
        i[1] = i[3]
        i[3] = swap_temp
    except:
        continue
    print "%s,%s,%s,%s,%s,%s,%s,%s,%s" % (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
