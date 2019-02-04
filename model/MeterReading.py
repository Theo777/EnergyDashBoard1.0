import datetime

class MeterReading():

    def __init__(self, buildingName, value, timeStamp):
        self.buildingName = buildingName
        self.value = value
        self.timeStamp = timeStamp

    def __add__(self, other):
        return self.value + other.value
