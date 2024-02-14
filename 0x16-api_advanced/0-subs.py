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
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        'AppleWebKit/537.36'
        '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    elif response.status_code == 404:
        return None
    else:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
