import tweepy
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve API credentials from environment variables
consumer_key = os.getenv("API_KEY_2")
consumer_secret = os.getenv("API_SECRET_KEY_2")
access_token = os.getenv("ACCESS_TOKEN_2")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET_2")
bearer_token = os.getenv("BEARER_TOKEN_2")

# Set up the client
client = tweepy.Client(bearer_token=bearer_token,
                       consumer_key=consumer_key,
                       consumer_secret=consumer_secret,
                       access_token=access_token,
                       access_token_secret=access_token_secret,
                       wait_on_rate_limit=True)

# Replace 'username' with the actual username of the target user
username = 'pktrpl'

# Fetch user information to get the user ID
user = client.get_user(username=username)

## NOT USING PAGINATOR Cause when it hits limit issues it just ends up waiting longer and not moving on and saving it and free account doesn't allow to go beyond 100 requests in a month so 900 sec wait is useless

# Use Paginator to fetch tweets in batches
# all_tweets = []
# for response in tweepy.Paginator(client.get_users_tweets, id=user.data.id, max_results=100):
#     all_tweets.extend(response.data)



# Fetch 100 tweets using the client
tweets = client.get_users_tweets(id=user.data.id, max_results=100).data

# Define the filename
filename = 'tweets.txt'

# Open the file in write mode
with open(filename, 'w', encoding='utf-8') as file:
    # Write each tweet's ID and text to the file
    for tweet in tweets:
        file.write(f"Tweet ID: {tweet.id}\n")
        file.write(f"Tweet: {tweet.text}\n\n")

# Print the total number of tweets retrieved and saved
print(f"Total tweets retrieved and saved: {len(tweets)}")
