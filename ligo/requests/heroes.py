"""Import heroes from opendota"""
import requests
from ligo import config
from ligo.models.Hero import Hero


def get():
    heroes = requests.get(config.opendota_api_url + "heroes").json()

    for hero in heroes:
        Hero.create(
            id=hero['id'],
            name=hero['name'],
            local_name=hero['localized_name']
        )
