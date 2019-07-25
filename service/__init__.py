from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:pwd@postgres:5432'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


import service.views.customer
