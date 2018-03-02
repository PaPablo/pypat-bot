import time
import tweepy
from datetime import date

# Credentials
CONSUMER_KEY = 'lzCIVKmAk5dFz66bdLahARZi5'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'PNsO3TRTbJVOHC7ukXpe6FnF3pr73ilOWQ8mAOGgvQ5sYF4d8d'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '969361386450112513-4Ce1pAaVYxYAscnXp6qxBNqnXScd3DI'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'gI2SRiOYr1e4JMKfZWhDMJUDabbCzplByjVE7CWpXH6u0'#keep the quotes, replace this with your access token secret

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

