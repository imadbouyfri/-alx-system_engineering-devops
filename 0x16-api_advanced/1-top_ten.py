import requests

def top_ten(subreddit):
    """Queries the Reddit API for the titles of the top 10 hot posts in a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Prints:
        The titles of the top 10 hot posts, or None if the subreddit is invalid.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, allow_redirects=False)  # Prevent following redirects

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts[:10]:
            print(post['data']['title'])
    else:
        print(None)
