import json
import tweepy
from tweepy import OAuthHandler



# What are we doing with the JSONs
from TwitterData import consumer_key, consumer_secret, access_token, access_secret


def process_or_store(tweet):
    print(json.dumps(tweet))


# We've to charge the program.
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# Let's try printing our friends.
for friend in tweepy.Cursor(api.friends).items():
    process_or_store(friend._json)
