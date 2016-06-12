from pyspark import SparkContext
import sys

class Analyzer:
    """
    Analyze a set of tweets (saved in a txt file in json).
    Define other functions to do whatever you want, currently it just finds simple info using Spark.
    """
    def __init__(self):
        """
        Make a new instance of Analyzer. Creates a new SparkContext and then runs the main program.
        """
        self.sc = SparkContext("local","Analyzer")
        self.go(sys.argv)

    def go(self, args):
        if len(args) <= 1:
            data = self.getFile()
        else:
            data = args[1]
        rdd = self.sc.textFile(data)
        print str(rdd.count())

    def getFile(self):
        print 'Enter the name of the file to parse:'
        name =  input()
        return name

if __name__=='__main__':
    Analyzer()
