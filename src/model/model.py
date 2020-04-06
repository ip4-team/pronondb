import pymysql


class Model:

    def __init__(self, ip, user, pswd, db):
        self.ip = ip
        self.user = user
        self.pswd = pswd
        self.db = db
        self.con = pymysql.connect(host=self.ip, 
                                   user=self.user, 
                                   password=self.pswd, 
                                   db=self.db,
                                   charset='utf8',
                                   cursorclass=pymysql.cursors.DictCursor)

    def insert(self, sql_query, data):
        sucess = False
        try:
            with self.con.cursor() as cursor:
                cursor.execute(sql_query, data)
            self.con.commit()
            sucess = True
        finally:
            self.con.close()

        return sucess
