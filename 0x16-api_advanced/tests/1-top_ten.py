import requests

def top_ten(subreddit):
    # Define the Reddit API endpoint for fetching the subreddit's hot posts
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    # Set a custom User-Agent to avoid issues with Reddit's API
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    # Make the API request
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract and print the titles of the first 10 hot posts
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        # Print None for invalid subreddits or other errors
        print(None)

# Run the function with the provided subreddit or a fake one
if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])

