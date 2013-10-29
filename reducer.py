#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys 

data = sys.stdin

result = {}
#i[0] 是某路段 i[1] 是某时段
for i in data:
    try:
        i = i.strip()
        i = i.split()
    except:
        continue
    
    if result.has_key(i[0]) == 0:
        result[i[0]] = {}
        result[i[0]]['count'] = 0
    if result[i[0]].has_key(i[1]) == 0:
        result[i[0]][i[1]] = 0
    if i[2] == '0':
        result[i[0]][i[1]] += 1
        result[i[0]]['count'] += 1
    else:
        result[i[0]]['count'] += 1


for i in result.keys():
    print '%s=>%s' % (i, result[i]['count'])
    for j in result[i].keys():
        if j == 'count':
            continue
        else :
            print '%s %s %s' % (i, j, result[i][j])







