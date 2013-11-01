#!/usr/bin/evn python
#-*- coding:utf-8 -*-

a = []
data = open('road1.txt','r')
for i in data:
    i = i.strip()
    a.append(eval(i))

minx = 999.0
miny = 999.0
maxx = 0.0
maxy = 0.0


for i in range(0,len(a)):
    if a[i][1] < minx and a[i][1] != 0:
        minx = a[i][1]
    if a[i][2] < miny and a[i][2] != 0:
        miny = a[i][2]
    if a[i][3] > maxx:
        maxx = a[i][3]
    if a[i][4] > maxy:
        maxy = a[i][4]

disx = maxx - minx
disy = maxy - miny

numx = int(disx/0.001)
numy = int(disy/0.001)

num = numx*numy

b = []

for i in range(0, num):
    b.append([])


print numx
print numy
#for i in x
