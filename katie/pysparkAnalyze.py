from pyspark import SparkContext

sc = SparkContext("local", "Pysparktest")
textFile = sc.textFile("Euro2016tweetsCollect.json")
print "Number of tweets total:" + str(textFile.count())
#print textFile.first()
lines_with_England = textFile.filter(lambda line: "England" in line)

print "Number of tweets with the word England: " + str(lines_with_England.count())
