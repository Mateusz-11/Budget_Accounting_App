import pytest
from django.contrib.auth.models import User
from django.test import Client

@pytest.fixture
def client():
    client = Client()
    return client

