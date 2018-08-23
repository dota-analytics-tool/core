from peewee import *
from ligo import config


class Hero(Model):

    id = IntegerField()
    name = CharField()
    local_name = CharField()

    class Meta:
        database = config.db
        db_table = 'heroes'


if not Hero.table_exists():
    Hero.create_table()