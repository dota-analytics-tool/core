"""Import matches from opendota"""
import requests
from ligo import config
from ligo.models.Match import Match


def get(last_match=""):
    matches = requests.get(config.opendota_api_url + "publicMatches", params={'less_than_match_id':last_match}).json()

    for match in matches:

        radiant_team = match['radiant_team'].split(',')
        dire_team =  match['dire_team'].split(',')

        Match.create(
            match_id=match['match_id'],
            r1=radiant_team[0],
            r2=radiant_team[1],
            r3=radiant_team[2],
            r4=radiant_team[3],
            r5=radiant_team[4],
            d1=dire_team[0],
            d2=dire_team[1],
            d3=dire_team[2],
            d4=dire_team[3],
            d5=dire_team[4],
            radiant_win=match['radiant_win']
        )
