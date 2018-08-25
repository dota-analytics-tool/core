from bootstrap.run import *
from ligo.requests import heroes, matches

#db = DB(config.conn_info)

test = list()
test.append({'id':3,'name':'meow'})
test.append({'id':5,'name':'5941101'})

heroes.get()

#db.builder.table(table_name='test').insert(test)
#print(db.builder.query)
#db.execute()