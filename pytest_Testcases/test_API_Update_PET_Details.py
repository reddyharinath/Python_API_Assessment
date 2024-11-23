from RestAPI_Assessment.PET_CRUD_Operations import Pet_CRUD_Operations
from Utility.UtilityClass import Util

CreatedPetID=Pet_CRUD_Operations.createPet()
print(str(CreatedPetID['id']))
updateRequestBody = Util.loadPayLoad('../testdata/payload.json')
updateRequestBody['id'] =str(CreatedPetID['id'])
updateRequestBody['name'] = 'Pet_Name_Updated'

def test_Update_Pet_Details():
    print('updating PET details..')
    updateResponseJson = Pet_CRUD_Operations.updatePETDetails(updateRequestBody)
    assert updateResponseJson['id'] == CreatedPetID['id']
    assert updateResponseJson['name'] == 'Pet_Name_Updated'