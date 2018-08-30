#!/usr/bin/python3
"""Top Ten"""
from requests import get


def count_words(subreddit, word_list, after="", counter={}, t=0):
    """prints titles of first 10 hot posts listed for a given subreddit
    Args:
        subreddit: input name of the subreddit
        word_list: input list of words to look for
    """
    if t == 0:
        for word in word_list:
            counter[word] = 0
    headers = {'User-Agent': 'yook00627'}
    json = get('https://api.reddit.com/r/{}/hot?after={}'.
               format(subreddit, after), headers=headers).json()
    try:
        key = json['data']['after']
        parent = json['data']['children']
        for obj in parent:
            for word in counter:
                counter[word] += obj['data']['title'].lower().split(' ').count(word)
        if key is not None:
            count_words(subreddit, word_list, key, counter, 1)
        else:
            for word in sorted(word_list):
                if counter[word] != 0:
                    print('{}: {}'.format(word, counter[word]))
    except Exception:
        return None
