#!/usr/bin/python3
import requests
"""
module to the top ten
"""


def top_ten(subreddit):
    'function to determinated the top ten'
    new_lst = []
    count = 0
    url = 'https://reddit.com/r/' + subreddit + '/hot/.json'
    headers = {'User-Agent': "lala"}
    r = requests.get(url, headers=headers)
    try:
        for data in r.json()['data'].get('children'):
            new_lst.append(data['data'].get('title'))
            count += 1
            if count > 9:
                break
        print("\n".join(x for x in new_lst))
    except Exception as err:
        print("None")
