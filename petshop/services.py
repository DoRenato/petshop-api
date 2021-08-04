import requests
from requests.api import get


url = 'https://qflashpetshop.herokuapp.com'

def get_pets():
    r = requests.get("{}/pet".format(url))
    pets = r.json()
    return pets


