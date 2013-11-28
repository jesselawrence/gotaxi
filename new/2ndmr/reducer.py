#!/usr/bin/env python
#-*- coding:utf-8 -*-


import sys 

data = sys.stdin

pre = ''

for i in data:
    try:
        i = i.strip()
        i = i.split()
        road_id = i[0]
        weekday = i[1]
        hour = i[2]
        minute = i[3]
        state = i[4]
        if pre == '':
            if state == '0':
                num = 1
                pre = i
                continue
            else :
                continue
        if pre != '':
            if i == pre:
                num += 1
                continue
            if i != pre:
                if state == '1':
                    print "%s %s %s %s %s" % (pre[0], pre[1], pre[2], pre[3], num)
                    num = 1
                    pre = ''
                    continue
                if state == '0':
                    print "%s %s %s %s %s" % (pre[0], pre[1], pre[2], pre[3], num)
                    num = 1
                    pre = i
                    continue
    except:
        pass

if pre != '':
    print "%s %s %s %s %s" % (pre[0], pre[1], pre[2], pre[3], num)
