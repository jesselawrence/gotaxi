#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys

#基础时间
timebase = 2.01211e+13

#标志位 是否进行路段输入
flag = 0

if flag == 0:
    #路段数据输入
    a = open('road.txt','r')
    #生成路段列表
    roadList = list()

    for i in a:
        i = i.strip()
        i = eval(i)
        roadList.append(i)

data = sys.stdin

car = {}

for i in data:
    try:
        i = i.strip()
        i = i.split(',')
    except:
        continue
    try:
        i[2] = eval(i[2])
        i[3] = eval(i[3])
        i[4] = eval(i[4])
        i[5] = eval(i[5])
        i[3] = i[3] % timebase / 100
        if i[2] != 0:
            i[2] = 1
    except:
        continue
    if i[4] == 0 or i[5] == 0:
        continue
    x = i[4]
    y = i[5]
    timec = int(i[3])
    minid = 0
    for k in roadList:
        if ((x - 0.0031) <= k[1] and (x + 0.0031) >= k[3] and (y - 0.0031) <= k[2] and (y + 0.0031) >= k[4]):
            minid = int(k[0])
            break

    if (car.has_key(i[0])) :
        if car[i[0]].count([timec, minid,i[2]]) == 0:
            car[i[0]].append([timec, minid, i[2]])        #判断是否有重复计算的情况
            print '%s %s %s' % (timec, minid, i[2])
        else :
            continue

    else :
        car[i[0]]=list([timec,minid,i[2]])
        print '%s %s %s' % (timec, minid, i[2])


