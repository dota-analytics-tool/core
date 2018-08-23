from peewee import MySQLDatabase

opendota_api_url = 'https://api.opendota.com/api/'

db = MySQLDatabase(
    host='localhost',
    user='ligo',
    password='1',
    database='opendota'
)
db.connect()