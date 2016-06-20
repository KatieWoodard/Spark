#from pyspark import SparkContext
#from pyspark import SQLContext
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
import re
import json
from nltk.tokenize import word_tokenize


all_data = []
with open('TMobile.json', 'r') as f:
    for line in f:
        tweet = json.loads(line) # load it as Python dict
        only_text = json.dumps(tweet['text'])
        all_data.append(only_text)

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)

def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

stopwords = ['what','who','is','a','at','is','the', 'amp', 'https', 'rt', 'u2026', 'ud83d', '@tmobile', '@johnlegere', '.co', 't.co', 'co.']
all_data = []
with open('TMobile.json', 'r') as f:
    for line in f:
        tweet = json.loads(line) # load it as Python dict
        only_text = preprocess(tweet['text'])
        joined_text = ' '.join(word for word in only_text if word.lower() not in stopwords and 'https' not in word)
        print joined_text
        all_data.append(joined_text)

#print all_data

data = ''.join(all_data)
#print data.split()
wordcloud = WordCloud().generate(data)
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig('TmobileWordCloud.png')

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
