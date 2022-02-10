import pymysql
 
class Database():
    def __init__(self):
        self.db= pymysql.connect(host='127.0.0.1',
                                  user='root',
                                  password='1111',
                                  db='User',
                                  charset='utf8')
        self.cursor= self.db.cursor(pymysql.cursors.DictCursor)
 
    def execute(self, query):
        self.cursor.execute(query)
 
    def executeOne(self, query):
        self.cursor.execute(query,)
        row= self.cursor.fetchone()
        return row
 
    def executeAll(self, query):
        self.cursor.execute(query)
        row = self.cursor.fetchall()
        return row
 
    def commit(self):
        self.db.commit()