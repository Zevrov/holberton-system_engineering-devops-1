#!/usr/bin/python3
"""Top Ten"""
from requests import get


def top_ten(subreddit):
    """prints titles of first 10 hot posts listed for a given subreddit
    Args:
        subreddit: input name of the subreddit
    """
    headers = {'User-Agent': 'yook00627'}
    json = get('https://api.reddit.com/r/{}/hot'.format(subreddit),
               headers=headers).json()
    try:
        for i in range(10):
            print(json['data']['children'][i]['data']['title'])
    except Exception:
        print(None)
