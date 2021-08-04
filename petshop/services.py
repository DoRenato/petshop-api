import requests
from requests.api import get, post
import json


# url = 'https://qflashpetshop.herokuapp.com'
url = 'http://localhost:8000'

def get_pets():
    r = requests.get("{}/pet/".format(url))
    pets = r.json()
    return pets

def post_pet(novopet):
    r = requests.post("{}/pet/".format(url), data=novopet)


