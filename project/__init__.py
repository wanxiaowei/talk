from flask import Flask
import os

app = Flask(__name__)
app.secret_key = 'sadfasdfas'
from project.users.views import users_blueprint

app.register_blueprint(users_blueprint)
