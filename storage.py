import os
import traceback
import MySQLdb

class DataServerSql(object):

    def __init__(self):
        self.host = os.environ.get("DB_HOST", "vidooly-webserver-oregon-snap.cvqiaycslvse.ap-southeast-1.rds.amazonaws.com")

    def connect(self):
        db = MySQLdb.connect("vidooly-webserver-oregon-snap.cvqiaycslvse.ap-southeast-1.rds.amazonaws.com","tred","7+cCG0","vidooly_v1" )
        cursor = db.cursor()
        return db, cursor

    def execute_query(self, _sql, _type):
        try:
            # print(_sql.format(*args))
            # cursor.execute(_sql.format(*args))
            _db, _cursor = self.connect()
            _cursor.execute(_sql)
            if _type.upper() == 'SELECT':
                return self.get_data(_db, _cursor)
            elif _type.upper().upper() == 'UPDATE':
                return self.update_data(_db, _cursor)
            elif _type.upper().upper() == 'INSERT':
                return self.update_data(_db, _cursor)
        except Exception as e:
            traceback.print_exc()
            return e.message
        _db.close()

    def get_data(self, db, cursor):
        results = cursor.fetchall()
        return results

    def update_data(self, db, cursor):
        try:
            db.commit()
            return 1
        except:
            db.rollback()
            return 0
