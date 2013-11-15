#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
import taxi

data = sys.stdin

if __name__ == '__main__':
    nowid = ''
    b = []
    c = []
    for i in data:
        try: 
            a = taxi.gpsRecord(i)
            if a.leen != 9:
                continue
        except:
            continue
           
        if nowid == '':
            nowid = a.carid
            b.append(a)
            continue

        if a.carid != nowid:
            nowid = a.carid
            lenb = len(b)
            b[0].vote2other(b[1])
            b[0].vote2other(b[2])
            b[0].vote2other(b[3])
            b[1].vote2other(b[0])
            b[1].vote2other(b[2])
            b[1].vote2other(b[3])
            b[1].vote2other(b[4])
            b[2].vote2other(b[0])
            b[2].vote2other(b[1])
            b[2].vote2other(b[3])
            b[2].vote2other(b[4])
            b[2].vote2other(b[5])
            b[lenb-1].vote2other(b[lenb-2])
            b[lenb-1].vote2other(b[lenb-3])
            b[lenb-1].vote2other(b[lenb-4])
            b[lenb-2].vote2other(b[lenb-1])
            b[lenb-2].vote2other(b[lenb-3])
            b[lenb-2].vote2other(b[lenb-4])
            b[lenb-2].vote2other(b[lenb-5])
            b[lenb-3].vote2other(b[lenb-1])
            b[lenb-3].vote2other(b[lenb-2])
            b[lenb-3].vote2other(b[lenb-4])
            b[lenb-3].vote2other(b[lenb-5])
            b[lenb-3].vote2other(b[lenb-6])
            for j in range(3,lenb-3):
                b[j].vote2other(b[j-3])
                b[j].vote2other(b[j-2])
                b[j].vote2other(b[j-1])
                b[j].vote2other(b[j+1])
                b[j].vote2other(b[j+2])
                b[j].vote2other(b[j+3])
            for j in b:
                j.gen_result()
                try:
                    if c.count(j.result) == 0:
                        c.append(j.result)
                except:
                    continue
            for j in c:
                print j
            b = []
            c = []

        b.append(a)

    nowid = a.carid
    lenb = len(b)
    b[0].vote2other(b[1])
    b[0].vote2other(b[2])
    b[0].vote2other(b[3])
    b[1].vote2other(b[0])
    b[1].vote2other(b[2])
    b[1].vote2other(b[3])
    b[1].vote2other(b[4])
    b[2].vote2other(b[0])
    b[2].vote2other(b[1])
    b[2].vote2other(b[3])
    b[2].vote2other(b[4])
    b[2].vote2other(b[5])
    b[lenb-1].vote2other(b[lenb-2])
    b[lenb-1].vote2other(b[lenb-3])
    b[lenb-1].vote2other(b[lenb-4])
    b[lenb-2].vote2other(b[lenb-1])
    b[lenb-2].vote2other(b[lenb-3])
    b[lenb-2].vote2other(b[lenb-4])
    b[lenb-2].vote2other(b[lenb-5])
    b[lenb-3].vote2other(b[lenb-1])
    b[lenb-3].vote2other(b[lenb-2])
    b[lenb-3].vote2other(b[lenb-4])
    b[lenb-3].vote2other(b[lenb-5])
    b[lenb-3].vote2other(b[lenb-6])
    for j in range(3,lenb-3):
        b[j].vote2other(b[j-3])
        b[j].vote2other(b[j-2])
        b[j].vote2other(b[j-1])
        b[j].vote2other(b[j+1])
        b[j].vote2other(b[j+2])
        b[j].vote2other(b[j+3])

    c = []

    for j in b:
        j.gen_result()
        try:
            if c.count(j.result) == 0:
                c.append(j.result)
        except:
            continue
    for j in c:
        print j
    
