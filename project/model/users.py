# -*- coding: utf-8 -*-
import MySQLdb
import config
class Users(object):
    def get_db(self):
        try:
            db = MySQLdb.connect(host=DB_HOST,
                                user=DB_USER,
                                passwd=DB_PASSWD,
                                db=DB_DATABASE)
        except MySQLdb.Error:
            db = None
        return db
    @classmethod
    def login(self, username, password):
        db = self.get_db(self);
        permission = ''
        if db:
            cur = None
            try:
                cur = db.cursor()
                sql = 'SELECT `context` FROM \
                        `permission` JOIN `user` ON \
                        `permission.level` = `user.permission_level` \
                        WHERE `name` = %s and `password` = %s'
                cur.execute(sql, (username, password))
                per = cur.fetchone()
                if per:
                    permission = per[0]
            except MySQLdb.Error as e:
                print('MySQLdb error %d: %s' % (e.args[0], e.args[1]))
            finally:
                if cur:
                    cur.close()
                db.close()
        return permission

