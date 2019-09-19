#!/usr/bin/python3
from requests import get
"""
module of recursion
"""

def recurse(subreddit, hot_list=[], after=""):
    'ask recursive'
    headers = {'User-Agent': 'Hello_User'}
    req = get('https://api.reddit.com/r/{}/hot?after={}'.
               format(subreddit, after), headers=headers).json()
    try:
        key = req['data']['after']
        parent = req['data']['children']
        for obj in parent:
            hot_list.append(obj['data']['title'])
        if key is not None:
            recurse(subreddit, hot_list, key)
        return hot_list
    except Exception:
        return None
