import os
import flask
from flask import request
import requests
from flask import jsonify
from flask import render_template
import json

import os

os.chdir("/Users/danielnixa/Documents/Projects/api_app")
# creates the Flask application project, including methods. app.run() is one of the methods
app = flask.Flask(__name__)
app.config["DEBUG"] = True


# routing == process of mappint urls to functions

# lets Flask know that function home is mapped to the / path. methods = ['GET'] tells Flask what kind of urls requests are allowed.
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/ticker', methods=['GET'])
def button():
    return render_template('ticker_search.html')


@app.route('/api/v1/resources/stocks/all', methods=['GET'])
def api_all():
    '''list all stocks '''

    with open('stocks', 'r') as stocks:
        stocks = json.load(stocks)

        return jsonify(stocks)


@app.route('/stocklookup', methods=['GET'])
def stock_lookup():
    with open('stocks_real_time', 'r') as realtime_stocks:
        realtime_stocks = json.load(realtime_stocks)


@app.route('/api/v1/resources/stocks/individual', methods=['GET'])
def api_indiv():

    if 'symbol' in request.args:
        ticker = request.args['symbol']
    else:
        return "Error: no symbol field provided. Please specify a symbol."

    with open('stocks', 'r') as stocks:
        stocks = json.load(stocks)

    results = []

    for item in stocks['symbolsList']:
        if item['symbol'] == ticker:
            results.append(item)
            name = results[0]['name']
            price = results[0]['price']
            helptext = 'The Company name is ' + name + \
                '. ' + ' The last stock price was $' + str(price)

            return helptext

    if not results:
        return ('you did not enter a correct stock ticker!')


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


app.run()
