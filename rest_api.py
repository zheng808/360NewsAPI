from mysql import Mysql

class rest_api(Mysql):
    
    def unique_users(self, os, device):
        query = "SELECT Count(Distinct(user)) FROM users"
        sql = self.getInputUnique(query, os, device)
        print(sql)
        self.c.execute(sql)
        
        count = self.c.fetchone()[0]
        self.close_connection()
        print(count)
        return {
          'count': count,
        }
    
    def loyal_users(self, os, device):
        #query userID 
        query = "SELECT  user from  users"
        end = " Group by user having Count(user) > 10;"
        #get all devices and os
        sql = self.getInputLoyal(query, os, device)
        sql = sql + end
        print(sql)
        self.c.execute(sql)
        
        count = self.c.fetchall()
        self.close_connection()
        #return the number of userID
        return {
          'count': len(count),
        }
    
    #return query for unique with option os and devicex
    def getInputUnique(self, query, os, device):
        #check both os and devices
        print('+++++++++')
        if(os == None and device == None):
            query+=';'
            return query
        os = self.parseInput(os)
        device = self.parseInput(device)
        #two flags
        count_os = 0
        count_device = 0
        query = self.constructSQL(query, os, device)
        return query
    
    #return query for loyal with option os and devicex
    def getInputLoyal(self, query, os, device):
        #loyal does not need to add;
        if(os == None and device == None):
            return query
        os = self.parseInput(os)
        device = self.parseInput(device)
        #two flags
        query = self.constructSQL(query, os, device)
        return query
    
    def constructSQL(self,query, os, device):
        count_os = 0
        count_device = 0
        for i in range(0, len(os)):
                if count_os == 0:
                    query += ' WHERE os= ' + os[i]
                    count_os = count_os + 1
                else:
                    #append &
                    query += '&' + os[i]
        
        for y in range(0, len(device)):
            #check os first
            if count_os > 0:
                    query += ' AND device= ' + device[y]
                    count_device = count_device + 1
                    count_os = 0
            elif count_device == 0 :
                    query += ' WHERE device= ' + device[y]
                    count_device = count_device + 1
            else:
                    query += '&' + device[y]
        return query
        
            
    def parseInput(self, input):
        listInput = []
        if input:
            for i in input.split(','):
                listInput.append(i)
        return listInput