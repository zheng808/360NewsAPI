import sqlite3
#from clickhouse_driver import Client

DATABASE = "users.db"


class Mysql(object):
    def __init__(self):
        self._init_db()

    def _init_db(self):
        #client = Client('localhost')
        self.conn = sqlite3.connect(DATABASE)
        self.c = self.conn.cursor()
#        client = Client('localhost')
        #print(client.execute('SHOW TABLES'))
        print("db connected")
    
    def createTable(self):
        self.c.execute("CREATE TABLE users (time, user, os, device);")

    def close_connection(self):
        self.conn.commit()
        self.conn.close()
