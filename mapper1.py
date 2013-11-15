#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
import scipy.io as sio
from math import sin as sin
from math import cos as cos
from math import acos as acos
from math import sqrt as sqrt

def disGps(x1,y1,x2,y2):
    pi = 3.1415
    R = 6371.004
    c = sin(y1)*sin(y2)*cos(x1 - x2) + cos(y1)*cos(y2)
    return (R*acos(c) * pi /180 )

def roadIndex(x,y,rd_index):
    huafen = 0.005
    minx = 115.375
    miny = 39.416667000000075
    numx = 425
    numy = 333
    ax = int((x - minx)/ huafen)
    ay = int((y - miny)/ huafen)
    re_id = ax * numy + ay
    return rd_index[re_id]

def PointToSegDist(x,y,x1,y1,x2,y2):
    cross = (x2 - x1)*(x - x1) + (y2 - y1)*(y - y1)
    if cross <= 0:
        return [x1,y1]
    d2 = (x2 - x1) * (x2 - x1) + (y2 - y1)*(y2 - y1)
    if cross >= d2:
        return [x2,y2]
    r = cross / d2
    px = x1 + (x2 - x1) * r
    py = y1 + (y2 - y1) * r
    return [px,py]



def yingshe(x,y,x1,y1,x2,y2):
    dis1 = (x - x1) * (x - x1) + (y - y1) * (y - y1)
    dis2 = (x - x2) * (x - x2) + (y - y2) * (y - y2)
    if dis1 < dis2:
        if dis1 < 0.0000001:
            return [x1,y1]
    if dis2 < dis1:
        if dis2 < 0.0000001:
            return [x2,y2]

    if y2 < y1:
        temp = y2
        y2 = y1
        y1 = temp
        temp = x2
        x2 = x1
        x1 = temp
    py= ((y2-y1)*(y*(y2-y1)+x*(x2-x1))+(x2-x1)*(y1*x2-y2*x1))/((y2-y1)*(y2-y1)+(x2-x)*(x2-x))
    px= ((x2-x1)*(y*(y2-y1)+x*(x2-x1))-(y2-y1)*(y1*x2-y2*x1))/((y2-y1)*(y2-y1)+(x2-x1)*(x2-x1))
    if (py <= y2 and py >= y1) or (py >= y2 and py <= y1):
        if (px <= x2 and px >= x1) or (py >= x2 and py <= x1):
            return ['chuizhi',px, py]
    else:
        return None


timebase = 2.01211e+13

road_data = sio.loadmat('road_all.mat')

road_index = []

gps_data = sys.stdin

index_file = open('index', 'r')

can = {}

for i in index_file:
    i = i.strip()
    road_index.append(eval(i))
    

pre = None
for i in gps_data:
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
        i[3] = int(i[3] % timebase)
        if i[2] != 0:
            i[2] = 1
    except:
        continue
    if i[4] == 0 or i[5] == 0:
        continue
    x = i[4]
    y = i[5]
    index_id = roadIndex(x, y, road_index)
    now = []
    for k in index_id:
        
        numroad = len(road_data['S'][k]['X'][0][0])
        dismin = 99999.0
        for j in range(0,numroad - 2):
            yingshetemp = PointToSegDist(x, y, road_data['S'][k]['X'][0][0][j], road_data['S'][k]['Y'][0][0][j],\
                    road_data['S'][k]['X'][0][0][j+1], road_data['S'][k]['Y'][0][0][j+1])
            dismintemp = (x - yingshetemp[0])*(x - yingshetemp[0]) + (y - yingshetemp[1]) * (y - yingshetemp[1])
            if dismintemp < dismin:
                roadcan = yingshetemp
                dismin = dismintemp
        if dismin <= 0.000001:
            if now.count(roadcan) == 0:
                now.append(roadcan)
        if len(now) == 0:
            now.append(roadcan)
    if pre == None:
        pre = now
        continue
    for k in now:
        print "%s,%s\r\n" % (k[0],k[1])
    del now



'''
            if yingshetemp == None:
                if j == numroad - 2:
                    if not can.has_key(i[3]):
                        can[i[3]] = []
                    can[i[3]].append([road_data['S'][k]['X'][0][0][j+1],road_data['S'][k]['Y'][0][0][j+1]])
                    continue
                else:
                    continue
            if not can.has_key(i[3]):
                can[i[3]] = []
            can[i[3]].append(yingshetemp)

for i in can:
    print "%s => %s" % (i ,can[i])
'''    
