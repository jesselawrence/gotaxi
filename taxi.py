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

def touying(x,y,x1,y1,x2,y2):
	theta = 0.000000005
	area = ((x1 - x) * (y2 - y) - (x2 - x)(y1 - y)) / 2
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
	    time1_year = eval(time1[0,3])
	    time1_month = eval(time1[4,5])
	    time1_day = eval(time1[6:7])
	    time1_hour = eval(time1[8:9])
	    time1_minute = eval(time1[10,11])
	    time1_second = eval(time1[12,13])
	    time2_year = eval(time2[0,3])
	    time2_month = eval(time2[4,5])
	    time2_day = eval(time2[6:7])
	    time2_hour = eval(time2[8:9])
	    time2_minute = eval(time2[10,11])
	    time2_second = eval(time2[12,13])
	    time1f = time.mktime(datetime.datetime(time1_year,time1_month,time1_day,time1_hour,time1_minute,\
	    	time1_second))
	    time2f = time.mktime(datetime.datetime(time2_year,time2_month,time2_day,time2_hour,time2_minute,\
	    	time2_second))
	    time_minus = fabs(time1f - time2f)
	    average_speed = (speed1 + speed2) / 2
	    jiaoducha = fabs(jiaodu1 - jiaodu2)
	    if jiaoducha > 180:
	    	jiaoducha = 360 - jiaoducha

	    huchang = average_speed * timecha
	    if jiaoducha != 0:
	    	banjingR = huchang / ((jiaoducha / 360) * 2 * M_PI)
	    	expect_dis = (2 * R * sin(jiaoducha)) * 1000 * huansuan

	    if jiaoducha == 0 || 180:
	    	expect_dis = average_speed * 1000 * huansuan / 3600

	    juliwucha = (expect_dis - dis_w) 
	    juliwucha = juliwucha * juliwucha
	    result =  exp (-0.5 * juliwucha) / 2.506628274631