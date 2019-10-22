from app import apiKey
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.cryptocurrencies import CryptoCurrencies
# from pprint import pprint

# import matplotlib.pyplot as plt

def get_company_timeseries(company_symbol, time_interval, out_size):

    ts = TimeSeries(key=apiKey, output_format='json')
    
    # Get json object with the timeseries data and another with  the call's metadata
    data, meta_data = ts.get_intraday(symbol=company_symbol, interval=time_interval, outputsize=out_size)
    
    return data, meta_data

def get_company_techindicators(company_symbol, interval):

    ts = TechIndicators(key=apiKey, output_format='json')
    
    # Get json object with the techindicator data and another with  the call's metadata
    data, meta_data = ts.get_bbands(symbol=company_symbol,interval=interval)

    return data, meta_data

def get_crypto_data(crypto_symbol, market):

    cc = CryptoCurrencies(key=apiKey, output_format='json')
    
    # Get json object with the crypto data and another with  the call's metadata
    data, meta_data = cc.get_digital_currency_daily(symbol=crypto_symbol, market=market)

    return data, meta_data