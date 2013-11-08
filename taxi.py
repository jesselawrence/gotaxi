#!/usr/bin/env python
#-*- coding:utf-8 -*-
from math import sin as sin
from math import cos as cos
from math import acos as acos
from math import sqrt as sqrt
from math import pi as M_PI

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