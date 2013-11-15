import sys
from pymongo import MongoClient
import pymongo


class road_set:
    

    def __init__(self, x, y):
        self.client = MongoClient('172.16.20.200', 27017)
        self.db = self.client.gisdb
        self.collection = self.db.xqpoint
        self.roadsets = []
        self.__query__(x, y)
        self.client.disconnect()


    def __query__(self, x, y):
        self.cursor = self.collection.find({"geom.coordinates":{"$geoWithin":{ "$center" : [[x,y], 0.004]}}})
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
