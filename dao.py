from pymongo import MongoClient
import datetime

class Dao():

    def __init__(self, database_ip='localhost', port=27017, database='MeterData', collection='MeterReadings'):
        client = MongoClient(database_ip, port)
        self.db = client[database]
        self.collection = self.db[collection]

    #Get documents by building name
    def getDocumentsByName(self, _buildingName):
        # return list of MeterReading by building name
        documents = self.collection.find({"buildingName": _buildingName})
        return [document for document in documents]

    #Get documents by heating type
    def getDocumentsByHeating(self, _heatingType):
        # return a list of meter readings by heating type
        document = self.collection.find({"heatingType": _heatingType})
        return [document for document in documents]

    #Get documents by time
    def getDocumentsAfterTimeStamp(self, _timeStamp):
        # return list of MeterReading after a specific timestamp
        documents = self.collection.find({"timeStamp": {"$lt": _timeStamp}})
        return [document for document in documents]

    def getAllDocumets(self):
        # return a list of all documents in collection
        documents = self.collection.find({})
        return [document for document in documents]
