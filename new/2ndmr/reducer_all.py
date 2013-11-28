#!/usr/bin/env python
#-*- coding:utf-8 -*-


import sys 

data = sys.stdin

pre = ''

for i in data:
    i = i.strip()
    i = i.split()
    road_id = i[0]
    weekday = i[1]
    hour = i[2]
    minute = i[3]
    state = i[4]
    if pre == '':
        num = 1
        pre = i
        continue
    else :
        if pre[0] == i[0] and pre[1] == i[1] and pre[2] == i[2] and pre[3] == i[3]:
            num += 1
            continue
        else:
            print "%s %s %s %s %s" % (pre[0],pre[1],pre[2],pre[3],num)
            num = 1
            pre = i
            continue


if pre != '':
    print "%s %s %s %s %s" % (pre[0],pre[1],pre[2],pre[3],num)
