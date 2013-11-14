import sys
from pymongo import MongoClient
import pymongo

global client
client = MongoClient('192.168.1.2', 27017)
global db
db = client.gisdb
global collection
collection = db.xqpoint

class road_set:
    

    def __init__(self, x, y):
        self.roadsets = []
        self.__query__(x, y)


    def __query__(self, x, y):
        cursor = collection.find({"geom.coordinates":{"$geoWithin":{ "$center" : [[x,y], 0.004]}}})
        len_cursor = cursor.count()
        for i in range(0,len_cursor):
            self.roadsets.append(cursor.next())
        self.length = len_cursor

    def idSearch(self,numstring):
        for i in self.roadsets:
            if i['ID'] == numstring:
                return i
        return None
