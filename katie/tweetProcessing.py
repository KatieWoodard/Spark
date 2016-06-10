import simplejson as json
from nltk.tokenize import word_tokenize

with open('tweetsCollect.json', 'r') as tweets:
    line = tweets.readline() #loads only the first line
    loadT = json.loads(line)
    print(json.dumps(loadT))

def tokenize(x):
    with open(x,'r') as tweets:
        for line in tweets:
            line = tweets.readline()
            print line


tokenize('tweetsCollect.json')
"""
def preprocess(x, lowercase = False):
    tokens = tokenize(x)
    if lowercase:
        tokens = [token.lower() for token in tokens]
    return tokens

with open('tweetsCollect.json', 'r') as tweets:
    for line in tweets:
        tweet = json.loads(line)
        tokens = preprocess(tweet['text'])
        do_something_else(tokens)
"""
