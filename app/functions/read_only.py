from app import apiKey
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
# from pprint import pprint

# import matplotlib.pyplot as plt

def get_company_intraday(company_name):

    ts = TechIndicators(key=apiKey, output_format='json')
    # # companySymbol = input("What is the symbol of the company you are looking for?")
    companySymbol = company_name
    
    # # Get json object with the intraday data and another with  the call's metadata
    data, meta_data = ts.get_bbands(symbol=companySymbol,interval='60min', time_period=60)
    # # data.plot()
    # # plt.title('Intraday Times Series for the ' + companySymbol + ' stock (60 min)')
    # # plt.show()

    return data, meta_data