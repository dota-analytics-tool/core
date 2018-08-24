import vertica_python
from ligo.orm.QueryBuilder import QueryBuilder

class DB:
    def __init__(self, config):
        self.connection = vertica_python.connect(**config)
        self.cursor = self.connection.cursor()
        self.builder = QueryBuilder()

    def execute(self):
        query = self.builder.get()
        self.cursor.execute(query)


