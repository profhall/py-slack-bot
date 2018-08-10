import requests
import json
import os


data = [
  ('grant_type', 'client_credentials'),
]


response = requests.post('https://master-data-security.apps-np.homedepot.com/security/oauth/token',
                         data=data,
                         auth=
                            (
                             os.environ['AUTH_CLIENT_ID'],
                             os.environ['AUTH_CLIENT_SECRET']
                            )
                         )
response_json =response.json()
token = response_json["access_token"]
head = {'Authorization': 'Bearer ' + token}


#print(response.content)
#print(response.json())
#print(json.dumps(response.json(), indent=4))
#print("Got Token!", response_json["access_token"])
print("Got Token!")

