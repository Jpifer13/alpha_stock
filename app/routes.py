import requests
import os

from flask import render_template
from app import app
from app.functions.read_only import *
from app.functions.read_write import *

@app.route('/', methods=['GET'])
def index():
    """
    This is a route that grabs stock info for google
    """

    data, meta_data = get_company_intraday('GOOGL')
    
    print(data['2019-10-14 15:30']['Real Lower Band'])
    list_of_data = dict_to_list(data)
    # print(list_of_data)

    return render_template('mainpage.html', title='Stock App', data=list_of_data)
