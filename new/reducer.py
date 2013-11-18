#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
import taxi
import querymongo 
import gc


data = sys.stdin

if __name__ == '__main__':
    
    b = []
    c = []
    count = 0

    for i in data:
        try:
            a = taxi.gpsRecord(i, querymongo)
            if a.success == 1:
                b.append(a)
                if len(b) < 3:
                    continue
                while( len(b) > 3):
                    del b[0]
                if len(b) == 3:
                    b[2].vote2other(b[0],3)
                    b[2].vote2other(b[1],2)
                    b[0].vote2other(b[2],0)
                    b[0].vote2other(b[1],1)
                    b[1].vote2other(b[2],1)
                    b[1].vote2other(b[0],2)
                    b[0].gen_result()
                    if c.count(b[0].result) == 0:
                        c.append(b[0].result)
                    del b[0]
                    count += 1
                    if count > 30:
                        for j in c:
                            print j
                        c = []
                        gc.collect()
                        count = 0 
            else:
                continue
        except:
            pass

    querymongo.client.disconnect()

