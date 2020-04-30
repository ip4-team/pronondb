import pymysql
import warnings


class Model:

    def __init__(self, ip, user, pswd, db):
        self.ip = ip
        self.user = user
        self.pswd = pswd
        self.db = db

    def insert(self, sql_query, data):
        con = pymysql.connect(host=self.ip,
                              user=self.user,
                              password=self.pswd,
                              db=self.db,
                              charset='utf8',
                              cursorclass=pymysql.cursors.DictCursor)
        cursor = con.cursor()
        result = -1
        code, message = '', ''

        warnings.filterwarnings('error', category=pymysql.Warning)

        try:
            cursor.execute(sql_query, data)
            con.commit()
            result = 0
        except Warning as warning:
            code, message = warning.args
            result = 1
        except pymysql.InternalError as error:
            code, message = error.args
            result = 2
        except pymysql.IntegrityError as error:
            code, message = error.args
            result = 2
        finally:
            con.close()

        return result, code, message

    def select(self, sql_query):
        con = pymysql.connect(host=self.ip,
                              user=self.user,
                              password=self.pswd,
                              db=self.db,
                              charset='utf8',
                              cursorclass=pymysql.cursors.DictCursor)
        cursor = con.cursor()
        result = -1
        code, message = '', ''

        warnings.filterwarnings('error', category=pymysql.Warning)

        try:
            cursor.execute(sql_query)
            message = cursor.fetchall()
            result = 0
        except Warning as warning:
            code, message = warning.args
            result = 1
        except pymysql.InternalError as error:
            code, message = error.args
            result = 2
        except pymysql.IntegrityError as error:
            code, message = error.args
            result = 2
        finally:
            con.close()

        return result, code, message

    def update(self, sql_query, data):
        con = pymysql.connect(host=self.ip,
                              user=self.user,
                              password=self.pswd,
                              db=self.db,
                              charset='utf8',
                              cursorclass=pymysql.cursors.DictCursor)
        cursor = con.cursor()
        result = -1
        code, message = '', ''

        warnings.filterwarnings('error', category=pymysql.Warning)

        try:
            cursor.execute(sql_query, data)
            con.commit()
            result = 0
        except Warning as warning:
            code, message = warning.args
            result = 1
        except pymysql.InternalError as error:
            code, message = error.args
            result = 2
        except pymysql.IntegrityError as error:
            code, message = error.args
            result = 2
        finally:
            con.close()

        return result, code, message


    def delete(self, sql_query):
        con = pymysql.connect(host=self.ip,
                              user=self.user,
                              password=self.pswd,
                              db=self.db,
                              charset='utf8',
                              cursorclass=pymysql.cursors.DictCursor)
        cursor = con.cursor()
        result = -1
        code, message = '', ''

        warnings.filterwarnings('error', category=pymysql.Warning)

        try:
            cursor.execute(sql_query)
            con.commit()
            result = 0
        except Warning as warning:
            code, message = warning.args
            result = 1
        except pymysql.InternalError as error:
            code, message = error.args
            result = 2
        except pymysql.IntegrityError as error:
            code, message = error.args
            result = 2
        finally:
            con.close()

        return result, code, message
