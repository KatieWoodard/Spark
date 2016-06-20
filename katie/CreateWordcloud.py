#This file takes an input of Tweets from a json file and exports a png of a wordcloud of the most common words
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re
import json
from nltk.tokenize import word_tokenize


all_data = []
with open('TMobile.json', 'r') as f:
    for line in f:
        tweet = json.loads(line) # load it as Python dict
        only_text = json.dumps(tweet['text'])
        all_data.append(only_text)
#below preprocess steps are from https://marcobonzanini.com/2015/03/09/mining-twitter-data-with-python-part-2/
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

stopwords = ['what','who','is','a','at','is','the', 'amp', 'https', 'rt', 'u2026', 'ud83d', '@tmobile']
all_data = []
with open('TMobile.json', 'r') as f:
    for line in f:
        tweet = json.loads(line) # load it as Python dict
        only_text = preprocess(tweet['text'])
        joined_text = ' '.join(word for word in only_text if word.lower() not in stopwords and 'https' not in word)
        #print joined_text
        all_data.append(joined_text)

#print all_data

data = ''.join(all_data)
#print data.split()
wordcloud = WordCloud(max_font_size = 35, background_color = "white", max_words = 1000, random_state = 50).generate(data)
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig('TmobileWordCloud.png')
