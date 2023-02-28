#!/usr/bin/python3
"""Function that queries the Reddit API."""
import requests
import sys
after = None


def recurse(subreddit, hot_list=[]):
    """
    Args:subreddit- subreddit name.

    Returns:a list containing title of all hot articles for a given subreddit

    """
    global after
    headers = {'User-Agent': 'Fao'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        next_ = response.json().get("data").get("after")
        if next_ is not None:
            after = next_
            recurse(subreddit, hot_list)
        titles = response.json().get('data').get('children')
        for title in titles:
            hot_list.append(title.get('data').get('title'))
        return hot_list
    else:
        return (None)
