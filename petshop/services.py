import requests
from requests.api import get, post
import json


url = 'https://qflashpetshop.herokuapp.com'
# url = 'http://localhost:8000'


def get_pets():
    r = requests.get("{}/pet/".format(url))
    pets = r.json()
    return pets

def post_pet(novopet):
    r = requests.post("{}/pet/".format(url), data=novopet)

def put_pet(pet, petId):
    r = requests.put("{}/pet/{}/".format(url, petId), data=pet)
    print("{}/pet/{}".format(url, petId))

def del_pet(petId):
    r = requests.delete("{}/pet/{}".format(url, petId))


def get_pictures():
    r = requests.get("{}/pictures/".format(url))
    pictures = r.json()
    return pictures


