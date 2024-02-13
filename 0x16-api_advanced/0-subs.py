#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers)
    for a given subreddit
    """
    user = {'User-Agent': 'ketralnis'}
    url = requests.get(
            'https://www.reddit.com/r/{}/about.json'.format(
                subreddit), headers=user).json()
    try:
        return url.get('data').get('subscribers')
    except Exception:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
