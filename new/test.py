#!/usr/bin/env python

import sys
import taxi

data = sys.stdin

for i in data:
    a = taxi.gpsRecord(i)
    print a.candiate
