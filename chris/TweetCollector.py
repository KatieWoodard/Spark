from pyspark import SparkContext

class TweetCollector:
    """
    A class for collecting tweets. We use pyspark to create an RDD of tweets and        look at some attributes of the data, such as the most used hashtag or the most verbose tweeters from the tweets collected.
    """

    def __init__(self):
        """
        Initialize a tweet collector. We create a SparkContext
        to help out with tweet collection and analysis.
        """
        self.sc = SparkContext('local','pyspark')

    def twitterConnect():
        
