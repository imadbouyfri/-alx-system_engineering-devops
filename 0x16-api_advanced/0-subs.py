#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""
import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API for the number of subscribers of a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'my_reddit_app/0.0.1'}  # Set a custom User-Agent
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0