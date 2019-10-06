import requests
import os

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from pprint import pprint

import matplotlib.pyplot as plt

# from flask import render_template
from app import app

@app.route('/printdata', methods=['GET', 'POST'])
def index():
    """
    This is a route that grabs stock info for google
    """
    print("here")
    ts = TechIndicators(key=apiKey, output_format='pandas')
    # companySymbol = input("What is the symbol of the company you are looking for?")
    companySymbol = "GOOGL"
    
    # Get json object with the intraday data and another with  the call's metadata
    data, meta_data = ts.get_bbands(symbol=companySymbol,interval='60min', time_period=60)
    # data.plot()
    # plt.title('Intraday Times Series for the ' + companySymbol + ' stock (60 min)')
    # plt.show()
    print(data)

    return 200
