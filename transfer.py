#!/usr/bin/env python
#-*- coding:utf-8 -*-

from math import sin as sin
from math import cos as cos
from math import sqrt as sqrt
from math import pi as M_PI

a = 6378245.0
ee = 0.00669342162296594323

def transform_earth_2_mars_lat(x, y):
    ret = -100.0 + 2.0 * x + 3.0 * y + 0.2 * y * y + 0.1 * x * y + 0.2 * sqrt(abs(x))
    ret += (20.0 * sin(6.0 * x * M_PI) + 20.0 * sin(2.0 * x * M_PI)) * 2.0 / 3.0
    ret += (20.0 * sin(y * M_PI) + 40.0 * sin(y / 3.0 * M_PI)) * 2.0 / 3.0
    ret += (160.0 * sin(y / 12.0 * M_PI) + 320 * sin(y * M_PI / 30.0)) * 2.0 / 3.0
    return ret

def transform_earth_2_mars_lng(x, y):
    ret = 300.0 + x + 2.0 * y + 0.1 * x * x + 0.1 * x * y + 0.1 * sqrt(abs(x))
    ret += (20.0 * sin(6.0 * x * M_PI) + 20.0 * sin(2.0 * x * M_PI)) * 2.0 / 3.0
    ret += (20.0 * sin(x * M_PI) + 40.0 * sin(x / 3.0 * M_PI)) * 2.0 / 3.0
    ret += (150.0 * sin(x / 12.0 * M_PI) + 300.0 * sin(x / 30.0 * M_PI)) * 2.0 / 3.0
    return ret

def transform_earth_2_mars(lng,lat):
    dLat = transform_earth_2_mars_lat(lng - 105.0, lat - 35.0)
    dLon = transform_earth_2_mars_lng(lng - 105.0, lat - 35.0)
    radLat = lat / 180.0 * M_PI
    magic = sin(radLat)
    magic = 1 - ee * magic * magic
    sqrtMagic = sqrt(magic)
    dLat = (dLat * 180.0) / ((a * (1 - ee)) / (magic * sqrtMagic) * M_PI)
    dLon = (dLon * 180.0) / (a / sqrtMagic * cos(radLat) * M_PI)
    tarLat = lat + dLat
    tarLng = lng + dLon
    return [tarLng,tarLat]




