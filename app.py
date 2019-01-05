from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb

app = Flask(__name__)
app.config.from_object('config.Configuration')
db = SQLAlchemy(app)

