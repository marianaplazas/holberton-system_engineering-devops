#!/usr/bin/python3

import json
import requests
from requests.exceptions import ConnectionError
"""
module to the top ten
"""

def top_ten(subreddit):
    'function to determinated the top ten'
    url = 'https://reddit.com/r/' + subreddit + '/hot/.json'
    headers = {'User-Agent': 'Hello_User'}
    req = requests.get(url, headers=headers, allow_redirects=False)
    if (req.status_code == requests.codes.ok):
        r = req.json()
        data = r['data']['children']
        for i in range(len(data)):
            title = data[i]['data']['title']
            print(title)
    else:
        print("None")
