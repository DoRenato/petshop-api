import requests
from requests.api import get


def get_pets():
    url = 'http://localhost:8000/api'
    r = requests.get("{}/pet".format(url))
    pets = r.json()
    return pets


