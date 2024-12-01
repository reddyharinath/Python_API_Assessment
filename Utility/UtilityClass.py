import configparser
import json


class Util:

    @staticmethod
    def loadPayLoad(filePath):
        with open(filePath) as dataFile:
            data_Dict = json.load(dataFile)
            return data_Dict

    @staticmethod
    def readConfigDetails():
        configParser=configparser.ConfigParser()
        configParser.read('../testdata/Properties.ini')
        return  configParser