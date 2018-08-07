import requests
import json
from THD_MD.generateToken import head

'''
Returns an array of stores based on stores, should only 
return one store given that all stores have unique store number
'''
def store_info(**kwargs):
    store_number = kwargs['store_number']
    print("Store:", store_number)
    #store_url = 'https://master-data-location.apps-np.homedepot.com/location/geographiclocations/type/store/number/{}'.format(store_number)
    #store_url = 'https://master-data-location.apps-np.homedepot.com/location/location/number/{}/type/STR'.format(store_number)
    store_url = 'https://master-data-location.apps-np.homedepot.com/location/location/search/location?numbers={}&type=STR'.format(store_number)
    #store_url = 'https://master-data-location.apps-np.homedepot.com/location/stores/search/stores?numbers={}'.format(store_number)
    response = requests.get(store_url, headers=head)
    #print (response.content)
    store_json = response.json()
    #print(json.dumps(store_json, indent=3))
    # print(len(store_json))
    #print('------------------------------')
    # for store in range(len(store_json)):
    #   if(store_json[store]['stateCode']=='TX'):
    #      print(store_json[store]['cityName'], store_json[store]['locationNumber'])
    store = store_json['_embedded']['locations'][0]
    store_city = store['cityName']
    store_addy = store['addressLineOneText']
    store_phone = store['phoneNumber']
    store_state = store['stateCode']
    store_info = {'number':store_number ,'city':store_city, 'address' : store_addy, 'state': store_state, 'phone': store_phone}
    return (store_info)

print(json.dumps(store_info(store_number=114), indent=3))


'''
stores =store_info()
if (len(stores) < 2):
    print(json.dumps(stores[0], indent=3))
else:
    for store in range(len(stores)):
        print(json.dumps(stores[store], indent=3))

stores =store_info(store_number=9749)
if (len(stores) < 2):
    print(json.dumps(stores[0], indent=3))
else:
    for store in range(len(stores)):
        print(json.dumps(stores(9749)[store], indent=3))

stores=store_info(store_number=165)
if (len(stores) < 2):
    print(json.dumps(stores[0], indent=3))
else:
    for store in range(len(stores)):
        print(json.dumps(stores[store], indent=3))
'''