import pytest

from RestAPI_Assessment.PET_CRUD_Operations import Pet_CRUD_Operations
from Utility.UtilityClass import Util
from pytest_Testcases.BaseClass import BaseClass

updateRequestBody = Util.loadPayLoad('../testdata/payload.json')


@pytest.mark.usefixtures("createPet")
class Test_e2e_PET_CRUD_Operations(BaseClass):

    def test_validate_Created_Pet_Details(self,createPet):
        log = self.getLogDetails()
        log.info("validating created PET details")
        fixtureResponse= self.CreatePetResponse
        petID=fixtureResponse['id']
        log.info("created PET ID is: "+str(petID))
        assert fixtureResponse['name'] == 'TestPET'

    def test_retrieve_Pet_Details(self,createPet):
        fixtureResponse = self.CreatePetResponse
        log = self.getLogDetails()
        log.info("validating retrieved PET details")
        petID = fixtureResponse['id']
        getPetResponseJson = Pet_CRUD_Operations.getPetByID(str(petID))
        #print('Retrieve PET json response is: ', getPetResponseJson)
        log.info("Retrieved PET id is: "+str( getPetResponseJson['id']))
        assert getPetResponseJson['id'] == petID

    def test_update_Pet_Details(self,createPet):
        fixtureResponse = self.CreatePetResponse
        log = self.getLogDetails()
        log.info("validating updated PET details")
        petID = fixtureResponse['id']
        updateRequestBody['id'] = str(petID)
        updateRequestBody['name'] = 'Pet_Name_Updated'
        updateResponseJson = Pet_CRUD_Operations.updatePETDetails(updateRequestBody)
        log.info("Updated PET id is: " + str(updateResponseJson['id']))
        assert updateResponseJson['id'] == petID
        assert updateResponseJson['name'] == 'Pet_Name_Updated'

    def test_Delete_Pet_Details(self,createPet):
        log = self.getLogDetails()
        log.info("validating deleted PET details")
        fixtureResponse = self.CreatePetResponse
        petID = fixtureResponse['id']
        deleteResponseJson = Pet_CRUD_Operations.deletePETById(str(petID))
        log.info("Deleted PET id is: " + str(deleteResponseJson['message']))
        assert deleteResponseJson['message'] == str(petID)

