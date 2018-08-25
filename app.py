from bootstrap.run import *
from ligo.requests import heroes, matches
import time
import os
start_time = time.time()

db = DB(config.conn_info)


def get_matches(last_match, count_of_requests=1000):
    hero_list = heroes.hero_names()

    for i in range(count_of_requests):
        print("Iteration ", i+1)

        list_matches = matches.get(last_match)
        last_match = list_matches[1]['match_id']

        matches.write_to_csv(hero_list, list_matches)


def import_from_csv_to_db():
    db.raw("copy matches from '/tmp/matches.csv' DELIMITER ',' TRAILING NULLCOLS;")
    os.remove(config.temp_folder + '/matches.csv')


def test():
    rows_win_radiant = db.raw(
        "select * from matches where npc_dota_hero_wisp = 0 and npc_dota_hero_spectre = 1 and npc_dota_hero_tiny = 1 and npc_dota_hero_bane = 1 and npc_dota_hero_enchantress = 1 and npc_dota_hero_earthshaker = 1")
    rows_win_dire = db.raw(
        "select * from matches where npc_dota_hero_wisp = 1 and npc_dota_hero_spectre = 0 and npc_dota_hero_tiny = 0 and npc_dota_hero_bane = 0 and npc_dota_hero_enchantress = 0 and npc_dota_hero_earthshaker = 0")

    count_matches = 0
    count_wins = 0
    for radiant in rows_win_radiant:
        count_matches = count_matches + 1
        if radiant[-1] == 0:
            count_wins = count_wins + 1

    for dire in rows_win_dire:
        count_matches = count_matches + 1
        if dire[-1] == 1:
            count_wins = count_wins + 1

    print("Count matches ", count_matches)
    print("Count wins ", count_wins)
    print("Winrate ", count_wins / count_matches * 100, "%")


def min_match_id():
    match = db.raw("select match_id from matches order by match_id desc limit 1")
    return match[0][0]


#test()
get_matches("", 10000)
#import_from_csv_to_db()
print("Time: ", time.time()-start_time)