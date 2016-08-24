from flask import Flask
import os

app = Flask(__name__)
from project.users.views import users_blueprint

app.register_blueprint(users_blueprint)
