from ligo import config
from ligo.orm.DB import DB

db = DB(config.conn_info)

db.builder.table(table_name='test')
db.execute()
