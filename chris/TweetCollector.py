import ConfigParser #so we can get user specific api keys etc.

#import a few Tweepy modules to get tweets
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener as listener
import sys

class TweetCollector:
    """
    A class for collecting tweets. We use pyspark to create an RDD of tweets and look at some attributes of the data, such as the most used hashtag or the most verbose tweeters from the tweets collected.
    """
    CONST_TWITTERAPIKEYS = 'Twitter API Keys'

    def __init__(self):
        """
        Initialize a tweet collector. Basically just connects to the Twitter API via Tweepy and opens a stream.
        """
        # parse twitter keys
        settings = self.getSettings(sys.argv)
        self.consumer_key = settings[0]
        self.consumer_secret = settings[1]
        self.access_token = settings[2]
        self.access_token_secret = settings[3]
        self.twitterConnect() #after getting keys, connect to twitter

    def getSettings(self, args):
        """
        Parse the user's Twitter API keys.

        @param args an array containing only the name of the file to be parsed.

        @return the Twitter API keys extracted from the file.
        """
        print 'args: %s' %args
        if len(args) != 2:
            self.usage() #tell user how not to be a dummy
            fname = self.getFileName()
        else: #User entered a filename (or something)
            fname = args[1]
        #now that we have a file, try to parse it and get the keys.
        cp = ConfigParser.ConfigParser()
        cp.read(fname)
        settings = []
        try:
            for k,v in cp.items(self.CONST_TWITTERAPIKEYS):
                settings.append(v)
        except ConfigParser.NoSectionError:
            print "Your config file isn't formatted correctly :(. Try again, following this format:"
            self.usage()
            sys.exit(0) #completely end program here. User should try again.
        return settings

    def getFileName(self):
        print('enter the name of your config file:')
        return raw_input()

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


    def usage(self):
        print '''Hey! Enter the name of a file containing your Twitter API keys to get started. The file must be formatted like an INI file as follows:

        [Twitter API KEYS]
        consumer_key=#########
        consumer_secret=###############
        access_token=#############
        access_token_secret=##############\n\nThe names of the variables are important! Anyways, have fun collecting tweets!
        '''
        return

class TweetStream(listener):

    def on_data(self,data):
        """
        Process a tweet and save it to our text file
        whenever a new one comes in.
        """
        try: #open the file in 'a'ppend mode and try to save the tweet in it
            with open('tweets.txt','a') as tf:
                tf.write(data)
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
