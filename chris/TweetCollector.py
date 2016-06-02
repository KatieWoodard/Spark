from pyspark import SparkContext
import ConfigParser #so we can get user specific api keys etc.

#import a few Tweepy modules to get tweets
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener as listener

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
        tweetStream = Stream(auth,TweetStream())
        tweetStream.filter(track=['#python','#spark'])

    def processTweets(self, auth):
        """
        Process or store stuff about the tweet here. The response (tweet) comes back as a json object with a *bunch* of properties. Some interesting ones could be:
        status.retweet_count (we could use spark to look at the average number of retweets in a dataset)
        status.source (look at how many tweets come from android vs iphone vs   web vs other sources)
        status.hashtags.text (check most frequently used hashtags)
        status.retweeted_status (see how many tweets on a feed are retweets)
        status.followers_count (check avg num of followers among tweets on a timeline)
        status.friends_count (how many people is the tweeter following)
        status.user.created_at (avg time that tweeter has had a twitter)
        status.user.geo (where are most tweets coming from?)
        status.user.statuses_count (number of a tweets [including rts] that a user has)
        status.user.location (where are tweets coming from in our feed?)
        """
        tweetStream = Stream(auth,TweetStream())



class TweetStream(listener):

    def on_data(self,data):
        """
        Process a tweet and save it to our text file
        whenever a new one comes in.
        """
        try: #open the file in 'a'ppend mode and try to save the tweet in it
            with open('tweets.json','a') as tf:
                tf.write(data)
                print 'wrote data: %s\n' % str(data)
                return True
        except BaseException as e:
                print("error processing tweet: %s" % str(e))
        return True

    def on_error(self, status):
        """
        Print the status of an error when it occurs,
        don't save it anywhere, though.
        """
        print(status)
        return True


#run TweetCollector when the command is given to do so!
if __name__ == '__main__':
    tc = TweetCollector()
