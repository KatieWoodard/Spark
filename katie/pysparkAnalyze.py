from pyspark import SparkContext
from pyspark import SQLContext

sc = SparkContext("local", "Pysparktest")
sql = SQLContext(sc)

df = sql.read.json("Euro2016Monday613.json")
df_distinctlang = df.select("lang").distinct()


df_lang = sql.read.json("TwitterLanguages.json")

df_join =df_distinctlang.join(df_lang, df_distinctlang.lang == df_lang.code).drop(df_lang.code).drop(df_lang.status)

df_join.show()

"""
textFile = sc.textFile("Euro2016tweetsCollect.json")
print "Number of tweets total:" + str(textFile.count())

#print textFile.first()
lines_with_England = textFile.filter(lambda line: "England" in line)

print "Number of tweets with the word England: " + str(lines_with_England.count())
"""
