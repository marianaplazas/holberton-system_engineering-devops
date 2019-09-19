#!/usr/bin/python3
import requests
"""
recurse 
"""


def recurse(subreddit, after=None, all_results=[]):
    'return the number of posts'
     param = {}
    if after is not None:
        param = {'after': after}
    url = 'https://reddit.com/r/' + subreddit + '/hot/.json'
    headers = {'User-Agent': "lala"}
    r = requests.get(url, headers=headers, params=param)
    try:
        new_after = r.json()['data'].get('after')
        for data in r.json()['data'].get('children'):
            all_results.append(data['data'].get('title'))
        if new_after is not None:
            return(recurse(subreddit, new_after, all_results))
        else:
            return(all_results)
    except:
        return(None)
