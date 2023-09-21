from django.test import TestCase
import pytest
from rest_framework.test import APIClient
from rest_framework import status
from .models import person


@pytest.fixture
def pytclea():
    base_data={
          "Name":"suntvuser",
          "Age": 19,
          "Address":"suntvuser st",
          "Colour":"null"
        }
    return base_data

@pytest.fixture
def client():
    return APIClient()

@pytest.mark.django_db
def testPost(client,base_data):
        response = client.post('/api/person/', base_data,format='json')
        print(base_data)
        assert response.status_code==201
        response = client.post('/api/person/', base_data,format='json')
        db_data=person.objects.get(id=1)
        assert db_data.Name==base_data["Name"]
        assert db_data.Age==base_data["Age"]
        assert db_data.Address==base_data["Address"]


@pytest.mark.django_db
class TestClass():
    def testPost1(self,client,base_data):
        response = client.post('/api/person/', base_data,format='json')
        print(response.data)
        assert response.status_code==201
        response = client.post('/api/person/', base_data,format='json')
        db_data=person.objects.get(id=1)
        assert db_data.Name==base_data["Name"]
        assert db_data.Age==base_data["Age"]
        assert db_data.Address==base_data["Address"]

    # def testPatch(self,client,base_data):
    #      responsepost=client.post('/api/person/',base_data,format='json')
    #      print(responsepost.data)
    #      assert responsepost.status_code==200
    #      db_data_post=person.objects.get(id=1)
    #      data={"Name":"patch_user"}
    #      responsepatch=client.patch('/api/edit_info/1/',data,format='json')
    #      db_data_patch=person.objects.get(id=1)
    #      assert responsepatch.status_code==200
    #      assert data["Name"] is not db_data_patch["Name"]

         

