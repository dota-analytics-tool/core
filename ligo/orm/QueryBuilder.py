class QueryBuilder:
    table_name = ''
    select_fields = '*'

    def table(self, table_name):
        self.table_name = table_name
        return self

    def select(self, fields='*'):
        self.select_fields = fields
        return self

    def get_select_fields(self):
        return self.select_fields

    def get(self):
        return "select " + self.get_select_fields() + " from " + self.table_name + ";"

    #TODO: make where and limit
