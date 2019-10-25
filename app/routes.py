import requests
import os

from flask import render_template
from app import app
from app.functions.read_only import *
from app.functions.read_write import *

@app.route('/', methods=['GET'])
def timeseries():
    """
    This is a route that grabs stock info for google
    """

    data, meta_data = get_company_timeseries('GOOGL', '15min', 'compact')
    
    list_of_data, keys = dict_to_list(data)
    print(keys[0])
    # print(next(iter(data.items())))
    # print(data)
    return render_template('mainpage.html', title='Stock App', list_of_data=list_of_data, keys=keys)

@app.route('/crypto', methods=['GET'])
def crypto():
    """
    This route grabs crypto data
    """

    data, meta_data = get_crypto_data('BTC', 'USD')
    
    list_of_data = dict_to_list(data)

    return render_template('mainpage.html', title='Stock App', list_of_data=list_of_data)

@app.route('/techindicators', methods=['GET'])
def techindicators():
    """
    This route grabs crypto data
    """

    data, meta_data = get_company_techindicators('GOOGL', '60min')
    list_of_data = dict_to_list(data)
    print(list_of_data)

    return render_template('mainpage.html', title='Stock App', list_of_data=list_of_data)
