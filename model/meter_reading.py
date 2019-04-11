import datetime

class MeterReading():

    def __init__(self, buildingName, value, timeStamp):
        self.buildingName = buildingName
        self.value = value
        self.timeStamp = timeStamp

    def to_json(self):
        return {'buildingName': self.buildingName, 'value': self.value, 'timeStamp': self.timeStamp.strftime('%Y-%m-%d')}

    @classmethod
    def from_dict(cls, data):
        return cls(data.get('buildingName'), data.get('value'), data.get('timeStamp'))

    def __add__(self, other):
        return self.value + other.value
