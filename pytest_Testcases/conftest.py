import pytest

from RestAPI_Assessment.PET_CRUD_Operations import Pet_CRUD_Operations

@pytest.fixture(scope='class')
def createPet(request):
    createPetResponseInJson = Pet_CRUD_Operations.createPet()
    #request.cls.Pet_ID = createPetResponseInJson['id']
    request.cls.CreatePetResponse = createPetResponseInJson