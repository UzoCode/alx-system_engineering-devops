#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import re
import requests
import sys

def add_title(dictionary, hot_posts):
    """ Adds item into a dictionary """
    if len(hot_posts) == 0:
        return

    title = hot_posts[0]['data']['title'].lower()
    for word in dictionary.keys():
        # Regex to match whole words and ignore case
        pattern = re.compile(r'\b{}\b'.format(re.escape(word)), re.I)
        matches = pattern.findall(title)
        dictionary[word] += len(matches)
    
    hot_posts.pop(0)
    add_title(dictionary, hot_posts)

def recurse(subreddit, dictionary, after=None):
    """ Queries to Reddit API """
    u_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': u_agent
    }

    params = {
        'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return None

    dic = res.json()
    hot_posts = dic['data']['children']
    add_title(dictionary, hot_posts)
    after = dic['data']['after']
    if not after:
        return
    recurse(subreddit, dictionary, after=after)

def count_words(subreddit, word_list):
    """ Init function """
    dictionary = {}

    for word in word_list:
        dictionary[word.lower()] = 0

    recurse(subreddit, dictionary)

    # Sort by count (desc) and then alphabetically (asc)
    sorted_items = sorted(dictionary.items(), key=lambda x: (-x[1], x[0]))

    if sorted_items:
        for item in sorted_items:
            if item[1] > 0:
                print("{}: {}".format(item[0], item[1]))
