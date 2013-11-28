#!/usr/bin/env python
# -*- coding=utf-8 -*-

import sys
from pymongo import MongoClient

filesave = open('./road_id.txt','w')

client = MongoClient('127.0.0.1', 27017)
db = client.gisdb
collection = db.xqpoint

cursor = collection.find()
len_cursor = cursor.count()

for i in range(0, len_cursor):
    temp = cursor.next()
    tempid = temp['ID']
    filesave.write("%s\n" % (tempid))

client.disconnect()
filesave.close()
