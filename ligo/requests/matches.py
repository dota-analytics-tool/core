"""Import matches from opendota"""
import requests
import csv
from bootstrap.run import *


def create_table():
    db = DB(config.conn_info)
    db.builder.table('heroes').select('name')

    query = "create table matches(match_id varchar, "
    for hero in db.execute():
        query = query + hero[0] + " int null, "
    query = query + "start_time varchar, duration varchar, winner int, avg_mmr int);"
    db.raw(query)


def get(last_match=""):
    try:
        matches = requests.get(config.opendota_api_url + "publicMatches", params={'less_than_match_id':last_match}).json()
        db = DB(config.conn_info)

        db.builder.table('heroes').select()
        heroes_db = db.execute()
        heroes = {}
        for hero in heroes_db:
            heroes[hero[0]] = hero[2]

        insert_matches = list()
        for match in matches:
            if match['duration'] < 600:
                continue
            if not match['lobby_type'] in [0, 7]:
                continue
            if not match['game_mode'] in [1, 2, 4]:
                continue
            match['winner'] = 0 if match['radiant_win'] == 1 else 1
            insert_match = {
                'match_id' : match['match_id'],
                'start_time': match['start_time'],
                'duration': match['duration'],
                'winner': match['winner'],
                'avg_mmr': match['avg_mmr']
            }
            radiant_team = map(int, match['radiant_team'].split(','))
            for radiant_hero in radiant_team:
                insert_match[heroes[radiant_hero]] = 0
            dire_team = map(int, match['dire_team'].split(','))
            for dire_hero in dire_team:
                insert_match[heroes[dire_hero]] = 1
            insert_matches.append(insert_match)
        if len(insert_matches) == 0:
            return get(matches[99]['match_id'])
        return insert_matches
    except Exception:
        return get(last_match)


def truncate():
    db = DB(config.conn_info)
    db.raw("truncate table matches")


def write_to_csv(hero_list, list_matches):
    with open(config.temp_folder + '/matches.csv', 'a', newline='') as csvfile:
        matchwriter = csv.writer(csvfile, delimiter=',')
        for match in list_matches:
            write_match = list()
            write_match.append(match['match_id'])
            for hero in hero_list:
                if hero in match:
                    write_match.append(match[hero])
                else:
                    write_match.append(None)
            write_match.append(match['start_time'])
            write_match.append(match['duration'])
            write_match.append(match['winner'])
            write_match.append(match['avg_mmr'])
            matchwriter.writerow(write_match)
    csvfile.close()