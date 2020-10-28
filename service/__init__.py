"""Setup code for the application itself."""
import os

from flask import Flask

from service.repos.database import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = '123'

db.init_app(app)


import service.views.employee
import service.views.main
