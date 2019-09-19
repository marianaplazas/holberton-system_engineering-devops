#!/usr/bin/python3
import requests
from requests.exceptions import ConnectionError
"""
recurse 
"""


def recurse(subreddit, after=None, all_results=[]):
    'return the number of posts'
    url = 'https://reddit.com/r/' + subreddit + '/hot/.json'
    headers = {'User-Agent': 'My User Agent'}
    req = requests.get(url, headers=headers, allow_redirects=False)
    if (req.status_code == requests.codes.ok):
        r = req.json()
        data = r['data']['children']
        for post in data:
            hot_list.append(post['data']['title'])
        after = r['data']['after']
        if after is not None:
            a = "?after={}".format(after)
            recurse(subreddit, hot_list, a)
        else:
            return hot_list
    else:
        return None
    return hot_list
