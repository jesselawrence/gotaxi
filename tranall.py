#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import transfer

data = sys.stdin

for i in data:
    try:
        i = i.strip()
        i = i.split(',')
        i[4] = eval(i[4])
        i[5] = eval(i[5])
        [i[4],i[5]] = transfer.transform_earth_2_mars(i[4],i[5])
    except:
        continue
    
    print "%s,%s,%s,%s,%s,%s,%s,%s,%s" % (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
