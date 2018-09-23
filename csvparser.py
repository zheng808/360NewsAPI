import os, csv, time
from mysql import Mysql, DATABASE
import sqlite3
DATABASE = "users.db"

class Parser(Mysql):
    def __init__(self):
        if os.path.exists(DATABASE):
            return

        self.users = {}
        self._init_db()
        self.createTable()
        self.__load_csvFile()
        self.__insertData()
        self.close_connection()

    #load csv
    def __load_csvFile(self):
        #filename = 'data-1.csv'
        filename = 'test.csv'
        
        with open(filename, 'rt') as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                self.__createUser(row)
        print("finish loading")
    
    #create User object
    def __createUser(self, row):
        time = (row[0])
        user = int(row[1])
        #print(user)
        os = int(row[2])
        device = int(row[3])
        self.users = [(
             time,
             user,
             os,
             device,
        )]
    
        self.__insertData()
        print(self.users)
        
    #insert table data
    def __insertData(self):
        self.c.executemany("INSERT INTO users (time, user, os, device) VALUES ( ?, ?, ?, ?);", self.users)
        self.c.execute("Select * from users;")
        

        

        
