import time
import tweepy
import os
from datetime import date

# Credentials

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

# Aunticarse usando lo antes seteado
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
tweets = []
while True:
    for tweet in tweepy.Cursor(api.search,q="#patagonia #python #meetup -filter:retweets since:{}".format(date.today().strftime('%Y-%m-%d')),tweet_mode='extended').items():
        try:
            if tweet.id not in tweets:
                tweet.retweet()
                tweets.append(tweet.id)
        except tweepy.TweepError as e:
            print(e.reason)

    time.sleep(5)

