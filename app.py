from bootstrap.run import *

db = DB(config.conn_info)

test = list()

test.append({'id':3,'name':'meow'})
test.append({'id':5,'name':'5941101'})

db.builder.table(table_name='test').insert(test)
print(db.builder.query)
db.execute()