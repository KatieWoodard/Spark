#This will return tweets. It will use the perms to my twitter account and query twitter

import tweepy
from tweepy import OAuthHandler
import ConfigParser
from tweepy import Stream
from tweepy.streaming import StreamListener as listener

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

"""
#This prints each of the top 10 tweets on my home timeline and all of their metadata
with open ("tweetsCollect.json", 'a') as tweets:
    for status in tweepy.Cursor(api.home_timeline).items(10):
        print(json.dumps(status))
"""
#MyListener will keep appending the tweetsCollect file with tweets and their metadata as they come through
#
class MyListener(listener):
    def on_data(self,data):
        try:
            with open('TMobile.json','a') as tweets:
                if 'created_at' in data:
                    tweets.write(data)
                    return True
        except BaseException as e:
            print "Error on_data: %s" % str(e)
        return True
    def on_error(self,status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#Tmobile', 'tmobile', 'Tmobile', '@Tmobilehelp', '@Tmobile', '@TMobile']) ## can add other filters like language: , languages = ["en"])
