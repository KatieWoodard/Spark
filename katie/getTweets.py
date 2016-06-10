#This will return tweets. It will use the perms to my twitter account and query twitter

import tweepy
from tweepy import OAuthHandler
import simplejson as json
import ConfigParser

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

# turn into streaming
with open ("tweetsCollect.json", 'a') as tweets:
    for status in tweepy.Cursor(api.home_timeline).items(10):
        #status.decode('utf-8')
        #txtdecode = txt.encode('utf-8')
    #    print(txtdecode)
    #    tweets.write(txtdecode)
    #    json.dump(status, tweets)
    #    tweets.write(status)
        print type(status.parse())
        #print status
'''
import json
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

with open("tweetsCollect.json","w+") as tweets:
    #try:
        for status in tweepy.Cursor(api.home_timeline).items(10):
            print type(status.text)
            x = json.dump(status.text, tweets)
            print x
            #tweets.write(x)
            #print "tweet saved"
#    except BaseException as ex:
#        print "error processing tweet %s" %str(ex)
    #print type(status)
    #data.append(str(status))
'''

"""with open("tweetsCollect.json","a") as tweets:
      tweets.write(data)

"""
#class tweet_collector(self):
 # def __init__(self):
