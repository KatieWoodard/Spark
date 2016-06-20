#from pyspark import SparkContext
#from pyspark import SQLContext
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
import re
import json

all_data = []
with open('TMobile.json', 'r') as f:
    for line in f:
        tweet = json.loads(line) # load it as Python dict
        only_text = json.dumps(tweet['text'])
        all_data.append(only_text)

#print all_data

data = ''.join(all_data)
#print data.split()
wordcloud = WordCloud().generate(data)
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig('TmobileWordCloud.png')

query = data
stopwords = ['what','who','is','a','at','is','the', 'amp', 'https', 'rt', 'u2026', 'ud83d', '@tmobile', '@johnlegere']
querywords = query.split()
resultwords  = [word for word in querywords if word.lower() not in stopwords]
print resultwords
result = ' '.join(resultwords)
print result
#result = ' '.join(filter(lambda x: x.lower() not in stopwords, data.split()))

wordcloud2 = WordCloud().generate(result)
plt.imshow(wordcloud2)
plt.axis("off")
plt.savefig('2testTmobileWordCloudTryStopWords.png')


#sc = SparkContext("local", "Pysparktest")
#sql = SQLContext(sc)

#create dataframe for json file
#df = sql.read.json("HitachiTimeline.json")
"""
#create new dataframe of just distinct languages, join to Twitter language map to get the long hand name of languages
df_distinctlang = df.select("lang").distinct()
df_lang = sql.read.json("TwitterLanguages.json")
df_join =df_distinctlang.join(df_lang, df_distinctlang.lang == df_lang.code).drop(df_lang.code).drop(df_lang.status)
df_join.show()
"""
#try pandas dataframe
"""

tweets_data = []
tweets_file = open('HitachiTimeline.json','r')
for line in tweets_file:
    try:
        tweet = json.loads(line)
        #need to check that the line is actually a tweet, twitter also sends limit info as lines through getTweets
        tweets_data.append(tweet)
    except:
        continue

print len(tweets_data)

tweets = pd.DataFrame()
tweets["text"] = map(lambda tweet: tweet["text"], tweets_data)
#tweets["lang"] = map(lambda tweet: tweet["lang"], tweets_data)

total_text = ''
for row in tweets.iterrows():
    total_text = total_text + ' ' + row

print total_text
"""
"""
df_text = df.select("text")
df_1 =  df_text.take(1)
print str(df_1)
"""

"""
wordcloud = WordCloud().generate(df_1)
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig('test.png')
"""
