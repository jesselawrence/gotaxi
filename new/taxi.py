#!/usr/bin/env python
#-*- coding:utf-8 -*-
from math import sin as sin
from math import cos as cos
from math import acos as acos
from math import sqrt as sqrt
from math import pi as M_PI
from math import fabs as fabs
from math import exp as exp
import time,datetime
import querymongo

#Example data = [...\n]
#for i in data:
#   cur = gpsRecord(i, road, index)

class gpsRecord:
    carid = ''
    state_run = ''
    event = ''
    time = 0
    x = 0.0
    y = 0.0
    speed = 0
    jiaodu = 0
    state = 0
    road = 0
    rdIndex = []
    candiate = []
    def __init__ (self, record):
        record = record.strip()
        record = record.split(',')
        self.leen = len(record)
        if self.leen != 9 or eval(record[4]) == 0 or eval(record[5]) == 0:
            pass
        else:
            self.carid = record[0]
            self.time = record[1]
            self.event = record[2]
            self.state_run = record[3]
            self.x = eval(record[4])
            self.y = eval(record[5])
            self.speed = eval(record[6])
            self.jiaodu = eval(record[7])
            self.state = eval(record[8])
            self.candiate = []
            self.roadset = querymongo.road_set(self.x,self.y)
            self.__toroad__()

    def display_full(self):
        print "%s %s %s %s %s %s %s %s %s" % (self.carid,self.time,self.event,self.state_run,self.x,self.y,self.speed,self.jiaodu,self.state)
    
    def display_id (self):
        return self.carid
    
    def gen_result(self):
        maxvote = 0.0
        maxid = 0
        mindi = 999
        milen = len(self.candiate)
        for mi in range(0,milen):
            if self.candiate[mi][0] > maxvote:
                maxvote = self.candiate[mi][0]
                maxid = mi
                mindi = self.candiate[mi][1]
            
            if self.candiate[mi][0] == maxvote:
                if self.candiate[mi][1] < mindi:
                    mindi = self.candiate[mi][1]
                    maxid = mi
        if milen != 0:
            self.road = self.candiate[maxid]
            self.result = "%s %s %s %s" % (self.carid, self.time[0:12]+'00', self.road[2], self.event)

    def display_result(self):
        print self.result

    def distance_other (self, otherx, othery):
        x1 = self.x - otherx
        x2 = self.y - othery
        dis_self_other = sqrt(x1 * x1 + x2 * x2)
        return dis_self_other

    def __rindex__(self,roadindex):
        huafen = 0.005
        minx = 115.375
        miny = 39.416667
        numy = 333
        ax = int((self.x - minx)/ huafen)
        ay = int((self.y - miny)/ huafen)
        re_id = ax * numy + ay
        self.rdIndex =  roadindex[re_id]
   
   #find the min distance point in a road array
    def __toroad__ (self):
        for i in self.roadset.roadsets:
            mindis = 999.0
            xlenth = len(i['geom']['coordinates'])
            reall = xlenth - 1
            for j in range(0, reall):
                [tmpx, tmpy ] = self.__touying__(self.x, self.y, i['geom']['coordinates'][j][0], i['geom']['coordinates'][j][1],\
                        i['geom']['coordinates'][j+1][0], i['geom']['coordinates'][j+1][1])
                tmpdis = self.distance_other(tmpx, tmpy)
                if tmpdis < mindis:
                    mindis = tmpdis
                    rtx = tmpx
                    rty = tmpy

            pointmin = [0.0, mindis,i['ID'], rtx, rty]
            self.candiate.append(pointmin)

        #print self.candiate
        self.candiate.sort()
        self.candiate = self.candiate[0:5]
        #print self.candiate
    
    def vote2other(self,gps1):
        can_len = len(gps1.candiate)
        can_len_self = len(self.candiate)
        for i in range(0,can_len):
            idequal = 1.5
            gps1.candiate[i][0] += self.__vote__(self.x,self.y,self.time,self.speed,self.jiaodu,\
                    gps1.candiate[i][3],gps1.candiate[i][4],gps1.time,gps1.speed,gps1.jiaodu) * idequal

            for j in range(0,can_len_self):
                idequal = 1
                if (gps1.candiate[i][2] == self.candiate[j][2]):
                    idequal = 1.7
                else:
                    if gps1.roadset.idSearch(gps1.candiate[i][2])['SNODEID'] == self.roadset.idSearch(self.candiate[j][2])['ENODEID']:
                        idequal = 1.5
                    if gps1.roadset.idSearch(gps1.candiate[i][2])['ENODEID'] == self.roadset.idSearch(self.candiate[j][2])['SNODEID']:
                        idequal = 1.5
                        
                gps1.candiate[i][0] += self.__vote__(self.candiate[j][3], self.candiate[j][4], self.time,self.speed, self.jiaodu,\
                        gps1.candiate[i][3] ,gps1.candiate[i][4], gps1.time, gps1.speed, gps1.jiaodu) * idequal


    def __vote__(self,x1,y1,time1,speed1,jiaodu1,x2,y2,time2,speed2,jiaodu2):
        huansuan = 0.0000036886
        time_year = 2012
        time_month = 11
        dis_w = sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
        time1_year = int(time1[0:4])
        time1_month = int(time1[4:6])
        time1_day = int(time1[6:8])
        time1_hour = int(time1[8:10])
        time1_minute = int(time1[10:12])
        time1_second = int(time1[12:14])
        time2_year = int(time2[0:4])
        time2_month = int(time2[4:6])
        time2_day = int(time2[6:8])
        time2_hour = int(time2[8:10])
        time2_minute = int(time2[10:12])
        time2_second = int(time2[12:14])
        time1f = time.mktime([time1_year,time1_month,time1_day,time1_hour,time1_minute,\
   	    time1_second,0,0,0])
        time2f = time.mktime([time2_year,time2_month,time2_day,time2_hour,time2_minute,\
   	    time2_second,0,0,0])
        time_minus = fabs(time1f - time2f)
        average_speed = (speed1 + speed2) * 0.1389
        jiaoducha = fabs(jiaodu1 - jiaodu2)
        if jiaoducha > 180:
    	    jiaoducha = 360 - jiaoducha
        if jiaoducha != 0:
    	    banjingR = (average_speed * time_minus * huansuan) / ((jiaoducha / 180) * M_PI)
    	    expect_dis = (2 * banjingR * sin(jiaoducha))
        if jiaoducha == 0 or 180:
    	    expect_dis = average_speed * time_minus

        juliwucha = (expect_dis - dis_w) 
        juliwucha = juliwucha * juliwucha * 1e5
        result =  exp (-0.5 * juliwucha) / 2.506628274631
        return result


    def __touying__(self,x,y,x1,y1,x2,y2):
        area = ((x1 - x) * (y2 - y) - (x2 - x) * (y1 - y)) / 2
        if area < 5e-10 and area > -5e-10:
            f = (x2 - x1) * (x - x1) + (y2 - y1) * (y - y1)
            d = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)
            f = f / d
            xt = x1 + f * (x2 - x1)
            yt = y1 + f * (y2 - y1)
            return [xt, yt]
	
        f = (x2 - x1)*(x - x1) + (y2 - y1)*(y - y1)	
        if f < 0:
		    return [x1, y1]
        d = (x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1)
        if f > d:
            return [x2, y2]

        f = f/d
        xt = x1 + f * (x2 - x1)
        yt = y1 + f * (y2 - y1)
        return [xt, yt]


def pDistance (x1,y1,x2,y2):
	earthR = 6371004
	x = cos(y1*M_PI/180) * cos(y2*M_PI/180) * cos((x1-x2)*M_PI/180)
	y = sin(y1*M_PI/180) * sin(y2*M_PI/180)
	s = x + y
	if (s > 1):
		s = 1
	
	if (s < -1):
		s = -1
	
	alpha = acos(s)
	distanceR = alpha * earthR
	return distanceR

def roadIndex (x,y,rd_index):
    huafen = 0.005
    minx = 115.375
    miny = 39.416667000000075
    numx = 425
    ax = int((x - minx)/ huafen)
    ay = int((y - miny)/ huafen)
    re_id = ax * numy + ay
    return rd_index[re_id]



