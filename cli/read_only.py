import click
import requests
import paramiko
import os
import subprocess
import pandas

from alpha_vantage.cryptocurrencies import CryptoCurrencies
from pprint import pprint

apiKey = os.environ.get('ALPHAVANTAGE_API_KEY')

@click.group()
@click.option('--symbol', '-s', help='This is the symbol of the company you wish to view data for.')
@click.option('--market', '-m', help='This is the market with which you wish to check values. Defaut = USD', default="USD")
@click.option('--graph', '-g', help='Boolean for if you want to view hard data on command line or see a graph. Default = False', type=bool, default=False)
@click.pass_context
def cli(ctx, symbol, market, graph):
    """
    CLI tool for viewing all stock information through the command line rather than using the web gui.
    """
    ctx.obj['SYMBOL'] = symbol
    ctx.obj['GRAPH'] = graph
    if(market):
        ctx.obj['MARKET'] = market

cli.command()
@click.pass_context
def find_crypto_daily(ctx):
    """
    Finds all data on cryptocurrency of choice and displays data for that day.
    """

    # Check output format
    if(ctx.obj['GRAPH']):
        out = 'pandas'
    else:
        out = 'json'

    # Get data from API
    cc = CryptoCurrencies(key=apiKey, output_format=out)
    
    # Get object with the crypto data and another with  the call's metadata
    data, meta_data = cc.get_digital_currency_daily(symbol=crypto_symbol, market=market)

    # Show data depending on output format
    # if(ctx.obj['GRAPH']):
    #     data['4b. close (USD)'].plot()
    # plt.tight_layout()
    # plt.title('Daily close value for bitcoin (BTC)')
    # plt.grid()
    # plt.show()
    # else:
    pprint(data)


if __name__ == '__main__':
    cli(obj={})
    