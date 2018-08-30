#!/usr/bin/python3
"""Find the number of subs"""
from requests import get


def number_of_subscribers(subreddit):
    """find the number of subscriber for subreddit
    Args:
        subreddit: input name of the subreddit
    Return:
        number of subreddit 0 if no subreddit found
    """
    headers = {'User-Agent': 'yook00627'}
    json = get('https://api.reddit.com/r/{}/about'.format(subreddit),
            headers=headers).json()
    try:
        sub = json['data']['subscribers']
        return sub
    except Exception:
        return 0
