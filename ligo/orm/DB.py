import vertica_python
from ligo.orm.QueryBuilder import QueryBuilder
from bootstrap.run import *


class DB:
    def __init__(self, config):
        self.connection = vertica_python.connect(**config)
        self.cursor = self.connection.cursor()
        self.builder = QueryBuilder()

    def execute(self):
        query = self.builder.run()
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def raw(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
