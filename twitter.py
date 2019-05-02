import os
import dotenv
dotenv.load_dotenv('.env')

consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

#use the Twitter API authorized session
from requests_oauthlib import OAuth1Session

session = OAuth1Session(consumer_key,
                        client_secret=consumer_secret,
                        resource_owner_key=access_token,
                        resource_owner_secret=access_token_secret)

# The URL endpoint to update a status (i.e. tweet)
url = 'https://api.twitter.com/1.1/statuses/update.json'

# The contents of status (i.e. tweet text)
status = 'Welcome to Shakespeare Tweet'

# Send a POST request to the url with a 'status' parameter
resp = session.post(url, { 'status': status })

def tweet(status):
    resp = session.post(url, { 'status': status })
    return resp.text

if __name__ == "__main__":
