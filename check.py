from mysql import Mysql, DATABASE
import os, csv

class Parser(Mysql):
    def __init__(self):
        #store users object
        if os.path.exists(DATABASE):
            return
        self.users = {}
        self.__load_csvFile()
        self.c = Mysql().get()
        self.__parseData()
        self.__insertData()
        self.close_connection()
    
    #load csv
    def __load_csvFile(self):
        filename = 'test.csv'
        with open(filename, 'rt') as csvfile:
             spamreader = csv.reader(csvfile)
             for row in spamreader:
                #print(row)
                self.__createUser(row)
                #print(self.users)
    
    #create User object
    def __createUser(self, row):
        time = (row[0])
        user = int(row[1])
        #print(user)
        os = int(row[2])
        device = int(row[3])
        
        #if it is a new user
        if user in self.users:
            self.users[user]['time'] = time
            self.users[user]['count'] = self.users[user]['count'] + 1
            self.users[user]['os'] |=os
            self.users[user]['device'] |=device
        else:
            self.users[user] = {
            'time': time,
            'count':1,
            'os': os,
            'device': device,
        }
        
    def __parseData(self):
        self.data = [(y['time'], user, y['os'], y['device'], y['count']) for user, y in self.users.items()]
        print(self.data)
        #return self.data
            
    #insert data to DB
    def __insertData(self):
#        query ="SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
#        #check if table exits
#        result = self.c.execute(query)
#        Mysql().close_connection()
#        print("++++++++++++")
#        if result:
#            # there is a table named "tableName"
#            print("there is table")
#            #print(self.users.items())
#            self.__parseData(self.users.items())
#            #self.c.execute("CREATE TABLE users (time, user, os, device, count);")
#            self.c.executemany("INSERT INTO users (time, user, os, device, count) VALUES (?, ?, ?, ?, ?);", self.data)
#            self.c.execute('SELECT * FROM users')
#            Mysql().close_connection()
#            print(self.c.fetchall())
#        else:
#            self.c.execute("CREATE TABLE users (time, user, os, device, count);")
#            self.c.executemany("INSERT INTO users (time, user, os, device, count) VALUES (?, ?, ?, ?, ?);", self.data)
#            Mysql().close_connection()
        self.c.execute("CREATE TABLE usersAPI (time, user, os, device, count);")
        self.c.executemany("INSERT INTO usersAPI (time, user, os, device, count) VALUES (?, ?, ?, ?, ?);", self.data)
        self.c.execute('SELECT * FROM usersAPI')
        print(self.cur.fetchall())

        

        