import sys
from pymongo import MongoClient
import pymongo

global client
client = MongoClient('192.168.1.4', 27017)
global db
db = client.gisdb
global collection
collection = db.xqpoint


class road_set:
    

    def __init__(self, x, y):
        try:
            self.roadsets = []
            self.__query__(x, y)
            self.success = 1
        except:
            self.success = 0


    def __query__(self, x, y):
        self.cursor = collection.find({"geom.coordinates":{"$geoWithin":{ "$center" : [[x,y], 0.004]}}})
        len_cursor = self.cursor.count()
        for i in range(0,len_cursor):
            self.roadsets.append(self.cursor.next())
        self.length = len_cursor
        self.cursor.close()

    def idSearch(self,numstring):
        for i in self.roadsets:
            if i['ID'] == numstring:
                return i
        return None
