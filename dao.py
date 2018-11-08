from pymongo import MongoClient
#from unqlite import import UnQLite

#Get rows by building name

#Get rows by heating type

#Get rows by time

client = MongoClient('localhost', 27017) # default host and port

db = client.MeterData

meter_collection = db.MeterReadings
