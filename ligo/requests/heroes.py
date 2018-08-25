"""Import heroes from opendota"""
import requests
from bootstrap.run import *

def create_table():
    query = "create table heroes(id int, localized_name varchar, name varchar);"
    db = DB(config.conn_info)
    db.raw(query)

def get():
    heroes = requests.get(config.opendota_api_url + "heroes").json()

    query = "truncate table heroes; commit;"
    db = DB(config.conn_info)
    db.raw(query)

    result_heroes = list()

    for hero in heroes:
        hero = {
            'id': hero['id'],
            'name': quote_escape(hero['name']),
            'localized_name': quote_escape(hero['localized_name'])
        }
        result_heroes.append(hero)

    db.builder.table('heroes').insert(result_heroes)
    db.execute()


def quote_escape(str):
    result = ""
    for char in str:
        if char == "'":
            continue
        result = result + char
    return result
