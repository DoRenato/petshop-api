import requests
from requests.api import get


def get_pets():
    url = 'https://qflashpetshop.herokuapp.com'
    r = requests.get("{}/pet".format(url))
    pets = r.json()
    return pets


