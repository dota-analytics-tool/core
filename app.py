from bootstrap.run import *
from ligo.requests import heroes, matches

db = DB(config.conn_info)

count_of_requests = 10000

hero_list = heroes.hero_names()

last_match = "4070119619"
for i in range(count_of_requests):
    print("Iteration ", i+1)

    list_matches = matches.get(last_match)
    last_match = list_matches[99]['match_id']

    matches.write_to_csv(hero_list, list_matches)
