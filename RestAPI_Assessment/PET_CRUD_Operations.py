import requests


from Utility.UtilityClass import Util

#D:/Learn/2024/PythonRelated/RestAPIAssessment  = ../

createUserPayload = Util.loadPayLoad('../testdata/payload.json')
createUserPayload['name'] = 'TestPET'
cate= createUserPayload['category']
cate['name']='TestPETCategory'
tags=createUserPayload['tags']
print(type(tags))
tags[0]['name'] = 'TestPETags'




headers = {"accept":"application/json","Content-Type":"application/json"}
header = {"accept":"application/json"}

class Pet_CRUD_Operations:

    @staticmethod
    def createPet():
        print('creating PET')
        createUserResponse = requests.post("https://petstore.swagger.io/v2/pet",json=createUserPayload,headers=headers)
        responseJson = createUserResponse.json()
        return  responseJson

    @staticmethod
    def getPetByID(pet_id):
        print('retrieving pet details...')
        retrieveResponse = requests.get('https://petstore.swagger.io/v2/pet/' + pet_id, headers=header)
        responseJson = retrieveResponse.json()
        return responseJson

    @staticmethod
    def updatePETDetails(updatedRequestBody):
        print('updating the PET details..')
        updatePetResponse = requests.put('https://petstore.swagger.io/v2/pet', json=updatedRequestBody, headers=headers)
        return updatePetResponse.json()

    @staticmethod
    def deletePETById(petID):
        deletePetResponse = requests.delete('https://petstore.swagger.io/v2/pet/' + petID,headers=header)
        return deletePetResponse.json()





