import requests
from requests_oauthlib import OAuth1
import json
import os
from generateToken import token



auth_token = token
head = {'Authorization': 'Bearer ' + auth_token}

data = [
    ('marketNumber', '3'),
    ('pageNumber', '3'),
]



location_url = 'https://master-data-location.apps-np.homedepot.com/location/stores/search/stores?numbers=9757'
#location_url = 'https://master-data-location.apps-np.homedepot.com/location/location/number/9757/type/STR'
#location_url = 'https://master-data-location.apps-np.homedepot.com/location/markets?page=0&active=false'
location_url = 'https://master-data-location.apps-np.homedepot.com/location/markets'


#response = requests.get(url, json=data, headers=hed)
response = requests.get(location_url, headers=head)
#print(response)
#print(response.status_code)
#print(response.text)
#print(response.json())
#display in easy readible json format with indentation
response_json =response.json()


print (json.dumps(response_json, indent=1))
print (response_json.keys())

'''
print(os.name )
print()
print(os.getcwd())
print()
print(os.environ)
print()
print(os.environ['TOKEN'])
'''