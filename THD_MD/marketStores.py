import requests
import json
from THD_MD.generateToken import head

def market_stores(market_number):
    stores_in_market = {}
    print("Market Number:{}".format(market_number))
    market_url = 'https://master-data-location.apps-np.homedepot.com/location/stores/search/markets?numbers={}'.format(
        market_number)
    response = requests.get(market_url, headers=head)
    market_json = response.json()
    # print (json.dumps(market_json, indent=3))
    # print (market_json.keys())
    for store in range(len(market_json['_embedded']['stores'])):
        # print (market_json['_embedded']['stores'][store]['storeName'])
        stores_in_market[market_json['_embedded']['stores'][store]['storeNumber']] = {
            "Store-Name": market_json['_embedded']['stores'][store]['storeName']}

    # return market_json
    return stores_in_market

print (json.dumps(market_stores(2), indent=3))