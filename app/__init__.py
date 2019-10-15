import os

from flask import Flask
# from app.config import Config

app = Flask(__name__)
apiKey = os.environ.get('ALPHAVANTAGE_API_KEY')
# app.config.from_object(Config)

from app import routes
