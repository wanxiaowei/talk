# -*- coding: utf-8 -*-
from project import app
app.config.from_object('config')
if __name__ == '__main__' :
    app.run()
