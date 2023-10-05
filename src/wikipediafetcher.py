import os

import requests
from dotenv import load_dotenv
from oauthlib.oauth2 import Client
from requests_oauthlib import OAuth2, OAuth2Session

load_dotenv()
client_id = os.getenv('CLIENT-ID')
access_token = {"access_token": os.getenv('ACCESS-TOKEN')}

endpoint = "http://en.wikipedia.org/w/api.php"

client = Client(client_id=client_id,
                access_token=access_token)
auth = OAuth2(
    client_id=client.client_id,
    client=client,
    token=client.access_token
)

data = {}

headers = {
    "Authorization": f"Bearer {access_token}"
}

r = requests.get(url='https://en.wikipedia.org/w/api.php',
                 data=data, auth=auth, headers=headers)

print(r.status_code)
