from flask import Flask
from service.repos.database import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:pwd@postgres:5432'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


import service.views.customer
import service.views.main
