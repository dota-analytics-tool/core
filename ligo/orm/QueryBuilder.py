class QueryBuilder:
    table_name = ''
    select_fields = '*'
    keys = list()
    items = list()

    query = ""

    def table(self, table_name):
        self.table_name = table_name
        return self

    def select(self, fields='*'):
        self.select_fields = fields
        self.query = "select " + self.get_select_fields() + " from " + self.table_name + ";"


    def get_select_fields(self):
        return self.select_fields

    def run(self):
        return self.query

    # TODO: make where and limit

    def insert(self, insert_array):
        query = ""
        for item in insert_array:
            query = query + "insert into " + self.table_name + "("
            for key in item:
                query = query + key + ","
            query = query[0:-1] + ") values("
            for key in item:
                if not type(item[key]) is int:
                    query = query + "\'"
                query = query + str(item[key])
                if not type(item[key]) is int:
                    query = query + "\'"
                query = query + ","
            query = query[0:-1]
            query = query + "); "
        query = query + "commit;"
        self.query = query
