"""
Simple Program to help you get started with Google's APIs
"""
import urllib.request, json, requests, googlemaps, datetime
from THD_MD.generateToken import token

print(token)
import os

############### Using requests (recommended) ###################

#Google MapsDirections API endpoint
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = os.environ['gmap_key']

#Asks the user to input Where they are and where they want to go.
#origin = input('Where are you?: ').replace(' ','+')
#destination = input('Where do you want to go?: ').replace(' ','+')

origin= "Atlanta+Ga"
destination = "Charlotte+NC"

#required Params
params = {
    'origin': origin,
    'destination': destination,
    'key': api_key
}
#optional params
#params['mode'] = "walking"



directions = requests.get(endpoint, params=params)
directions = directions.json()
#print(json.dumps(directions, indent=4))
print(directions.keys())
#print(directions.keys())






####################Using urllib#############################

#Building the URL for the request
nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
request = endpoint + nav_request
#Sends the request and reads the response.
response = urllib.request.urlopen(request).read()
#Loads response as JSON
directions = json.loads(response)
#print(json.dumps(directions, indent=4))
#print(directions)


def get_directions_duration(address_dep, address_arriv, name_dest):
    """
    Get the duration in traffic using Google Maps API
    :param address_dep: departure address (as on Google Maps)
    :param address_arriv: arrival address
    :param name_dest: name of the destination
    :return: text with the ETA
    """
    # Connect to the API
    gmaps = googlemaps.Client(key=api_key)
    now = datetime.datetime.now()
    # Compute the directions
    results = gmaps.directions(address_dep, address_arriv, mode="driving",departure_time=now)
    directions_result = results[0]['legs'][0]
    # Get resukts
    duration = directions_result['duration_in_traffic']
    # Text (fstring) with well formatted addresses
    t = f'Time to {name_dest} : %s _(%s to %s)_' % (duration['text'], directions_result['start_address'],  directions_result['end_address'])
    print (t)
    trip ={'duration': duration['text'],'start_addy':directions_result['start_address'], 'end_addy':directions_result['end_address'] }
    return trip

print(get_directions_duration('Charlotte, NC', 'Atlanta, Ga', 'Home'))