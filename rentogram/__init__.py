import os
import sys
import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# initialize app
app.config.from_object(os.environ.get('APP_CONFIG'))

# configure database
db = SQLAlchemy(app)
db.init_app(app)
sql_engine = create_engine(app.config.get("SQLALCHEMY_DATABASE_URI"), connect_args={"check_same_thread": False})

# Конфиг логгера
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(funcName)s - %(levelname)s - %(message)s')
std_handler = logging.StreamHandler(sys.stdout)
std_handler.setFormatter(formatter)
logger.addHandler(std_handler)

from rentogram.views import * # noqa

from rentogram.models import * # noqa
db.create_all()
