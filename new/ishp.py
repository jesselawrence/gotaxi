import os 
import sys 
import json 
from bson import json_util 
from pymongo.connection import Connection 
from progressbar import ProgressBar 
from osgeo import ogr
def shp2mongodb(shape_path, mongodb_server, mongodb_port, mongodb_db, mongodb_collection, append, query_filter): 
        """Convert a shapefile to a mongodb collection""" 
        print 'Converting a shapefile to a mongodb collection ' 
        driver = ogr.GetDriverByName('ESRI Shapefile') 
        print 'Opening the shapefile %s' % shape_path 
        ds = driver.Open(shape_path, 0) 
        if ds is None: 
                print 'Can not open', ds 
                sys.exit(1) 
        lyr = ds.GetLayer() 
        totfeats = lyr.GetFeatureCount() 
        lyr.SetAttributeFilter(query_filter) 
        print 'Starting to load %s of %s features in shapefile %s to MonoDB' % (lyr.GetFeatureCount(), totfeats, lyr.GetName()) 
        print 'Opening MongoDB connection to server %s:%i' % (mongodb_server, mongodb_port) 
        connection = Connection(mongodb_server, mongodb_port) 
        print 'Getting database %s' % mongodb_db 
        db = connection[mongodb_db] 
        print 'Getting the collection %s' % mongodb_collection 
        collection = db[mongodb_collection] 
        if append == False: 
                print 'Removing features from the collection' 
                collection.remove({}) 
        print 'Starting loading features' 
        # define the progressbar 
        pbar = ProgressBar(maxval=lyr.GetFeatureCount()).start() 
        k=0 
        # iterate the features and access its attributes (including geometry) to store them in MongoDb 
        feat = lyr.GetNextFeature() 
        while feat: 
                mongofeat = {} 
                geom = feat.GetGeometryRef() 
                mongogeom = geom.ExportToJson() 
                # store the geometry data with json format 
                mongofeat['geom'] = json.loads(mongogeom,object_hook=json_util.object_hook)
                # iterate the feature's  fields to get its values and store them in MongoDb 
                feat_defn = lyr.GetLayerDefn() 
                for i in range(feat_defn.GetFieldCount()): 
                        value = feat.GetField(i) 
                        if isinstance(value, str): 
                                value = unicode(value, "utf-8") 
                        field = feat.GetFieldDefnRef(i) 
                        fieldname = field.GetName() 
                        mongofeat[fieldname] = value 
                # insert the feature in the collection 
                collection.insert(mongofeat) 
                feat.Destroy() 
                feat = lyr.GetNextFeature() 
                k = k + 1 
                pbar.update(k) 
        pbar.finish() 
        print '%s features loaded in MongoDb from shapefile.' % lyr.GetFeatureCount() 
        
        
input_shape = './Road.shp' 
mongodb_server = 'localhost' 
mongodb_port = 27017 
mongodb_db = 'gisdb' 
mongodb_collection = 'xqpoint' 
filter = ''

print 'Importing data to mongodb' 
shp2mongodb(input_shape, mongodb_server, mongodb_port, mongodb_db, mongodb_collection, False, filter)
