#!/usr/bin/env python
import sys
data = sys.stdin

for i in data:
    i = i.strip()
    i = i.split(',')
    leni = len(i)
    if leni != 9: #or eval(i[4]) < 115.375 or eval(i[5]) < 39.416 or eval(i[4] > 117.5 or eval(i[5] > 41.08333)):
        pass
    else :
        if i[4] == '0.0' or i[5] == '0.0':
            pass
        else:
            print "%s,%s,%s,%s,%s,%s,%s,%s,%s" % (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
