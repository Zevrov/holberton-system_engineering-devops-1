#!/usr/bin/python3
"""Top Ten"""
from requests import get


def recurse(subreddit, hot_list=[], after=""):
    """prints titles of first 10 hot posts listed for a given subreddit
    Args:
        subreddit: input name of the subreddit
        hot_list:
    """
    headers = {'User-Agent': 'yook00627'}
    json = get('https://api.reddit.com/r/{}/hot?after={}'.
               format(subreddit, after), headers=headers).json()
    try:
        key = json['data']['after']
        parent = json['data']['children']
        for obj in parent:
            hot_list.append(obj['data']['title'])
        if key is not None:
            recurse(subreddit, hot_list, key)
        return hot_list
    except Exception:
        return None
