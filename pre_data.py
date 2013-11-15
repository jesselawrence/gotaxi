#!/usr/bin/evn python
#-*- coding:utf-8 -*-

a = []
data = open('index.txt','r')

huafen = 0.005

for i in data:
    i = i.strip()
    a.append(eval(i))

minx = 115.375
miny = 39.41667
maxx = 117.5
maxy = 41.083333



disx = maxx - minx
disy = maxy - miny

numx = int(disx/huafen)
numy = int(disy/huafen)

num = (numx + 1)* (1 + numy)

b = []
#c = []

#for i in range(0, len(a)):
#    c.append(0)
print num

for i in range(0, num + 1):
    b.append([])
'''
print numx
print numy
'''
tempid = 0

for i in range(0,len(a)):
    aminx = int ((a[i][1] - minx)/huafen)
    aminy = int ((a[i][2] - miny)/huafen) 
    amaxx = int ((a[i][3] - minx)/huafen)
    amaxy = int ((a[i][4] - miny)/huafen)
    startid = aminx * numy + aminy
    height = amaxy - aminy + 1
    width = amaxx - aminx + 1
    for j in range(0,width) :
        for k in range(0,height) :
            nowid = startid + height * j + k
            #print nowid
            b[nowid].append(i)


c = open('index','w')
for i in b:
    c.write(repr(i)+'\n')

c.close()
data.close()
del a
'''            
    if i[0] == 9998:
        tempid = i[0]
        print "%s %s %s %s %s %s" % (i[0], aminx, aminy, startid, height,width)

test case
for i in range(0,len(b)):
        for j in b[i]:
            c[j - 1] =c[j - 1] + 1
            if j == tempid:
                print "%s %s" % (i, b[i])

for i in range(0, len(c)):
    if c[i] == 10:
        print i
'''
