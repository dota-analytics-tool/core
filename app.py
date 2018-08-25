from bootstrap.run import *
from ligo.requests import heroes, matches
import csv

db = DB(config.conn_info)


hero_list = heroes.hero_names()
list_matches = matches.get()
with open('matches.csv', 'w', newline='') as csvfile:
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
        matchwriter.writerow(write_match)