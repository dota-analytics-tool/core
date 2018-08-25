from bootstrap.run import *
from ligo.requests import heroes, matches

db = DB(config.conn_info)
#matches.get()
print(db.raw("select match_id, winner from matches where npc_dota_hero_bloodseeker is not null"))
