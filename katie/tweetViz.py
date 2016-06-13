import json
import pandas as pd
import matplotlib.pyplot as plt


tweets_data = []
tweets_file = open('Euro2016tweetsCollect.json','r')
for line in tweets_file:
    try:
        tweet = json.loads(line)
        #need to check that the line is actually a tweet, twitter also sends limit info as lines through getTweets
        if 'created_at' in tweet:
            tweets_data.append(tweet)
    except:
        continue

print len(tweets_data)

tweets = pd.DataFrame()
tweets["text"] = map(lambda tweet: tweet["text"], tweets_data)
tweets["lang"] = map(lambda tweet: tweet["lang"], tweets_data)
tweets["country"] = map(lambda tweet: tweet["place"]["country"] if tweet["place"] != None else None, tweets_data)

tweets_by_lang = tweets['lang'].value_counts()
#print tweets_by_lang

#below creates a bar chart using matplotlib (matlab) plt.savefig saves it to a png in the current folder
fig, ax = plt.subplots()
ax.tick_params(axis = 'x', labelsize=10)
ax.tick_params(axis = 'y', labelsize=10)
ax.set_xlabel('Languages', fontsize = 10)
ax.set_ylabel('Number of Tweets', fontsize = 10)
ax.set_title('Top 5 languages', fontsize = 10, fontweight = 'bold')
tweets_by_lang[:5].plot(ax = ax, kind = 'bar', color='blue')
plt.savefig('Euro2016Languages.png')
