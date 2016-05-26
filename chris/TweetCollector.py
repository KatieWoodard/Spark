from pyspark import SparkContext
import ConfigParser #so we can get user specific api keys etc.

#import a few Tweepy modules to get tweets
import tweepy
from tweepy import OAuthHandler

class TweetCollector:
    """
    A class for collecting tweets. We use pyspark to create an RDD of tweets and look at some attributes of the data, such as the most used hashtag or the most verbose tweeters from the tweets collected.
    """
    def __init__(self):
        """
        Initialize a tweet collector. We create a SparkContext
        to help out with tweet collection and analysis.
        """
        self.sc = SparkContext('local','pyspark')
        # parse twitter keys
        # TODO This is too specific, could it be more general?
        # TODO Should config parsing be moved to another module altogether?
        cp = ConfigParser.ConfigParser()
        cp.read("config/keys.ini") #possible to un-hardcode this?
        self.consumer_key = cp.get('Twitter API Keys','consumer_key')
        self.consumer_secret = cp.get('Twitter API Keys','consumer_secret')
        self.access_token = cp.get('Twitter API Keys','access_token')
        self.access_token_secret = cp.get('Twitter API Keys','access_token_secret')
        self.twitterConnect() #after getting keys, connect to twitter

    def twitterConnect(self):
        """
        Authorize the current user and log in to twitter. Get a single tweet from the user's timeline and print it to the console so the user can look at the structure of what tweepy returns as a tweet.
        """
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)
        # here's where we ge the single tweet and print to console.
        for status in tweepy.Cursor(api.home_timeline).items(1):
            print status

#run TweetCollector when the command is given to do so!
if __name__ == '__main__':
    tc = TweetCollector()
