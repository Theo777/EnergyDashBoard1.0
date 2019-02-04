from pymongo import MongoClient
import datetime

class Dao():

    def __init__(self, database_ip='localhost', port=27017, database='MeterData', collection='MeterReadings'):
        client = MongoClient(database_ip, port)
        self.db = client[database]
        self.collection = db[collection]

    #Get documents by building name
    def getDocumentsByName(self, _buildingName, collection=self.collection):
        # return list of MeterReading by building name
        return collection.find({"buildingName": _name})

    #Get documents by heating type
    def getDocumentsByHeating(self, _heatingType):
        # return a list of meter readings by heating type
        return self.collection.find({"heatingType": _heatingType})

    #Get documents by time
    def getDocumentsAfterTimeStamp(self, _timeStamp):
        # return list of MeterReading after a specific timestamp
        return self.collection.find({"timeStamp": {"$lt": _timeStamp}})
