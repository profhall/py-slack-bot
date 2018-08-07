# import dependencies
import os, sys, json
from flask import Flask
from THD_MD.marketStores import market_stores
from THD_MD.store_info import store_info
from THD_MD.getMarkets import listMarkets

# bootstrap the app
app = Flask(__name__)

# set the port dynamically with a default of 3000 for local development
port = int(os.getenv('PORT', '3000'))
python = sys.executable

# our base route which just returns a string
@app.route('/')
def homePage():
    return 'Home Page! %s'

@app.route('/test')
def anotherPage():
    markets = listMarkets()
    print(markets)
    return 'On Another Page %m' % markets

@app.route('/test2')
def yetAnotherPage():
    store = store_info(store_number=114)
    return 'On Yet Another Page %s' % store

@app.route('/events')
def events():
    return 'Events page'


# start the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)