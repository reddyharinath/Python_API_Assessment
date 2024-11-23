import json


class Util:

    @staticmethod
    def loadPayLoad(filePath):
        with open(filePath) as dataFile:
            data_Dict = json.load(dataFile)
            return data_Dict