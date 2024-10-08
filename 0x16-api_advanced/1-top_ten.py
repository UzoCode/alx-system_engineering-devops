#!/usr/bin/python3
"""This module contains a function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit."""

import requests
import sys


def top_ten(subreddit):
    """Function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            children = response.json().get('data').get('children')
            for i in range(10):
                print(children[i].get('data').get('title'))
        else:
            print("None")
    except requests.exceptions.RequestException as e:
        print("None", file=sys.stderr)
