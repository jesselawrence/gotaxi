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
    def __init__ (self, record,roadindex,road):
        record = record.strip()
        record = record.split(',')
        self.carid = record[0]
        self.time = eval(record[1])
        self.event = record[2]
        self.state_run = record[3]
        self.x = eval(record[4])
        self.y = eval(record[5])
        self.speed = eval(record[6])
        self.jiaodu = eval(record[7])
        self.state = eval(record[8])
        self.__rindex__(roadindex)
        self.__toroad__(road)

    def display_full(self):
        print "%s %s %s %s %s %s %s %s %s" % (self.carid,self.time,self.event,self.state_run,self.x,self.y,self.speed,self.jiaodu,self.state)
    
    def display_result(self):
        self.candiate.sort()
        self.road = self.candiate[0]
        print "%s %s %s" % (self.carid, self.time, self.road)

    def distance_other (self, otherx, othery):
        dis_self_other = sqrt((self.x - otherx)*(self.x - otherx) + (self.y - othery)*(self.y - othery))
        return dis_self_other

    def __rindex__(self,roadindex):
        huafen = 0.005
        minx = 115.375
        miny = 39.416667
        numy = 333
        ax = int((self.x - minx)/ huafen)
        ay = int((self.y - miny)/ huafen)
        re_id = ax * numy + ay
        print re_id
        self.rdIndex =  roadindex[re_id]
    
    def __toroad__ (self,road):
        for j in self.rdIndex:
            mindis = 999
            le = len(road['S'][j]['X'][0][0]) - 2
            rtx = 0.0
            rty = 0.0
            for i in range(0, le):
                tmpx, tmpy = touying(self.x, self.y, road['S'][j]['X'][0][0][i],\
                    road['S'][j]['Y'][0][0][i], road['S'][j]['X'][0][0][i+1],\
                    road['S'][j]['Y'][0][0][i+1])
                tmpdis = self.distance_other(tmpx, tmpy)
                if tmpdis < mindis:
                    mindis = tmpdis
                    rtx = tmpx
                    rty = tmpy
            pointmin = [0.0,mindis,j,rtx,rty]
            self.candiate.append(pointmin)
        self.candiate.sort()
        self.candiate = self.candiate[0:5]
    
    def vote2other(self,gps1):
        can_len = len(gps1.candiate)
        can_len_self = len(self.candiate)
        for i in range(0,can_len):
            gps1.candiate[i][0] += vote(self.x,self.y,self.time,self.speed,self.jiaodu,\
                    gps1.candiate[i][3],gps1.candiate[i][4],gps1.time,gps1.speed,gps1.jiaodu)

            for j in range(0,can_len_self):
                gps1.candiate[i][0] += vote(self.candiate[j][3],self.candiate[j][4],self.time,self.speed,self.jiaodu,\
                        gps1.candiate[i][3],gps1.candiate[i][4],gps1.time,gps1.speed,gps1.jiaodu)



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


def touying(x,y,x1,y1,x2,y2):
	theta = 0.000000005
	area = ((x1 - x) * (y2 - y) - (x2 - x) * (y1 - y)) / 2
	if area <= theta and area >= -theta:
		return [x, y]

	f = (x2 - x1)*(x - x1) + (y2 - y1)*(y - y1)
	if f < 0:
		return [x1, y1]
	d = (x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1)
	if f > d:
		return [x2, y2]

	f = f/d
	return [x1 + f *(x2 - x1), y1 + f * (y2 - y1)]

def vote(x1,y1,time1,speed1,jiaodu1,x2,y2,time2,speed2,jiaodu2):
    huansuan = 0.0000036886
    time_year = 2012
    time_month = 11
    dis_w = sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
    time1_year = eval(time1[0:4])
    time1_month = eval(time1[4:6])
    time1_day = eval(time1[6:8])
    time1_hour = eval(time1[8:10])
    time1_minute = eval(time1[10:12])
    time1_second = eval(time1[12:14])
    time2_year = eval(time2[0:4])
    time2_month = eval(time2[4:6])
    time2_day = eval(time2[6:8])
    time2_hour = eval(time2[8:10])
    time2_minute = eval(time2[10:12])
    time2_second = eval(time2[12:14])
    time1f = time.mktime(datetime.datetime(time1_year,time1_month,time1_day,time1_hour,time1_minute,\
   	time1_second))
    time2f = time.mktime(datetime.datetime(time2_year,time2_month,time2_day,time2_hour,time2_minute,\
   	time2_second))
    time_minus = fabs(time1f - time2f)
    average_speed = (speed1 + speed2) / 2
    jiaoducha = fabs(jiaodu1 - jiaodu2)
    if jiaoducha > 180:
    	jiaoducha = 360 - jiaoducha
	huchang = average_speed * timeminus
    if jiaoducha != 0:
    	banjingR = huchang / ((jiaoducha / 360) * 2 * M_PI)
    	expect_dis = (2 * banjingR * sin(jiaoducha)) * 1000 * huansuan
    if jiaoducha == 0 or 180:
    	expect_dis = average_speed * 1000 * huansuan / 3600

    juliwucha = (expect_dis - dis_w) 
    juliwucha = juliwucha * juliwucha
    result =  exp (-0.5 * juliwucha) / 2.506628274631
    return result



