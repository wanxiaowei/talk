from flask import Flask
import os

app = Flask(__name__)
from project.users.views import users_blueprint
from project.admin.views import admin_blueprint
app.register_blueprint(users_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')
