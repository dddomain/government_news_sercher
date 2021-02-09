import MySQLdb

class DataBase():
    def __init__(self, user, password, host, db):
        self.user = user
        self.password = password
        self.host = host
        self.db = db

    def conn_db(self):
        self.conn = MySQLdb.connect(user=self.user, password=self.password, host=self.host, db=self.db)
        self.cursor = self.conn.cursor()

    def disconn_db(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    def execute(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def insert(self, sql ,candd):
        print(f"Latest news: [{candd[0]}: {candd[2]}]")
        self.execute(sql)

    def select(self, sql, value):
        selects = list(self.execute(sql))
        # selects = self.cursor.fetchall()
        return selects
        # return self.cursor.fetchall()
