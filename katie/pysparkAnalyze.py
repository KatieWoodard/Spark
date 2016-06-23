from pyspark import SparkContext
from pyspark import SQLContext
from pyspark.sql import Row
import pandas

sc = SparkContext("local", "Pysparktest")
sqlContext = SQLContext(sc)
"""
df = sql.read.json("Euro2016Monday613.json")
df_distinctlang = df.select("lang").distinct()


df_lang = sql.read.json("TwitterLanguages.json")

df_join =df_distinctlang.join(df_lang, df_distinctlang.lang == df_lang.code).drop(df_lang.code).drop(df_lang.status)

df_join.show()
"""
currentFile = "TMobile.json"


textFile = sc.textFile(currentFile)
print "Number of tweets total:" + str(textFile.count())

#print textFile.first()
lines_with_keyword = textFile.filter(lambda line: "@TMobileHelp" in line)

print "Number of tweets with TMobileHelp: " + str(lines_with_keyword.count())
print lines_with_keyword.lookup("text")
#print lines_with_keyword
#schemaTweets = sqlContext.createDataFrame(lines_with_keyword)
#schemaTweets.registerTempTable("tweets")
#row = Row("text")
#lines_with_keyword.map(row).toDF()
#lines_with_keyword.printSchema()
#print tweets.take(5)
#print keyword_onlytext.take(5)


df = sqlContext.read.json(currentFile)
#df.printSchema()
#df_distinctlang = df.select("lang").distinct()
#df_lang = sql.read.json("TwitterLanguages.json")
#df_join =df_distinctlang.join(df_lang, df_distinctlang.lang == df_lang.code).drop(df_lang.code).drop(df_lang.status)
#df_join.show()
df.registerTempTable("df")
df_text = df.select("text")
#df_text.printSchema()
df_sql = sqlContext.sql("SELECT text FROM df WHERE text like '%TMobileHelp%'")


print df_sql.collect()

#df_sql.rdd.map(lambda x: ",".join(map(str, x))).coalesce(1).saveAsTextFile("file.csv")
#df.toPandas().to_csv('mycsv.csv')
