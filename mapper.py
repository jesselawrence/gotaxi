#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys

from math import sin as sin
from math import cos as cos
from math import acos as acos

#GPS Distance calculate
def disGps(x1,y1,x2,y2):
    pi = 3.1415
    R = 6371.004
    c = sin(y1)*sin(y2)*cos(x1-x2)+cos(y1)*cos(y2)
    result = R * acos(c) * pi / 180
    return result


#di
di = 0.0008


#基础时间
timebase = 2.01211e+13
#datainput
data = sys.stdin

#路段数据输入
try :
    type(eval('roadList'))
except:
    a = open('road1.txt','r')
    #生成路段列表
    roadList = list()

    for i in a:
        i = i.strip()
        i = eval(i)
        roadList.append(i)

    a.close()
else :
    temp = 1    

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
    minid = []
    
    mid = len(roadList)/2
    x1 = x + di
    x2 = x - di
    y1 = y + di
    y2 = y - di
    p1 = 0
    p2 = len(roadList)
    
    while (roadList[p1][1] < x1):
        mid = (p1 + p2) / 2
        if roadList[mid][1] < x2:
            p1 = mid
        else:
            break
    

    for k in roadList:
        if (x1 >= k[1]):
            if (x2 <= k[3]):
                if (y1 >= k[2]): 
                    if (y2 <= k[4]):
                        minid.append(int(k[0]))   
    temp_min = 9999
    if len(minid) > 0:
        temp_minid = minid[0]
        for k in minid:
            temp = disGps(x, y, roadList[k-1][5], roadList[k-1][6])
            if temp < temp_min:
                temp_min = temp
                temp_minid = k
    else:
        temp_minid = 0

    if (car.has_key(i[0])) :
        if car[i[0]].count([timec, temp_minid,i[2]]) == 0 :
            car[i[0]].append([timec, temp_minid, i[2]])        #判断是否有重复计算的情况
            print '%s %s %s' % (timec, temp_minid, i[2])
        else :
            continue

    else :
        car[i[0]]=list([timec,temp_minid,i[2]])
        print '%s %s %s' % (timec, temp_minid, i[2])


