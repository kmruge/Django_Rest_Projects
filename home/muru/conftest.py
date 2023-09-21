import pytest

@pytest.fixture
def base_data():
    base_data={
          "Name":"user",
          "Age": 1,
          "Address":"user2 st",
          "Colour":"null"
        }
    return base_data