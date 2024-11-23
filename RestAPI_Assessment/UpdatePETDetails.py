import json

import requests

from RestAPI_Assessment.PET_CRUD_Operations import CreatePet
from RestAPI_Assessment.ReteievePETByID import RetrievePETByID
from Utility.UtilityClass import Util

getPetResponseJson = RetrievePETByID.getPetByID()

Header= {"accept":"application/json","Content-Type":"application/json"}
dataDict = Util.loadPayLoad('D:/Learn/2024/PythonRelated/RestAPIAssessment/testdata/payload.json')
dataDict['id'] = str(getPetResponseJson['id'])
dataDict['name'] = 'updateed pet'


class UpdatePetDetailsById:
    @staticmethod
    def updatePETDetails():
        print('updating the PET details..')
        updatePetResponse = requests.put('https://petstore.swagger.io/v2/pet',json=dataDict,headers=Header)
        return  updatePetResponse.json()

responseJson = UpdatePetDetailsById.updatePETDetails()
print(type(responseJson))
print(responseJson)

assert responseJson['name'] == dataDict['name']