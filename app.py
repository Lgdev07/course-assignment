import os

from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
from src.database.db import initialize_db

app = Flask(__name__)

load_dotenv()

from src.routes import initialize_routes

api = Api(app)

app.config['MONGODB_SETTINGS'] = {
  'host': os.getenv("MONGODB_URL")
}

initialize_db(app)
initialize_routes(api)