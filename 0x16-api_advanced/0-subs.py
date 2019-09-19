#!/usr/bin/python3
import requests
"""
module to request the number of subscribers
"""


def number_of_subscribers(subreddit):
    'function to ask the number os susbcribers'
    url = 'https://reddit.com/r/' + subreddit + '/about/.json'
    headers = {'User-Agent': "Hey_user"}
    req = requests.get(url, headers=headers)
    try:
        return(req.json().get('data').get('subscribers'))
    except:
        return(0)
