"""Import heroes from opendota"""
import requests
from ligo import config
from bootstrap.run import *

def get():
    heroes = requests.get(config.opendota_api_url + "heroes").json()

    for hero in heroes:
        pass

