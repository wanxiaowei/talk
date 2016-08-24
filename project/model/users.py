# -*- coding: utf-8 -*-
import MySQLdb
from flask import current_app
def get_db():
    app = current_app
    try:
        db = MySQLdb.connect(host=app.config.get('DB_HOST'),
                            user=app.config.get('DB_USER'),
                            passwd=app.config.get('DB_PASSWORD'),
                            db=app.config.get('DB_DATABASE'))
    except MySQLdb.Error:
        db = None
    return db
def login(username, password):
    db = get_db();
    permission = ''
    if db:
        cur = None
        try:
            cur = db.cursor()
            sql = 'SELECT `context`,`level` FROM \
                    `permission` JOIN `user` ON \
                    permission.level = user.permission_level \
                    WHERE `name` = %s and `password` = %s'
            cur.execute(sql, (username, password))
            per = cur.fetchone()
            if per:
                permission = per[0]
                per_id = int(per[1])
        except MySQLdb.Error as e:
            print('MySQLdb error %d: %s' % (e.args[0], e.args[1]))
        finally:
            if cur:
                cur.close()
            db.close()
    return permission, per_id

