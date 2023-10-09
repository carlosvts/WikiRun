import os
from typing import Type

import requests
from dotenv import load_dotenv
from oauthlib.oauth2 import Client
from requests_oauthlib import OAuth2, OAuth2Session

load_dotenv()
client_id = os.getenv('CLIENT-ID')
access_token = {"access_token": os.getenv('ACCESS-TOKEN')}

basepoint = "http://en.wikipedia.org/w/api.php"

client = Client(client_id=client_id,
                access_token=access_token)
auth = OAuth2(
    client_id=client.client_id,
    client=client,
    token=client.access_token
)

data: dict[type, type] = {}

headers = {
    "Authorization": f"Bearer {access_token}"
}

# r = requests.get(url='https://en.wikipedia.org/w/api.php',
#                 data=data, auth=auth, headers=headers)


def get_related_titles(article_title):
    _params = {
        "action": "query",
        "format": "json",
        "prop": "links",
        "titles": article_title,
        "pllimit": 50
    }

    response = requests.get(
        basepoint, params=_params
    )

    def _fetch_info(data):
        _all_links = data['query']['pages']['6690']['links']
        print(_all_links)
        queue = []
        for link in _all_links:
            link_title = link['title']
            queue.append(link_title)
        return queue

    _fetch_info(response.json())


print(get_related_titles("Coca-Cola"))
