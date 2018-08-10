import requests
import json
from THD_MD.generateToken import head

'''  
{
   "ATLANTA": {
      "number": 1,
      "stores": 79
   },
   "MIAMI/FTL/WPALM": {
      "number": 2,
      "stores": 62
   },...
}
'''


def listMarkets():
    markets_url = 'https://master-data-location.apps-np.homedepot.com/location/markets'

    response = requests.get(markets_url, headers=head)
    markets_json = response.json()

    total_pages = markets_json['page']['totalPages']
    #print (json.dumps(markets_json, indent=1))
    #print (markets_json.keys())
    #print (total_pages)
    markets_with_stores={}
    markets_without_stores={}

    for current_page in range(total_pages):
    #for current_page in range(1):
        markets_url = 'https://master-data-location.apps-np.homedepot.com/location/markets?page={}'.format(current_page)

        response = requests.get(markets_url, headers=head)
        markets_json = response.json()
        #print (json.dumps( markets_json['_embedded']['markets'], indent=3))
        #print (len(markets_json['_embedded']['markets']))

        #print ( "\n----new page------\n")

        markets_on_current_page = markets_json['_embedded']['markets']
        lenOfCurrent_page = len(markets_json['_embedded']['markets'])

        for market in range(lenOfCurrent_page):
            market_num = markets_on_current_page[market]['marketNumber']
            market_name = markets_on_current_page[market]['marketName']

            #print (market_name, ":", market_num , "\n---------")

            stores_in_market_url = 'https://master-data-location.apps-np.homedepot.com/location/stores/search/markets?numbers={}'.format(market_num)
            response = requests.get(stores_in_market_url, headers=head)
            stores_in_markets_json = response.json()

            #print (json.dumps(stores_in_markets_json, indent=3))

            if ('_embedded' in stores_in_markets_json):
                num_stores_in_market = len(stores_in_markets_json['_embedded']['stores'])
                #print ("Stores:", num_stores_in_market, "\n")
                markets_with_stores[market_name] = {'number':market_num,'stores':num_stores_in_market}
            else:
                #print ("No Stores\n")
                markets_without_stores[market_name] = {'number':market_num}

    #print (json.dumps( markets_without_stores, indent=3))
    #print (json.dumps(markets_with_stores, indent=3))
    return markets_with_stores

#print (json.dumps(listMarkets(), indent=3))