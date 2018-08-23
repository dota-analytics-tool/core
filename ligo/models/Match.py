from peewee import *
from ligo import config


class Match(Model):

    match_id = CharField()
    r1 = IntegerField()
    r2 = IntegerField()
    r3 = IntegerField()
    r4 = IntegerField()
    r5 = IntegerField()
    d1 = IntegerField()
    d2 = IntegerField()
    d3 = IntegerField()
    d4 = IntegerField()
    d5 = IntegerField()
    radiant_win = BooleanField()

    def getLastMatch(self):
        return 0
        #return Match.select(fn.Min(Match.match_id))


    class Meta:
        database = config.db
        db_table = 'matches'


if not Match.table_exists():
    Match.create_table()