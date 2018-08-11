# import dependencies
import os, sys, json, time, requests
from flask import Flask, request, Response, jsonify, make_response
#from THD_MD.marketStores import market_stores
#from THD_MD.store_info import store_info
#from THD_MD.getMarkets import listMarkets
from slack_botClass import slackCommunication
#from THD_MD.generateToken import head


# bootstrap the app
app = Flask(__name__)

# set the port dynamically with a default of 3000 for local development
port = int(os.getenv('PORT', '3000'))
python = sys.executable
link = '<https://media.makeameme.org/created/that-would-be-3dsosw.jpg|That would be great>'


# our base route which just returns a string
@app.route('/')
def homePage():
    return 'Home Page! %s'

@app.route('/test')
def anotherPage():
    #markets = listMarkets()
    #print(markets)
    return 'On Another Page %m'

@app.route('/test2')
def yetAnotherPage():
    #store = store_info(store_number=114)
    return 'On Yet Another Page %s' % store

@app.route('/events', methods=['POST', 'GET'])
def events():
    slack_message = request.data
    if(slack_message.get('type') == 'url_verification'):
        print('url verification')

    return (request.data)
#https://myapp-optimistic-topi.apps-np.homedepot.com/events/


# start the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)

