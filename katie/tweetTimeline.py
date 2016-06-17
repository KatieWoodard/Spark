#This file will grab all the tweets on a timeline of a single user and save them to a file


import tweepy
from tweepy import OAuthHandler
import ConfigParser
from tweepy import Stream
from tweepy.streaming import StreamListener as listener
import json

cp = ConfigParser.ConfigParser()
cp.read('config/twitterkeys')
#print cp.sections()
consumer_key = cp.get('twitter api keys','consumer_key')
consumer_secret = cp.get('twitter api keys', 'consumer_secret')
access_token = cp.get('twitter api keys', 'access_token')
access_secret = cp.get('twitter api keys', 'access_secret')

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

#writes each tweet object from a user's timeline to a json file
with open ("HitachiTimeline.json", 'a') as tweets:
    for status in tweepy.Cursor(api.user_timeline, id = "HIT_Consulting").items():
        tweets.write('\n')
        tweets.write(json.dumps(status._json))
