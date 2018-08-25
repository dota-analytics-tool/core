"""Import matches from opendota"""
import requests
from bootstrap.run import *


def create_table():
    db = DB(config.conn_info)
    db.builder.table('heroes').select('name')

    query = "create table matches(match_id varchar, "
    for hero in db.execute():
        query = query + hero[0] + " int null, "
    query = query + "start_time varchar, duration varchar, winner int);"
    db.raw(query)


def get(last_match=""):
    matches = requests.get(config.opendota_api_url + "publicMatches", params={'less_than_match_id':last_match}).json()
    db = DB(config.conn_info)

    db.builder.table('heroes').select()
    heroes_db = db.execute()
    heroes = {}
    for hero in heroes_db:
        heroes[hero[0]] = hero[2]

    insert_matches = list()
    for match in matches:
        match['winner'] = 0 if match['radiant_win'] == 1 else 1
        insert_match = {
            'match_id' : match['match_id'],
            'start_time': match['start_time'],
            'duration': match['duration'],
            'winner': match['winner']
        }
        radiant_team = map(int, match['radiant_team'].split(','))
        for radiant_hero in radiant_team:
            insert_match[heroes[radiant_hero]] = 0
        dire_team = map(int, match['dire_team'].split(','))
        for dire_hero in dire_team:
            insert_match[heroes[dire_hero]] = 1
        insert_matches.append(insert_match)
    return insert_matches


def truncate():
    db = DB(config.conn_info)
    db.raw("truncate table matches")